import pandas as pd
import plotly.express as px
import streamlit as st
from google.cloud import bigquery

from config.base import BQ_MART_DATASET_ID, BQ_PROJECT_ID


# Initialize BigQuery client
@st.cache_resource
def get_bq_client():
    return bigquery.Client(project=BQ_PROJECT_ID)


@st.cache_data(ttl=3600)
def run_query(query):
    client = get_bq_client()
    # db-dtypes is required under the hood for to_dataframe()
    return client.query(query).to_dataframe()


st.set_page_config(
    page_title="Glamira Executive Dashboard", page_icon="💎", layout="wide"
)

st.title("💎 Glamira Executive Dashboard")
st.markdown("Live Data Warehouse Analytics directly from Google BigQuery")

# Load data safely
try:
    # 1. Revenue Analysis
    st.header("1. Revenue Analysis")
    rev_query = f"""
        SELECT 
            SUM(amount_usd) as total_revenue,
            AVG(amount_usd) as average_order_value,
            COUNT(DISTINCT order_id) as total_orders
        FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order`
    """
    rev_data = run_query(rev_query)

    col1, col2, col3 = st.columns(3)
    # Using simple checks if data is empty or NA
    total_rev = (
        rev_data["total_revenue"][0] if not pd.isna(rev_data["total_revenue"][0]) else 0
    )
    aov = (
        rev_data["average_order_value"][0]
        if not pd.isna(rev_data["average_order_value"][0])
        else 0
    )
    total_ord = (
        rev_data["total_orders"][0] if not pd.isna(rev_data["total_orders"][0]) else 0
    )

    col1.metric("Total Revenue", f"${total_rev:,.2f}")
    col2.metric("Average Order Value (AOV)", f"${aov:,.2f}")
    col3.metric("Total Orders", f"{int(total_ord):,}")

    st.markdown("---")

    # 2. Time-based trends
    st.header("2. Time-Based Trends")
    time_query = f"""
        SELECT 
            d.full_date,
            SUM(f.amount_usd) as daily_revenue
        FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order` f
        JOIN `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.dim_date` d ON f.date_id = d.date_id
        GROUP BY 1
        ORDER BY full_date
    """
    time_data = run_query(time_query)

    if not time_data.empty:
        # Create line chart
        fig_time = px.line(
            time_data,
            x="full_date",
            y="daily_revenue",
            title="Daily Revenue Trend",
            markers=True,
        )
        # Enhance aesthetic layout
        fig_time.update_layout(xaxis_title="Date", yaxis_title="Revenue ($)")
        st.plotly_chart(fig_time, use_container_width=True)
    else:
        st.info("No time-based data available yet in the Fact table.")

    # Two columns for Geo and Product
    col1, col2 = st.columns(2)

    # 3. Geographic Distribution
    with col1:
        st.header("3. Geographic Distribution")
        geo_query = f"""
            SELECT 
                l.country_long as country,
                SUM(f.amount) as revenue
            FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order` f
            JOIN `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.dim_location` l ON f.location_id = cast(l.ip_address_int as string)
            GROUP BY 1
            ORDER BY revenue DESC
            LIMIT 10
        """
        # Note: in dbt architecture, f.location_id was mapped to l.location_id directly as the IP string.
        # So we update our query here:
        geo_query_fixed = f"""
            SELECT 
                l.country_long as country,
                SUM(f.amount_usd) as revenue
            FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order` f
            JOIN `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.dim_location` l ON f.location_id = l.location_id
            GROUP BY 1
            ORDER BY revenue DESC
            LIMIT 10
        """
        geo_data = run_query(geo_query_fixed)
        if not geo_data.empty:
            fig_geo = px.bar(
                geo_data,
                x="country",
                y="revenue",
                color="revenue",
                color_continuous_scale="Viridis",
                title="Top 10 Countries by Revenue",
            )
            fig_geo.update_layout(xaxis_title="Country", yaxis_title="Revenue ($)")
            st.plotly_chart(fig_geo, use_container_width=True)
        else:
            st.info("No geographic data available yet.")

    # 4. Product performance
    with col2:
        st.header("4. Product Performance")
        prod_query = f"""
            SELECT 
                p.product_name,
                SUM(f.amount_usd) as revenue
            FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order` f
            JOIN `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.dim_product` p ON f.product_id = p.product_id
            GROUP BY 1
            ORDER BY revenue DESC
            LIMIT 10
        """
        prod_data = run_query(prod_query)
        if not prod_data.empty:
            fig_prod = px.bar(
                prod_data,
                y="product_name",
                x="revenue",
                orientation="h",
                color="revenue",
                color_continuous_scale="Plasma",
                title="Top 10 Products by Revenue",
            )
            fig_prod.update_layout(
                yaxis={"categoryorder": "total ascending"},
                xaxis_title="Revenue ($)",
                yaxis_title="",
            )
            st.plotly_chart(fig_prod, use_container_width=True)
        else:
            st.info("No product data available yet.")

    # Optional: Tabular detail view
    with st.expander("View Raw Fact Table Samples"):
        sample_query = f"SELECT * FROM `{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.fact_sales_order` LIMIT 100"
        st.dataframe(run_query(sample_query))

except Exception as e:
    st.error(f"Error establishing connection or querying BigQuery: {e}")
