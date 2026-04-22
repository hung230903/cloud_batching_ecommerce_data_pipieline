# Data Dictionary: BigQuery: summary

Generated at: 2026-04-22 16:14:19

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_version | str | 1000 | 0 (0.0%) | 1 | 1.0 | Version of the tracking API |
| cart_products | dict | 1000 | 0 (0.0%) | 1 | N/A | Array of products currently in the user's cart |
| cart_products.list | list | 1000 | 986 (98.6%) | 1 | N/A | N/A (See parent components for context) |
| cart_products.list.element | dict | 20 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| cart_products.list.element.amount | int | 20 | 0 (0.0%) | 2 | 0, 1 | N/A (See parent components for context) |
| cart_products.list.element.currency | NoneType, str | 20 | 19 (95.0%) | 1 | € | Currency code (e.g., EUR, USD, GBP) |
| cart_products.list.element.option | dict | 20 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| cart_products.list.element.option.list | list | 20 | 3 (15.0%) | 1 | N/A | N/A (See parent components for context) |
| cart_products.list.element.option.list.element | dict | 29 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| cart_products.list.element.option.list.element.option_id | str | 29 | 0 (0.0%) | 27 | 245116, 245117, 332084 | Internal system identifier for option |
| cart_products.list.element.option.list.element.option_label | str | 29 | 0 (0.0%) | 2 | diamond, alloy | Localized display name/label for the field: option |
| cart_products.list.element.option.list.element.value_id | str | 29 | 0 (0.0%) | 27 | 2033747, 2033763, 3279324 | Internal system identifier for value |
| cart_products.list.element.option.list.element.value_label | str | 29 | 0 (0.0%) | 9 | Diamond, Weißgold 585, Gelbgold 585 | Localized display name/label for the field: value |
| cart_products.list.element.price | NoneType, str | 20 | 19 (95.0%) | 1 | 281,00 | Monetary value or price-related setting |
| cart_products.list.element.product_id | int | 20 | 0 (0.0%) | 19 | 89381, 110474, 103331 | Internal system identifier for product |
| category_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Unique ID of the primary category |
| collection | str | 1000 | 0 (0.0%) | 23 | view_product_detail, product_detail_recommendation_clicked, view_shopping_cart | Project collection name |
| collection_id | NoneType, int | 1000 | 945 (94.5%) | 29 | 4620, 4090, 4380 | Unique ID of the collection |
| currency | NoneType, str | 1000 | 972 (97.2%) | 4 | €, MXN $, Kč | Currency code (e.g., EUR, USD, GBP) |
| current_url | str | 1000 | 0 (0.0%) | 947 | https://www.glamira.co.uk/glamira-pendant-imene.html?alloy=white-750&diamond=rose-quartz&utm_source=criteo&utm_medium=retargeting&utm_campaign=webconversion, https://www.glamira.fr/glamira-ring-alonnisos.html?stone2=diamond-sapphire&alloy=yellow-375&diamond=diamond-sapphire&gclid=EAIaIQobChMIvaT7ypzS6QIVCtPVCh2mCQ1JEAEYASABEgLfi_D_BwE, https://www.glamira.de/alluring-tear-3-mm.html?alloy=white_red-585&stone=diamond-Zirconia&itm_source=recommendation&itm_medium=detail | Full URL of the page where the event occurred |
| device_id | str | 1000 | 0 (0.0%) | 860 | 9a3cbb9e-91d9-425e-9411-6cc328381b2a, f5134202-5348-4cc0-814c-ace35edfc487, d953062f-b365-4293-94bd-6ca5e087bdce | Unique persistent identifier for the user's device |
| email_address | str | 1000 | 0 (0.0%) | 60 | , tomouel@hotmail.com, chr.collart@gmail.com | User's email address if captured during the session |
| ip | str | 1000 | 0 (0.0%) | 824 | 45.58.49.210, 46.4.224.79, 109.70.100.29 | IP address of the user |
| is_paypal | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Flag indicating if PayPal was selected or used |
| key_search | NoneType, str | 1000 | 999 (99.9%) | 1 | su smaragdais | Search keywords entered by the user |
| local_time | NoneType, str | 1000 | 1 (0.1%) | 992 | 2020-05-26 9:7:50, 2020-05-27 9:19:18, 2020-05-26 4:26:25 | Literal local time captured from the user's device |
| option | dict | 1000 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| option.list | list | 1000 | 532 (53.2%) | 1 | N/A | N/A (See parent components for context) |
| option.list.element | dict | 726 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| option.list.element.alloy | NoneType | 726 | 726 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.category_id | NoneType | 726 | 726 (100.0%) | 0 | N/A | Internal system identifier for category |
| option.list.element.collection | NoneType | 726 | 726 (100.0%) | 0 | N/A | Project collection name |
| option.list.element.collection_id | NoneType | 726 | 726 (100.0%) | 0 | N/A | Internal system identifier for collection |
| option.list.element.diamond | NoneType | 726 | 726 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.finish | NoneType | 726 | 726 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.option_id | NoneType, str | 726 | 3 (0.4%) | 530 | 323422, 323421, 328028 | Internal system identifier for option |
| option.list.element.option_label | str | 726 | 0 (0.0%) | 9 | alloy, diamond, stone/diamonds | Localized display name/label for the field: option |
| option.list.element.pearlcolor | NoneType | 726 | 726 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.price | NoneType | 726 | 726 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| option.list.element.quality | NoneType, str | 726 | 663 (91.3%) | 4 | AAAA, AAA, A | N/A (See parent components for context) |
| option.list.element.quality_label | NoneType, str | 726 | 670 (92.3%) | 17 | AAAA, AAA, Fancy Deep | Localized display name/label for the field: quality |
| option.list.element.shapediamond | NoneType | 726 | 726 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.stone | NoneType | 726 | 726 (100.0%) | 0 | N/A | List of gemstone configurations currently assigned to the product |
| option.list.element.value_id | NoneType, str | 726 | 6 (0.8%) | 552 | 2745622, 2745566, 3184848 | Internal system identifier for value |
| option.list.element.value_label | str | 726 | 0 (0.0%) | 56 | , sapphire, emerald | Localized display name/label for the field: value |
| order_id | NoneType, int | 1000 | 999 (99.9%) | 1 | 620295665 | ID of the sales order if applicable |
| price | NoneType, str | 1000 | 972 (97.2%) | 8 | 717,00, 2.977,00, 8,258.00 | Price of the product during the event |
| product_id | NoneType, int | 1000 | 532 (53.2%) | 378 | 109484, 97845, 86913 | Unique identifier for the product |
| recommendation | NoneType, bool | 1000 | 788 (78.8%) | 1 | False | Flag for recommendation-related interactions |
| recommendation_clicked_position | NoneType, str | 1000 | 990 (99.0%) | 1 | 0.0 | Position in the UI where the recommendation was clicked |
| recommendation_product_id | NoneType, int | 1000 | 986 (98.6%) | 14 | 98644, 90294, 97418 | ID of the product recommended to the user |
| recommendation_product_position | NoneType, int | 1000 | 999 (99.9%) | 1 | 1 | Index of the product in the recommendation list |
| referrer_url | str | 1000 | 0 (0.0%) | 647 | https://paid.outbrain.com, , https://www.glamira.de/natural-sensation-3-mm.html?alloy=white_red-585 | URL of the previous page that referred the user |
| resolution | NoneType, str | 1000 | 1 (0.1%) | 110 | 0x0, 1000x1001, 1000x600 | Screen resolution of the device (Width x Height) |
| show_recommendation | NoneType, bool | 1000 | 134 (13.4%) | 1 | True | Boolean indicating if the recommendation block was visible |
| store_id | str | 1000 | 0 (0.0%) | 62 | 7, 12, 6 | Store or Country code |
| time_stamp | str | 1000 | 0 (0.0%) | 1000 | 1590003478, 1590520073, 1590571209 | Unix epoch timestamp of the event |
| user_agent | str | 1000 | 0 (0.0%) | 315 | Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727), Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36, Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0 | Browser and OS information of the user |
| user_id_db | str | 1000 | 0 (0.0%) | 59 | , 482539, 494529 | Internal database ID of the logged-in user |
| utm_medium | NoneType, str | 1000 | 788 (78.8%) | 2 | retargeting, False | Marketing medium identifier from the URL |
| utm_source | NoneType, str | 1000 | 788 (78.8%) | 2 | criteo, False | Marketing source identifier from the URL |
| viewing_product_id | NoneType, int | 1000 | 900 (90.0%) | 99 | 98003, 96486, 85808 | ID of the product being viewed |

---
*Ghi chú: Bảng này được tạo tự động dựa trên mẫu dữ liệu hiện tại.*