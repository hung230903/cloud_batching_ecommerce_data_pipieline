# Data Dictionary: Local File: product_info_21.json

Generated at: 2026-06-27 18:20:18

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| attribute_set | str | 500 | 0 (0.0%) | 3 | diamonds, trauring, default | Name of the attribute set |
| attribute_set_id | int | 500 | 0 (0.0%) | 3 | 55, 26, 4 | ID of the product's attribute set |
| category_id | int, str | 500 | 0 (0.0%) | 11 | 617, 601, 61 | Unique ID of the primary category |
| category_name | str | 500 | 0 (0.0%) | 84 | Ringe, COLGANTES, Vėriniai | Display name of the category |
| collection | str | 500 | 0 (0.0%) | 34 | fashion, flower, symbols | Project collection name |
| collection_id | NoneType, str | 500 | 1 (0.2%) | 33 | 4378, 4716, 5157 | Unique ID of the collection |
| colour | list | 500 | 1 (0.2%) | 1 | N/A | Metal and Alloy configuration options |
| colour.colour_code | str | 10205 | 0 (0.0%) | 7 | white_yellow, yellow_white, white | N/A (See parent components for context) |
| colour.colour_label | str | 10205 | 0 (0.0%) | 186 | Weiß/Gelb, Gelb/Weiß, Weiß | Localized display name/label for the field: colour |
| colour.default_title | str | 10205 | 0 (0.0%) | 25 | Weiß-Gelbgold 375, Gelb-Weißgold 375, Weißgold 375 | Localized display name/label for the field: default |
| colour.is_default | bool | 10205 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| colour.metal | str | 10205 | 0 (0.0%) | 6 | 375, 585, 750 | Metal material code |
| colour.metal_label | str | 10205 | 0 (0.0%) | 142 | Gold 375 <span class='seperate-line'>-</span> <span>9K</span>, Gold 585 <span class='seperate-line'>-</span> <span>14K</span>, Gold 750 <span class='seperate-line'>-</span> <span>18K</span> | Display name of the metal material |
| colour.option_id | str | 10205 | 0 (0.0%) | 499 | 250432, 250697, 170054 | Internal system identifier for option |
| colour.option_type_id | str | 10205 | 0 (0.0%) | 10205 | 2081601, 2081602, 2081603 | Internal system identifier for option_type |
| colour.price | str | 10205 | 0 (0.0%) | 71 | 0.00, 31.00, 76.00 | Price adjustment for this metal selection |
| colour.price_type | str | 10205 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| colour.sku | str | 10205 | 0 (0.0%) | 24 | white_yellow-375, yellow_white-375, white-375 | Unique Stock Keeping Unit code |
| colour.store_title | str | 10205 | 0 (0.0%) | 730 | Weiß & Gelbgold 375, 375 Gelb & Weißgold, Weißgold 375 | Localized display name/label for the field: store |
| colour.title | str | 10205 | 0 (0.0%) | 730 | Weiß & Gelbgold 375, 375 Gelb & Weißgold, Weißgold 375 | N/A (See parent components for context) |
| custom | list | 500 | 1 (0.2%) | 1 | N/A | Miscellaneous custom options |
| custom.default_title | str | 2550 | 0 (0.0%) | 31 | Yes, No, 10.0 mm | Localized display name/label for the field: default |
| custom.is_default | bool | 2550 | 0 (0.0%) | 2 | True, False | Boolean flag/binary status: default |
| custom.option_id | str | 2550 | 0 (0.0%) | 1002 | 344008, 344080, 344116 | Internal system identifier for option |
| custom.option_type_id | str | 2550 | 0 (0.0%) | 2550 | 3386466, 3419233, 3386538 | Internal system identifier for option_type |
| custom.price | str | 2550 | 0 (0.0%) | 7 | 0.00, 3.00, -27.00 | Monetary value or price-related setting |
| custom.price_type | str | 2550 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| custom.sku | str | 2550 | 0 (0.0%) | 32 | rhodium-plated-y, rhodium-plated-n, w10 | Unique Stock Keeping Unit code |
| custom.store_title | str | 2550 | 0 (0.0%) | 204 | Ja, Nein, Sí | Localized display name/label for the field: store |
| custom.title | str | 2550 | 0 (0.0%) | 204 | Ja, Nein, Sí | N/A (See parent components for context) |
| fixed_silver_weight | int | 500 | 0 (0.0%) | 1 | 0 | Fixed silver weight for silver items |
| gender | bool, str | 500 | 0 (0.0%) | 3 | men, women, False | Target gender |
| gold_weight | NoneType, str | 500 | 1 (0.2%) | 218 | 1.911, 2.0046, 0.4056 | Estimated gold weight of the metal part |
| material_design | NoneType | 500 | 500 (100.0%) | 0 | N/A | Design code for the material/alloy |
| max_price | str | 500 | 0 (0.0%) | 471 | € 6.908,00, CLP 9.676.786,00, 2 052,00 € | Formatted highest possible price for the product |
| media_image | dict | 500 | 0 (0.0%) | 1 | N/A | Product images container |
| media_image.default_position | int | 500 | 0 (0.0%) | 3 | 1, 3, 2 | N/A (See parent components for context) |
| media_image.image_load_type | NoneType, str | 500 | 452 (90.4%) | 1 | layer | N/A (See parent components for context) |
| media_image.image_view_types | list | 500 | 438 (87.6%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.metadata | str | 62 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.position | list | 62 | 0 (0.0%) | 1 | N/A | Display sequence or sorting order |
| media_image.image_view_types.type | str | 62 | 0 (0.0%) | 1 | try_on_with_ai | N/A (See parent components for context) |
| media_image.images | list | 500 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.area_view | NoneType, str | 1997 | 357 (17.9%) | 2 | grid, thumb | N/A (See parent components for context) |
| media_image.images.config | NoneType | 1997 | 1997 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.image_view | str | 1997 | 0 (0.0%) | 3 | general, 3d, compare | N/A (See parent components for context) |
| media_image.images.is_default | NoneType, bool | 1997 | 92 (4.6%) | 2 | True, False | Boolean flag/binary status: default |
| media_image.images.is_feature | bool | 1997 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: feature |
| media_image.images.is_video | NoneType | 1997 | 1997 (100.0%) | 0 | N/A | Boolean flag/binary status: video |
| media_image.images.label | str | 1997 | 0 (0.0%) | 500 | Herrenring Bellanca, Colgante de Mujer Costa, Vaiko pakabukas Breda | N/A (See parent components for context) |
| media_image.images.large_image_url | str | 1997 | 0 (0.0%) | 1997 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg | Web URL link to the resource: large_image |
| media_image.images.media_type | str | 1997 | 0 (0.0%) | 1 | image | N/A (See parent components for context) |
| media_image.images.medium_image_url | str | 1997 | 0 (0.0%) | 1997 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516 | Web URL link to the resource: medium_image |
| media_image.images.medium_middle_image_url | str | 1997 | 0 (0.0%) | 1997 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.images.meta | NoneType | 1997 | 1997 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.placeholder_alt | str | 1242 | 0 (0.0%) | 1242 | ALLOY_TITLE Rund STONE_TITLE Herrenring Bellanca view 1, ALLOY_TITLE Rund STONE_TITLE Herrenring Bellanca view 2, ALLOY_TITLE Rund STONE_TITLE Herrenring Bellanca view 3 | N/A (See parent components for context) |
| media_image.images.position | NoneType, int | 1997 | 92 (4.6%) | 6 | 1, 2, 3 | Display sequence or sorting order |
| media_image.images.small_image_url | str | 1997 | 0 (0.0%) | 1997 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220 | Web URL link to the resource: small_image |
| media_image.images.sticky_image_url | str | 1997 | 0 (0.0%) | 1997 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/Bellancav1/diamond/diamond-Brillant_AAA/stone2/diamond-Brillant_AAA/alloycolour/yellow_white.jpg?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.images.watermark_link | NoneType | 1997 | 1997 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.lcpMediaUrl | NoneType, str | 500 | 498 (99.6%) | 2 | https://www.glamira.co.nz/media, https://www.glamira.com.au/media | N/A (See parent components for context) |
| media_image.paths | dict | 500 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.paths.large_image_url | str | 500 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/, https://cdn.glamira.cn/media/product/newgeneration/, https://cdn-media.glamira.com/media/catalog/product/ | Web URL link to the resource: large_image |
| media_image.paths.medium_image_url | str | 500 | 0 (0.0%) | 4 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/?width=700&height=700 | Web URL link to the resource: medium_image |
| media_image.paths.medium_middle_image_url | str | 500 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/catalog/product/ | Web URL link to the resource: medium_middle_image |
| media_image.paths.small_image_url | str | 500 | 0 (0.0%) | 4 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/?width=110&height=110 | Web URL link to the resource: small_image |
| media_image.paths.sticky_image_url | str | 500 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/catalog/product/ | Web URL link to the resource: sticky_image |
| media_image.sku_image | NoneType, str | 500 | 1 (0.2%) | 435 | Bellancav1, Costa, EPK-06 | URL for the main SKU image |
| media_image.total_thumbs | int, str | 500 | 0 (0.0%) | 4 | 6, 4, 4 | N/A (See parent components for context) |
| media_video | dict | 500 | 0 (0.0%) | 1 | N/A | Product video container |
| media_video.videos | list | 500 | 140 (28.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.file_name | str | 393 | 0 (0.0%) | 389 | BELLANCA.mp4, COSTA.mp4, Breda.mp4 | N/A (See parent components for context) |
| media_video.videos.hidden | bool | 393 | 0 (0.0%) | 1 | False | N/A (See parent components for context) |
| media_video.videos.id | str | 393 | 0 (0.0%) | 2 | 1191, 1392 | N/A (See parent components for context) |
| media_video.videos.label | str | 393 | 0 (0.0%) | 360 | Herrenring Bellanca, Colgante de Mujer Costa, Vaiko pakabukas Breda | N/A (See parent components for context) |
| media_video.videos.media_type | str | 393 | 0 (0.0%) | 1 | video | N/A (See parent components for context) |
| media_video.videos.name | str | 393 | 0 (0.0%) | 2 | video, video2 | N/A (See parent components for context) |
| media_video.videos.url | str | 393 | 0 (0.0%) | 393 | https://cdn-media.glamira.com/media/product/layer/bellancav1/BELLANCA.mp4, https://cdn-media.glamira.com/media/product/layer/costa/COSTA.mp4, https://cdn-media.glamira.com/media/product/layer/epk-06/Breda.mp4 | N/A (See parent components for context) |
| min_price | str | 500 | 0 (0.0%) | 452 | € 613,00, CLP 757.211,00, 214,00 € | Formatted lowest possible price for the product |
| none_metal_weight | int | 500 | 0 (0.0%) | 1 | 0 | Weight of the non-metal components |
| options | list | 500 | 1 (0.2%) | 1 | N/A | Raw JSON configuration options containing all possible choices |
| options.custom_size | str | 3799 | 0 (0.0%) | 2 | 0, 1 | N/A (See parent components for context) |
| options.default_price | NoneType, str | 3799 | 3481 (91.6%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.default_price_type | NoneType, str | 3799 | 3481 (91.6%) | 1 | fixed | Monetary value or price-related setting |
| options.default_title | str | 3799 | 0 (0.0%) | 25 | Ring Size, Stone/Diamonds, Stone 2 | Localized display name/label for the field: default |
| options.default_value | NoneType | 3799 | 3799 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.detail_title | str | 3799 | 0 (0.0%) | 437 | Ringgröße, Hauptstein, Stein 2 | Localized display name/label for the field: detail |
| options.engraving_position | NoneType, str | 3799 | 3225 (84.9%) | 2 | inside, | N/A (See parent components for context) |
| options.engraving_type | NoneType, str | 3799 | 3225 (84.9%) | 4 | ring, herrenring, damenring | N/A (See parent components for context) |
| options.extension_attributes | dict | 3799 | 3799 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.file_extension | NoneType | 3799 | 3799 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.group | str | 3799 | 0 (0.0%) | 8 | ringsize, stone, alloy | N/A (See parent components for context) |
| options.image_size_x | NoneType, str | 3799 | 2814 (74.1%) | 1 | 0 | N/A (See parent components for context) |
| options.image_size_y | NoneType, str | 3799 | 2814 (74.1%) | 1 | 0 | N/A (See parent components for context) |
| options.is_require | int | 3799 | 0 (0.0%) | 2 | 1, 0 | Boolean flag/binary status: require |
| options.max_characters | NoneType, str | 3799 | 2649 (69.7%) | 2 | 0, 25 | N/A (See parent components for context) |
| options.max_characters_wrong | NoneType, str | 3799 | 3758 (98.9%) | 1 | 0 | N/A (See parent components for context) |
| options.option_id | str | 3799 | 0 (0.0%) | 3799 | 250430, 250431, 250437 | Internal system identifier for option |
| options.part_type | NoneType, str | 3799 | 584 (15.4%) | 19 | default_ringsize, stone1, stone2 | N/A (See parent components for context) |
| options.price | NoneType, str | 3799 | 3481 (91.6%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.price_type | NoneType, str | 3799 | 3481 (91.6%) | 1 | fixed | Monetary value or price-related setting |
| options.product_id | str | 3799 | 0 (0.0%) | 499 | 97372, 97444, 97480 | Internal system identifier for product |
| options.sku | NoneType, str | 3799 | 3635 (95.7%) | 1 | N/A | Unique Stock Keeping Unit code |
| options.sort_order | str | 3799 | 0 (0.0%) | 20 | 0, 10, 15 | Display sequence or sorting order |
| options.stones | list | 327 | 2 (0.6%) | 1 | N/A | N/A (See parent components for context) |
| options.stones.carat | str | 463 | 0 (0.0%) | 44 | 0.0250, 0.0050, 0.0060 | N/A (See parent components for context) |
| options.stones.clarity | NoneType | 463 | 463 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.stones.diameter | str | 463 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | N/A (See parent components for context) |
| options.stones.id | str | 463 | 0 (0.0%) | 463 | 2135, 10546, 12097 | N/A (See parent components for context) |
| options.stones.option_id | str | 463 | 0 (0.0%) | 112 | 250431, 250437, 250696 | Internal system identifier for option |
| options.stones.part_type | str | 463 | 0 (0.0%) | 4 | stone1, stone2, womenstone | N/A (See parent components for context) |
| options.stones.product_id | str | 463 | 0 (0.0%) | 218 | 97372, 97444, 97408 | Internal system identifier for product |
| options.stones.qty | str | 463 | 0 (0.0%) | 60 | 1, 3, 7 | Quantity or count of items |
| options.stones.shape | str | 463 | 0 (0.0%) | 10 | 1, 11, 7 | N/A (See parent components for context) |
| options.store_id | int | 3799 | 0 (0.0%) | 48 | 9, 85, 57 | Internal system identifier for store |
| options.store_price | NoneType | 3799 | 3799 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.store_price_type | NoneType | 3799 | 3799 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.store_title | NoneType, str | 3799 | 3784 (99.6%) | 7 | Stone/Diamonds, Alloy/Colour, Rhodium Plated | Localized display name/label for the field: store |
| options.title | str | 3799 | 0 (0.0%) | 447 | Ringgröße, Hauptstein, Stein 2 | N/A (See parent components for context) |
| options.type | str | 3799 | 0 (0.0%) | 13 | ctsize, stone, alloy | N/A (See parent components for context) |
| options.use_stone | NoneType | 3799 | 3799 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values | list | 3799 | 205 (5.4%) | 1 | N/A | N/A (See parent components for context) |
| options.values.average_size | dict | 276 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.average_size.diameter | str | 276 | 0 (0.0%) | 2 | 19,1, 16,5 | N/A (See parent components for context) |
| options.values.average_size.value | str | 276 | 0 (0.0%) | 2 | 19,1, 16,5 | N/A (See parent components for context) |
| options.values.colour_code | str | 10205 | 0 (0.0%) | 7 | white_yellow, yellow_white, white | N/A (See parent components for context) |
| options.values.colour_label | str | 10205 | 0 (0.0%) | 186 | Weiß/Gelb, Gelb/Weiß, Weiß | Localized display name/label for the field: colour |
| options.values.configure_quality | str | 4910 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| options.values.data_stones | list | 4910 | 2 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.carat | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.carat.default_label | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | Localized display name/label for the field: default |
| options.values.data_stones.carat.default_option_title | str | 6310 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.data_stones.carat.label | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | N/A (See parent components for context) |
| options.values.data_stones.carat.option_title | str | 6310 | 0 (0.0%) | 15 | Karat, Quilates, Carat | Localized display name/label for the field: option |
| options.values.data_stones.carat.value | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | N/A (See parent components for context) |
| options.values.data_stones.certificate | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.certificate.default_label | str | 6310 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.data_stones.certificate.default_option_title | str | 6310 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.data_stones.certificate.label | str | 6310 | 0 (0.0%) | 22 | GL Zertifiziert, GL Certificado, GL Certified | N/A (See parent components for context) |
| options.values.data_stones.certificate.option_title | str | 6310 | 0 (0.0%) | 21 | Zertifizierung, Certificado, Certification | Localized display name/label for the field: option |
| options.values.data_stones.certificate.value | str | 6310 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.data_stones.clarity | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.clarity.default_label | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | Localized display name/label for the field: default |
| options.values.data_stones.clarity.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.data_stones.clarity.label | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.clarity.option_title | str | 6310 | 0 (0.0%) | 21 | Reinheit, Calidad, Stone Clarity | Localized display name/label for the field: option |
| options.values.data_stones.clarity.value | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.colour | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.colour.default_label | str | 6310 | 0 (0.0%) | 22 | H, Black, Green | Localized display name/label for the field: default |
| options.values.data_stones.colour.default_option_title | str | 6310 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.data_stones.colour.label | str | 6310 | 0 (0.0%) | 187 | H, Schwarz, Grün | N/A (See parent components for context) |
| options.values.data_stones.colour.option_title | str | 6310 | 0 (0.0%) | 21 | Farbe, Color, Colour | Localized display name/label for the field: option |
| options.values.data_stones.colour.value | str | 6310 | 0 (0.0%) | 22 | H, Black, Green | N/A (See parent components for context) |
| options.values.data_stones.cut | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.cut.default_label | str | 6310 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| options.values.data_stones.cut.default_option_title | str | 6310 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.data_stones.cut.label | str | 6310 | 0 (0.0%) | 40 | Ausgezeichnet, Sehr gut, Excelente | N/A (See parent components for context) |
| options.values.data_stones.cut.option_title | str | 6310 | 0 (0.0%) | 20 | Schliff, Corte, Cut | Localized display name/label for the field: option |
| options.values.data_stones.cut.value | str | 6310 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| options.values.data_stones.diameter | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.diameter.default_label | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | Localized display name/label for the field: default |
| options.values.data_stones.diameter.default_option_title | str | 6310 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.data_stones.diameter.label | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | N/A (See parent components for context) |
| options.values.data_stones.diameter.option_title | str | 6310 | 0 (0.0%) | 17 | Durchmesser, Diámetro, Diameter | Localized display name/label for the field: option |
| options.values.data_stones.diameter.value | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | N/A (See parent components for context) |
| options.values.data_stones.origin | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.origin.default_label | NoneType, str | 6310 | 5660 (89.7%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.values.data_stones.origin.default_option_title | str | 6310 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.data_stones.origin.label | str | 6310 | 0 (0.0%) | 25 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| options.values.data_stones.origin.option_title | str | 6310 | 0 (0.0%) | 27 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| options.values.data_stones.origin.value | NoneType, str | 6310 | 5660 (89.7%) | 2 | african, heated | N/A (See parent components for context) |
| options.values.data_stones.origin_colour | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.origin_colour.default_label | NoneType, str | 6310 | 5764 (91.3%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.values.data_stones.origin_colour.default_option_title | str | 6310 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.data_stones.origin_colour.label | str | 6310 | 0 (0.0%) | 16 | , Farblich Behandelt, Natürliche Steine | N/A (See parent components for context) |
| options.values.data_stones.origin_colour.option_title | str | 6310 | 0 (0.0%) | 23 | Farbursprung, Origen del color, Colour Origin | Localized display name/label for the field: option |
| options.values.data_stones.origin_colour.value | NoneType, str | 6310 | 5764 (91.3%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.values.data_stones.qty | dict | 6310 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.data_stones.qty.default_label | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | Localized display name/label for the field: default |
| options.values.data_stones.qty.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.data_stones.qty.label | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | N/A (See parent components for context) |
| options.values.data_stones.qty.option_title | str | 6310 | 0 (0.0%) | 22 | Anzahl der Steine, Cantidad de piedras, Quantity of stones | Localized display name/label for the field: option |
| options.values.data_stones.qty.value | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | N/A (See parent components for context) |
| options.values.data_stones.quality | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.quality.default_label | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | Localized display name/label for the field: default |
| options.values.data_stones.quality.default_option_title | str | 6310 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.data_stones.quality.label | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.quality.option_title | str | 6310 | 0 (0.0%) | 20 | Qualität, Calidad, Quality | Localized display name/label for the field: option |
| options.values.data_stones.quality.value | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.shape | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.shape.default_label | str | 6310 | 0 (0.0%) | 10 | Round, Princess, Emerald | Localized display name/label for the field: default |
| options.values.data_stones.shape.default_option_title | str | 6310 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.data_stones.shape.label | str | 6310 | 0 (0.0%) | 37 | Rund, Redondo, Princesa | N/A (See parent components for context) |
| options.values.data_stones.shape.option_title | str | 6310 | 0 (0.0%) | 17 | Schliffform, Forma, Shape | Localized display name/label for the field: option |
| options.values.data_stones.shape.value | str | 6310 | 0 (0.0%) | 10 | 1, 11, 7 | N/A (See parent components for context) |
| options.values.data_stones.stone_name | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_name.default_label | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.data_stones.stone_name.default_option_title | str | 6310 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.data_stones.stone_name.label | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_name.option_title | str | 6310 | 0 (0.0%) | 17 | Name, Nombre, Jméno | Localized display name/label for the field: option |
| options.values.data_stones.stone_name.value | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_type | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_type.default_label | str | 6310 | 0 (0.0%) | 50 | Diamond, Black Diamond, Emerald | Localized display name/label for the field: default |
| options.values.data_stones.stone_type.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.data_stones.stone_type.label | str | 6310 | 0 (0.0%) | 465 | Diamant, Schwarzer Diamant, Smaragd | N/A (See parent components for context) |
| options.values.data_stones.stone_type.option_title | str | 6310 | 0 (0.0%) | 17 | Steinarten, Con Piedras, Stone Type | Localized display name/label for the field: option |
| options.values.data_stones.stone_type.value | str | 6310 | 0 (0.0%) | 50 | diamond-Brillant, blackdiamond, emerald | N/A (See parent components for context) |
| options.values.data_stones.total_carat | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.total_carat.default_label | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | Localized display name/label for the field: default |
| options.values.data_stones.total_carat.default_option_title | str | 6310 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.values.data_stones.total_carat.label | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | N/A (See parent components for context) |
| options.values.data_stones.total_carat.option_title | str | 6310 | 0 (0.0%) | 27 | Karat, Steinkarat insgesamt, Total de quilates de la piedra | Localized display name/label for the field: option |
| options.values.data_stones.total_carat.value | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | N/A (See parent components for context) |
| options.values.default_quality | NoneType, str | 4910 | 2747 (55.9%) | 6 | AAA, AAAAA, AAAA | N/A (See parent components for context) |
| options.values.default_title | str | 22840 | 0 (0.0%) | 131 | Diamond, Black Diamond, Emerald | Localized display name/label for the field: default |
| options.values.is_default | NoneType, bool, int | 23099 | 50 (0.2%) | 2 | True, False | Boolean flag/binary status: default |
| options.values.max_characters | str | 17 | 0 (0.0%) | 1 | 25 | N/A (See parent components for context) |
| options.values.max_characters_wrong | NoneType | 17 | 17 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.metal | str | 10205 | 0 (0.0%) | 6 | 375, 585, 750 | N/A (See parent components for context) |
| options.values.metal_label | str | 10205 | 0 (0.0%) | 142 | Gold 375 <span class='seperate-line'>-</span> <span>9K</span>, Gold 585 <span class='seperate-line'>-</span> <span>14K</span>, Gold 750 <span class='seperate-line'>-</span> <span>18K</span> | Localized display name/label for the field: metal |
| options.values.name | str | 276 | 0 (0.0%) | 19 | EU, US, UK | N/A (See parent components for context) |
| options.values.option_id | str | 22840 | 0 (0.0%) | 3368 | 250431, 250437, 250432 | Internal system identifier for option |
| options.values.option_type_id | int, str | 22840 | 0 (0.0%) | 21729 | 2081587, 2081597, 2081590 | Internal system identifier for option_type |
| options.values.price | int, str | 22840 | 0 (0.0%) | 1192 | 23.00, 8.00, 5.00 | Monetary value or price-related setting |
| options.values.price_type | str | 22840 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| options.values.ringsize_values | list | 276 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.ringsize_values.circumference | str | 9329 | 0 (0.0%) | 73 | , 45,9, 47,1 | N/A (See parent components for context) |
| options.values.ringsize_values.diameter | str | 9329 | 0 (0.0%) | 75 | , 14,6, 15 | N/A (See parent components for context) |
| options.values.ringsize_values.size | str | 9329 | 0 (0.0%) | 202 | , 46, 47 | N/A (See parent components for context) |
| options.values.ringsize_values.title | str | 9329 | 0 (0.0%) | 366 | Optionen auswählen, 46 ( Ø 14,6 ), 47 ( Ø 15,0 ) | N/A (See parent components for context) |
| options.values.ringsize_values.value | str | 9329 | 0 (0.0%) | 75 | , 14,6, 15 | N/A (See parent components for context) |
| options.values.sku | NoneType, str | 22840 | 1376 (6.0%) | 117 | diamond-Brillant, blackdiamond, emerald | Unique Stock Keeping Unit code |
| options.values.stone_gia | list | 43 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.carat | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.carat.default_label | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | Localized display name/label for the field: default |
| options.values.stone_gia.carat.default_option_title | str | 11620 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_gia.carat.label | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| options.values.stone_gia.carat.option_title | str | 11620 | 0 (0.0%) | 7 | Karat, Carat, Quilates | Localized display name/label for the field: option |
| options.values.stone_gia.carat.value | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| options.values.stone_gia.certificate | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.certificate.default_label | str | 11620 | 0 (0.0%) | 1 | GIA | Localized display name/label for the field: default |
| options.values.stone_gia.certificate.default_option_title | str | 11620 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.stone_gia.certificate.label | str | 11620 | 0 (0.0%) | 1 | GIA | N/A (See parent components for context) |
| options.values.stone_gia.certificate.option_title | str | 11620 | 0 (0.0%) | 7 | Zertifizierung, Certification, Certificado | Localized display name/label for the field: option |
| options.values.stone_gia.certificate.value | str | 11620 | 0 (0.0%) | 1 | 2 | N/A (See parent components for context) |
| options.values.stone_gia.clarity | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.clarity.default_label | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | Localized display name/label for the field: default |
| options.values.stone_gia.clarity.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.stone_gia.clarity.label | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| options.values.stone_gia.clarity.option_title | str | 11620 | 0 (0.0%) | 7 | Reinheit, Stone Clarity, Calidad | Localized display name/label for the field: option |
| options.values.stone_gia.clarity.value | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| options.values.stone_gia.colour | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.colour.default_label | str | 11620 | 0 (0.0%) | 7 | J, I, H | Localized display name/label for the field: default |
| options.values.stone_gia.colour.default_option_title | str | 11620 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.stone_gia.colour.label | str | 11620 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| options.values.stone_gia.colour.option_title | str | 11620 | 0 (0.0%) | 7 | Farbe, Colour, Color | Localized display name/label for the field: option |
| options.values.stone_gia.colour.value | str | 11620 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| options.values.stone_gia.cut | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.cut.default_label | str | 11620 | 0 (0.0%) | 4 | Good, Very Good, Fair | Localized display name/label for the field: default |
| options.values.stone_gia.cut.default_option_title | str | 11620 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.stone_gia.cut.label | str | 11620 | 0 (0.0%) | 28 | Gut, Sehr gut, Mäßig | N/A (See parent components for context) |
| options.values.stone_gia.cut.option_title | str | 11620 | 0 (0.0%) | 7 | Schliff, Cut, Corte | Localized display name/label for the field: option |
| options.values.stone_gia.cut.value | str | 11620 | 0 (0.0%) | 4 | 2, 3, 1 | N/A (See parent components for context) |
| options.values.stone_gia.diameter | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.diameter.default_label | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | Localized display name/label for the field: default |
| options.values.stone_gia.diameter.default_option_title | str | 11620 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.stone_gia.diameter.label | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| options.values.stone_gia.diameter.option_title | str | 11620 | 0 (0.0%) | 6 | Durchmesser, Diameter, Diámetro | Localized display name/label for the field: option |
| options.values.stone_gia.diameter.value | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| options.values.stone_gia.id | str | 11620 | 0 (0.0%) | 3584 | 12996, 12997, 12998 | N/A (See parent components for context) |
| options.values.stone_gia.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_gia.origin.default_option_title | str | 11620 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: default |
| options.values.stone_gia.origin.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin.option_title | str | 11620 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: option |
| options.values.stone_gia.origin.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin_colour | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin_colour.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_gia.origin_colour.default_option_title | str | 11620 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.stone_gia.origin_colour.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.origin_colour.option_title | str | 11620 | 0 (0.0%) | 7 | Farbursprung, Colour Origin, Origen del color | Localized display name/label for the field: option |
| options.values.stone_gia.origin_colour.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.price | int | 11620 | 0 (0.0%) | 5002 | 4722, 4918, 5134 | Monetary value or price-related setting |
| options.values.stone_gia.qty | dict | 11620 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.stone_gia.qty.default_label | int | 11620 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| options.values.stone_gia.qty.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.stone_gia.qty.label | int | 11620 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.values.stone_gia.qty.option_title | str | 11620 | 0 (0.0%) | 7 | Anzahl der Steine, Quantity of stones, Cantidad de piedras | Localized display name/label for the field: option |
| options.values.stone_gia.qty.value | int | 11620 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.values.stone_gia.quality | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.quality.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_gia.quality.default_option_title | str | 11620 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.stone_gia.quality.label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.quality.option_title | str | 11620 | 0 (0.0%) | 7 | Qualität, Quality, Calidad | Localized display name/label for the field: option |
| options.values.stone_gia.quality.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.shape | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.shape.default_label | str | 11620 | 0 (0.0%) | 6 | Princess, Emerald, Cushion | Localized display name/label for the field: default |
| options.values.stone_gia.shape.default_option_title | str | 11620 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.stone_gia.shape.label | str | 11620 | 0 (0.0%) | 18 | Prinzess, Princess, Emerald | N/A (See parent components for context) |
| options.values.stone_gia.shape.option_title | str | 11620 | 0 (0.0%) | 6 | Schliffform, Shape, Forma | Localized display name/label for the field: option |
| options.values.stone_gia.shape.value | str | 11620 | 0 (0.0%) | 6 | 11, 7, 6 | N/A (See parent components for context) |
| options.values.stone_gia.stone_name | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.stone_name.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_gia.stone_name.default_option_title | str | 11620 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.stone_gia.stone_name.label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.stone_name.option_title | str | 11620 | 0 (0.0%) | 6 | Name, Nombre, Nume | Localized display name/label for the field: option |
| options.values.stone_gia.stone_name.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.stone_type | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.stone_type.default_label | str | 11620 | 0 (0.0%) | 1 | Diamond | Localized display name/label for the field: default |
| options.values.stone_gia.stone_type.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.stone_gia.stone_type.label | str | 11620 | 0 (0.0%) | 4 | Diamant, Diamond, Diamante | N/A (See parent components for context) |
| options.values.stone_gia.stone_type.option_title | str | 11620 | 0 (0.0%) | 6 | Steinarten, Stone Type, Con Piedras | Localized display name/label for the field: option |
| options.values.stone_gia.stone_type.value | str | 11620 | 0 (0.0%) | 1 | diamond-Brillant | N/A (See parent components for context) |
| options.values.stone_gia.total_carat | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_gia.total_carat.default_label | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | Localized display name/label for the field: default |
| options.values.stone_gia.total_carat.default_option_title | str | 11620 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.values.stone_gia.total_carat.label | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| options.values.stone_gia.total_carat.option_title | str | 11620 | 0 (0.0%) | 10 | Karat, Carat, Total de quilates de la piedra | Localized display name/label for the field: option |
| options.values.stone_gia.total_carat.value | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| options.values.stone_group | str | 4910 | 0 (0.0%) | 10 | diamond, precious_stone, semi_precious | N/A (See parent components for context) |
| options.values.stone_quality | list | 1805 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.carat | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.carat.default_label | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | Localized display name/label for the field: default |
| options.values.stone_quality.carat.default_option_title | str | 5105 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_quality.carat.label | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | N/A (See parent components for context) |
| options.values.stone_quality.carat.option_title | str | 5105 | 0 (0.0%) | 13 | Karat, Quilates, Carat | Localized display name/label for the field: option |
| options.values.stone_quality.carat.value | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | N/A (See parent components for context) |
| options.values.stone_quality.certificate | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.certificate.default_label | str | 5105 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.stone_quality.certificate.default_option_title | str | 5105 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.stone_quality.certificate.label | str | 5105 | 0 (0.0%) | 19 | GL Zertifiziert, GL Certificado, GL Certified | N/A (See parent components for context) |
| options.values.stone_quality.certificate.option_title | str | 5105 | 0 (0.0%) | 18 | Zertifizierung, Certificado, Certification | Localized display name/label for the field: option |
| options.values.stone_quality.certificate.value | str | 5105 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.clarity | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.clarity.default_label | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | Localized display name/label for the field: default |
| options.values.stone_quality.clarity.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.stone_quality.clarity.label | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | N/A (See parent components for context) |
| options.values.stone_quality.clarity.option_title | str | 5105 | 0 (0.0%) | 19 | Reinheit, Calidad, Stone Clarity | Localized display name/label for the field: option |
| options.values.stone_quality.clarity.value | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | N/A (See parent components for context) |
| options.values.stone_quality.colour | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.colour.default_label | str | 5105 | 0 (0.0%) | 33 | H, G, Green | Localized display name/label for the field: default |
| options.values.stone_quality.colour.default_option_title | str | 5105 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.stone_quality.colour.label | str | 5105 | 0 (0.0%) | 180 | H, G, Grün | N/A (See parent components for context) |
| options.values.stone_quality.colour.option_title | str | 5105 | 0 (0.0%) | 19 | Farbe, Color, Colour | Localized display name/label for the field: option |
| options.values.stone_quality.colour.value | str | 5105 | 0 (0.0%) | 33 | H, G, Green | N/A (See parent components for context) |
| options.values.stone_quality.cut | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.cut.default_label | str | 5105 | 0 (0.0%) | 3 | Excellent, Very Good, Good | Localized display name/label for the field: default |
| options.values.stone_quality.cut.default_option_title | str | 5105 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.stone_quality.cut.label | str | 5105 | 0 (0.0%) | 43 | Ausgezeichnet, Sehr gut, Excelente | N/A (See parent components for context) |
| options.values.stone_quality.cut.option_title | str | 5105 | 0 (0.0%) | 19 | Schliff, Corte, Cut | Localized display name/label for the field: option |
| options.values.stone_quality.cut.value | str | 5105 | 0 (0.0%) | 3 | 4, 3, 2 | N/A (See parent components for context) |
| options.values.stone_quality.diameter | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.diameter.default_label | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | Localized display name/label for the field: default |
| options.values.stone_quality.diameter.default_option_title | str | 5105 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.stone_quality.diameter.label | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.diameter.option_title | str | 5105 | 0 (0.0%) | 15 | Durchmesser, Diámetro, Diameter | Localized display name/label for the field: option |
| options.values.stone_quality.diameter.value | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.id | str | 5105 | 0 (0.0%) | 2056 | 6330, 6312, 30477 | N/A (See parent components for context) |
| options.values.stone_quality.label | str | 5105 | 0 (0.0%) | 114 | VS, VVS, I | N/A (See parent components for context) |
| options.values.stone_quality.origin | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.origin.default_label | NoneType, str | 5105 | 4775 (93.5%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.values.stone_quality.origin.default_option_title | str | 5105 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.stone_quality.origin.label | str | 5105 | 0 (0.0%) | 13 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| options.values.stone_quality.origin.option_title | str | 5105 | 0 (0.0%) | 15 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| options.values.stone_quality.origin.value | NoneType, str | 5105 | 4775 (93.5%) | 2 | african, heated | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour.default_label | NoneType, str | 5105 | 4461 (87.4%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.values.stone_quality.origin_colour.default_option_title | str | 5105 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.stone_quality.origin_colour.label | str | 5105 | 0 (0.0%) | 14 | , Farblich Behandelt, Parannettu | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour.option_title | str | 5105 | 0 (0.0%) | 20 | Farbursprung, Origen del color, Colour Origin | Localized display name/label for the field: option |
| options.values.stone_quality.origin_colour.value | NoneType, str | 5105 | 4461 (87.4%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.values.stone_quality.price | int | 5105 | 0 (0.0%) | 1805 | 23, 81, 12 | Monetary value or price-related setting |
| options.values.stone_quality.qty | dict | 5105 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.stone_quality.qty.default_label | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | Localized display name/label for the field: default |
| options.values.stone_quality.qty.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.stone_quality.qty.label | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | N/A (See parent components for context) |
| options.values.stone_quality.qty.option_title | str | 5105 | 0 (0.0%) | 19 | Anzahl der Steine, Cantidad de piedras, Quantity of stones | Localized display name/label for the field: option |
| options.values.stone_quality.qty.value | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | N/A (See parent components for context) |
| options.values.stone_quality.quality | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality.default_label | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| options.values.stone_quality.quality.default_option_title | str | 5105 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.stone_quality.quality.label | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.values.stone_quality.quality.option_title | str | 5105 | 0 (0.0%) | 18 | Qualität, Calidad, Quality | Localized display name/label for the field: option |
| options.values.stone_quality.quality.value | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins | list | 330 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat.default_label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.carat.default_option_title | str | 660 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.carat.label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat.option_title | str | 660 | 0 (0.0%) | 7 | Karat, Carat, Karát | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.carat.value | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate.default_label | str | 660 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.certificate.default_option_title | str | 660 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.certificate.label | str | 660 | 0 (0.0%) | 7 | GL Zertifiziert, GL Certified, Certifikováno GL | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate.option_title | str | 660 | 0 (0.0%) | 7 | Zertifizierung, Certification, Certifikace | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.certificate.value | str | 660 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity.default_label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.clarity.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.clarity.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity.option_title | str | 660 | 0 (0.0%) | 7 | Reinheit, Stone Clarity, Čistota kamene | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.clarity.value | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour.default_label | str | 660 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.colour.default_option_title | str | 660 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.colour.label | str | 660 | 0 (0.0%) | 20 | Grün, Rot, Dunkelblau | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour.option_title | str | 660 | 0 (0.0%) | 7 | Farbe, Colour, Barva | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.colour.value | str | 660 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut.default_label | str | 660 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.cut.default_option_title | str | 660 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.cut.label | str | 660 | 0 (0.0%) | 7 | Sehr gut, Very Good, Velmi dobré | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut.option_title | str | 660 | 0 (0.0%) | 7 | Schliff, Cut, Řez | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.cut.value | str | 660 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter.default_label | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.diameter.default_option_title | str | 660 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.diameter.label | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter.option_title | str | 660 | 0 (0.0%) | 6 | Durchmesser, Diameter, Průměr | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.diameter.value | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.id | str | 660 | 0 (0.0%) | 288 | 146, 5816, 145 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin.default_label | str | 660 | 0 (0.0%) | 4 | African, Colombian, Heated | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin.default_option_title | str | 660 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin.label | str | 660 | 0 (0.0%) | 24 | Afrikanisch, Kolumbianisch, Wärme behandelt | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin.option_title | str | 660 | 0 (0.0%) | 14 | Ursprungsland, Hitzebehandlung, Country of Origin | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.origin.value | str | 660 | 0 (0.0%) | 4 | african, colombian, heated | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour.default_label | NoneType | 660 | 660 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin_colour.default_option_title | str | 660 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin_colour.label | str | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour.option_title | str | 660 | 0 (0.0%) | 7 | Farbursprung, Colour Origin, Původ barvy | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.origin_colour.value | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.price | int | 660 | 0 (0.0%) | 471 | 1442, 5409, 3173 | Monetary value or price-related setting |
| options.values.stone_quality.quality_origins.qty | dict | 660 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.stone_quality.quality_origins.qty.default_label | int | 660 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.qty.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.qty.label | int | 660 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.qty.option_title | str | 660 | 0 (0.0%) | 7 | Anzahl der Steine, Quantity of stones, Počet kamenů | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.qty.value | int | 660 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality.default_label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.quality.default_option_title | str | 660 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.quality.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality.option_title | str | 660 | 0 (0.0%) | 7 | Qualität, Quality, Kvalita | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.quality.value | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape.default_label | str | 660 | 0 (0.0%) | 8 | Princess, Emerald, Cushion | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.shape.default_option_title | str | 660 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.shape.label | str | 660 | 0 (0.0%) | 22 | Prinzess, Princess, Smaragd | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape.option_title | str | 660 | 0 (0.0%) | 6 | Schliffform, Shape, tvar | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.shape.value | str | 660 | 0 (0.0%) | 8 | 11, 7, 6 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name.default_label | NoneType | 660 | 660 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_name.default_option_title | str | 660 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_name.label | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name.option_title | str | 660 | 0 (0.0%) | 6 | Name, Jméno, Nombre | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.stone_name.value | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type.default_label | str | 660 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_type.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_type.label | str | 660 | 0 (0.0%) | 18 | Smaragd, Rubin, Saphir | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type.option_title | str | 660 | 0 (0.0%) | 6 | Steinarten, Stone Type, Typ kamene | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.stone_type.value | str | 660 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat.default_label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.total_carat.default_option_title | str | 660 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.total_carat.label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat.option_title | str | 660 | 0 (0.0%) | 11 | Karat, Carat, Počet karátů | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.total_carat.value | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| options.values.stone_quality.shape | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.shape.default_label | str | 5105 | 0 (0.0%) | 10 | Round, Princess, Emerald | Localized display name/label for the field: default |
| options.values.stone_quality.shape.default_option_title | str | 5105 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.stone_quality.shape.label | str | 5105 | 0 (0.0%) | 34 | Rund, Redondo, Princesa | N/A (See parent components for context) |
| options.values.stone_quality.shape.option_title | str | 5105 | 0 (0.0%) | 14 | Schliffform, Forma, Shape | Localized display name/label for the field: option |
| options.values.stone_quality.shape.value | str | 5105 | 0 (0.0%) | 10 | 1, 11, 7 | N/A (See parent components for context) |
| options.values.stone_quality.stone_name | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_name.default_label | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.stone_name.default_option_title | str | 5105 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.stone_quality.stone_name.label | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_name.option_title | str | 5105 | 0 (0.0%) | 16 | Name, Nombre, Nom et Prénom | Localized display name/label for the field: option |
| options.values.stone_quality.stone_name.value | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_type | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_type.default_label | str | 5105 | 0 (0.0%) | 35 | Diamond, Lab Grown Diamond, Emerald | Localized display name/label for the field: default |
| options.values.stone_quality.stone_type.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.stone_quality.stone_type.label | str | 5105 | 0 (0.0%) | 230 | Diamant, Labor-gezüchteter Diamant, Diamante | N/A (See parent components for context) |
| options.values.stone_quality.stone_type.option_title | str | 5105 | 0 (0.0%) | 15 | Steinarten, Con Piedras, Stone Type | Localized display name/label for the field: option |
| options.values.stone_quality.stone_type.value | str | 5105 | 0 (0.0%) | 35 | diamond-Brillant, lab-grown-diamond, emerald | N/A (See parent components for context) |
| options.values.stone_quality.total_carat | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.total_carat.default_label | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | Localized display name/label for the field: default |
| options.values.stone_quality.total_carat.default_option_title | str | 5105 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.values.stone_quality.total_carat.label | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | N/A (See parent components for context) |
| options.values.stone_quality.total_carat.option_title | str | 5105 | 0 (0.0%) | 23 | Karat, Total de quilates de la piedra, Total Stone Carat | Localized display name/label for the field: option |
| options.values.stone_quality.total_carat.value | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | N/A (See parent components for context) |
| options.values.store_title | str | 22840 | 0 (0.0%) | 1569 | Diamant, Schwarzer Diamant, Smaragd | Localized display name/label for the field: store |
| options.values.title | str | 23116 | 0 (0.0%) | 1586 | EU, Diamant, Schwarzer Diamant | N/A (See parent components for context) |
| options.without_stone_same_men | int | 77 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| product_id | int | 500 | 0 (0.0%) | 500 | 97372, 97444, 97480 | Unique identifier for the product |
| product_name | str | 500 | 0 (0.0%) | 500 | Herrenring Bellanca, Colgante de Mujer Costa, Vaiko pakabukas Breda | Full name of the product |
| product_type | str | 500 | 0 (0.0%) | 7 | ring, pendant, necklace | Broad product category |
| product_type_value | NoneType, str | 500 | 1 (0.2%) | 6 | 1, 4, 3 | Internal identifier for the product type |
| sku | str | 500 | 0 (0.0%) | 500 | Bellanca, COSTA, EPK-06 | Stock Keeping Unit |
| stone | list | 500 | 282 (56.4%) | 1 | N/A | List of gemstone configurations currently assigned to the product |
| stone.configure_quality | str | 4910 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| stone.data_stones | list | 4910 | 2 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.carat | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.carat.default_label | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | Localized display name/label for the field: default |
| stone.data_stones.carat.default_option_title | str | 6310 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.data_stones.carat.label | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | N/A (See parent components for context) |
| stone.data_stones.carat.option_title | str | 6310 | 0 (0.0%) | 15 | Karat, Quilates, Carat | Localized display name/label for the field: option |
| stone.data_stones.carat.value | float, int | 6310 | 0 (0.0%) | 44 | 0.025, 0.005, 0.006 | N/A (See parent components for context) |
| stone.data_stones.certificate | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.certificate.default_label | str | 6310 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.data_stones.certificate.default_option_title | str | 6310 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.data_stones.certificate.label | str | 6310 | 0 (0.0%) | 22 | GL Zertifiziert, GL Certificado, GL Certified | N/A (See parent components for context) |
| stone.data_stones.certificate.option_title | str | 6310 | 0 (0.0%) | 21 | Zertifizierung, Certificado, Certification | Localized display name/label for the field: option |
| stone.data_stones.certificate.value | str | 6310 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.data_stones.clarity | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.clarity.default_label | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | Localized display name/label for the field: default |
| stone.data_stones.clarity.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.data_stones.clarity.label | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| stone.data_stones.clarity.option_title | str | 6310 | 0 (0.0%) | 21 | Reinheit, Calidad, Stone Clarity | Localized display name/label for the field: option |
| stone.data_stones.clarity.value | str | 6310 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| stone.data_stones.colour | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.colour.default_label | str | 6310 | 0 (0.0%) | 22 | H, Black, Green | Localized display name/label for the field: default |
| stone.data_stones.colour.default_option_title | str | 6310 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.data_stones.colour.label | str | 6310 | 0 (0.0%) | 187 | H, Schwarz, Grün | N/A (See parent components for context) |
| stone.data_stones.colour.option_title | str | 6310 | 0 (0.0%) | 21 | Farbe, Color, Colour | Localized display name/label for the field: option |
| stone.data_stones.colour.value | str | 6310 | 0 (0.0%) | 22 | H, Black, Green | N/A (See parent components for context) |
| stone.data_stones.cut | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.cut.default_label | str | 6310 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| stone.data_stones.cut.default_option_title | str | 6310 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.data_stones.cut.label | str | 6310 | 0 (0.0%) | 40 | Ausgezeichnet, Sehr gut, Excelente | N/A (See parent components for context) |
| stone.data_stones.cut.option_title | str | 6310 | 0 (0.0%) | 20 | Schliff, Corte, Cut | Localized display name/label for the field: option |
| stone.data_stones.cut.value | str | 6310 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| stone.data_stones.diameter | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.diameter.default_label | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | Localized display name/label for the field: default |
| stone.data_stones.diameter.default_option_title | str | 6310 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.data_stones.diameter.label | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | N/A (See parent components for context) |
| stone.data_stones.diameter.option_title | str | 6310 | 0 (0.0%) | 17 | Durchmesser, Diámetro, Diameter | Localized display name/label for the field: option |
| stone.data_stones.diameter.value | str | 6310 | 0 (0.0%) | 40 | 1.8 mm, 1.0 mm, 1.1 mm | N/A (See parent components for context) |
| stone.data_stones.origin | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.origin.default_label | NoneType, str | 6310 | 5660 (89.7%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.data_stones.origin.default_option_title | str | 6310 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.data_stones.origin.label | str | 6310 | 0 (0.0%) | 25 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| stone.data_stones.origin.option_title | str | 6310 | 0 (0.0%) | 27 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| stone.data_stones.origin.value | NoneType, str | 6310 | 5660 (89.7%) | 2 | african, heated | N/A (See parent components for context) |
| stone.data_stones.origin_colour | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.origin_colour.default_label | NoneType, str | 6310 | 5764 (91.3%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.data_stones.origin_colour.default_option_title | str | 6310 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.data_stones.origin_colour.label | str | 6310 | 0 (0.0%) | 16 | , Farblich Behandelt, Natürliche Steine | N/A (See parent components for context) |
| stone.data_stones.origin_colour.option_title | str | 6310 | 0 (0.0%) | 23 | Farbursprung, Origen del color, Colour Origin | Localized display name/label for the field: option |
| stone.data_stones.origin_colour.value | NoneType, str | 6310 | 5764 (91.3%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.data_stones.qty | dict | 6310 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.data_stones.qty.default_label | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | Localized display name/label for the field: default |
| stone.data_stones.qty.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.data_stones.qty.label | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | N/A (See parent components for context) |
| stone.data_stones.qty.option_title | str | 6310 | 0 (0.0%) | 22 | Anzahl der Steine, Cantidad de piedras, Quantity of stones | Localized display name/label for the field: option |
| stone.data_stones.qty.value | int | 6310 | 0 (0.0%) | 60 | 1, 3, 7 | N/A (See parent components for context) |
| stone.data_stones.quality | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.quality.default_label | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | Localized display name/label for the field: default |
| stone.data_stones.quality.default_option_title | str | 6310 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.data_stones.quality.label | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| stone.data_stones.quality.option_title | str | 6310 | 0 (0.0%) | 20 | Qualität, Calidad, Quality | Localized display name/label for the field: option |
| stone.data_stones.quality.value | str | 6310 | 0 (0.0%) | 4 | AAA, AAAA, AAAAA | N/A (See parent components for context) |
| stone.data_stones.shape | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.shape.default_label | str | 6310 | 0 (0.0%) | 10 | Round, Princess, Emerald | Localized display name/label for the field: default |
| stone.data_stones.shape.default_option_title | str | 6310 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.data_stones.shape.label | str | 6310 | 0 (0.0%) | 37 | Rund, Redondo, Princesa | N/A (See parent components for context) |
| stone.data_stones.shape.option_title | str | 6310 | 0 (0.0%) | 17 | Schliffform, Forma, Shape | Localized display name/label for the field: option |
| stone.data_stones.shape.value | str | 6310 | 0 (0.0%) | 10 | 1, 11, 7 | N/A (See parent components for context) |
| stone.data_stones.stone_name | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_name.default_label | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.data_stones.stone_name.default_option_title | str | 6310 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.data_stones.stone_name.label | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_name.option_title | str | 6310 | 0 (0.0%) | 17 | Name, Nombre, Jméno | Localized display name/label for the field: option |
| stone.data_stones.stone_name.value | NoneType | 6310 | 6310 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_type | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_type.default_label | str | 6310 | 0 (0.0%) | 50 | Diamond, Black Diamond, Emerald | Localized display name/label for the field: default |
| stone.data_stones.stone_type.default_option_title | str | 6310 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.data_stones.stone_type.label | str | 6310 | 0 (0.0%) | 465 | Diamant, Schwarzer Diamant, Smaragd | N/A (See parent components for context) |
| stone.data_stones.stone_type.option_title | str | 6310 | 0 (0.0%) | 17 | Steinarten, Con Piedras, Stone Type | Localized display name/label for the field: option |
| stone.data_stones.stone_type.value | str | 6310 | 0 (0.0%) | 50 | diamond-Brillant, blackdiamond, emerald | N/A (See parent components for context) |
| stone.data_stones.total_carat | dict | 6310 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.total_carat.default_label | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | Localized display name/label for the field: default |
| stone.data_stones.total_carat.default_option_title | str | 6310 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.data_stones.total_carat.label | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | N/A (See parent components for context) |
| stone.data_stones.total_carat.option_title | str | 6310 | 0 (0.0%) | 27 | Karat, Steinkarat insgesamt, Total de quilates de la piedra | Localized display name/label for the field: option |
| stone.data_stones.total_carat.value | float, int | 6310 | 0 (0.0%) | 120 | 0.025, 0.015, 0.018 | N/A (See parent components for context) |
| stone.default_quality | NoneType, str | 4910 | 2747 (55.9%) | 6 | AAA, AAAAA, AAAA | N/A (See parent components for context) |
| stone.default_title | str | 4910 | 0 (0.0%) | 60 | Diamond, Black Diamond, Emerald | Localized display name/label for the field: default |
| stone.is_default | bool | 4910 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| stone.option_id | str | 4910 | 0 (0.0%) | 327 | 250431, 250437, 250696 | Internal system identifier for option |
| stone.option_type_id | str | 4910 | 0 (0.0%) | 4910 | 2081587, 2081597, 2081590 | Internal system identifier for option_type |
| stone.price | str | 4910 | 0 (0.0%) | 1118 | 23.00, 8.00, 5.00 | Additional price for selecting this stone |
| stone.price_type | str | 4910 | 0 (0.0%) | 1 | fixed | Monetary value or price-related setting |
| stone.sku | str | 4910 | 0 (0.0%) | 51 | diamond-Brillant, blackdiamond, emerald | Gemstone unique SKU code |
| stone.stone_gia | list | 43 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.carat | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.carat.default_label | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | Localized display name/label for the field: default |
| stone.stone_gia.carat.default_option_title | str | 11620 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_gia.carat.label | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| stone.stone_gia.carat.option_title | str | 11620 | 0 (0.0%) | 7 | Karat, Carat, Quilates | Localized display name/label for the field: option |
| stone.stone_gia.carat.value | float, int | 11620 | 0 (0.0%) | 17 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| stone.stone_gia.certificate | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.certificate.default_label | str | 11620 | 0 (0.0%) | 1 | GIA | Localized display name/label for the field: default |
| stone.stone_gia.certificate.default_option_title | str | 11620 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.stone_gia.certificate.label | str | 11620 | 0 (0.0%) | 1 | GIA | N/A (See parent components for context) |
| stone.stone_gia.certificate.option_title | str | 11620 | 0 (0.0%) | 7 | Zertifizierung, Certification, Certificado | Localized display name/label for the field: option |
| stone.stone_gia.certificate.value | str | 11620 | 0 (0.0%) | 1 | 2 | N/A (See parent components for context) |
| stone.stone_gia.clarity | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.clarity.default_label | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | Localized display name/label for the field: default |
| stone.stone_gia.clarity.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.stone_gia.clarity.label | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| stone.stone_gia.clarity.option_title | str | 11620 | 0 (0.0%) | 7 | Reinheit, Stone Clarity, Calidad | Localized display name/label for the field: option |
| stone.stone_gia.clarity.value | str | 11620 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| stone.stone_gia.colour | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.colour.default_label | str | 11620 | 0 (0.0%) | 7 | J, I, H | Localized display name/label for the field: default |
| stone.stone_gia.colour.default_option_title | str | 11620 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.stone_gia.colour.label | str | 11620 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| stone.stone_gia.colour.option_title | str | 11620 | 0 (0.0%) | 7 | Farbe, Colour, Color | Localized display name/label for the field: option |
| stone.stone_gia.colour.value | str | 11620 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| stone.stone_gia.cut | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.cut.default_label | str | 11620 | 0 (0.0%) | 4 | Good, Very Good, Fair | Localized display name/label for the field: default |
| stone.stone_gia.cut.default_option_title | str | 11620 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.stone_gia.cut.label | str | 11620 | 0 (0.0%) | 28 | Gut, Sehr gut, Mäßig | N/A (See parent components for context) |
| stone.stone_gia.cut.option_title | str | 11620 | 0 (0.0%) | 7 | Schliff, Cut, Corte | Localized display name/label for the field: option |
| stone.stone_gia.cut.value | str | 11620 | 0 (0.0%) | 4 | 2, 3, 1 | N/A (See parent components for context) |
| stone.stone_gia.diameter | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.diameter.default_label | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | Localized display name/label for the field: default |
| stone.stone_gia.diameter.default_option_title | str | 11620 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.stone_gia.diameter.label | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| stone.stone_gia.diameter.option_title | str | 11620 | 0 (0.0%) | 6 | Durchmesser, Diameter, Diámetro | Localized display name/label for the field: option |
| stone.stone_gia.diameter.value | str | 11620 | 0 (0.0%) | 12 | 5.0x5.0 mm, 6.0x4.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| stone.stone_gia.id | str | 11620 | 0 (0.0%) | 3584 | 12996, 12997, 12998 | N/A (See parent components for context) |
| stone.stone_gia.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_gia.origin.default_option_title | str | 11620 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: default |
| stone.stone_gia.origin.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin.option_title | str | 11620 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: option |
| stone.stone_gia.origin.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin_colour | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin_colour.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_gia.origin_colour.default_option_title | str | 11620 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.stone_gia.origin_colour.label | str | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.origin_colour.option_title | str | 11620 | 0 (0.0%) | 7 | Farbursprung, Colour Origin, Origen del color | Localized display name/label for the field: option |
| stone.stone_gia.origin_colour.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.price | int | 11620 | 0 (0.0%) | 5002 | 4722, 4918, 5134 | Monetary value or price-related setting |
| stone.stone_gia.qty | dict | 11620 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.stone_gia.qty.default_label | int | 11620 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| stone.stone_gia.qty.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.stone_gia.qty.label | int | 11620 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.stone_gia.qty.option_title | str | 11620 | 0 (0.0%) | 7 | Anzahl der Steine, Quantity of stones, Cantidad de piedras | Localized display name/label for the field: option |
| stone.stone_gia.qty.value | int | 11620 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.stone_gia.quality | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.quality.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_gia.quality.default_option_title | str | 11620 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.stone_gia.quality.label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.quality.option_title | str | 11620 | 0 (0.0%) | 7 | Qualität, Quality, Calidad | Localized display name/label for the field: option |
| stone.stone_gia.quality.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.shape | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.shape.default_label | str | 11620 | 0 (0.0%) | 6 | Princess, Emerald, Cushion | Localized display name/label for the field: default |
| stone.stone_gia.shape.default_option_title | str | 11620 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.stone_gia.shape.label | str | 11620 | 0 (0.0%) | 18 | Prinzess, Princess, Emerald | N/A (See parent components for context) |
| stone.stone_gia.shape.option_title | str | 11620 | 0 (0.0%) | 6 | Schliffform, Shape, Forma | Localized display name/label for the field: option |
| stone.stone_gia.shape.value | str | 11620 | 0 (0.0%) | 6 | 11, 7, 6 | N/A (See parent components for context) |
| stone.stone_gia.stone_name | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.stone_name.default_label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_gia.stone_name.default_option_title | str | 11620 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.stone_gia.stone_name.label | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.stone_name.option_title | str | 11620 | 0 (0.0%) | 6 | Name, Nombre, Nume | Localized display name/label for the field: option |
| stone.stone_gia.stone_name.value | NoneType | 11620 | 11620 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_gia.stone_type | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.stone_type.default_label | str | 11620 | 0 (0.0%) | 1 | Diamond | Localized display name/label for the field: default |
| stone.stone_gia.stone_type.default_option_title | str | 11620 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.stone_gia.stone_type.label | str | 11620 | 0 (0.0%) | 4 | Diamant, Diamond, Diamante | N/A (See parent components for context) |
| stone.stone_gia.stone_type.option_title | str | 11620 | 0 (0.0%) | 6 | Steinarten, Stone Type, Con Piedras | Localized display name/label for the field: option |
| stone.stone_gia.stone_type.value | str | 11620 | 0 (0.0%) | 1 | diamond-Brillant | N/A (See parent components for context) |
| stone.stone_gia.total_carat | dict | 11620 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_gia.total_carat.default_label | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | Localized display name/label for the field: default |
| stone.stone_gia.total_carat.default_option_title | str | 11620 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.stone_gia.total_carat.label | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| stone.stone_gia.total_carat.option_title | str | 11620 | 0 (0.0%) | 10 | Karat, Carat, Total de quilates de la piedra | Localized display name/label for the field: option |
| stone.stone_gia.total_carat.value | float, int | 11620 | 0 (0.0%) | 18 | 0.93, 0.62, 1 | N/A (See parent components for context) |
| stone.stone_group | str | 4910 | 0 (0.0%) | 10 | diamond, precious_stone, semi_precious | Classification of the stone |
| stone.stone_quality | list | 1805 | 0 (0.0%) | 1 | N/A | Gemstone quality and attribute details |
| stone.stone_quality.carat | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.carat.default_label | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | Localized display name/label for the field: default |
| stone.stone_quality.carat.default_option_title | str | 5105 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_quality.carat.label | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | N/A (See parent components for context) |
| stone.stone_quality.carat.option_title | str | 5105 | 0 (0.0%) | 13 | Karat, Quilates, Carat | Localized display name/label for the field: option |
| stone.stone_quality.carat.value | float, int | 5105 | 0 (0.0%) | 41 | 0.025, 0.008, 0.2 | N/A (See parent components for context) |
| stone.stone_quality.certificate | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.certificate.default_label | str | 5105 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.stone_quality.certificate.default_option_title | str | 5105 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.stone_quality.certificate.label | str | 5105 | 0 (0.0%) | 19 | GL Zertifiziert, GL Certificado, GL Certified | N/A (See parent components for context) |
| stone.stone_quality.certificate.option_title | str | 5105 | 0 (0.0%) | 18 | Zertifizierung, Certificado, Certification | Localized display name/label for the field: option |
| stone.stone_quality.certificate.value | str | 5105 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.clarity | dict | 5105 | 0 (0.0%) | 1 | N/A | Gemstone clarity level |
| stone.stone_quality.clarity.default_label | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | Localized display name/label for the field: default |
| stone.stone_quality.clarity.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.stone_quality.clarity.label | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | N/A (See parent components for context) |
| stone.stone_quality.clarity.option_title | str | 5105 | 0 (0.0%) | 19 | Reinheit, Calidad, Stone Clarity | Localized display name/label for the field: option |
| stone.stone_quality.clarity.value | str | 5105 | 0 (0.0%) | 10 | VS, VVS, I | N/A (See parent components for context) |
| stone.stone_quality.colour | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.colour.default_label | str | 5105 | 0 (0.0%) | 33 | H, G, Green | Localized display name/label for the field: default |
| stone.stone_quality.colour.default_option_title | str | 5105 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.stone_quality.colour.label | str | 5105 | 0 (0.0%) | 180 | H, G, Grün | N/A (See parent components for context) |
| stone.stone_quality.colour.option_title | str | 5105 | 0 (0.0%) | 19 | Farbe, Color, Colour | Localized display name/label for the field: option |
| stone.stone_quality.colour.value | str | 5105 | 0 (0.0%) | 33 | H, G, Green | N/A (See parent components for context) |
| stone.stone_quality.cut | dict | 5105 | 0 (0.0%) | 1 | N/A | Gemstone cut quality |
| stone.stone_quality.cut.default_label | str | 5105 | 0 (0.0%) | 3 | Excellent, Very Good, Good | Localized display name/label for the field: default |
| stone.stone_quality.cut.default_option_title | str | 5105 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.stone_quality.cut.label | str | 5105 | 0 (0.0%) | 43 | Ausgezeichnet, Sehr gut, Excelente | N/A (See parent components for context) |
| stone.stone_quality.cut.option_title | str | 5105 | 0 (0.0%) | 19 | Schliff, Corte, Cut | Localized display name/label for the field: option |
| stone.stone_quality.cut.value | str | 5105 | 0 (0.0%) | 3 | 4, 3, 2 | N/A (See parent components for context) |
| stone.stone_quality.diameter | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.diameter.default_label | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | Localized display name/label for the field: default |
| stone.stone_quality.diameter.default_option_title | str | 5105 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.stone_quality.diameter.label | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | N/A (See parent components for context) |
| stone.stone_quality.diameter.option_title | str | 5105 | 0 (0.0%) | 15 | Durchmesser, Diámetro, Diameter | Localized display name/label for the field: option |
| stone.stone_quality.diameter.value | str | 5105 | 0 (0.0%) | 37 | 1.8 mm, 1.2 mm, 3.0x3.0 mm | N/A (See parent components for context) |
| stone.stone_quality.id | str | 5105 | 0 (0.0%) | 2056 | 6330, 6312, 30477 | N/A (See parent components for context) |
| stone.stone_quality.label | str | 5105 | 0 (0.0%) | 114 | VS, VVS, I | N/A (See parent components for context) |
| stone.stone_quality.origin | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.origin.default_label | NoneType, str | 5105 | 4775 (93.5%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.stone_quality.origin.default_option_title | str | 5105 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.stone_quality.origin.label | str | 5105 | 0 (0.0%) | 13 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| stone.stone_quality.origin.option_title | str | 5105 | 0 (0.0%) | 15 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| stone.stone_quality.origin.value | NoneType, str | 5105 | 4775 (93.5%) | 2 | african, heated | N/A (See parent components for context) |
| stone.stone_quality.origin_colour | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.origin_colour.default_label | NoneType, str | 5105 | 4461 (87.4%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.stone_quality.origin_colour.default_option_title | str | 5105 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.stone_quality.origin_colour.label | str | 5105 | 0 (0.0%) | 14 | , Farblich Behandelt, Parannettu | N/A (See parent components for context) |
| stone.stone_quality.origin_colour.option_title | str | 5105 | 0 (0.0%) | 20 | Farbursprung, Origen del color, Colour Origin | Localized display name/label for the field: option |
| stone.stone_quality.origin_colour.value | NoneType, str | 5105 | 4461 (87.4%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.stone_quality.price | int | 5105 | 0 (0.0%) | 1805 | 23, 81, 12 | Monetary value or price-related setting |
| stone.stone_quality.qty | dict | 5105 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.stone_quality.qty.default_label | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | Localized display name/label for the field: default |
| stone.stone_quality.qty.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.stone_quality.qty.label | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | N/A (See parent components for context) |
| stone.stone_quality.qty.option_title | str | 5105 | 0 (0.0%) | 19 | Anzahl der Steine, Cantidad de piedras, Quantity of stones | Localized display name/label for the field: option |
| stone.stone_quality.qty.value | int | 5105 | 0 (0.0%) | 52 | 1, 7, 30 | N/A (See parent components for context) |
| stone.stone_quality.quality | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality.default_label | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| stone.stone_quality.quality.default_option_title | str | 5105 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.stone_quality.quality.label | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.stone_quality.quality.option_title | str | 5105 | 0 (0.0%) | 18 | Qualität, Calidad, Quality | Localized display name/label for the field: option |
| stone.stone_quality.quality.value | str | 5105 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins | list | 330 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat.default_label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.carat.default_option_title | str | 660 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.carat.label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat.option_title | str | 660 | 0 (0.0%) | 7 | Karat, Carat, Karát | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.carat.value | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate.default_label | str | 660 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.certificate.default_option_title | str | 660 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.certificate.label | str | 660 | 0 (0.0%) | 7 | GL Zertifiziert, GL Certified, Certifikováno GL | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate.option_title | str | 660 | 0 (0.0%) | 7 | Zertifizierung, Certification, Certifikace | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.certificate.value | str | 660 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity.default_label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.clarity.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.clarity.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity.option_title | str | 660 | 0 (0.0%) | 7 | Reinheit, Stone Clarity, Čistota kamene | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.clarity.value | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour.default_label | str | 660 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.colour.default_option_title | str | 660 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.colour.label | str | 660 | 0 (0.0%) | 20 | Grün, Rot, Dunkelblau | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour.option_title | str | 660 | 0 (0.0%) | 7 | Farbe, Colour, Barva | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.colour.value | str | 660 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut.default_label | str | 660 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.cut.default_option_title | str | 660 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.cut.label | str | 660 | 0 (0.0%) | 7 | Sehr gut, Very Good, Velmi dobré | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut.option_title | str | 660 | 0 (0.0%) | 7 | Schliff, Cut, Řez | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.cut.value | str | 660 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter.default_label | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.diameter.default_option_title | str | 660 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.diameter.label | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter.option_title | str | 660 | 0 (0.0%) | 6 | Durchmesser, Diameter, Průměr | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.diameter.value | str | 660 | 0 (0.0%) | 16 | 5.0x5.0 mm, 8.0x6.0 mm, 6.0x4.0 mm | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.id | str | 660 | 0 (0.0%) | 288 | 146, 5816, 145 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin.default_label | str | 660 | 0 (0.0%) | 4 | African, Colombian, Heated | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin.default_option_title | str | 660 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin.label | str | 660 | 0 (0.0%) | 24 | Afrikanisch, Kolumbianisch, Wärme behandelt | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin.option_title | str | 660 | 0 (0.0%) | 14 | Ursprungsland, Hitzebehandlung, Country of Origin | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.origin.value | str | 660 | 0 (0.0%) | 4 | african, colombian, heated | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour.default_label | NoneType | 660 | 660 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin_colour.default_option_title | str | 660 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin_colour.label | str | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour.option_title | str | 660 | 0 (0.0%) | 7 | Farbursprung, Colour Origin, Původ barvy | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.origin_colour.value | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.price | int | 660 | 0 (0.0%) | 471 | 1442, 5409, 3173 | Monetary value or price-related setting |
| stone.stone_quality.quality_origins.qty | dict | 660 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.stone_quality.quality_origins.qty.default_label | int | 660 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.qty.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.qty.label | int | 660 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.qty.option_title | str | 660 | 0 (0.0%) | 7 | Anzahl der Steine, Quantity of stones, Počet kamenů | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.qty.value | int | 660 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality.default_label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.quality.default_option_title | str | 660 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.quality.label | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality.option_title | str | 660 | 0 (0.0%) | 7 | Qualität, Quality, Kvalita | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.quality.value | str | 660 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape.default_label | str | 660 | 0 (0.0%) | 8 | Princess, Emerald, Cushion | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.shape.default_option_title | str | 660 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.shape.label | str | 660 | 0 (0.0%) | 22 | Prinzess, Princess, Smaragd | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape.option_title | str | 660 | 0 (0.0%) | 6 | Schliffform, Shape, tvar | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.shape.value | str | 660 | 0 (0.0%) | 8 | 11, 7, 6 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name.default_label | NoneType | 660 | 660 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_name.default_option_title | str | 660 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_name.label | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name.option_title | str | 660 | 0 (0.0%) | 6 | Name, Jméno, Nombre | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.stone_name.value | NoneType | 660 | 660 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type.default_label | str | 660 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_type.default_option_title | str | 660 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_type.label | str | 660 | 0 (0.0%) | 18 | Smaragd, Rubin, Saphir | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type.option_title | str | 660 | 0 (0.0%) | 6 | Steinarten, Stone Type, Typ kamene | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.stone_type.value | str | 660 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat | dict | 660 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat.default_label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.total_carat.default_option_title | str | 660 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.total_carat.label | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat.option_title | str | 660 | 0 (0.0%) | 11 | Karat, Carat, Počet karátů | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.total_carat.value | float, int | 660 | 0 (0.0%) | 22 | 0.93, 2.15, 0.62 | N/A (See parent components for context) |
| stone.stone_quality.shape | dict | 5105 | 0 (0.0%) | 1 | N/A | Gemstone shape |
| stone.stone_quality.shape.default_label | str | 5105 | 0 (0.0%) | 10 | Round, Princess, Emerald | Localized display name/label for the field: default |
| stone.stone_quality.shape.default_option_title | str | 5105 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.stone_quality.shape.label | str | 5105 | 0 (0.0%) | 34 | Rund, Redondo, Princesa | N/A (See parent components for context) |
| stone.stone_quality.shape.option_title | str | 5105 | 0 (0.0%) | 14 | Schliffform, Forma, Shape | Localized display name/label for the field: option |
| stone.stone_quality.shape.value | str | 5105 | 0 (0.0%) | 10 | 1, 11, 7 | N/A (See parent components for context) |
| stone.stone_quality.stone_name | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_name.default_label | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.stone_name.default_option_title | str | 5105 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.stone_quality.stone_name.label | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_name.option_title | str | 5105 | 0 (0.0%) | 16 | Name, Nombre, Nom et Prénom | Localized display name/label for the field: option |
| stone.stone_quality.stone_name.value | NoneType | 5105 | 5105 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_type | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_type.default_label | str | 5105 | 0 (0.0%) | 35 | Diamond, Lab Grown Diamond, Emerald | Localized display name/label for the field: default |
| stone.stone_quality.stone_type.default_option_title | str | 5105 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.stone_quality.stone_type.label | str | 5105 | 0 (0.0%) | 230 | Diamant, Labor-gezüchteter Diamant, Diamante | N/A (See parent components for context) |
| stone.stone_quality.stone_type.option_title | str | 5105 | 0 (0.0%) | 15 | Steinarten, Con Piedras, Stone Type | Localized display name/label for the field: option |
| stone.stone_quality.stone_type.value | str | 5105 | 0 (0.0%) | 35 | diamond-Brillant, lab-grown-diamond, emerald | N/A (See parent components for context) |
| stone.stone_quality.total_carat | dict | 5105 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.total_carat.default_label | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | Localized display name/label for the field: default |
| stone.stone_quality.total_carat.default_option_title | str | 5105 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.stone_quality.total_carat.label | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | N/A (See parent components for context) |
| stone.stone_quality.total_carat.option_title | str | 5105 | 0 (0.0%) | 23 | Karat, Total de quilates de la piedra, Total Stone Carat | Localized display name/label for the field: option |
| stone.stone_quality.total_carat.value | float, int | 5105 | 0 (0.0%) | 100 | 0.025, 0.056, 0.24 | N/A (See parent components for context) |
| stone.store_title | str | 4910 | 0 (0.0%) | 467 | Diamant, Schwarzer Diamant, Smaragd | Localized display name/label for the field: store |
| stone.title | str | 4910 | 0 (0.0%) | 467 | Diamant, Schwarzer Diamant, Smaragd | Display name of the gemstone |
| store_id | str | 500 | 0 (0.0%) | 48 | glat, glcl, gllt | Store or Country code |
| type_id | str | 500 | 0 (0.0%) | 3 | simple, product_set, virtual | Product type code |

---
*Note: This table is automatically generated based on the current data sample.*