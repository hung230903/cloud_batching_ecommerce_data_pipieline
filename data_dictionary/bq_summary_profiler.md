# Data Dictionary: BigQuery: summary

Generated at: 2026-06-27 18:20:24

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_version | str | 1000 | 0 (0.0%) | 1 | 1.0 | Version of the tracking API |
| cart_products | dict | 1000 | 0 (0.0%) | 1 | N/A | Array of products currently in the user's cart |
| cart_products.list | list | 1000 | 1000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| category_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Unique ID of the primary category |
| collection | str | 1000 | 0 (0.0%) | 1 | add_to_cart_action | Project collection name |
| collection_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Unique ID of the collection |
| currency | NoneType, str | 1000 | 3 (0.3%) | 34 | AU $, ₩, ￥ | Currency code (e.g., EUR, USD, GBP) |
| current_url | str | 1000 | 0 (0.0%) | 890 | https://www.glamira.com.au/glamira-ring-zanyria.html?diamond=opal&gclid=CjwKCAjw1v_0BRAkEiwALFkj5jVTCBbVzZ0-rq532bE2wDE9YnOzsUuSIAIh5d0X-uKIIbKoFg4z6RoCXO0QAvD_BwE&stone3=diamond-Brillant&alloy=white-585&stone2=diamond-Brillant, https://www.glamira.com.au/glamira-ring-larina.html?diamond=diamond-Brillant, https://www.glamira.com.au/womens-ring-classic-inspiration-2mm.html?alloy=white-375?stone=diamond-brillant | Full URL of the page where the event occurred |
| device_id | str | 1000 | 0 (0.0%) | 489 | b56e016f-6276-4447-8fa5-3c92dda51eff, a6f7cb76-2ffd-407c-96fa-9c9604b2b7a9, 90c5805e-7107-47d8-b137-58ce46afd1a1 | Unique persistent identifier for the user's device |
| email_address | str | 1000 | 0 (0.0%) | 59 | , bonnie.isiah@gmail.com, oaykiran@hotmail.com | User's email address if captured during the session |
| ip | str | 1000 | 0 (0.0%) | 455 | 1.132.108.236, 1.136.104.225, 1.136.111.166 | IP address of the user |
| is_paypal | NoneType, bool | 1000 | 997 (99.7%) | 1 | True | Flag indicating if PayPal was selected or used |
| key_search | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Search keywords entered by the user |
| local_time | str | 1000 | 0 (0.0%) | 943 | 2020-04-23 3:10:16, 2020-04-23 3:43:1, 2020-04-23 5:51:45 | Literal local time captured from the user's device |
| option | dict | 1000 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| option.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| option.list.element | dict | 2000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| option.list.element.alloy | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.category_id | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Internal system identifier for category |
| option.list.element.collection | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Project collection name |
| option.list.element.collection_id | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Internal system identifier for collection |
| option.list.element.diamond | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.finish | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.option_id | NoneType, str | 2000 | 365 (18.2%) | 942 | 261154, 261151, 160507 | Internal system identifier for option |
| option.list.element.option_label | str | 2000 | 0 (0.0%) | 2 | alloy, diamond | Localized display name/label for the field: option |
| option.list.element.pearlcolor | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.price | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| option.list.element.quality | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.quality_label | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Localized display name/label for the field: quality |
| option.list.element.shapediamond | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| option.list.element.stone | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | List of gemstone configurations currently assigned to the product |
| option.list.element.value_id | NoneType, str | 2000 | 365 (18.2%) | 1056 | 2166328, 2166253, 1229030 | Internal system identifier for value |
| option.list.element.value_label | NoneType | 2000 | 2000 (100.0%) | 0 | N/A | Localized display name/label for the field: value |
| order_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | ID of the sales order if applicable |
| price | NoneType, str | 1000 | 3 (0.3%) | 729 | 1,141.00, 2,316.00, 165.00 | Price of the product during the event |
| product_id | str | 1000 | 0 (0.0%) | 582 | 103324, 96647, 93107 | Unique identifier for the product |
| recommendation | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Flag for recommendation-related interactions |
| recommendation_clicked_position | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Position in the UI where the recommendation was clicked |
| recommendation_product_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | ID of the product recommended to the user |
| recommendation_product_position | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Index of the product in the recommendation list |
| referrer_url | str | 1000 | 0 (0.0%) | 706 | https://www.google.com/, https://www.glamira.com.au/checkout/cart/, https://www.glamira.com.au/county/recommendation/list/id/93107/alloy/white-375/stone/diamond-brillant/finish/sandy/profile/prb/price/289.00 | URL of the previous page that referred the user |
| resolution | str | 1000 | 0 (0.0%) | 62 | 412x892, 360x740, 414x896 | Screen resolution of the device (Width x Height) |
| show_recommendation | NoneType, bool | 1000 | 48 (4.8%) | 1 | True | Boolean indicating if the recommendation block was visible |
| store_id | str | 1000 | 0 (0.0%) | 55 | 29, 49, 27 | Store or Country code |
| time_stamp | int | 1000 | 0 (0.0%) | 998 | 1587619037, 1587620779, 1587628367 | Unix epoch timestamp of the event |
| user_agent | str | 1000 | 0 (0.0%) | 210 | Mozilla/5.0 (Linux; Android 10; SM-A305YN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36, Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36, Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1 | Browser and OS information of the user |
| user_id_db | str | 1000 | 0 (0.0%) | 59 | , 484371, 485979 | Internal database ID of the logged-in user |
| utm_medium | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Marketing medium identifier from the URL |
| utm_source | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Marketing source identifier from the URL |
| viewing_product_id | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | ID of the product being viewed |

---
*Note: This table is automatically generated based on the current data sample.*