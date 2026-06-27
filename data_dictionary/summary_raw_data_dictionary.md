# Data Dictionary: MongoDB: summary

Generated at: 2026-06-27 18:20:11

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_version | str | 1000 | 0 (0.0%) | 1 | 1.0 | Version of the tracking API |
| cart_products | list | 12 | 3 (25.0%) | 1 | N/A | Array of products currently in the user's cart |
| cart_products.amount | int | 4 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| cart_products.currency | str | 1 | 0 (0.0%) | 1 | £ | Currency code (e.g., EUR, USD, GBP) |
| cart_products.option | list | 20 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| cart_products.option.option_id | int | 29 | 0 (0.0%) | 24 | 261151, 261154, 152820 | Internal system identifier for option |
| cart_products.option.option_label | str | 29 | 0 (0.0%) | 2 | diamond, alloy | Localized display name/label for the field: option |
| cart_products.option.value_id | int | 29 | 0 (0.0%) | 24 | 2166253, 2166328, 1156867 | Internal system identifier for value |
| cart_products.option.value_label | str | 29 | 0 (0.0%) | 12 | Swarovsky Cristall, Weißgold 585, White Sapphire | Localized display name/label for the field: value |
| cart_products.price | str | 1 | 0 (0.0%) | 1 | 880.00 | Monetary value or price-related setting |
| cart_products.product_id | int | 20 | 0 (0.0%) | 15 | 103324, 96047, 97471 | Internal system identifier for product |
| cat_id | NoneType | 295 | 295 (100.0%) | 0 | N/A | Internal system identifier for cat |
| collect_id | str | 295 | 0 (0.0%) | 20 | , 4380, 159 | Internal system identifier for collect |
| collection | str | 1000 | 0 (0.0%) | 16 | view_product_detail, checkout, view_listing_page | Project collection name |
| currency | str | 6 | 0 (0.0%) | 5 | €, zł, kr | Currency code (e.g., EUR, USD, GBP) |
| current_url | str | 1000 | 0 (0.0%) | 782 | https://www.glamira.fr/glamira-pendant-viktor.html?alloy=yellow-375, https://www.glamira.com.au/customcheckout/onepage/payment/, https://www.glamira.es/alianzas/?gclid=CjwKCAjwt-L2BRA_EiwAacX32XIKXImV_rFgP1XrUgK-tjd9ibaONdePmEkZvIhJvkyD6y_2gbEAPxoCCEAQAvD_BwE | Full URL of the page where the event occurred |
| device_id | str | 1000 | 0 (0.0%) | 432 | beb2cacb-20af-4f05-9c03-c98e54a1b71a, b2d1024d-a62e-480d-ade8-20cf7f618270, b2cf91cd-456b-4bca-a1a7-a73fac8f4038 | Unique persistent identifier for the user's device |
| email_address | str | 1000 | 0 (0.0%) | 34 | pereira.vivien@yahoo.fr, Kodyjaden.n@hotmail.com, | User's email address if captured during the session |
| ip | str | 1000 | 0 (0.0%) | 410 | 37.170.17.183, 194.193.38.240, 212.237.237.184 | IP address of the user |
| is_paypal | NoneType | 6 | 6 (100.0%) | 0 | N/A | Flag indicating if PayPal was selected or used |
| key_search | NoneType | 4 | 4 (100.0%) | 0 | N/A | Search keywords entered by the user |
| local_time | str | 1000 | 0 (0.0%) | 452 | 2020-06-04 12:21:27, 2020-06-04 8:21:27, 2020-06-04 12:21:25 | Literal local time captured from the user's device |
| option | dict, list | 779 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| option.alloy | str | 295 | 0 (0.0%) | 16 | , white-585, yellow_white-silber_375 | Metal alloy specification |
| option.diamond | str | 295 | 0 (0.0%) | 23 | , diamond-Brillant, opal | Diamond specification or grade |
| option.option_id | str | 766 | 0 (0.0%) | 329 | 332084, , 57695 | Technical identifier for the option type |
| option.option_label | str | 771 | 0 (0.0%) | 8 | alloy, diamond, stone/diamonds | Human-readable label for the product option (e.g., Metal, Size) |
| option.quality | str | 53 | 0 (0.0%) | 4 | A, AAAA, AAA | Quality grade code for gems or materials |
| option.quality_label | str | 47 | 0 (0.0%) | 10 | I, AAAA, AAA | Display name for the quality grade |
| option.shapediamond | str | 295 | 0 (0.0%) | 6 | , 4397, 4163 | Shape of the diamond (e.g., Round, Princess) |
| option.value_id | str | 771 | 0 (0.0%) | 372 | 3279318, , 308213 | Technical identifier for the selected value |
| option.value_label | str | 771 | 0 (0.0%) | 43 | , diamond-Brillant, ruby | Human-readable label for the selected value (e.g., Rose Gold, 52) |
| order_id | int, str | 4 | 0 (0.0%) | 2 | , 720251727 | ID of the sales order if applicable |
| price | str | 6 | 0 (0.0%) | 6 | 1 278,00, 364,00, 1 099,00 | Price of the product during the event |
| product_id | str | 484 | 0 (0.0%) | 190 | 110474, 85796, 99316 | Unique identifier for the product |
| recommendation | bool | 281 | 0 (0.0%) | 1 | False | Flag for recommendation-related interactions |
| recommendation_clicked_position | int | 5 | 0 (0.0%) | 1 | 0 | Position in the UI where the recommendation was clicked |
| recommendation_product_id | str | 5 | 0 (0.0%) | 5 | 102110, 102107, 84776 | ID of the product recommended to the user |
| referrer_url | str | 1000 | 0 (0.0%) | 388 | https://www.glamira.fr/men-s-necklaces/, https://www.glamira.com.au/customcheckout/customer/login/address/1/, https://www.google.com/ | URL of the previous page that referred the user |
| resolution | str | 1000 | 0 (0.0%) | 58 | 375x667, 412x846, 360x780 | Screen resolution of the device (Width x Height) |
| show_recommendation | NoneType, str | 1000 | 194 (19.4%) | 2 | false, true | Boolean indicating if the recommendation block was visible |
| store_id | str | 1000 | 0 (0.0%) | 48 | 12, 29, 8 | Store or Country code |
| time_stamp | int | 1000 | 0 (0.0%) | 141 | 1591266092, 1591266091, 1591266090 | Unix epoch timestamp of the event |
| user_agent | str | 1000 | 0 (0.0%) | 204 | Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1, Mozilla/5.0 (Linux; Android 10; SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36, Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 | Browser and OS information of the user |
| user_id_db | str | 1000 | 0 (0.0%) | 34 | 502567, 503390, | Internal database ID of the logged-in user |
| utm_medium | bool, str | 281 | 0 (0.0%) | 3 | False, retargeting, autocomplete | Marketing medium identifier from the URL |
| utm_source | bool, str | 281 | 0 (0.0%) | 3 | False, criteo, recommendation | Marketing source identifier from the URL |
| viewing_product_id | str | 50 | 0 (0.0%) | 39 | 89454, 92291, 102107 | ID of the product being viewed |

---
*Note: This table is automatically generated based on the current data sample.*