"""
Alert System DAG.

Centralized alerting framework with configurable alert rules,
severity levels, escalation, and multi-channel notification.

Schedule: Every 15 minutes.
"""

from datetime import datetime, timedelta
from typing import Dict

from airflow.models import TaskInstance
from airflow.operators.python import PythonOperator

from airflow import DAG

# ─── Default Arguments ────────────────────────────────────────────────

default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# ─── Alert Configuration ────────────────────────────────────────────
ALERT_RULES = [
    {
        "name": "dag_failure_detected",
        "description": "One or more DAGs failed recently",
        "severity": "CRITICAL",
        "check_type": "dag_failure",
    }
]

SEVERITY_PRIORITY = {"CRITICAL": 1, "HIGH": 2, "MEDIUM": 3, "LOW": 4}


# ─── Task Callables ──────────────────────────────────────────────────


def _evaluate_alert_rules(ti: TaskInstance, **kwargs):
    """Evaluate all alert rules and identify triggered alerts."""
    triggered_alerts = []

    for rule in ALERT_RULES:
        try:
            result = _check_rule(rule)

            if isinstance(result, tuple):
                is_triggered, dynamic_desc = result
            else:
                is_triggered = result
                dynamic_desc = rule["description"]

            if is_triggered:
                alert = {
                    "name": rule["name"],
                    "description": dynamic_desc,
                    "severity": rule["severity"],
                    "priority": SEVERITY_PRIORITY.get(rule["severity"], 5),
                    "triggered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                triggered_alerts.append(alert)
                print(f"🚨 ALERT: {rule['severity']} - {rule['name']}: {dynamic_desc}")
            else:
                print(f"✅ Rule OK: {rule['name']}")
        except Exception as e:
            print(f"⚠️  Error evaluating rule {rule['name']}: {e}")

    triggered_alerts.sort(key=lambda x: x["priority"])
    ti.xcom_push(key="triggered_alerts", value=triggered_alerts)

    return triggered_alerts


def _check_rule(rule: Dict) -> bool:
    """Check a single alert rule. Returns True if alert should trigger."""
    check_type = rule.get("check_type")

    if check_type == "dag_failure":
        try:
            from datetime import timedelta

            from airflow.models import DagRun, TaskInstance
            from airflow.utils import timezone
            from airflow.utils.session import create_session
            from airflow.utils.state import State

            with create_session() as session:
                time_threshold = timezone.utcnow() - timedelta(minutes=15)

                # 1. Check xem có DAG nào sập hẳn không
                failed_runs = (
                    session.query(DagRun)
                    .filter(
                        DagRun.state == State.FAILED, DagRun.end_date >= time_threshold
                    )
                    .all()
                )

                # 2. Check xem có Task nhỏ nào sập không (Cái này giúp alert ngay lập tức)
                failed_tasks = (
                    session.query(TaskInstance)
                    .filter(
                        TaskInstance.state == State.FAILED,
                        TaskInstance.end_date >= time_threshold,
                    )
                    .all()
                )

                if failed_runs or failed_tasks:
                    desc_parts = []
                    if failed_runs:
                        failed_dag_ids = list(set([run.dag_id for run in failed_runs]))
                        desc_parts.append(f"Failed DAGs: {', '.join(failed_dag_ids)}")
                    if failed_tasks:
                        # Gom nhóm lỗi theo DAG ID và Task ID
                        failed_task_ids = list(
                            set([f"{t.dag_id}.{t.task_id}" for t in failed_tasks])
                        )
                        desc_parts.append(f"Failed Tasks: {', '.join(failed_task_ids)}")

                    desc = " | ".join(desc_parts)
                    return True, desc
                return False
        except Exception as e:
            print(f"Error checking dag/task failures: {e}")
            return False

    return False


def _classify_and_prioritize(ti: TaskInstance, **kwargs):
    """Classify alerts by severity and apply escalation rules."""
    alerts = ti.xcom_pull(task_ids="evaluate_alert_rules", key="triggered_alerts")

    if not alerts:
        print("ℹ️  No alerts triggered.")
        ti.xcom_push(
            key="classified_alerts", value={"alerts": [], "requires_escalation": False}
        )
        return

    classified = {
        "CRITICAL": [],
        "HIGH": [],
        "MEDIUM": [],
        "LOW": [],
    }

    for alert in alerts:
        severity = alert.get("severity", "LOW")
        classified[severity].append(alert)

    requires_escalation = len(classified["CRITICAL"]) > 0

    result = {
        "alerts": alerts,
        "classified": classified,
        "requires_escalation": requires_escalation,
        "summary": {
            "total": len(alerts),
            "critical": len(classified["CRITICAL"]),
            "high": len(classified["HIGH"]),
            "medium": len(classified["MEDIUM"]),
            "low": len(classified["LOW"]),
        },
    }

    ti.xcom_push(key="classified_alerts", value=result)
    print(f"📊 Alert Summary: {result['summary']}")
    return result


def _send_notifications(ti: TaskInstance, **kwargs):
    """Send notifications for triggered alerts via Telegram."""
    import requests
    from airflow.models import Variable

    classified = ti.xcom_pull(
        task_ids="classify_and_prioritize", key="classified_alerts"
    )

    if not classified or not classified.get("alerts"):
        print("ℹ️  No notifications to send.")
        return

    print("=" * 60)
    print("📬 ALERT NOTIFICATIONS")
    print("=" * 60)

    message_lines = ["🚨 <b>CLOUD BATCHING PIPELINE ALERTS</b> 🚨\n"]

    for alert in classified["alerts"]:
        severity_emoji = {
            "CRITICAL": "🔴",
            "HIGH": "🟠",
            "MEDIUM": "🟡",
            "LOW": "🟢",
        }.get(alert["severity"], "⚪")

        print(f"  {severity_emoji} [{alert['severity']}] {alert['name']}")
        print(f"     {alert['description']}")
        print(f"     Triggered: {alert['triggered_at']}\n")

        message_lines.append(
            f"{severity_emoji} <b>[{alert['severity']}] {alert['name']}</b>"
        )
        message_lines.append(f"<i>{alert['description']}</i>")
        message_lines.append(f"⏱ Triggered: {alert['triggered_at']}\n")

    if classified.get("requires_escalation"):
        print("⚠️  ESCALATION REQUIRED: Critical alerts detected!")
        message_lines.append("⚠️ <b>ESCALATION REQUIRED:</b> Critical alerts detected!")

    print("=" * 60)
    message_text = "\n".join(message_lines)

    bot_token = Variable.get("CLOUD_TELEGRAM_BOT_TOKEN", default_var="").strip()
    chat_id = Variable.get("TELEGRAM_CHAT_ID", default_var="").strip()

    if bot_token and chat_id:
        try:
            telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {"chat_id": chat_id, "text": message_text, "parse_mode": "HTML"}
            response = requests.post(telegram_url, json=payload, timeout=10)
            response.raise_for_status()
            print("✅ Telegram notification sent successfully!")
        except Exception as e:
            print(f"❌ Failed to send Telegram notification: {e}")
    else:
        print("ℹ️  Telegram credentials not configured. Skipping Telegram notification.")
        print(
            "   Please set 'TELEGRAM_BOT_TOKEN' and 'TELEGRAM_CHAT_ID' in Airflow Variables."
        )

    notifications_sent = {
        "total_alerts": len(classified["alerts"]),
        "escalated": classified.get("requires_escalation", False),
        "channels": ["log", "telegram"] if (bot_token and chat_id) else ["log"],
        "timestamp": datetime.now().isoformat(),
    }

    ti.xcom_push(key="notifications_sent", value=notifications_sent)
    return notifications_sent


# ─── DAG Definition ──────────────────────────────────────────────────

with DAG(
    dag_id="alert_system",
    default_args=default_args,
    description="Centralized alert system for batch pipeline",
    schedule="*/1 * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["alerting", "monitoring", "batch"],
) as dag:
    evaluate_rules = PythonOperator(
        task_id="evaluate_alert_rules",
        python_callable=_evaluate_alert_rules,
    )

    classify = PythonOperator(
        task_id="classify_and_prioritize",
        python_callable=_classify_and_prioritize,
    )

    notify = PythonOperator(
        task_id="send_notifications",
        python_callable=_send_notifications,
    )

    evaluate_rules >> classify >> notify
