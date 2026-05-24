import json
import re

# Regex to get JSON0-LD product
_JSON_LD_RE = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL,
)

# Regex to get react_data param
_REACT_DATA_RE = re.compile(r"var\s+react_data\s*=\s*(\{.*?\});", re.DOTALL)


def extract_product_data(html):
    """
    Extract product info from HTML
    Prioritize react_data param because it contains most info
    If not -> get JSON-LD for fallback
    """

    # Extract react_data
    match = _REACT_DATA_RE.search(html)
    if match:
        try:
            react_data = json.loads(match.group(1))
            if react_data.get("product_id"):
                data = {
                    "product_id": react_data.get("product_id"),
                    "product_name": react_data.get("name"),
                    "sku": react_data.get("sku"),
                    "attribute_set_id": react_data.get("attribute_set_id"),
                    "attribute_set": react_data.get("attribute_set"),
                    "type_id": react_data.get("type_id"),
                    "min_price": react_data.get("min_price_format"),
                    "max_price": react_data.get("max_price_format"),
                    "gold_weight": react_data.get("gold_weight"),
                    "none_metal_weight": react_data.get("none_metal_weight"),
                    "fixed_silver_weight": react_data.get("fixed_silver_weight"),
                    "material_design": react_data.get("material_design"),
                    "collection": react_data.get("collection"),
                    "collection_id": react_data.get("collection_id"),
                    "product_type": react_data.get("product_type"),
                    "product_type_value": react_data.get("product_type_value"),
                    "category_id": react_data.get("category"),
                    "category_name": react_data.get("category_name"),
                    "store_id": react_data.get("store_code"),
                    "gender": react_data.get("gender"),
                    "media_image": react_data.get("media_image"),
                    "media_video": react_data.get("media_video"),
                }

                # Extract details from options (stone, alloy/color, custom)
                options = react_data.get("options", [])
                data["options"] = (
                    options  # Save all options as a JSON string for fallback
                )

                stone_list = []
                colour_list = []
                custom_list = []

                for option in options:
                    group = option.get("group")
                    values = option.get("values", [])
                    if group == "stone":
                        stone_list.extend(values)
                    elif group == "alloy":
                        # Change 'colour' -> 'colour_code' to avoid duplicate with root field
                        for v in values:
                            if "colour" in v:
                                v["colour_code"] = v.pop("colour")
                        colour_list.extend(values)
                    elif group == "custom":
                        custom_list.extend(values)

                # Save as list objects so PyArrow can process mapping to struct/list instead of string
                data["stone"] = stone_list
                data["colour"] = colour_list
                data["custom"] = custom_list

                return data
        except json.JSONDecodeError:
            pass

    # Extract JSON-LD for fallback
    json_ld_data = _extract_product_json_ld(html)
    if json_ld_data:
        return json_ld_data

    return None


def _extract_product_json_ld(html):
    for match in _JSON_LD_RE.findall(html):
        try:
            clean_match = match.strip()
            if not clean_match:
                continue
            data = json.loads(clean_match)
        except json.JSONDecodeError:
            continue

        if isinstance(data, dict):
            if data.get("@type") == "Product":
                return data
            if data.get("@type") == "ItemPage":
                main = data.get("mainEntity")
                if isinstance(main, dict) and main.get("@type") == "Product":
                    return main

    return None
