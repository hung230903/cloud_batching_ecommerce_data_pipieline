import pandas as pd
from utils.data_transform_utils import safe_bool, safe_int, safe_string


def transform_summary_data(df):
    # Standardization data before loading to PyArrow Schema

    # rename fields
    rename_rules = {
        'cat_id': 'category_id',
        'collect_id': 'collection_id'
    }
    for old_name, new_name in rename_rules.items():
        if old_name in df.columns:
            df = df.rename(columns={old_name: new_name})

    # Casting data types
    bool_cols = ['show_recommendation', 'recommendation', 'is_paypal']
    int_cols = [
        'recommendation_product_position', 'amount',
        'product_id', 'viewing_product_id', 'recommendation_product_id',
        'category_id', 'collection_id', 'order_id'
    ]
    nested_cols = ['option', 'cart_products']

    # Hàm làm sạch sâu các Object và Array lồng nhau
    def clean_nested_list(val, is_cart_products=False):
        if not isinstance(val, list):
            return []

        cleaned_list = []
        for item in val:
            if not isinstance(item, dict):
                continue

            # Casting fields for cart_products
            if is_cart_products:
                # product_id cast to INT64
                if 'product_id' in item:
                    item['product_id'] = safe_int(item['product_id'])

                # price, currency cast as STRING
                for k in ['price', 'currency']:
                    if k in item:
                        item[k] = safe_string(item[k])

                # amount cast to INT64
                if 'amount' in item:
                    item['amount'] = safe_int(item['amount'])
                    if item['amount'] is None:
                        item['amount'] = 0
                else:
                    item['amount'] = 0

                # Làm sạch sâu option lồng trong cart_products
                if 'option' not in item or not isinstance(item['option'], list):
                    item['option'] = []
                else:
                    for sub_opt in item['option']:
                        if isinstance(sub_opt, dict):
                            for f in ['option_id', 'option_label', 'value_id', 'value_label']:
                                if f in sub_opt:
                                    sub_opt[f] = safe_string(sub_opt[f])
            else:
                # rename fields
                if 'kollektion' in item: item['collection'] = item.pop('kollektion')
                if 'kollektion_id' in item: item['collection_id'] = item.pop('kollektion_id')

                # Casting String for options fields
                for field in [
                    'option_label', 'option_id', 'value_label', 'value_id',
                    'quality', 'quality_label', 'alloy', 'diamond', 'shapediamond',
                    'stone', 'pearlcolor', 'finish', 'price', 'collection'
                ]:
                    if field in item:
                        item[field] = safe_string(item[field])

                # Casting int for options fields
                for int_f in ['category_id', 'collection_id']:
                    if int_f in item:
                        item[int_f] = safe_int(item[int_f])

            cleaned_list.append(item)
        return cleaned_list

    # Lặp qua tất cả các cột của DataFrame hiện tại
    for col in df.columns:
        if col in nested_cols:
            is_cart = (col == 'cart_products')
            df[col] = df[col].apply(lambda x: clean_nested_list(x, is_cart))
            continue

        if col in bool_cols:
            df[col] = df[col].apply(safe_bool).astype('boolean')
        elif col in int_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
        else:
            df[col] = df[col].apply(lambda x: str(x) if pd.notnull(x) else None)

    return df
