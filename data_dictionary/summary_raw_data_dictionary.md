# Data Dictionary: MongoDB: summary

Generated at: 2026-04-22 16:14:06

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_version | str | 1000 | 0 (0.0%) | 1 | 1.0 | Version of the tracking API |
| cart_products | list | 16 | 2 (12.5%) | 1 | N/A | Array of products currently in the user's cart |
| cart_products.amount | int | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| cart_products.currency | str | 1 | 0 (0.0%) | 1 | £ | Currency code (e.g., EUR, USD, GBP) |
| cart_products.option | list | 23 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| cart_products.option.option_id | int | 37 | 0 (0.0%) | 28 | 152820, 255804, 255803 | Internal system identifier for option |
| cart_products.option.option_label | str | 37 | 0 (0.0%) | 2 | alloy, diamond | Localized display name/label for the field: option |
| cart_products.option.value_id | int | 37 | 0 (0.0%) | 28 | 1156867, 2119119, 2119094 | Internal system identifier for value |
| cart_products.option.value_label | str | 37 | 0 (0.0%) | 9 | Weißgold 585, White Sapphire, Rot-Weißgold 585 | Localized display name/label for the field: value |
| cart_products.price | str | 1 | 0 (0.0%) | 1 | 880.00 | Monetary value or price-related setting |
| cart_products.product_id | int | 23 | 0 (0.0%) | 16 | 96047, 102429, 111314 | Internal system identifier for product |
| cat_id | NoneType | 309 | 309 (100.0%) | 0 | N/A | Internal system identifier for cat |
| collect_id | str | 309 | 0 (0.0%) | 22 | , 4110, 5170 | Internal system identifier for collect |
| collection | str | 1000 | 0 (0.0%) | 17 | view_product_detail, view_listing_page, view_landing_page | Project collection name |
| currency | str | 4 | 0 (0.0%) | 3 | €, kr, £ | Currency code (e.g., EUR, USD, GBP) |
| current_url | str | 1000 | 0 (0.0%) | 831 | https://www.glamira.at/glamira-initialen-anhanger-j.html, https://www.glamira.fr/alliances-de-mariage/?stone2=diamond&gclid=CjwKCAjwt-L2BRA_EiwAacX32egIsffoFksA4MtfCMpZyeshlgW7voRJdsG0dkVCithwQ5YnOZwAChoCLtEQAvD_BwE, https://www.glamira.de/verlobungsringe/ | Full URL of the page where the event occurred |
| device_id | str | 1000 | 0 (0.0%) | 469 | c3230f73-1486-453f-a76a-678b1e468ef8, 4147dc41-1442-4e43-b54c-f241d3d2b31a, 86e7d5ea-3fa7-46bf-add1-fdfdbdaddec7 | Unique persistent identifier for the user's device |
| email_address | str | 1000 | 0 (0.0%) | 33 | , ay.perera@gmail.com, Dcoombs@bam.co.uk | User's email address if captured during the session |
| ip | str | 1000 | 0 (0.0%) | 443 | 91.141.3.33, 79.90.160.80, 80.187.101.129 | IP address of the user |
| is_paypal | NoneType | 4 | 4 (100.0%) | 0 | N/A | Flag indicating if PayPal was selected or used |
| key_search | NoneType | 5 | 5 (100.0%) | 0 | N/A | Search keywords entered by the user |
| local_time | str | 1000 | 0 (0.0%) | 527 | 2020-06-04 12:19:42, 2020-06-04 12:19:48, 2020-06-04 8:15:27 | Literal local time captured from the user's device |
| option | dict, list | 785 | 0 (0.0%) | 1 | N/A | User-selected product option in interaction events |
| option.alloy | str | 309 | 0 (0.0%) | 15 | , white-585, white-750 | Metal alloy specification |
| option.diamond | str | 309 | 0 (0.0%) | 19 | , diamond-Brillant, ruby | Diamond specification or grade |
| option.option_id | str | 775 | 0 (0.0%) | 376 | 245675, 245674, 2750186 | Technical identifier for the option type |
| option.option_label | str | 777 | 0 (0.0%) | 9 | alloy, diamond, stone2 | Human-readable label for the product option (e.g., Metal, Size) |
| option.quality | str | 39 | 0 (0.0%) | 4 | AAAA, AAA, AA | Quality grade code for gems or materials |
| option.quality_label | str | 33 | 0 (0.0%) | 8 | AAAA, AAA, VVS | Display name for the quality grade |
| option.shapediamond | str | 309 | 0 (0.0%) | 6 | , 3597, 4408 | Shape of the diamond (e.g., Round, Princess) |
| option.value_id | str | 776 | 0 (0.0%) | 417 | 2039041, 2039024, 2750179 | Technical identifier for the selected value |
| option.value_label | str | 777 | 0 (0.0%) | 46 | , diamond-Brillant, white-platin | Human-readable label for the selected value (e.g., Rose Gold, 52) |
| order_id | int, str | 3 | 0 (0.0%) | 2 | , 720251727 | ID of the sales order if applicable |
| price | str | 4 | 0 (0.0%) | 4 | 375,00, 4 576,00, 213.00 | Price of the product during the event |
| product_id | str | 476 | 0 (0.0%) | 227 | 90186, 84843, 90657 | Unique identifier for the product |
| recommendation | bool | 294 | 0 (0.0%) | 1 | False | Flag for recommendation-related interactions |
| recommendation_clicked_position | int | 3 | 0 (0.0%) | 1 | 0 | Position in the UI where the recommendation was clicked |
| recommendation_product_id | str | 3 | 0 (0.0%) | 3 | 102110, 102107, 84776 | ID of the product recommended to the user |
| referrer_url | str | 1000 | 0 (0.0%) | 416 | https://www.glamira.at/glamira-initialen-anhanger-g.html?alloy=yellow-375&diamond=ruby, , https://www.glamira.de/glamira-ring-zanyria.html?itm_source=recommendation&itm_medium=sorting&alloy=yellow-585 | URL of the previous page that referred the user |
| resolution | str | 1000 | 0 (0.0%) | 66 | 412x846, 412x892, 414x896 | Screen resolution of the device (Width x Height) |
| show_recommendation | NoneType, str | 1000 | 183 (18.3%) | 2 | false, true | Boolean indicating if the recommendation block was visible |
| store_id | str | 1000 | 0 (0.0%) | 49 | 9, 12, 6 | Store or Country code |
| time_stamp | int | 1000 | 0 (0.0%) | 164 | 1591265989, 1591265988, 1591265986 | Unix epoch timestamp of the event |
| user_agent | str | 1000 | 0 (0.0%) | 229 | Mozilla/5.0 (Linux; Android 9; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36, Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A505FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.0 Chrome/67.0.3396.87 Mobile Safari/537.36, Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.5;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5] | Browser and OS information of the user |
| user_id_db | str | 1000 | 0 (0.0%) | 33 | , 501514, 501139 | Internal database ID of the logged-in user |
| utm_medium | bool, str | 294 | 0 (0.0%) | 3 | False, retargeting, sorting | Marketing medium identifier from the URL |
| utm_source | bool, str | 294 | 0 (0.0%) | 3 | False, criteo, recommendation | Marketing source identifier from the URL |
| viewing_product_id | str | 49 | 0 (0.0%) | 45 | 97868, 97916, 92735 | ID of the product being viewed |

---
*Ghi chú: Bảng này được tạo tự động dựa trên mẫu dữ liệu hiện tại.*