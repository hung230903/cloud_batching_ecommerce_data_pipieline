# Data Dictionary: Local File: product_info_5.json

Generated at: 2026-03-27 16:09:14

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| attribute_set | str | 500 | 0 (0.0%) | 2 | trauring, diamonds | Name of the attribute set |
| attribute_set_id | int | 500 | 0 (0.0%) | 2 | 26, 55 | ID of the product's attribute set |
| category_id | int, str | 500 | 0 (0.0%) | 5 | 0, 688, 690 | Unique ID of the primary category |
| category_name | str | 500 | 0 (0.0%) | 54 | , 結婚戒指, 结婚戒指 | Display name of the category |
| collection | str | 500 | 0 (0.0%) | 7 | twinset, simple, vintage | Project collection name |
| collection_id | str | 500 | 0 (0.0%) | 7 | 4090, 164, 4291 | Unique ID of the collection |
| colour | list | 500 | 0 (0.0%) | 1 | N/A | Metal and Alloy configuration options |
| colour.colour_code | str | 11177 | 0 (0.0%) | 7 | white, yellow, red | N/A (See parent components for context) |
| colour.colour_label | str | 11177 | 0 (0.0%) | 179 | Bianco, Giallo, Rosso | Localized display name/label for the field: colour |
| colour.default_title | str | 11177 | 0 (0.0%) | 24 | Weißgold 375, Gelbgold 375, Rotgold 375 | Localized display name/label for the field: default |
| colour.is_default | bool | 11177 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| colour.metal | str | 11177 | 0 (0.0%) | 6 | 375, 585, 750 | Metal material code |
| colour.metal_label | str | 11177 | 0 (0.0%) | 142 | Oro 375 <span class='seperate-line'>-</span> <span>9K</span>, Oro 585 <span class='seperate-line'>-</span> <span>14K</span>, Oro 750 <span class='seperate-line'>-</span> <span>18K</span> | Display name of the metal material |
| colour.option_id | str | 11177 | 0 (0.0%) | 500 | 304891, 306438, 304193 | Internal system identifier for option |
| colour.option_type_id | str | 11177 | 0 (0.0%) | 11177 | 2472269, 2472270, 2472271 | Internal system identifier for option_type |
| colour.price | str | 11177 | 0 (0.0%) | 22 | 0.00, 65.00, 105.00 | Price adjustment for this metal selection |
| colour.price_type | str | 11177 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| colour.sku | str | 11177 | 0 (0.0%) | 24 | white-375, yellow-375, red-375 | Unique Stock Keeping Unit code |
| colour.store_title | str | 11177 | 0 (0.0%) | 713 | Oro Bianco 375, Oro Giallo 375, Oro Rosso 375 | Localized display name/label for the field: store |
| colour.title | str | 11177 | 0 (0.0%) | 713 | Oro Bianco 375, Oro Giallo 375, Oro Rosso 375 | N/A (See parent components for context) |
| custom | list | 500 | 0 (0.0%) | 1 | N/A | Miscellaneous custom options |
| custom.default_title | str | 5678 | 0 (0.0%) | 20 | 10.0 mm, A, B | Localized display name/label for the field: default |
| custom.is_default | bool | 5678 | 0 (0.0%) | 2 | True, False | Boolean flag/binary status: default |
| custom.option_id | str | 5678 | 0 (0.0%) | 2380 | 304890, 304893, 304894 | Internal system identifier for option |
| custom.option_type_id | str | 5678 | 0 (0.0%) | 5678 | 2472266, 2472311, 2472312 | Internal system identifier for option_type |
| custom.price | str | 5678 | 0 (0.0%) | 4 | 0.00, 3.00, 15.00 | Monetary value or price-related setting |
| custom.price_type | str | 5678 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| custom.sku | str | 5678 | 0 (0.0%) | 20 | w10, prA, prB | Unique Stock Keeping Unit code |
| custom.store_title | str | 5678 | 0 (0.0%) | 179 | 10.0 mm, A, B | Localized display name/label for the field: store |
| custom.title | str | 5678 | 0 (0.0%) | 179 | 10.0 mm, A, B | N/A (See parent components for context) |
| fixed_silver_weight | int | 500 | 0 (0.0%) | 1 | 0 | Fixed silver weight for silver items |
| gender | bool, str | 500 | 0 (0.0%) | 3 | False, men, women | Target gender |
| gold_weight | str | 500 | 0 (0.0%) | 123 | 6.6534, 2.48, 3.8922 | Estimated gold weight of the metal part |
| material_design | NoneType | 500 | 500 (100.0%) | 0 | N/A | Design code for the material/alloy |
| max_price | str | 500 | 0 (0.0%) | 473 | 26.982,00 €, HK $114,676.00, ¥133,697.00 | Formatted highest possible price for the product |
| media_image | dict | 500 | 0 (0.0%) | 1 | N/A | Product images container |
| media_image.default_position | int | 500 | 0 (0.0%) | 3 | 1, 3, 2 | N/A (See parent components for context) |
| media_image.image_load_type | str | 500 | 0 (0.0%) | 1 | layer | N/A (See parent components for context) |
| media_image.image_view_types | list | 500 | 500 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images | list | 500 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.area_view | NoneType, str | 1236 | 18 (1.5%) | 2 | grid, thumb | N/A (See parent components for context) |
| media_image.images.config | NoneType | 1236 | 1236 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.image_view | str | 1236 | 0 (0.0%) | 3 | general, 3d, compare | N/A (See parent components for context) |
| media_image.images.is_default | NoneType, bool | 1236 | 18 (1.5%) | 2 | True, False | Boolean flag/binary status: default |
| media_image.images.is_feature | bool | 1236 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: feature |
| media_image.images.is_video | NoneType | 1236 | 1236 (100.0%) | 0 | N/A | Boolean flag/binary status: video |
| media_image.images.label | str | 1236 | 0 (0.0%) | 500 | Elegant World 10 mm, 結婚戒指 Pretty Tale 4 mm, 婚戒 Bright Start 6 mm | N/A (See parent components for context) |
| media_image.images.large_image_url | str | 1236 | 0 (0.0%) | 1236 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg | Web URL link to the resource: large_image |
| media_image.images.media_type | str | 1236 | 0 (0.0%) | 1 | image | N/A (See parent components for context) |
| media_image.images.medium_image_url | str | 1236 | 0 (0.0%) | 1236 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516 | Web URL link to the resource: medium_image |
| media_image.images.medium_middle_image_url | str | 1236 | 0 (0.0%) | 1236 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.images.meta | NoneType | 1236 | 1236 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.placeholder_alt | str | 1209 | 0 (0.0%) | 1209 | ALLOY_TITLE Rotondo STONE_TITLE Elegant World 10 mm view 1, ALLOY_TITLE Rotondo STONE_TITLE Elegant World 10 mm view 2, ALLOY_TITLE Rotondo STONE_TITLE Elegant World 10 mm view 3 | N/A (See parent components for context) |
| media_image.images.position | NoneType, int | 1236 | 18 (1.5%) | 5 | 1, 2, 3 | Display sequence or sorting order |
| media_image.images.small_image_url | str | 1236 | 0 (0.0%) | 1236 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220 | Web URL link to the resource: small_image |
| media_image.images.sticky_image_url | str | 1236 | 0 (0.0%) | 1236 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/gwd-l-9300/womenstone/none_AAAAA/alloycolour/yellow/width/w10/profile/prA/surface/polished_icematte.jpg?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.images.watermark | NoneType | 1236 | 1236 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.lcpMediaUrl | NoneType, str | 500 | 487 (97.4%) | 2 | https://www.glamira.com.au/media, https://www.glamira.co.nz/media | N/A (See parent components for context) |
| media_image.paths | dict | 500 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.paths.large_image_url | str | 500 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/, https://cdn.glamira.cn/media/product/newgeneration/ | Web URL link to the resource: large_image |
| media_image.paths.medium_image_url | str | 500 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/?width=700&height=700 | Web URL link to the resource: medium_image |
| media_image.paths.medium_middle_image_url | str | 500 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.paths.small_image_url | str | 500 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/?width=110&height=110 | Web URL link to the resource: small_image |
| media_image.paths.sticky_image_url | str | 500 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.sku_image | str | 500 | 0 (0.0%) | 154 | gwd-l-9300, gwd-l-33000, gwd-l-6500 | URL for the main SKU image |
| media_image.total_thumbs | str | 500 | 0 (0.0%) | 2 | 4, 5 | N/A (See parent components for context) |
| media_video | dict | 500 | 0 (0.0%) | 1 | N/A | Product video container |
| media_video.videos | list | 500 | 487 (97.4%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.file_name | str | 17 | 0 (0.0%) | 17 | video1_1.mp4, video1_2.mp4, video1-6_1.mp4 | N/A (See parent components for context) |
| media_video.videos.hidden | bool | 17 | 0 (0.0%) | 2 | False, True | N/A (See parent components for context) |
| media_video.videos.id | str | 17 | 0 (0.0%) | 2 | 1191, 1392 | N/A (See parent components for context) |
| media_video.videos.label | str | 17 | 0 (0.0%) | 13 | Trauring Brilliant Ornament 5 mm, Trauring Brilliant Ornament 6 mm, Brilliant Ornament 8 mm | N/A (See parent components for context) |
| media_video.videos.media_type | str | 17 | 0 (0.0%) | 1 | video | N/A (See parent components for context) |
| media_video.videos.name | str | 17 | 0 (0.0%) | 2 | video, video2 | N/A (See parent components for context) |
| media_video.videos.url | str | 17 | 0 (0.0%) | 17 | https://cdn-media.glamira.com/media/product/layer/gwd-l-7000-r/video1_1.mp4, https://cdn-media.glamira.com/media/product/layer/gwd-l-7000-r/video1_2.mp4, https://cdn-media.glamira.com/media/product/layer/gwd-l-7000-r/video1-6_1.mp4 | N/A (See parent components for context) |
| min_price | str | 500 | 0 (0.0%) | 412 | 1.065,00 €, HK $4,535.00, ¥5,296.00 | Formatted lowest possible price for the product |
| none_metal_weight | int | 500 | 0 (0.0%) | 1 | 0 | Weight of the non-metal components |
| options | list | 500 | 0 (0.0%) | 1 | N/A | Raw JSON configuration options containing all possible choices |
| options.custom_size | str | 5806 | 0 (0.0%) | 2 | 0, 1 | N/A (See parent components for context) |
| options.default_price | NoneType, str | 5806 | 4445 (76.6%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.default_price_type | NoneType, str | 5806 | 4445 (76.6%) | 1 | fixed | Monetary value or price-related setting |
| options.default_title | str | 5806 | 0 (0.0%) | 26 | Damenring, Herrenring, Width | Localized display name/label for the field: default |
| options.default_value | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.detail_title | str | 5806 | 0 (0.0%) | 385 | Taglia Dell'anello Da Donna, Taglia Dell'anello Da Uomo, Larghezza | Localized display name/label for the field: detail |
| options.engraving_position | NoneType, str | 5806 | 4419 (76.1%) | 2 | inside, outside | N/A (See parent components for context) |
| options.engraving_type | NoneType, str | 5806 | 4419 (76.1%) | 2 | damenring, herrenring | N/A (See parent components for context) |
| options.extension_attributes | dict | 5806 | 5806 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.file_extension | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.group | str | 5806 | 0 (0.0%) | 8 | ringsize, custom, alloy | N/A (See parent components for context) |
| options.image_size_x | NoneType, str | 5806 | 4481 (77.2%) | 1 | 0 | N/A (See parent components for context) |
| options.image_size_y | NoneType, str | 5806 | 4481 (77.2%) | 1 | 0 | N/A (See parent components for context) |
| options.is_require | int | 5806 | 0 (0.0%) | 2 | 1, 0 | Boolean flag/binary status: require |
| options.max_characters | NoneType, str | 5806 | 3943 (67.9%) | 5 | 25, 0, 15 | N/A (See parent components for context) |
| options.max_characters_wrong | NoneType, str | 5806 | 5615 (96.7%) | 1 | 0 | N/A (See parent components for context) |
| options.option_id | str | 5806 | 0 (0.0%) | 5806 | 304888, 304889, 304890 | Internal system identifier for option |
| options.part_type | NoneType, str | 5806 | 1878 (32.3%) | 17 | women_ring_size, men_ring_size, width | N/A (See parent components for context) |
| options.price | NoneType, str | 5806 | 4445 (76.6%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.price_type | NoneType, str | 5806 | 4445 (76.6%) | 1 | fixed | Monetary value or price-related setting |
| options.product_id | str | 5806 | 0 (0.0%) | 500 | 107826, 107945, 107743 | Internal system identifier for product |
| options.sku | NoneType, str | 5806 | 5783 (99.6%) | 2 | 23.07.2018, DALANE | Unique Stock Keeping Unit code |
| options.sort_order | str | 5806 | 0 (0.0%) | 23 | 0, 2, 3 | Display sequence or sorting order |
| options.stones | list | 343 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.stones.carat | str | 400 | 0 (0.0%) | 12 | 0.0150, 0.0080, 0.0050 | N/A (See parent components for context) |
| options.stones.clarity | NoneType | 400 | 400 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.stones.diameter | str | 400 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| options.stones.id | str | 400 | 0 (0.0%) | 400 | 42862, 44456, 45994 | N/A (See parent components for context) |
| options.stones.option_id | str | 400 | 0 (0.0%) | 84 | 0, 304277, 304295 | Internal system identifier for option |
| options.stones.part_type | str | 400 | 0 (0.0%) | 4 | womenstone, stone1, stone2 | N/A (See parent components for context) |
| options.stones.product_id | str | 400 | 0 (0.0%) | 331 | 107826, 107945, 107743 | Internal system identifier for product |
| options.stones.qty | str | 400 | 0 (0.0%) | 22 | 5, 3, 6 | Quantity or count of items |
| options.stones.shape | str | 400 | 0 (0.0%) | 5 | 1, 11, 3 | N/A (See parent components for context) |
| options.store_id | int | 5806 | 0 (0.0%) | 52 | 14, 110, 25 | Internal system identifier for store |
| options.store_price | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.store_price_type | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.store_title | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | Localized display name/label for the field: store |
| options.title | str | 5806 | 0 (0.0%) | 399 | Taglia Dell'anello Da Donna, Taglia Dell'anello Da Uomo, Larghezza | N/A (See parent components for context) |
| options.type | str | 5806 | 0 (0.0%) | 13 | ctsize, width, alloy | N/A (See parent components for context) |
| options.use_stone | NoneType | 5806 | 5806 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values | list | 5806 | 692 (11.9%) | 1 | N/A | N/A (See parent components for context) |
| options.values.average_size | dict | 913 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.average_size.diameter | str | 913 | 0 (0.0%) | 2 | 16,5, 19,1 | N/A (See parent components for context) |
| options.values.average_size.value | str | 913 | 0 (0.0%) | 2 | 16,5, 19,1 | N/A (See parent components for context) |
| options.values.colour | str | 11177 | 0 (0.0%) | 7 | white, yellow, red | N/A (See parent components for context) |
| options.values.colour_label | str | 11177 | 0 (0.0%) | 179 | Bianco, Giallo, Rosso | Localized display name/label for the field: colour |
| options.values.configure_quality | str | 6165 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.values.data_stones | list | 6165 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.carat | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.carat.default_label | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | Localized display name/label for the field: default |
| options.values.data_stones.carat.default_option_title | str | 7185 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.data_stones.carat.label | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| options.values.data_stones.carat.option_title | str | 7185 | 0 (0.0%) | 17 | Carati, 重量（克拉）, 重量 | Localized display name/label for the field: option |
| options.values.data_stones.carat.value | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| options.values.data_stones.certificate | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.certificate.default_label | str | 7185 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.data_stones.certificate.default_option_title | str | 7185 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.data_stones.certificate.label | str | 7185 | 0 (0.0%) | 26 | Certificato GL, GL 認證, GL 认证 | N/A (See parent components for context) |
| options.values.data_stones.certificate.option_title | str | 7185 | 0 (0.0%) | 25 | Certificazione, 證書, 证书 | Localized display name/label for the field: option |
| options.values.data_stones.certificate.value | str | 7185 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.data_stones.clarity | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.clarity.default_label | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | Localized display name/label for the field: default |
| options.values.data_stones.clarity.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.data_stones.clarity.label | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.clarity.option_title | str | 7185 | 0 (0.0%) | 25 | Purezza, 寶石凈度, Stone Clarity | Localized display name/label for the field: option |
| options.values.data_stones.clarity.value | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | N/A (See parent components for context) |
| options.values.data_stones.colour | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.colour.default_label | str | 7185 | 0 (0.0%) | 18 | , H, Black | Localized display name/label for the field: default |
| options.values.data_stones.colour.default_option_title | str | 7185 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.data_stones.colour.label | str | 7185 | 0 (0.0%) | 272 | , H, Nero | N/A (See parent components for context) |
| options.values.data_stones.colour.option_title | str | 7185 | 0 (0.0%) | 24 | Colore, 成色, Color | Localized display name/label for the field: option |
| options.values.data_stones.colour.value | str | 7185 | 0 (0.0%) | 18 | , H, Black | N/A (See parent components for context) |
| options.values.data_stones.cut | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.cut.default_label | str | 7185 | 0 (0.0%) | 2 | Very Good, Excellent | Localized display name/label for the field: default |
| options.values.data_stones.cut.default_option_title | str | 7185 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.data_stones.cut.label | str | 7185 | 0 (0.0%) | 49 | Ottimo, Eccellente, 很好 | N/A (See parent components for context) |
| options.values.data_stones.cut.option_title | str | 7185 | 0 (0.0%) | 23 | Taglio, 切工, Cut | Localized display name/label for the field: option |
| options.values.data_stones.cut.value | str | 7185 | 0 (0.0%) | 2 | 3, 4 | N/A (See parent components for context) |
| options.values.data_stones.diameter | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.diameter.default_label | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | Localized display name/label for the field: default |
| options.values.data_stones.diameter.default_option_title | str | 7185 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.data_stones.diameter.label | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| options.values.data_stones.diameter.option_title | str | 7185 | 0 (0.0%) | 21 | Diametro, 直径, Diameter | Localized display name/label for the field: option |
| options.values.data_stones.diameter.value | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| options.values.data_stones.origin | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.origin.default_label | NoneType, str | 7185 | 6223 (86.6%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.values.data_stones.origin.default_option_title | str | 7185 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.data_stones.origin.label | str | 7185 | 0 (0.0%) | 42 | , Africano, Scaldato | N/A (See parent components for context) |
| options.values.data_stones.origin.option_title | str | 7185 | 0 (0.0%) | 47 | Origin / Heat Treatment, Paese d\'Origine, Trattamento termico | Localized display name/label for the field: option |
| options.values.data_stones.origin.value | NoneType, str | 7185 | 6223 (86.6%) | 2 | african, heated | N/A (See parent components for context) |
| options.values.data_stones.origin_colour | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.origin_colour.default_label | NoneType, str | 7185 | 5621 (78.2%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.values.data_stones.origin_colour.default_option_title | str | 7185 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.data_stones.origin_colour.label | str | 7185 | 0 (0.0%) | 47 | , Migliorato, Naturale | N/A (See parent components for context) |
| options.values.data_stones.origin_colour.option_title | str | 7185 | 0 (0.0%) | 26 | Origine del Colore, 顏色來源, 颜色来源 | Localized display name/label for the field: option |
| options.values.data_stones.origin_colour.value | NoneType, str | 7185 | 5621 (78.2%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.values.data_stones.qty | dict | 7185 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.data_stones.qty.default_label | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | Localized display name/label for the field: default |
| options.values.data_stones.qty.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.data_stones.qty.label | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| options.values.data_stones.qty.option_title | str | 7185 | 0 (0.0%) | 26 | Quantità di pietre, 石頭數量, 石头数量 | Localized display name/label for the field: option |
| options.values.data_stones.qty.value | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| options.values.data_stones.quality | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.quality.default_label | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | Localized display name/label for the field: default |
| options.values.data_stones.quality.default_option_title | str | 7185 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.data_stones.quality.label | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.values.data_stones.quality.option_title | str | 7185 | 0 (0.0%) | 24 | Qualità, 質量, 质量 | Localized display name/label for the field: option |
| options.values.data_stones.quality.value | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.values.data_stones.shape | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.shape.default_label | str | 7185 | 0 (0.0%) | 5 | Round, Princess, Cabochon Round | Localized display name/label for the field: default |
| options.values.data_stones.shape.default_option_title | str | 7185 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.data_stones.shape.label | str | 7185 | 0 (0.0%) | 31 | Rotondo, 圓形, 圆形 | N/A (See parent components for context) |
| options.values.data_stones.shape.option_title | str | 7185 | 0 (0.0%) | 20 | Forma, 形狀, 宝石形状 | Localized display name/label for the field: option |
| options.values.data_stones.shape.value | str | 7185 | 0 (0.0%) | 5 | 1, 11, 3 | N/A (See parent components for context) |
| options.values.data_stones.stone_name | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_name.default_label | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.data_stones.stone_name.default_option_title | str | 7185 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.data_stones.stone_name.label | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_name.option_title | str | 7185 | 0 (0.0%) | 20 | Nome, 名字, Name | Localized display name/label for the field: option |
| options.values.data_stones.stone_name.value | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_type | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.stone_type.default_label | str | 7185 | 0 (0.0%) | 35 | Without Stone, Diamond, Black Diamond | Localized display name/label for the field: default |
| options.values.data_stones.stone_type.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.data_stones.stone_type.label | str | 7185 | 0 (0.0%) | 462 | Senza Pietra, Diamante, Diamante Nero | N/A (See parent components for context) |
| options.values.data_stones.stone_type.option_title | str | 7185 | 0 (0.0%) | 20 | Tipo di Pietra, 寶石類型, 宝石类型 | Localized display name/label for the field: option |
| options.values.data_stones.stone_type.value | str | 7185 | 0 (0.0%) | 35 | none, diamond-Brillant, blackdiamond | N/A (See parent components for context) |
| options.values.data_stones.total_carat | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.data_stones.total_carat.default_label | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | Localized display name/label for the field: default |
| options.values.data_stones.total_carat.default_option_title | str | 7185 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| options.values.data_stones.total_carat.label | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| options.values.data_stones.total_carat.option_title | str | 7185 | 0 (0.0%) | 35 | Carato totale della pietra, 寶石總重量, 宝石总重量 | Localized display name/label for the field: option |
| options.values.data_stones.total_carat.value | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| options.values.default_quality | NoneType, str | 6165 | 4357 (70.7%) | 3 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.values.default_title | str | 26899 | 0 (0.0%) | 96 | 10.0 mm, Weißgold 375, Gelbgold 375 | Localized display name/label for the field: default |
| options.values.is_default | NoneType, bool, int | 27812 | 244 (0.9%) | 2 | True, False | Boolean flag/binary status: default |
| options.values.metal | str | 11177 | 0 (0.0%) | 6 | 375, 585, 750 | N/A (See parent components for context) |
| options.values.metal_label | str | 11177 | 0 (0.0%) | 142 | Oro 375 <span class='seperate-line'>-</span> <span>9K</span>, Oro 585 <span class='seperate-line'>-</span> <span>14K</span>, Oro 750 <span class='seperate-line'>-</span> <span>18K</span> | Localized display name/label for the field: metal |
| options.values.name | str | 913 | 0 (0.0%) | 28 | IT, EU, Default | N/A (See parent components for context) |
| options.values.option_id | str | 26899 | 0 (0.0%) | 4445 | 304890, 304891, 304892 | Internal system identifier for option |
| options.values.option_type_id | int, str | 26899 | 0 (0.0%) | 26864 | 2472266, 2472269, 2472270 | Internal system identifier for option_type |
| options.values.price | int, str | 26899 | 0 (0.0%) | 694 | 0.00, 65.00, 105.00 | Monetary value or price-related setting |
| options.values.price_type | str | 26899 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| options.values.ringsize_values | list | 913 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.ringsize_values.circumference | str | 30457 | 0 (0.0%) | 73 | , 45,9, 46,8 | N/A (See parent components for context) |
| options.values.ringsize_values.diameter | str | 30457 | 0 (0.0%) | 76 | , 14,6, 14,9 | N/A (See parent components for context) |
| options.values.ringsize_values.size | str | 30457 | 0 (0.0%) | 375 | , 6, 7 | N/A (See parent components for context) |
| options.values.ringsize_values.title | str | 30457 | 0 (0.0%) | 553 | Seleziona la tua taglia, 6 ( Ø 14,6 ), 7 ( Ø 14,9 ) | N/A (See parent components for context) |
| options.values.ringsize_values.value | str | 30457 | 0 (0.0%) | 76 | , 14,6, 14,9 | N/A (See parent components for context) |
| options.values.sku | NoneType, str | 26899 | 2789 (10.4%) | 91 | w10, white-375, yellow-375 | Unique Stock Keeping Unit code |
| options.values.stone_group | str | 6165 | 0 (0.0%) | 7 | without_stone, diamond, semi_precious | N/A (See parent components for context) |
| options.values.stone_quality | list | 1474 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.carat | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.carat.default_label | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | Localized display name/label for the field: default |
| options.values.stone_quality.carat.default_option_title | str | 1843 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_quality.carat.label | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| options.values.stone_quality.carat.option_title | str | 1843 | 0 (0.0%) | 16 | Carati, 重量（克拉）, 重量 | Localized display name/label for the field: option |
| options.values.stone_quality.carat.value | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| options.values.stone_quality.certificate | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.certificate.default_label | str | 1843 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.stone_quality.certificate.default_option_title | str | 1843 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.stone_quality.certificate.label | str | 1843 | 0 (0.0%) | 25 | Certificato GL, GL 認證, GL 认证 | N/A (See parent components for context) |
| options.values.stone_quality.certificate.option_title | str | 1843 | 0 (0.0%) | 24 | Certificazione, 證書, 证书 | Localized display name/label for the field: option |
| options.values.stone_quality.certificate.value | str | 1843 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.clarity | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.clarity.default_label | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | Localized display name/label for the field: default |
| options.values.stone_quality.clarity.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.stone_quality.clarity.label | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | N/A (See parent components for context) |
| options.values.stone_quality.clarity.option_title | str | 1843 | 0 (0.0%) | 24 | Purezza, 寶石凈度, Stone Clarity | Localized display name/label for the field: option |
| options.values.stone_quality.clarity.value | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | N/A (See parent components for context) |
| options.values.stone_quality.colour | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.colour.default_label | str | 1843 | 0 (0.0%) | 18 | H, Fancy Dark, Fancy Yellow | Localized display name/label for the field: default |
| options.values.stone_quality.colour.default_option_title | str | 1843 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.stone_quality.colour.label | str | 1843 | 0 (0.0%) | 89 | H,  Scuro Fantasia, Giallo Fantasia | N/A (See parent components for context) |
| options.values.stone_quality.colour.option_title | str | 1843 | 0 (0.0%) | 23 | Colore, 成色, Color | Localized display name/label for the field: option |
| options.values.stone_quality.colour.value | str | 1843 | 0 (0.0%) | 18 | H, Fancy Dark, Fancy Yellow | N/A (See parent components for context) |
| options.values.stone_quality.cut | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.cut.default_label | str | 1843 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| options.values.stone_quality.cut.default_option_title | str | 1843 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.stone_quality.cut.label | str | 1843 | 0 (0.0%) | 47 | Eccellente, Ottimo, 優良 | N/A (See parent components for context) |
| options.values.stone_quality.cut.option_title | str | 1843 | 0 (0.0%) | 22 | Taglio, 切工, Cut | Localized display name/label for the field: option |
| options.values.stone_quality.cut.value | str | 1843 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| options.values.stone_quality.diameter | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.diameter.default_label | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | Localized display name/label for the field: default |
| options.values.stone_quality.diameter.default_option_title | str | 1843 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.stone_quality.diameter.label | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.diameter.option_title | str | 1843 | 0 (0.0%) | 20 | Diametro, 直径, Diameter | Localized display name/label for the field: option |
| options.values.stone_quality.diameter.value | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.id | str | 1843 | 0 (0.0%) | 109 | 6326, 6308, 9089 | N/A (See parent components for context) |
| options.values.stone_quality.label | str | 1843 | 0 (0.0%) | 85 | VS, VVS,  Scuro Fantasia | N/A (See parent components for context) |
| options.values.stone_quality.origin | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.origin.default_label | NoneType, str | 1843 | 1840 (99.8%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.values.stone_quality.origin.default_option_title | str | 1843 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.stone_quality.origin.label | str | 1843 | 0 (0.0%) | 3 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| options.values.stone_quality.origin.option_title | str | 1843 | 0 (0.0%) | 3 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| options.values.stone_quality.origin.value | NoneType, str | 1843 | 1840 (99.8%) | 2 | african, heated | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour.default_label | NoneType, str | 1843 | 1005 (54.5%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.values.stone_quality.origin_colour.default_option_title | str | 1843 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.stone_quality.origin_colour.label | str | 1843 | 0 (0.0%) | 25 | , Migliorato, 增強的 | N/A (See parent components for context) |
| options.values.stone_quality.origin_colour.option_title | str | 1843 | 0 (0.0%) | 25 | Origine del Colore, 顏色來源, 颜色来源 | Localized display name/label for the field: option |
| options.values.stone_quality.origin_colour.value | NoneType, str | 1843 | 1005 (54.5%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.values.stone_quality.price | int | 1843 | 0 (0.0%) | 519 | 58, 230, 120 | Monetary value or price-related setting |
| options.values.stone_quality.qty | dict | 1843 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.stone_quality.qty.default_label | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | Localized display name/label for the field: default |
| options.values.stone_quality.qty.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.stone_quality.qty.label | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| options.values.stone_quality.qty.option_title | str | 1843 | 0 (0.0%) | 25 | Quantità di pietre, 石頭數量, 石头数量 | Localized display name/label for the field: option |
| options.values.stone_quality.qty.value | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| options.values.stone_quality.quality | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality.default_label | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| options.values.stone_quality.quality.default_option_title | str | 1843 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.stone_quality.quality.label | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.values.stone_quality.quality.option_title | str | 1843 | 0 (0.0%) | 23 | Qualità, 質量, 质量 | Localized display name/label for the field: option |
| options.values.stone_quality.quality.value | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins | list | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat.default_label | float | 3 | 0 (0.0%) | 1 | 0.36 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.carat.default_option_title | str | 3 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.carat.label | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.carat.option_title | str | 3 | 0 (0.0%) | 1 | Karat | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.carat.value | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate.default_label | str | 3 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.certificate.default_option_title | str | 3 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.certificate.label | str | 3 | 0 (0.0%) | 1 | GL Zertifiziert | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.certificate.option_title | str | 3 | 0 (0.0%) | 1 | Zertifizierung | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.certificate.value | str | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity.default_label | str | 3 | 0 (0.0%) | 1 | AAA | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.clarity.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.clarity.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.clarity.option_title | str | 3 | 0 (0.0%) | 1 | Reinheit | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.clarity.value | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour.default_label | str | 3 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.colour.default_option_title | str | 3 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.colour.label | str | 3 | 0 (0.0%) | 3 | Grün, Rot, Dunkelblau | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.colour.option_title | str | 3 | 0 (0.0%) | 1 | Farbe | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.colour.value | str | 3 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut.default_label | str | 3 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.cut.default_option_title | str | 3 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.cut.label | str | 3 | 0 (0.0%) | 1 | Sehr gut | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.cut.option_title | str | 3 | 0 (0.0%) | 1 | Schliff | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.cut.value | str | 3 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter.default_label | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.diameter.default_option_title | str | 3 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.diameter.label | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.diameter.option_title | str | 3 | 0 (0.0%) | 1 | Durchmesser | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.diameter.value | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.id | str | 3 | 0 (0.0%) | 3 | 6338, 6378, 6418 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin.default_label | str | 3 | 0 (0.0%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin.default_option_title | str | 3 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin.label | str | 3 | 0 (0.0%) | 2 | Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin.option_title | str | 3 | 0 (0.0%) | 2 | Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.origin.value | str | 3 | 0 (0.0%) | 2 | african, heated | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour.default_label | NoneType | 3 | 3 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin_colour.default_option_title | str | 3 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.origin_colour.label | str | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.origin_colour.option_title | str | 3 | 0 (0.0%) | 1 | Farbursprung | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.origin_colour.value | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.price | int | 3 | 0 (0.0%) | 3 | 479, 383, 299 | Monetary value or price-related setting |
| options.values.stone_quality.quality_origins.qty | dict | 3 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.values.stone_quality.quality_origins.qty.default_label | int | 3 | 0 (0.0%) | 1 | 1 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.qty.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.qty.label | int | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.qty.option_title | str | 3 | 0 (0.0%) | 1 | Anzahl der Steine | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.qty.value | int | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality.default_label | str | 3 | 0 (0.0%) | 1 | AAA | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.quality.default_option_title | str | 3 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.quality.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.quality.option_title | str | 3 | 0 (0.0%) | 1 | Qualität | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.quality.value | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape.default_label | str | 3 | 0 (0.0%) | 1 | Oval | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.shape.default_option_title | str | 3 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.shape.label | str | 3 | 0 (0.0%) | 1 | Oval | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.shape.option_title | str | 3 | 0 (0.0%) | 1 | Schliffform | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.shape.value | str | 3 | 0 (0.0%) | 1 | 9 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name.default_label | NoneType | 3 | 3 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_name.default_option_title | str | 3 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_name.label | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_name.option_title | str | 3 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.stone_name.value | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type.default_label | str | 3 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_type.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.stone_type.label | str | 3 | 0 (0.0%) | 3 | Smaragd, Rubin, Saphir | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.stone_type.option_title | str | 3 | 0 (0.0%) | 1 | Steinarten | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.stone_type.value | str | 3 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat.default_label | float | 3 | 0 (0.0%) | 1 | 0.36 | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.total_carat.default_option_title | str | 3 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.values.stone_quality.quality_origins.total_carat.label | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| options.values.stone_quality.quality_origins.total_carat.option_title | str | 3 | 0 (0.0%) | 1 | Karat | Localized display name/label for the field: option |
| options.values.stone_quality.quality_origins.total_carat.value | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| options.values.stone_quality.shape | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.shape.default_label | str | 1843 | 0 (0.0%) | 5 | Round, Princess, Cabochon Round | Localized display name/label for the field: default |
| options.values.stone_quality.shape.default_option_title | str | 1843 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.values.stone_quality.shape.label | str | 1843 | 0 (0.0%) | 28 | Rotondo, 圓形, 圆形 | N/A (See parent components for context) |
| options.values.stone_quality.shape.option_title | str | 1843 | 0 (0.0%) | 19 | Forma, 形狀, 宝石形状 | Localized display name/label for the field: option |
| options.values.stone_quality.shape.value | str | 1843 | 0 (0.0%) | 5 | 1, 11, 3 | N/A (See parent components for context) |
| options.values.stone_quality.stone_name | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_name.default_label | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.values.stone_quality.stone_name.default_option_title | str | 1843 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.values.stone_quality.stone_name.label | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_name.option_title | str | 1843 | 0 (0.0%) | 19 | Nome, 名字, Name | Localized display name/label for the field: option |
| options.values.stone_quality.stone_name.value | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_type | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.stone_type.default_label | str | 1843 | 0 (0.0%) | 20 | Diamond, Green Diamond, Yellow Diamond | Localized display name/label for the field: default |
| options.values.stone_quality.stone_type.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.values.stone_quality.stone_type.label | str | 1843 | 0 (0.0%) | 137 | Diamante, Diamante Verde, Diamante Giallo | N/A (See parent components for context) |
| options.values.stone_quality.stone_type.option_title | str | 1843 | 0 (0.0%) | 19 | Tipo di Pietra, 寶石類型, 宝石类型 | Localized display name/label for the field: option |
| options.values.stone_quality.stone_type.value | str | 1843 | 0 (0.0%) | 20 | diamond-Brillant, greendiamond, yellowdiamond | N/A (See parent components for context) |
| options.values.stone_quality.total_carat | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.values.stone_quality.total_carat.default_label | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | Localized display name/label for the field: default |
| options.values.stone_quality.total_carat.default_option_title | str | 1843 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| options.values.stone_quality.total_carat.label | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| options.values.stone_quality.total_carat.option_title | str | 1843 | 0 (0.0%) | 34 | Carato totale della pietra, 寶石總重量, 宝石总重量 | Localized display name/label for the field: option |
| options.values.stone_quality.total_carat.value | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| options.values.store_title | str | 26899 | 0 (0.0%) | 1392 | 10.0 mm, Oro Bianco 375, Oro Giallo 375 | Localized display name/label for the field: store |
| options.values.title | str | 27812 | 0 (0.0%) | 1417 | IT, EU, 10.0 mm | N/A (See parent components for context) |
| options.without_stone_same_men | int | 322 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| product_id | int | 500 | 0 (0.0%) | 500 | 107826, 107945, 107743 | Unique identifier for the product |
| product_name | str | 500 | 0 (0.0%) | 500 | Elegant World 10 mm, 結婚戒指 Pretty Tale 4 mm, 婚戒 Bright Start 6 mm | Full name of the product |
| product_type | str | 500 | 0 (0.0%) | 2 | wedding_ring, necklace | Broad product category |
| product_type_value | str | 500 | 0 (0.0%) | 2 | 12, 3 | Internal identifier for the product type |
| sku | str | 500 | 0 (0.0%) | 500 | GWD-L-9300-10, GWD-L-33000-4, GWD-L-6500-6 | Stock Keeping Unit |
| stone | list | 500 | 169 (33.8%) | 1 | N/A | List of gemstone configurations currently assigned to the product |
| stone.configure_quality | str | 6165 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.data_stones | list | 6165 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.carat | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.carat.default_label | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | Localized display name/label for the field: default |
| stone.data_stones.carat.default_option_title | str | 7185 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.data_stones.carat.label | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| stone.data_stones.carat.option_title | str | 7185 | 0 (0.0%) | 17 | Carati, 重量（克拉）, 重量 | Localized display name/label for the field: option |
| stone.data_stones.carat.value | float | 7185 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| stone.data_stones.certificate | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.certificate.default_label | str | 7185 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.data_stones.certificate.default_option_title | str | 7185 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.data_stones.certificate.label | str | 7185 | 0 (0.0%) | 26 | Certificato GL, GL 認證, GL 认证 | N/A (See parent components for context) |
| stone.data_stones.certificate.option_title | str | 7185 | 0 (0.0%) | 25 | Certificazione, 證書, 证书 | Localized display name/label for the field: option |
| stone.data_stones.certificate.value | str | 7185 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.data_stones.clarity | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.clarity.default_label | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | Localized display name/label for the field: default |
| stone.data_stones.clarity.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.data_stones.clarity.label | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | N/A (See parent components for context) |
| stone.data_stones.clarity.option_title | str | 7185 | 0 (0.0%) | 25 | Purezza, 寶石凈度, Stone Clarity | Localized display name/label for the field: option |
| stone.data_stones.clarity.value | str | 7185 | 0 (0.0%) | 4 | AAA, VS, AAAAA | N/A (See parent components for context) |
| stone.data_stones.colour | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.colour.default_label | str | 7185 | 0 (0.0%) | 18 | , H, Black | Localized display name/label for the field: default |
| stone.data_stones.colour.default_option_title | str | 7185 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.data_stones.colour.label | str | 7185 | 0 (0.0%) | 272 | , H, Nero | N/A (See parent components for context) |
| stone.data_stones.colour.option_title | str | 7185 | 0 (0.0%) | 24 | Colore, 成色, Color | Localized display name/label for the field: option |
| stone.data_stones.colour.value | str | 7185 | 0 (0.0%) | 18 | , H, Black | N/A (See parent components for context) |
| stone.data_stones.cut | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.cut.default_label | str | 7185 | 0 (0.0%) | 2 | Very Good, Excellent | Localized display name/label for the field: default |
| stone.data_stones.cut.default_option_title | str | 7185 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.data_stones.cut.label | str | 7185 | 0 (0.0%) | 49 | Ottimo, Eccellente, 很好 | N/A (See parent components for context) |
| stone.data_stones.cut.option_title | str | 7185 | 0 (0.0%) | 23 | Taglio, 切工, Cut | Localized display name/label for the field: option |
| stone.data_stones.cut.value | str | 7185 | 0 (0.0%) | 2 | 3, 4 | N/A (See parent components for context) |
| stone.data_stones.diameter | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.diameter.default_label | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | Localized display name/label for the field: default |
| stone.data_stones.diameter.default_option_title | str | 7185 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.data_stones.diameter.label | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| stone.data_stones.diameter.option_title | str | 7185 | 0 (0.0%) | 21 | Diametro, 直径, Diameter | Localized display name/label for the field: option |
| stone.data_stones.diameter.value | str | 7185 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| stone.data_stones.origin | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.origin.default_label | NoneType, str | 7185 | 6223 (86.6%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.data_stones.origin.default_option_title | str | 7185 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.data_stones.origin.label | str | 7185 | 0 (0.0%) | 42 | , Africano, Scaldato | N/A (See parent components for context) |
| stone.data_stones.origin.option_title | str | 7185 | 0 (0.0%) | 47 | Origin / Heat Treatment, Paese d\'Origine, Trattamento termico | Localized display name/label for the field: option |
| stone.data_stones.origin.value | NoneType, str | 7185 | 6223 (86.6%) | 2 | african, heated | N/A (See parent components for context) |
| stone.data_stones.origin_colour | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.origin_colour.default_label | NoneType, str | 7185 | 5621 (78.2%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.data_stones.origin_colour.default_option_title | str | 7185 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.data_stones.origin_colour.label | str | 7185 | 0 (0.0%) | 47 | , Migliorato, Naturale | N/A (See parent components for context) |
| stone.data_stones.origin_colour.option_title | str | 7185 | 0 (0.0%) | 26 | Origine del Colore, 顏色來源, 颜色来源 | Localized display name/label for the field: option |
| stone.data_stones.origin_colour.value | NoneType, str | 7185 | 5621 (78.2%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.data_stones.qty | dict | 7185 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.data_stones.qty.default_label | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | Localized display name/label for the field: default |
| stone.data_stones.qty.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.data_stones.qty.label | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| stone.data_stones.qty.option_title | str | 7185 | 0 (0.0%) | 26 | Quantità di pietre, 石頭數量, 石头数量 | Localized display name/label for the field: option |
| stone.data_stones.qty.value | int | 7185 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| stone.data_stones.quality | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.quality.default_label | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | Localized display name/label for the field: default |
| stone.data_stones.quality.default_option_title | str | 7185 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.data_stones.quality.label | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.data_stones.quality.option_title | str | 7185 | 0 (0.0%) | 24 | Qualità, 質量, 质量 | Localized display name/label for the field: option |
| stone.data_stones.quality.value | str | 7185 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.data_stones.shape | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.shape.default_label | str | 7185 | 0 (0.0%) | 5 | Round, Princess, Cabochon Round | Localized display name/label for the field: default |
| stone.data_stones.shape.default_option_title | str | 7185 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.data_stones.shape.label | str | 7185 | 0 (0.0%) | 31 | Rotondo, 圓形, 圆形 | N/A (See parent components for context) |
| stone.data_stones.shape.option_title | str | 7185 | 0 (0.0%) | 20 | Forma, 形狀, 宝石形状 | Localized display name/label for the field: option |
| stone.data_stones.shape.value | str | 7185 | 0 (0.0%) | 5 | 1, 11, 3 | N/A (See parent components for context) |
| stone.data_stones.stone_name | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_name.default_label | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.data_stones.stone_name.default_option_title | str | 7185 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.data_stones.stone_name.label | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_name.option_title | str | 7185 | 0 (0.0%) | 20 | Nome, 名字, Name | Localized display name/label for the field: option |
| stone.data_stones.stone_name.value | NoneType | 7185 | 7185 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_type | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.stone_type.default_label | str | 7185 | 0 (0.0%) | 35 | Without Stone, Diamond, Black Diamond | Localized display name/label for the field: default |
| stone.data_stones.stone_type.default_option_title | str | 7185 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.data_stones.stone_type.label | str | 7185 | 0 (0.0%) | 462 | Senza Pietra, Diamante, Diamante Nero | N/A (See parent components for context) |
| stone.data_stones.stone_type.option_title | str | 7185 | 0 (0.0%) | 20 | Tipo di Pietra, 寶石類型, 宝石类型 | Localized display name/label for the field: option |
| stone.data_stones.stone_type.value | str | 7185 | 0 (0.0%) | 35 | none, diamond-Brillant, blackdiamond | N/A (See parent components for context) |
| stone.data_stones.total_carat | dict | 7185 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.data_stones.total_carat.default_label | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | Localized display name/label for the field: default |
| stone.data_stones.total_carat.default_option_title | str | 7185 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| stone.data_stones.total_carat.label | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| stone.data_stones.total_carat.option_title | str | 7185 | 0 (0.0%) | 35 | Carato totale della pietra, 寶石總重量, 宝石总重量 | Localized display name/label for the field: option |
| stone.data_stones.total_carat.value | float | 7185 | 0 (0.0%) | 44 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| stone.default_quality | NoneType, str | 6165 | 4357 (70.7%) | 3 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.default_title | str | 6165 | 0 (0.0%) | 36 | ohne Stein, Diamond, Black Diamond | Localized display name/label for the field: default |
| stone.is_default | bool | 6165 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| stone.option_id | str | 6165 | 0 (0.0%) | 343 | 304892, 306439, 304194 | Internal system identifier for option |
| stone.option_type_id | str | 6165 | 0 (0.0%) | 6165 | 2472294, 2472295, 2472296 | Internal system identifier for option_type |
| stone.price | str | 6165 | 0 (0.0%) | 683 | 0.00, 78.00, 21.00 | Additional price for selecting this stone |
| stone.price_type | str | 6165 | 0 (0.0%) | 1 | fixed | Monetary value or price-related setting |
| stone.sku | str | 6165 | 0 (0.0%) | 35 | none, diamond-Brillant, blackdiamond | Gemstone unique SKU code |
| stone.stone_group | str | 6165 | 0 (0.0%) | 7 | without_stone, diamond, semi_precious | Classification of the stone |
| stone.stone_quality | list | 1474 | 0 (0.0%) | 1 | N/A | Gemstone quality and attribute details |
| stone.stone_quality.carat | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.carat.default_label | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | Localized display name/label for the field: default |
| stone.stone_quality.carat.default_option_title | str | 1843 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_quality.carat.label | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| stone.stone_quality.carat.option_title | str | 1843 | 0 (0.0%) | 16 | Carati, 重量（克拉）, 重量 | Localized display name/label for the field: option |
| stone.stone_quality.carat.value | float | 1843 | 0 (0.0%) | 12 | 0.015, 0.008, 0.005 | N/A (See parent components for context) |
| stone.stone_quality.certificate | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.certificate.default_label | str | 1843 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.stone_quality.certificate.default_option_title | str | 1843 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.stone_quality.certificate.label | str | 1843 | 0 (0.0%) | 25 | Certificato GL, GL 認證, GL 认证 | N/A (See parent components for context) |
| stone.stone_quality.certificate.option_title | str | 1843 | 0 (0.0%) | 24 | Certificazione, 證書, 证书 | Localized display name/label for the field: option |
| stone.stone_quality.certificate.value | str | 1843 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.clarity | dict | 1843 | 0 (0.0%) | 1 | N/A | Gemstone clarity level |
| stone.stone_quality.clarity.default_label | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | Localized display name/label for the field: default |
| stone.stone_quality.clarity.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.stone_quality.clarity.label | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | N/A (See parent components for context) |
| stone.stone_quality.clarity.option_title | str | 1843 | 0 (0.0%) | 24 | Purezza, 寶石凈度, Stone Clarity | Localized display name/label for the field: option |
| stone.stone_quality.clarity.value | str | 1843 | 0 (0.0%) | 7 | VS, VVS, VS1 | N/A (See parent components for context) |
| stone.stone_quality.colour | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.colour.default_label | str | 1843 | 0 (0.0%) | 18 | H, Fancy Dark, Fancy Yellow | Localized display name/label for the field: default |
| stone.stone_quality.colour.default_option_title | str | 1843 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.stone_quality.colour.label | str | 1843 | 0 (0.0%) | 89 | H,  Scuro Fantasia, Giallo Fantasia | N/A (See parent components for context) |
| stone.stone_quality.colour.option_title | str | 1843 | 0 (0.0%) | 23 | Colore, 成色, Color | Localized display name/label for the field: option |
| stone.stone_quality.colour.value | str | 1843 | 0 (0.0%) | 18 | H, Fancy Dark, Fancy Yellow | N/A (See parent components for context) |
| stone.stone_quality.cut | dict | 1843 | 0 (0.0%) | 1 | N/A | Gemstone cut quality |
| stone.stone_quality.cut.default_label | str | 1843 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| stone.stone_quality.cut.default_option_title | str | 1843 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.stone_quality.cut.label | str | 1843 | 0 (0.0%) | 47 | Eccellente, Ottimo, 優良 | N/A (See parent components for context) |
| stone.stone_quality.cut.option_title | str | 1843 | 0 (0.0%) | 22 | Taglio, 切工, Cut | Localized display name/label for the field: option |
| stone.stone_quality.cut.value | str | 1843 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| stone.stone_quality.diameter | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.diameter.default_label | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | Localized display name/label for the field: default |
| stone.stone_quality.diameter.default_option_title | str | 1843 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.stone_quality.diameter.label | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| stone.stone_quality.diameter.option_title | str | 1843 | 0 (0.0%) | 20 | Diametro, 直径, Diameter | Localized display name/label for the field: option |
| stone.stone_quality.diameter.value | str | 1843 | 0 (0.0%) | 13 | 1.5 mm, 1.2 mm, 1.0 mm | N/A (See parent components for context) |
| stone.stone_quality.id | str | 1843 | 0 (0.0%) | 109 | 6326, 6308, 9089 | N/A (See parent components for context) |
| stone.stone_quality.label | str | 1843 | 0 (0.0%) | 85 | VS, VVS,  Scuro Fantasia | N/A (See parent components for context) |
| stone.stone_quality.origin | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.origin.default_label | NoneType, str | 1843 | 1840 (99.8%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.stone_quality.origin.default_option_title | str | 1843 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.stone_quality.origin.label | str | 1843 | 0 (0.0%) | 3 | , Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| stone.stone_quality.origin.option_title | str | 1843 | 0 (0.0%) | 3 | Origin / Heat Treatment, Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| stone.stone_quality.origin.value | NoneType, str | 1843 | 1840 (99.8%) | 2 | african, heated | N/A (See parent components for context) |
| stone.stone_quality.origin_colour | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.origin_colour.default_label | NoneType, str | 1843 | 1005 (54.5%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.stone_quality.origin_colour.default_option_title | str | 1843 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.stone_quality.origin_colour.label | str | 1843 | 0 (0.0%) | 25 | , Migliorato, 增強的 | N/A (See parent components for context) |
| stone.stone_quality.origin_colour.option_title | str | 1843 | 0 (0.0%) | 25 | Origine del Colore, 顏色來源, 颜色来源 | Localized display name/label for the field: option |
| stone.stone_quality.origin_colour.value | NoneType, str | 1843 | 1005 (54.5%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.stone_quality.price | int | 1843 | 0 (0.0%) | 519 | 58, 230, 120 | Monetary value or price-related setting |
| stone.stone_quality.qty | dict | 1843 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.stone_quality.qty.default_label | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | Localized display name/label for the field: default |
| stone.stone_quality.qty.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.stone_quality.qty.label | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| stone.stone_quality.qty.option_title | str | 1843 | 0 (0.0%) | 25 | Quantità di pietre, 石頭數量, 石头数量 | Localized display name/label for the field: option |
| stone.stone_quality.qty.value | int | 1843 | 0 (0.0%) | 22 | 5, 3, 6 | N/A (See parent components for context) |
| stone.stone_quality.quality | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality.default_label | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| stone.stone_quality.quality.default_option_title | str | 1843 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.stone_quality.quality.label | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.stone_quality.quality.option_title | str | 1843 | 0 (0.0%) | 23 | Qualità, 質量, 质量 | Localized display name/label for the field: option |
| stone.stone_quality.quality.value | str | 1843 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins | list | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat.default_label | float | 3 | 0 (0.0%) | 1 | 0.36 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.carat.default_option_title | str | 3 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.carat.label | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.carat.option_title | str | 3 | 0 (0.0%) | 1 | Karat | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.carat.value | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate.default_label | str | 3 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.certificate.default_option_title | str | 3 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.certificate.label | str | 3 | 0 (0.0%) | 1 | GL Zertifiziert | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.certificate.option_title | str | 3 | 0 (0.0%) | 1 | Zertifizierung | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.certificate.value | str | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity.default_label | str | 3 | 0 (0.0%) | 1 | AAA | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.clarity.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.clarity.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.clarity.option_title | str | 3 | 0 (0.0%) | 1 | Reinheit | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.clarity.value | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour.default_label | str | 3 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.colour.default_option_title | str | 3 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.colour.label | str | 3 | 0 (0.0%) | 3 | Grün, Rot, Dunkelblau | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.colour.option_title | str | 3 | 0 (0.0%) | 1 | Farbe | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.colour.value | str | 3 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut.default_label | str | 3 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.cut.default_option_title | str | 3 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.cut.label | str | 3 | 0 (0.0%) | 1 | Sehr gut | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.cut.option_title | str | 3 | 0 (0.0%) | 1 | Schliff | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.cut.value | str | 3 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter.default_label | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.diameter.default_option_title | str | 3 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.diameter.label | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.diameter.option_title | str | 3 | 0 (0.0%) | 1 | Durchmesser | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.diameter.value | str | 3 | 0 (0.0%) | 1 | 6.0x4.0 mm | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.id | str | 3 | 0 (0.0%) | 3 | 6338, 6378, 6418 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin.default_label | str | 3 | 0 (0.0%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin.default_option_title | str | 3 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin.label | str | 3 | 0 (0.0%) | 2 | Afrikanisch, Wärme behandelt | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin.option_title | str | 3 | 0 (0.0%) | 2 | Ursprungsland, Hitzebehandlung | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.origin.value | str | 3 | 0 (0.0%) | 2 | african, heated | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour.default_label | NoneType | 3 | 3 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin_colour.default_option_title | str | 3 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.origin_colour.label | str | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.origin_colour.option_title | str | 3 | 0 (0.0%) | 1 | Farbursprung | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.origin_colour.value | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.price | int | 3 | 0 (0.0%) | 3 | 479, 383, 299 | Monetary value or price-related setting |
| stone.stone_quality.quality_origins.qty | dict | 3 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.stone_quality.quality_origins.qty.default_label | int | 3 | 0 (0.0%) | 1 | 1 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.qty.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.qty.label | int | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.qty.option_title | str | 3 | 0 (0.0%) | 1 | Anzahl der Steine | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.qty.value | int | 3 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality.default_label | str | 3 | 0 (0.0%) | 1 | AAA | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.quality.default_option_title | str | 3 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.quality.label | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.quality.option_title | str | 3 | 0 (0.0%) | 1 | Qualität | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.quality.value | str | 3 | 0 (0.0%) | 1 | AAA | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape.default_label | str | 3 | 0 (0.0%) | 1 | Oval | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.shape.default_option_title | str | 3 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.shape.label | str | 3 | 0 (0.0%) | 1 | Oval | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.shape.option_title | str | 3 | 0 (0.0%) | 1 | Schliffform | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.shape.value | str | 3 | 0 (0.0%) | 1 | 9 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name.default_label | NoneType | 3 | 3 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_name.default_option_title | str | 3 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_name.label | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_name.option_title | str | 3 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.stone_name.value | NoneType | 3 | 3 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type.default_label | str | 3 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_type.default_option_title | str | 3 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.stone_type.label | str | 3 | 0 (0.0%) | 3 | Smaragd, Rubin, Saphir | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.stone_type.option_title | str | 3 | 0 (0.0%) | 1 | Steinarten | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.stone_type.value | str | 3 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat | dict | 3 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat.default_label | float | 3 | 0 (0.0%) | 1 | 0.36 | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.total_carat.default_option_title | str | 3 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.stone_quality.quality_origins.total_carat.label | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| stone.stone_quality.quality_origins.total_carat.option_title | str | 3 | 0 (0.0%) | 1 | Karat | Localized display name/label for the field: option |
| stone.stone_quality.quality_origins.total_carat.value | float | 3 | 0 (0.0%) | 1 | 0.36 | N/A (See parent components for context) |
| stone.stone_quality.shape | dict | 1843 | 0 (0.0%) | 1 | N/A | Gemstone shape |
| stone.stone_quality.shape.default_label | str | 1843 | 0 (0.0%) | 5 | Round, Princess, Cabochon Round | Localized display name/label for the field: default |
| stone.stone_quality.shape.default_option_title | str | 1843 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.stone_quality.shape.label | str | 1843 | 0 (0.0%) | 28 | Rotondo, 圓形, 圆形 | N/A (See parent components for context) |
| stone.stone_quality.shape.option_title | str | 1843 | 0 (0.0%) | 19 | Forma, 形狀, 宝石形状 | Localized display name/label for the field: option |
| stone.stone_quality.shape.value | str | 1843 | 0 (0.0%) | 5 | 1, 11, 3 | N/A (See parent components for context) |
| stone.stone_quality.stone_name | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_name.default_label | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.stone_quality.stone_name.default_option_title | str | 1843 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.stone_quality.stone_name.label | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_name.option_title | str | 1843 | 0 (0.0%) | 19 | Nome, 名字, Name | Localized display name/label for the field: option |
| stone.stone_quality.stone_name.value | NoneType | 1843 | 1843 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_type | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.stone_type.default_label | str | 1843 | 0 (0.0%) | 20 | Diamond, Green Diamond, Yellow Diamond | Localized display name/label for the field: default |
| stone.stone_quality.stone_type.default_option_title | str | 1843 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.stone_quality.stone_type.label | str | 1843 | 0 (0.0%) | 137 | Diamante, Diamante Verde, Diamante Giallo | N/A (See parent components for context) |
| stone.stone_quality.stone_type.option_title | str | 1843 | 0 (0.0%) | 19 | Tipo di Pietra, 寶石類型, 宝石类型 | Localized display name/label for the field: option |
| stone.stone_quality.stone_type.value | str | 1843 | 0 (0.0%) | 20 | diamond-Brillant, greendiamond, yellowdiamond | N/A (See parent components for context) |
| stone.stone_quality.total_carat | dict | 1843 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.stone_quality.total_carat.default_label | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | Localized display name/label for the field: default |
| stone.stone_quality.total_carat.default_option_title | str | 1843 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| stone.stone_quality.total_carat.label | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| stone.stone_quality.total_carat.option_title | str | 1843 | 0 (0.0%) | 34 | Carato totale della pietra, 寶石總重量, 宝石总重量 | Localized display name/label for the field: option |
| stone.stone_quality.total_carat.value | float | 1843 | 0 (0.0%) | 37 | 0.075, 0.024, 0.03 | N/A (See parent components for context) |
| stone.store_title | str | 6165 | 0 (0.0%) | 469 | Senza Pietra, Diamante, Diamante Nero | Localized display name/label for the field: store |
| stone.title | str | 6165 | 0 (0.0%) | 469 | Senza Pietra, Diamante, Diamante Nero | Display name of the gemstone |
| store_id | str | 500 | 0 (0.0%) | 52 | glit, glhk, glcn | Store or Country code |
| type_id | str | 500 | 0 (0.0%) | 2 | product_set, simple | Product type code |

---
*Ghi chú: Bảng này được tạo tự động dựa trên mẫu dữ liệu hiện tại.*