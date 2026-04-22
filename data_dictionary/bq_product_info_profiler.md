# Data Dictionary: BigQuery: product_info

Generated at: 2026-04-22 16:14:25

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| attribute_set | str | 1000 | 0 (0.0%) | 3 | diamonds, default, trauring | Name of the attribute set |
| attribute_set_id | int | 1000 | 0 (0.0%) | 3 | 55, 4, 26 | ID of the product's attribute set |
| category_id | int | 1000 | 0 (0.0%) | 15 | 0, 751, 605 | Unique ID of the primary category |
| category_name | str | 1000 | 0 (0.0%) | 129 | , Anelli Nocca, Anelli di fidanzamento | Display name of the category |
| collection | str | 1000 | 0 (0.0%) | 3 | , 4380,6071, classic | Project collection name |
| collection_id | NoneType, int | 1000 | 585 (58.5%) | 1 | 159 | Unique ID of the collection |
| colour | dict | 1000 | 0 (0.0%) | 1 | N/A | Metal and Alloy configuration options |
| colour.list | list | 1000 | 1000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| custom | dict | 1000 | 0 (0.0%) | 1 | N/A | Miscellaneous custom options |
| custom.list | list | 1000 | 1000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| fixed_silver_weight | float | 1000 | 0 (0.0%) | 1 | 0.0 | Fixed silver weight for silver items |
| gender | str | 1000 | 0 (0.0%) | 3 | women, False, men | Target gender |
| gold_weight | str | 1000 | 0 (0.0%) | 408 | 4.1535, 3.8415, 4.8867 | Estimated gold weight of the metal part |
| material_design | NoneType, str | 1000 | 960 (96.0%) | 1 | nan | Design code for the material/alloy |
| max_price | str | 1000 | 0 (0.0%) | 924 | 16.663,00 €, 13.688,00 €, 17.038,00 € | Formatted highest possible price for the product |
| media_image | dict | 1000 | 0 (0.0%) | 1 | N/A | Product images container |
| media_image.default_position | int | 1000 | 0 (0.0%) | 3 | 1, 2, 3 | N/A (See parent components for context) |
| media_image.image_load_type | NoneType, str | 1000 | 887 (88.7%) | 1 | layer | N/A (See parent components for context) |
| media_image.image_view_types | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list | list | 1000 | 925 (92.5%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element | dict | 75 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element.metadata | str | 75 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element.position | NoneType | 75 | 75 (100.0%) | 0 | N/A | Display sequence or sorting order |
| media_image.image_view_types.list.element.type | str | 75 | 0 (0.0%) | 1 | try_on_with_ai | N/A (See parent components for context) |
| media_image.images | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list.element | dict | 4234 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.area_view | NoneType, str | 4234 | 247 (5.8%) | 2 | grid, thumb | N/A (See parent components for context) |
| media_image.images.list.element.config | NoneType | 4234 | 4234 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.image_view | str | 4234 | 0 (0.0%) | 3 | general, 3d, compare | N/A (See parent components for context) |
| media_image.images.list.element.is_default | NoneType, bool | 4234 | 118 (2.8%) | 2 | True, False | Boolean flag/binary status: default |
| media_image.images.list.element.is_feature | bool | 4234 | 0 (0.0%) | 2 | True, False | Boolean flag/binary status: feature |
| media_image.images.list.element.is_video | NoneType | 4234 | 4234 (100.0%) | 0 | N/A | Boolean flag/binary status: video |
| media_image.images.list.element.label | str | 4234 | 0 (0.0%) | 998 | GLAMIRA Armband Kizzy 20 cm, GLAMIRA Armband Bettie 16 cm, GLAMIRA Armband Bettie 20 cm | N/A (See parent components for context) |
| media_image.images.list.element.large_image_url | str | 4234 | 0 (0.0%) | 4117 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg | Web URL link to the resource: large_image |
| media_image.images.list.element.media_type | str | 4234 | 0 (0.0%) | 1 | image | N/A (See parent components for context) |
| media_image.images.list.element.medium_image_url | str | 4234 | 0 (0.0%) | 4117 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516 | Web URL link to the resource: medium_image |
| media_image.images.list.element.medium_middle_image_url | str | 4234 | 0 (0.0%) | 4117 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.images.list.element.meta | NoneType | 4234 | 4234 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.placeholder_alt | NoneType, str | 4234 | 956 (22.6%) | 3273 | ALLOY_TITLE Oval STONE_TITLE Armband Kizzy 20 cm view 1, ALLOY_TITLE Oval STONE_TITLE Armband Kizzy 20 cm view 2, ALLOY_TITLE Oval STONE_TITLE Armband Kizzy 20 cm view 3 | N/A (See parent components for context) |
| media_image.images.list.element.position | NoneType, int | 4234 | 118 (2.8%) | 7 | 1, 2, 3 | Display sequence or sorting order |
| media_image.images.list.element.small_image_url | str | 4234 | 0 (0.0%) | 4117 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220 | Web URL link to the resource: small_image |
| media_image.images.list.element.sticky_image_url | str | 4234 | 0 (0.0%) | 4117 | https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/3/sku/kizzy/diamond/multisapphire_AAA/stone2/diamond-zirconia_AAAAA/alloycolour/white.jpg?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.images.list.element.watermark | NoneType | 4234 | 4234 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.lcpMediaUrl | NoneType, str | 1000 | 995 (99.5%) | 1 | https://www.glamira.com.au/media | N/A (See parent components for context) |
| media_image.paths | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.paths.large_image_url | str | 1000 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/, https://cdn-media.glamira.com/media/catalog/product/, https://cdn.glamira.cn/media/product/newgeneration/ | Web URL link to the resource: large_image |
| media_image.paths.medium_image_url | str | 1000 | 0 (0.0%) | 4 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/?width=700&height=700, https://cdn-media.glamira.com/media/catalog/product/ | Web URL link to the resource: medium_image |
| media_image.paths.medium_middle_image_url | str | 1000 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/catalog/product/, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.paths.small_image_url | str | 1000 | 0 (0.0%) | 4 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/?width=110&height=110, https://cdn-media.glamira.com/media/catalog/product/ | Web URL link to the resource: small_image |
| media_image.paths.sticky_image_url | str | 1000 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/catalog/product/, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.sku_image | NoneType, str | 1000 | 5 (0.5%) | 647 | kizzy, monica-bra, myrl | URL for the main SKU image |
| media_image.total_thumbs | int | 1000 | 0 (0.0%) | 7 | 5, 3, 4 | N/A (See parent components for context) |
| media_video | dict | 1000 | 0 (0.0%) | 1 | N/A | Product video container |
| media_video.videos | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list | list | 1000 | 542 (54.2%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list.element | dict | 503 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list.element.file_name | str | 503 | 0 (0.0%) | 443 | kizzy.mp4, monica-bra.mp4, myrl.mp4 | N/A (See parent components for context) |
| media_video.videos.list.element.hidden | bool | 503 | 0 (0.0%) | 2 | False, True | N/A (See parent components for context) |
| media_video.videos.list.element.id | str | 503 | 0 (0.0%) | 2 | 1191, 1392 | N/A (See parent components for context) |
| media_video.videos.list.element.label | str | 503 | 0 (0.0%) | 457 | GLAMIRA Armband Kizzy 20 cm, GLAMIRA Armband Bettie 16 cm, GLAMIRA Armband Bettie 20 cm | N/A (See parent components for context) |
| media_video.videos.list.element.media_type | str | 503 | 0 (0.0%) | 1 | video | N/A (See parent components for context) |
| media_video.videos.list.element.name | str | 503 | 0 (0.0%) | 2 | video, video2 | N/A (See parent components for context) |
| media_video.videos.list.element.url | str | 503 | 0 (0.0%) | 469 | https://cdn-media.glamira.com/media/product/layer/kizzy/kizzy.mp4, https://cdn-media.glamira.com/media/product/layer/monica-bra/monica-bra.mp4, https://cdn-media.glamira.com/media/product/layer/myrl/myrl.mp4 | N/A (See parent components for context) |
| min_price | str | 1000 | 0 (0.0%) | 798 | 1.253,00 €, 1.350,00 €, 1.672,00 € | Formatted lowest possible price for the product |
| none_metal_weight | float | 1000 | 0 (0.0%) | 1 | 0.0 | Weight of the non-metal components |
| product_id | int | 1000 | 0 (0.0%) | 999 | 110681, 110682, 110683 | Unique identifier for the product |
| product_name | str | 1000 | 0 (0.0%) | 998 | GLAMIRA Armband Kizzy 20 cm, GLAMIRA Armband Bettie 16 cm, GLAMIRA Armband Bettie 20 cm | Full name of the product |
| product_type | str | 1000 | 0 (0.0%) | 14 | bracelet, earring, --_select_-- | Broad product category |
| product_type_value | str | 1000 | 0 (0.0%) | 14 | 6, 2, nan | Internal identifier for the product type |
| sku | str | 1000 | 0 (0.0%) | 999 | kizzy-20, monica-bra-16, monica-bra-20 | Stock Keeping Unit |
| stone | dict | 1000 | 0 (0.0%) | 1 | N/A | List of gemstone configurations currently assigned to the product |
| stone.list | list | 1000 | 1000 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| store_id | str | 1000 | 0 (0.0%) | 53 | glde, glat, glch | Store or Country code |
| type_id | str | 1000 | 0 (0.0%) | 4 | simple, virtual, deposit | Product type code |

---
*Ghi chú: Bảng này được tạo tự động dựa trên mẫu dữ liệu hiện tại.*