# Data Dictionary: BigQuery: product_info

Generated at: 2026-06-27 18:21:40

| Field Path | Types | Instances | Nulls | Uniques | Sample Data | Description |
| --- | --- | --- | --- | --- | --- | --- |
| attribute_set | str | 1000 | 0 (0.0%) | 2 | trauring, diamonds | Name of the attribute set |
| attribute_set_id | int | 1000 | 0 (0.0%) | 2 | 26, 55 | ID of the product's attribute set |
| category_id | int | 1000 | 0 (0.0%) | 12 | 689, 690, 688 | Unique ID of the primary category |
| category_name | NoneType, str | 1000 | 720 (72.0%) | 77 | Fedi nuziali da donna, Kobiece Pierścionki, Anéis Femininos de Casamento | Display name of the category |
| collection | NoneType, str | 1000 | 25 (2.5%) | 16 | twinset, vintage, memoire | Project collection name |
| collection_id | NoneType, int | 1000 | 37 (3.7%) | 14 | 4090, 4291, 4396 | Unique ID of the collection |
| colour | dict | 1000 | 0 (0.0%) | 1 | N/A | Metal and Alloy configuration options |
| colour.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| colour.list.element | dict | 19258 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| colour.list.element.colour_code | str | 19258 | 0 (0.0%) | 10 | white_yellow, yellow_white, white | N/A (See parent components for context) |
| colour.list.element.colour_label | str | 19258 | 0 (0.0%) | 213 | Bianco/Giallo, Giallo/Bianco, Bianco | Localized display name/label for the field: colour |
| colour.list.element.default_title | str | 19258 | 0 (0.0%) | 33 | Weiß-Gelbgold 375, Gelb-Weißgold 375, Weißgold 375 | Localized display name/label for the field: default |
| colour.list.element.is_default | bool | 19258 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| colour.list.element.metal | str | 19258 | 0 (0.0%) | 6 | 375, 585, 750 | N/A (See parent components for context) |
| colour.list.element.metal_label | str | 19258 | 0 (0.0%) | 148 | Oro 375 <span class='seperate-line'>-</span> <span>9K</span>, Oro 585 <span class='seperate-line'>-</span> <span>14K</span>, Oro 750 <span class='seperate-line'>-</span> <span>18K</span> | Localized display name/label for the field: metal |
| colour.list.element.option_id | str | 19258 | 0 (0.0%) | 1000 | 291174, 291973, 289239 | Internal system identifier for option |
| colour.list.element.option_type_id | str | 19258 | 0 (0.0%) | 19258 | 2395486, 2395487, 2395483 | Internal system identifier for option_type |
| colour.list.element.price | str | 19258 | 0 (0.0%) | 46 | 0.00, 65.00, 105.00 | Monetary value or price-related setting |
| colour.list.element.price_type | str | 19258 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| colour.list.element.sku | str | 19258 | 0 (0.0%) | 33 | white_yellow-375, yellow_white-375, white-375 | Unique Stock Keeping Unit code |
| colour.list.element.store_title | str | 19258 | 0 (0.0%) | 825 | Oro Bianco & Giallo 375, Oro Giallo & Bianco 375, Oro Bianco 375 | Localized display name/label for the field: store |
| colour.list.element.title | str | 19258 | 0 (0.0%) | 825 | Oro Bianco & Giallo 375, Oro Giallo & Bianco 375, Oro Bianco 375 | N/A (See parent components for context) |
| custom | dict | 1000 | 0 (0.0%) | 1 | N/A | Miscellaneous custom options |
| custom.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| custom.list.element | dict | 9825 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| custom.list.element.default_title | str | 9825 | 0 (0.0%) | 26 | 4.0 mm, A, B | Localized display name/label for the field: default |
| custom.list.element.is_default | bool | 9825 | 0 (0.0%) | 2 | True, False | Boolean flag/binary status: default |
| custom.list.element.option_id | str | 9825 | 0 (0.0%) | 4133 | 291178, 291175, 291176 | Internal system identifier for option |
| custom.list.element.option_type_id | str | 9825 | 0 (0.0%) | 9825 | 2395519, 2395508, 2395509 | Internal system identifier for option_type |
| custom.list.element.price | str | 9825 | 0 (0.0%) | 6 | 0.00, 3.00, 15.00 | Monetary value or price-related setting |
| custom.list.element.price_type | str | 9825 | 0 (0.0%) | 2 | fixed, percent | Monetary value or price-related setting |
| custom.list.element.sku | str | 9825 | 0 (0.0%) | 28 | w4, prA, prB | Unique Stock Keeping Unit code |
| custom.list.element.store_title | str | 9825 | 0 (0.0%) | 216 | 4.0 mm, A, B | Localized display name/label for the field: store |
| custom.list.element.title | str | 9825 | 0 (0.0%) | 216 | 4.0 mm, A, B | N/A (See parent components for context) |
| fixed_silver_weight | float | 1000 | 0 (0.0%) | 1 | 0.0 | Fixed silver weight for silver items |
| gender | str | 1000 | 0 (0.0%) | 3 | women, men, False | Target gender |
| gold_weight | str | 1000 | 0 (0.0%) | 292 | 1.19, 1.56, 1.8213 | Estimated gold weight of the metal part |
| material_design | NoneType | 1000 | 1000 (100.0%) | 0 | N/A | Design code for the material/alloy |
| max_price | str | 1000 | 0 (0.0%) | 954 | 5.395,00 €, 23 078,00 zł, 7 990,00 € | Formatted highest possible price for the product |
| media_image | dict | 1000 | 0 (0.0%) | 1 | N/A | Product images container |
| media_image.default_position | int | 1000 | 0 (0.0%) | 3 | 2, 3, 1 | N/A (See parent components for context) |
| media_image.image_load_type | NoneType, str | 1000 | 170 (17.0%) | 1 | layer | N/A (See parent components for context) |
| media_image.image_view_types | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list | list | 1000 | 918 (91.8%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element | dict | 82 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element.metadata | NoneType | 82 | 82 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.image_view_types.list.element.position | NoneType | 82 | 82 (100.0%) | 0 | N/A | Display sequence or sorting order |
| media_image.image_view_types.list.element.type | str | 82 | 0 (0.0%) | 1 | try_on_with_ai | N/A (See parent components for context) |
| media_image.images | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list.element | dict | 2812 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.area_view | NoneType, str | 2812 | 42 (1.5%) | 2 | grid, thumb | N/A (See parent components for context) |
| media_image.images.list.element.config | NoneType | 2812 | 2812 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.image_view | str | 2812 | 0 (0.0%) | 3 | general, 3d, compare | N/A (See parent components for context) |
| media_image.images.list.element.is_default | NoneType, bool | 2812 | 42 (1.5%) | 2 | True, False | Boolean flag/binary status: default |
| media_image.images.list.element.is_feature | bool | 2812 | 0 (0.0%) | 2 | True, False | Boolean flag/binary status: feature |
| media_image.images.list.element.is_video | NoneType | 2812 | 2812 (100.0%) | 0 | N/A | Boolean flag/binary status: video |
| media_image.images.list.element.label | str | 2812 | 0 (0.0%) | 1000 | Fede nuziale donna Bright Line 4 mm, Obrączka ślubna damska Charming Queen 4 mm, Anel Casamento Feminino Golden Infinity 5 mm | N/A (See parent components for context) |
| media_image.images.list.element.large_image_url | str | 2812 | 0 (0.0%) | 2812 | https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/4/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319100-WOMEN/womenstone/sapphire_AAAAA/alloycolour/red/width/w4/profile/prA/surface/polished.jpg | Web URL link to the resource: large_image |
| media_image.images.list.element.media_type | str | 2812 | 0 (0.0%) | 1 | image | N/A (See parent components for context) |
| media_image.images.list.element.medium_image_url | str | 2812 | 0 (0.0%) | 2812 | https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/4/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319100-WOMEN/womenstone/sapphire_AAAAA/alloycolour/red/width/w4/profile/prA/surface/polished.jpg?width=516&height=516 | Web URL link to the resource: medium_image |
| media_image.images.list.element.medium_middle_image_url | str | 2812 | 0 (0.0%) | 2812 | https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/4/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319100-WOMEN/womenstone/sapphire_AAAAA/alloycolour/red/width/w4/profile/prA/surface/polished.jpg?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.images.list.element.meta | NoneType | 2812 | 2812 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.images.list.element.placeholder_alt | NoneType, str | 2812 | 58 (2.1%) | 2754 | ALLOY_TITLE Rotondo STONE_TITLE Fede nuziale donna Bright Line 4 mm view 1, ALLOY_TITLE Rotondo STONE_TITLE Fede nuziale donna Bright Line 4 mm view 2, ALLOY_TITLE Okrągły STONE_TITLE Obrączka ślubna damska Charming Queen 4 mm view 1 | N/A (See parent components for context) |
| media_image.images.list.element.position | NoneType, int | 2812 | 42 (1.5%) | 6 | 2, 4, 3 | Display sequence or sorting order |
| media_image.images.list.element.small_image_url | str | 2812 | 0 (0.0%) | 2812 | https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/4/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319100-WOMEN/womenstone/sapphire_AAAAA/alloycolour/red/width/w4/profile/prA/surface/polished.jpg?width=220&height=220 | Web URL link to the resource: small_image |
| media_image.images.list.element.sticky_image_url | str | 2812 | 0 (0.0%) | 2812 | https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/4/sku/gwd-h14319081-WOMEN/womenstone/diamond-zirconia_AAAAA/alloycolour/white/width/w4/profile/prB/surface/polished.jpg?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/view/2/sku/gwd-h14319100-WOMEN/womenstone/sapphire_AAAAA/alloycolour/red/width/w4/profile/prA/surface/polished.jpg?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.images.list.element.watermark_link | NoneType | 2812 | 2812 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| media_image.lcpMediaUrl | NoneType, str | 1000 | 986 (98.6%) | 2 | https://www.glamira.com.au/media, https://www.glamira.co.nz/media | N/A (See parent components for context) |
| media_image.paths | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_image.paths.large_image_url | str | 1000 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/, https://cdn.glamira.cn/media/product/newgeneration/ | Web URL link to the resource: large_image |
| media_image.paths.medium_image_url | str | 1000 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn-media.glamira.com/media/product/newgeneration/?width=700&height=700, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516 | Web URL link to the resource: medium_image |
| media_image.paths.medium_middle_image_url | str | 1000 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/?width=516&height=516, https://cdn.glamira.cn/media/product/newgeneration/?width=516&height=516 | Web URL link to the resource: medium_middle_image |
| media_image.paths.small_image_url | str | 1000 | 0 (0.0%) | 3 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn-media.glamira.com/media/product/newgeneration/?width=110&height=110, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220 | Web URL link to the resource: small_image |
| media_image.paths.sticky_image_url | str | 1000 | 0 (0.0%) | 2 | https://cdn-media.glamira.com/media/product/newgeneration/?width=220&height=220, https://cdn.glamira.cn/media/product/newgeneration/?width=220&height=220 | Web URL link to the resource: sticky_image |
| media_image.sku_image | str | 1000 | 0 (0.0%) | 618 | gwd-h14319081-WOMEN, gwd-h14319100-WOMEN, gwd-h14319035-WOMEN | URL for the main SKU image |
| media_image.total_thumbs | int | 1000 | 0 (0.0%) | 5 | 4, 6, 3 | N/A (See parent components for context) |
| media_video | dict | 1000 | 0 (0.0%) | 1 | N/A | Product video container |
| media_video.videos | dict | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list | list | 1000 | 890 (89.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list.element | dict | 138 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| media_video.videos.list.element.file_name | str | 138 | 0 (0.0%) | 138 | gwd-h14319086n-4_1.mp4, gwd-h14319086n-4_2.mp4, gwd-h14319086n-8_1.mp4 | N/A (See parent components for context) |
| media_video.videos.list.element.hidden | bool | 138 | 0 (0.0%) | 2 | False, True | N/A (See parent components for context) |
| media_video.videos.list.element.id | str | 138 | 0 (0.0%) | 2 | 1191, 1392 | N/A (See parent components for context) |
| media_video.videos.list.element.label | str | 138 | 0 (0.0%) | 110 | Vigselring Charming Harmony 4 mm, Charming Harmony 8 mm, Charming Harmony 10 mm | N/A (See parent components for context) |
| media_video.videos.list.element.media_type | str | 138 | 0 (0.0%) | 1 | video | N/A (See parent components for context) |
| media_video.videos.list.element.name | str | 138 | 0 (0.0%) | 2 | video, video2 | N/A (See parent components for context) |
| media_video.videos.list.element.url | str | 138 | 0 (0.0%) | 138 | https://cdn-media.glamira.com/media/product/layer/gwd-h14319086n/gwd-h14319086n-4_1.mp4, https://cdn-media.glamira.com/media/product/layer/gwd-h14319086n/gwd-h14319086n-4_2.mp4, https://cdn-media.glamira.com/media/product/layer/gwd-h14319086n/gwd-h14319086n-8_1.mp4 | N/A (See parent components for context) |
| min_price | str | 1000 | 0 (0.0%) | 797 | 212,00 €, 911,00 zł, 284,00 € | Formatted lowest possible price for the product |
| none_metal_weight | float | 1000 | 0 (0.0%) | 1 | 0.0 | Weight of the non-metal components |
| options | dict | 1000 | 0 (0.0%) | 1 | N/A | Raw JSON configuration options containing all possible choices |
| options.list | list | 1000 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element | dict | 11069 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.custom_size | str | 11069 | 0 (0.0%) | 2 | 0, 1 | N/A (See parent components for context) |
| options.list.element.default_price | NoneType, str | 11069 | 8405 (75.9%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.list.element.default_price_type | NoneType, str | 11069 | 8405 (75.9%) | 1 | fixed | Monetary value or price-related setting |
| options.list.element.default_title | str | 11069 | 0 (0.0%) | 37 | Damenring, Width, Alloy/Colour | Localized display name/label for the field: default |
| options.list.element.default_value | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.detail_title | str | 11069 | 0 (0.0%) | 469 | Taglia Dell'anello Da Donna, Larghezza, Metallo-Purezza | Localized display name/label for the field: detail |
| options.list.element.engraving_position | NoneType, str | 11069 | 8328 (75.2%) | 2 | inside, outside | N/A (See parent components for context) |
| options.list.element.engraving_type | NoneType, str | 11069 | 8328 (75.2%) | 5 | damenring, herrenring, ring | N/A (See parent components for context) |
| options.list.element.file_extension | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.group | str | 11069 | 0 (0.0%) | 8 | ringsize, custom, alloy | N/A (See parent components for context) |
| options.list.element.image_size_x | NoneType, str | 11069 | 8227 (74.3%) | 1 | 0 | N/A (See parent components for context) |
| options.list.element.image_size_y | NoneType, str | 11069 | 8227 (74.3%) | 1 | 0 | N/A (See parent components for context) |
| options.list.element.is_require | int | 11069 | 0 (0.0%) | 2 | 1, 0 | Boolean flag/binary status: require |
| options.list.element.max_characters | NoneType, str | 11069 | 7214 (65.2%) | 4 | 25, 0, 1 | N/A (See parent components for context) |
| options.list.element.max_characters_wrong | NoneType, str | 11069 | 10876 (98.3%) | 1 | 0 | N/A (See parent components for context) |
| options.list.element.option_id | str | 11069 | 0 (0.0%) | 11069 | 291179, 291178, 291174 | Internal system identifier for option |
| options.list.element.part_type | NoneType, str | 11069 | 3728 (33.7%) | 22 | women_ring_size, width, alloy | N/A (See parent components for context) |
| options.list.element.price | NoneType, str | 11069 | 8405 (75.9%) | 1 | 0.000000 | Monetary value or price-related setting |
| options.list.element.price_type | NoneType, str | 11069 | 8405 (75.9%) | 1 | fixed | Monetary value or price-related setting |
| options.list.element.product_id | str | 11069 | 0 (0.0%) | 1000 | 106468, 106548, 106265 | Internal system identifier for product |
| options.list.element.sku | NoneType, str | 11069 | 11057 (99.9%) | 5 | DALANE, ALEX, M | Unique Stock Keeping Unit code |
| options.list.element.sort_order | str | 11069 | 0 (0.0%) | 27 | 0, 2, 3 | Display sequence or sorting order |
| options.list.element.stones | NoneType, dict | 11069 | 10285 (92.9%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.stones.list | list | 784 | 3 (0.4%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.stones.list.element | dict | 1017 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.stones.list.element.carat | str | 1017 | 0 (0.0%) | 37 | 0.0100, 0.0050, 0.0150 | N/A (See parent components for context) |
| options.list.element.stones.list.element.clarity | NoneType | 1017 | 1017 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.stones.list.element.diameter | str | 1017 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| options.list.element.stones.list.element.id | str | 1017 | 0 (0.0%) | 1017 | 44611, 49971, 45713 | N/A (See parent components for context) |
| options.list.element.stones.list.element.option_id | str | 1017 | 0 (0.0%) | 220 | 0, 289253, 315158 | Internal system identifier for option |
| options.list.element.stones.list.element.part_type | str | 1017 | 0 (0.0%) | 5 | womenstone, menstone, stone2 | N/A (See parent components for context) |
| options.list.element.stones.list.element.product_id | str | 1017 | 0 (0.0%) | 748 | 106468, 106548, 106265 | Internal system identifier for product |
| options.list.element.stones.list.element.qty | str | 1017 | 0 (0.0%) | 70 | 2, 3, 56 | Quantity or count of items |
| options.list.element.stones.list.element.shape | str | 1017 | 0 (0.0%) | 6 | 1, 11, 8 | N/A (See parent components for context) |
| options.list.element.store_id | int | 11069 | 0 (0.0%) | 55 | 14, 50, 34 | Internal system identifier for store |
| options.list.element.store_price | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.list.element.store_price_type | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.list.element.store_title | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | Localized display name/label for the field: store |
| options.list.element.title | str | 11069 | 0 (0.0%) | 482 | Misura Anello, Larghezza, Metallo-Purezza | N/A (See parent components for context) |
| options.list.element.type | str | 11069 | 0 (0.0%) | 13 | ctsize, width, alloy | N/A (See parent components for context) |
| options.list.element.use_stone | NoneType | 11069 | 11069 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values | dict | 11069 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list | list | 11069 | 1361 (12.3%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element | dict | 51606 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.average_size | NoneType, dict | 51606 | 49738 (96.4%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.average_size.diameter | str | 1868 | 0 (0.0%) | 2 | 16,5, 19,1 | N/A (See parent components for context) |
| options.list.element.values.list.element.average_size.value | str | 1868 | 0 (0.0%) | 2 | 16,5, 19,1 | N/A (See parent components for context) |
| options.list.element.values.list.element.colour_code | NoneType, str | 51606 | 32348 (62.7%) | 10 | white_yellow, yellow_white, white | N/A (See parent components for context) |
| options.list.element.values.list.element.colour_label | NoneType, str | 51606 | 32348 (62.7%) | 213 | Bianco/Giallo, Giallo/Bianco, Bianco | Localized display name/label for the field: colour |
| options.list.element.values.list.element.configure_quality | NoneType, str | 51606 | 38480 (74.6%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones | NoneType, dict | 51606 | 38480 (74.6%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list | list | 13126 | 33 (0.3%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.carat | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.carat.default_label | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.carat.default_option_title | str | 16927 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.carat.label | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.carat.option_title | str | 16927 | 0 (0.0%) | 15 | Carati, Karat, Quilate | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.carat.value | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.certificate | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.certificate.default_label | str | 16927 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.certificate.default_option_title | str | 16927 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.certificate.label | str | 16927 | 0 (0.0%) | 28 | Certificato GL, Certyfikowany przez GL, Certificado GL | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.certificate.option_title | str | 16927 | 0 (0.0%) | 26 | Certificazione, Zaświadczenie, Certificação | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.certificate.value | str | 16927 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.clarity | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.clarity.default_label | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.clarity.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.clarity.label | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.clarity.option_title | str | 16927 | 0 (0.0%) | 26 | Purezza, Czystość Kamienia, Claridade | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.clarity.value | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.colour | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.colour.default_label | NoneType, str | 16927 | 498 (2.9%) | 23 | H, Black, Violet | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.colour.default_option_title | str | 16927 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.colour.label | NoneType, str | 16927 | 499 (2.9%) | 299 | H, Nero, Viola | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.colour.option_title | str | 16927 | 0 (0.0%) | 24 | Colore, Kolor, COR | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.colour.value | NoneType, str | 16927 | 498 (2.9%) | 23 | H, Black, Violet | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.cut | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.cut.default_label | str | 16927 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.cut.default_option_title | str | 16927 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.cut.label | str | 16927 | 0 (0.0%) | 49 | Eccellente, Ottimo, Doskonały | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.cut.option_title | str | 16927 | 0 (0.0%) | 23 | Taglio, Szlif Kamienia, CORTE | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.cut.value | str | 16927 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.diameter | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.diameter.default_label | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.diameter.default_option_title | str | 16927 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.diameter.label | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.diameter.option_title | str | 16927 | 0 (0.0%) | 22 | Diametro, Średnica, Diâmetro | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.diameter.value | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.id | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin.default_label | NoneType, str | 16927 | 14756 (87.2%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.origin.default_option_title | str | 16927 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.origin.label | NoneType, str | 16927 | 14756 (87.2%) | 46 | Africano, Scaldato, Podgrzany | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin.option_title | str | 16927 | 0 (0.0%) | 52 | Origin / Heat Treatment, Paese d\'Origine, Trattamento termico | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.origin.value | NoneType, str | 16927 | 14756 (87.2%) | 2 | african, heated | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin_colour | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin_colour.default_label | NoneType, str | 16927 | 13685 (80.8%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.origin_colour.default_option_title | str | 16927 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.origin_colour.label | NoneType, str | 16927 | 13685 (80.8%) | 45 | Migliorato, Naturale, Wzmocniony | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.origin_colour.option_title | str | 16927 | 0 (0.0%) | 27 | Origine del Colore, Pochodzenie koloru, Origem da cor | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.origin_colour.value | NoneType, str | 16927 | 13685 (80.8%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.price | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| options.list.element.values.list.element.data_stones.list.element.qty | dict | 16927 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.list.element.values.list.element.data_stones.list.element.qty.default_label | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.qty.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.qty.label | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.qty.option_title | str | 16927 | 0 (0.0%) | 27 | Quantità di pietre, Ilość kamieni, Quantidade de pedras | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.qty.value | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.quality | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.quality.default_label | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.quality.default_option_title | str | 16927 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.quality.label | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.quality.option_title | str | 16927 | 0 (0.0%) | 24 | Qualità, Jakość, Qualidade | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.quality.value | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.shape | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.shape.default_label | str | 16927 | 0 (0.0%) | 6 | Round, Princess, Heart | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.shape.default_option_title | str | 16927 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.shape.label | str | 16927 | 0 (0.0%) | 36 | Rotondo, Okrągły, Redondo | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.shape.option_title | str | 16927 | 0 (0.0%) | 20 | Forma, Kształt, Formato | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.shape.value | str | 16927 | 0 (0.0%) | 6 | 1, 11, 8 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_name | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_name.default_label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.stone_name.default_option_title | str | 16927 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.stone_name.label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_name.option_title | str | 16927 | 0 (0.0%) | 21 | Nome, Imię, Név | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.stone_name.value | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_type | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_type.default_label | NoneType, str | 16927 | 1 (0.0%) | 50 | Diamond, Black Diamond, Amethyst | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.stone_type.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.stone_type.label | NoneType, str | 16927 | 1 (0.0%) | 628 | Diamante, Diamante Nero, Ametista | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.stone_type.option_title | str | 16927 | 0 (0.0%) | 21 | Tipo di Pietra, Rodzaj kamienia, Stone Type | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.stone_type.value | str | 16927 | 0 (0.0%) | 51 | diamond-Brillant, blackdiamond, amethyst | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.total_carat | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.total_carat.default_label | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.total_carat.default_option_title | str | 16927 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.data_stones.list.element.total_carat.label | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| options.list.element.values.list.element.data_stones.list.element.total_carat.option_title | str | 16927 | 0 (0.0%) | 39 | Carato totale della pietra, Masa diamentu (w karatach), Carat Total da Pedra | Localized display name/label for the field: option |
| options.list.element.values.list.element.data_stones.list.element.total_carat.value | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| options.list.element.values.list.element.default_quality | NoneType, str | 51606 | 47507 (92.1%) | 5 | AAA, AAAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.default_title | NoneType, str | 51606 | 1868 (3.6%) | 130 | 4.0 mm, Weiß-Gelbgold 375, Gelb-Weißgold 375 | Localized display name/label for the field: default |
| options.list.element.values.list.element.is_default | NoneType, str | 51606 | 481 (0.9%) | 3 | True, False, 0 | Boolean flag/binary status: default |
| options.list.element.values.list.element.max_characters | NoneType, str | 51606 | 51597 (100.0%) | 1 | 25 | N/A (See parent components for context) |
| options.list.element.values.list.element.max_characters_wrong | NoneType, str | 51606 | 51599 (100.0%) | 1 | 0 | N/A (See parent components for context) |
| options.list.element.values.list.element.metal | NoneType, str | 51606 | 32348 (62.7%) | 6 | 375, 585, 750 | N/A (See parent components for context) |
| options.list.element.values.list.element.metal_label | NoneType, str | 51606 | 32348 (62.7%) | 148 | Oro 375 <span class='seperate-line'>-</span> <span>9K</span>, Oro 585 <span class='seperate-line'>-</span> <span>14K</span>, Oro 750 <span class='seperate-line'>-</span> <span>18K</span> | Localized display name/label for the field: metal |
| options.list.element.values.list.element.name | NoneType, str | 51606 | 49738 (96.4%) | 33 | IT, EU, PL | N/A (See parent components for context) |
| options.list.element.values.list.element.option_id | NoneType, str | 51606 | 1868 (3.6%) | 8312 | 291178, 291174, 291182 | Internal system identifier for option |
| options.list.element.values.list.element.option_type_id | NoneType, str | 51606 | 1868 (3.6%) | 49711 | 2395519, 2395486, 2395487 | Internal system identifier for option_type |
| options.list.element.values.list.element.price | NoneType, str | 51606 | 1868 (3.6%) | 1754 | 0.00, 65.00, 105.00 | Monetary value or price-related setting |
| options.list.element.values.list.element.price_type | NoneType, str | 51606 | 1868 (3.6%) | 2 | fixed, percent | Monetary value or price-related setting |
| options.list.element.values.list.element.ringsize_values | NoneType, dict | 51606 | 49738 (96.4%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list | list | 1868 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element | dict | 62963 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element.circumference | NoneType, str | 62963 | 1868 (3.0%) | 72 | 45,9, 46,8, 48,1 | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element.diameter | NoneType, str | 62963 | 1868 (3.0%) | 75 | 14,6, 14,9, 15,3 | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element.size | NoneType, str | 62963 | 1868 (3.0%) | 239 | 6, 7, 8 | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element.title | str | 62963 | 0 (0.0%) | 474 | Seleziona la tua taglia, 6 ( Ø 14,6 ), 7 ( Ø 14,9 ) | N/A (See parent components for context) |
| options.list.element.values.list.element.ringsize_values.list.element.value | NoneType, str | 62963 | 1868 (3.0%) | 75 | 14,6, 14,9, 15,3 | N/A (See parent components for context) |
| options.list.element.values.list.element.sku | NoneType, str | 51606 | 7339 (14.2%) | 124 | w4, white_yellow-375, yellow_white-375 | Unique Stock Keeping Unit code |
| options.list.element.values.list.element.stone_gia | NoneType, dict | 51606 | 51588 (100.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list | list | 18 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.carat | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.carat.default_label | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.carat.default_option_title | str | 4424 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.carat.label | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.carat.option_title | str | 4424 | 0 (0.0%) | 4 | Carats, Karat, Carat | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.carat.value | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.certificate | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.certificate.default_label | str | 4424 | 0 (0.0%) | 1 | GIA | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.certificate.default_option_title | str | 4424 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.certificate.label | str | 4424 | 0 (0.0%) | 1 | GIA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.certificate.option_title | str | 4424 | 0 (0.0%) | 5 | Le Certificat, Zertifizierung, Certification | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.certificate.value | str | 4424 | 0 (0.0%) | 1 | 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.clarity | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.clarity.default_label | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.clarity.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.clarity.label | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.clarity.option_title | str | 4424 | 0 (0.0%) | 6 | Clarté, Reinheit, Stone Clarity | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.clarity.value | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.colour | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.colour.default_label | str | 4424 | 0 (0.0%) | 7 | J, I, H | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.colour.default_option_title | str | 4424 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.colour.label | str | 4424 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.colour.option_title | str | 4424 | 0 (0.0%) | 7 | Couleurs, Farbe, Colour | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.colour.value | str | 4424 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.cut | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.cut.default_label | str | 4424 | 0 (0.0%) | 4 | Good, Very Good, Fair | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.cut.default_option_title | str | 4424 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.cut.label | str | 4424 | 0 (0.0%) | 23 | Bien, Très Bien, Passable | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.cut.option_title | str | 4424 | 0 (0.0%) | 6 | Taille, Schliff, Cut | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.cut.value | str | 4424 | 0 (0.0%) | 4 | 2, 3, 1 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.diameter | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.diameter.default_label | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.diameter.default_option_title | str | 4424 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.diameter.label | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.diameter.option_title | str | 4424 | 0 (0.0%) | 3 | Diamètre, Durchmesser, Diameter | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.diameter.value | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.id | str | 4424 | 0 (0.0%) | 1820 | 11036, 11037, 11038 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.origin.default_option_title | str | 4424 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.origin.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin.option_title | str | 4424 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.origin.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour.default_option_title | str | 4424 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour.option_title | str | 4424 | 0 (0.0%) | 7 | Couleur Original, Farbursprung, Colour Origin | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.origin_colour.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.price | str | 4424 | 0 (0.0%) | 2310 | 5428, 5768, 6220 | Monetary value or price-related setting |
| options.list.element.values.list.element.stone_gia.list.element.qty | dict | 4424 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.list.element.values.list.element.stone_gia.list.element.qty.default_label | str | 4424 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.qty.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.qty.label | str | 4424 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.qty.option_title | str | 4424 | 0 (0.0%) | 6 | Quantité de pierres, Anzahl der Steine, Quantity of stones | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.qty.value | str | 4424 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.quality | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.quality.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.quality.default_option_title | str | 4424 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.quality.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.quality.option_title | str | 4424 | 0 (0.0%) | 6 | Qualité, Qualität, Quality | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.quality.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.shape | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.shape.default_label | str | 4424 | 0 (0.0%) | 3 | Round, Heart, Oval | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.shape.default_option_title | str | 4424 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.shape.label | str | 4424 | 0 (0.0%) | 8 | Rond, Rund, Heart | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.shape.option_title | str | 4424 | 0 (0.0%) | 5 | Formes, Schliffform, Shape | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.shape.value | str | 4424 | 0 (0.0%) | 3 | 1, 8, 9 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_name | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_name.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.stone_name.default_option_title | str | 4424 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.stone_name.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_name.option_title | str | 4424 | 0 (0.0%) | 5 | Nom et Prénom, Name, Naam | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.stone_name.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_type | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_type.default_label | str | 4424 | 0 (0.0%) | 1 | Diamond | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.stone_type.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.stone_type.label | str | 4424 | 0 (0.0%) | 2 | Diamant, Diamond | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.stone_type.option_title | str | 4424 | 0 (0.0%) | 4 | Stone Type, Steinarten, Stentyp | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.stone_type.value | str | 4424 | 0 (0.0%) | 1 | diamond-Brillant | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.total_carat | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.total_carat.default_label | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.total_carat.default_option_title | str | 4424 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_gia.list.element.total_carat.label | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_gia.list.element.total_carat.option_title | str | 4424 | 0 (0.0%) | 5 | Carats, Steinkarat insgesamt, Carat | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_gia.list.element.total_carat.value | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_group | NoneType, str | 51606 | 38480 (74.6%) | 10 | diamond, semi_precious, precious_stone | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality | NoneType, dict | 51606 | 48319 (93.6%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list | list | 3287 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.carat | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.carat.default_label | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.carat.default_option_title | str | 5125 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.carat.label | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.carat.option_title | str | 5125 | 0 (0.0%) | 15 | Carati, Karat, Quilate | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.carat.value | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.certificate | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.certificate.default_label | str | 5125 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.certificate.default_option_title | str | 5125 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.certificate.label | str | 5125 | 0 (0.0%) | 27 | Certificato GL, Certyfikowany przez GL, Certificado GL | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.certificate.option_title | str | 5125 | 0 (0.0%) | 26 | Certificazione, Zaświadczenie, Certificação | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.certificate.value | str | 5125 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.clarity | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.clarity.default_label | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.clarity.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.clarity.label | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.clarity.option_title | str | 5125 | 0 (0.0%) | 26 | Purezza, Czystość Kamienia, Claridade | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.clarity.value | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.colour | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.colour.default_label | str | 5125 | 0 (0.0%) | 33 | H, Fancy Dark, Fancy Yellow | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.colour.default_option_title | str | 5125 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.colour.label | str | 5125 | 0 (0.0%) | 187 | H, Scuro Fantasia, Giallo Fantasia | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.colour.option_title | str | 5125 | 0 (0.0%) | 24 | Colore, Kolor, COR | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.colour.value | str | 5125 | 0 (0.0%) | 33 | H, Fancy Dark, Fancy Yellow | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.cut | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.cut.default_label | str | 5125 | 0 (0.0%) | 3 | Excellent, Very Good, Good | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.cut.default_option_title | str | 5125 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.cut.label | str | 5125 | 0 (0.0%) | 55 | Eccellente, Ottimo, Doskonały | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.cut.option_title | str | 5125 | 0 (0.0%) | 23 | Taglio, Szlif Kamienia, CORTE | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.cut.value | str | 5125 | 0 (0.0%) | 3 | 4, 3, 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.diameter | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.diameter.default_label | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.diameter.default_option_title | str | 5125 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.diameter.label | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.diameter.option_title | str | 5125 | 0 (0.0%) | 22 | Diametro, Średnica, Diâmetro | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.diameter.value | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.id | str | 5125 | 0 (0.0%) | 982 | 6324, 6306, 9087 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.label | str | 5125 | 0 (0.0%) | 138 | VS, VVS, Scuro Fantasia | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin.default_label | NoneType, str | 5125 | 4999 (97.5%) | 2 | African, Heated | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.origin.default_option_title | str | 5125 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.origin.label | NoneType, str | 5125 | 4999 (97.5%) | 11 | Africain, Chauffée, Afrikanisch | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin.option_title | str | 5125 | 0 (0.0%) | 12 | Origin / Heat Treatment, Pays d'Origine, Traitement de Chauffe | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.origin.value | NoneType, str | 5125 | 4999 (97.5%) | 2 | african, heated | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour.default_label | NoneType, str | 5125 | 3350 (65.4%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour.default_option_title | str | 5125 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour.label | NoneType, str | 5125 | 3350 (65.4%) | 30 | Migliorato, Wzmocniony, Realçada | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour.option_title | str | 5125 | 0 (0.0%) | 27 | Origine del Colore, Pochodzenie koloru, Origem da cor | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.origin_colour.value | NoneType, str | 5125 | 3350 (65.4%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.price | str | 5125 | 0 (0.0%) | 1649 | 17, 64, 36 | Monetary value or price-related setting |
| options.list.element.values.list.element.stone_quality.list.element.qty | dict | 5125 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.list.element.values.list.element.stone_quality.list.element.qty.default_label | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.qty.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.qty.label | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.qty.option_title | str | 5125 | 0 (0.0%) | 26 | Quantità di pietre, Ilość kamieni, Quantidade de pedras | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.qty.value | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality.default_label | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality.default_option_title | str | 5125 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality.label | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality.option_title | str | 5125 | 0 (0.0%) | 24 | Qualità, Jakość, Qualidade | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality.value | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins | NoneType, dict | 5125 | 4999 (97.5%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list | list | 126 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat.default_label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat.default_option_title | str | 252 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat.label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat.option_title | str | 252 | 0 (0.0%) | 4 | Carats, Karat, Carat | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.carat.value | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate.default_label | str | 252 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate.default_option_title | str | 252 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate.label | str | 252 | 0 (0.0%) | 6 | Certifié GL, GL Zertifiziert, GL Certified | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate.option_title | str | 252 | 0 (0.0%) | 5 | Le Certificat, Zertifizierung, Certification | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.certificate.value | str | 252 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity.default_label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity.option_title | str | 252 | 0 (0.0%) | 6 | Clarté, Reinheit, Stone Clarity | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.clarity.value | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour.default_label | str | 252 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour.default_option_title | str | 252 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour.label | str | 252 | 0 (0.0%) | 18 | Vert, Rose, Bleu Foncé | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour.option_title | str | 252 | 0 (0.0%) | 7 | Couleurs, Farbe, Colour | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.colour.value | str | 252 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut.default_label | str | 252 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut.default_option_title | str | 252 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut.label | str | 252 | 0 (0.0%) | 6 | Très Bien, Sehr gut, Very Good | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut.option_title | str | 252 | 0 (0.0%) | 6 | Taille, Schliff, Cut | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.cut.value | str | 252 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter.default_label | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter.default_option_title | str | 252 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter.label | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter.option_title | str | 252 | 0 (0.0%) | 3 | Diamètre, Durchmesser, Diameter | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.diameter.value | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.id | str | 252 | 0 (0.0%) | 120 | 14, 5774, 13 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin.default_label | str | 252 | 0 (0.0%) | 4 | African, Colombian, Heated | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin.default_option_title | str | 252 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin.label | str | 252 | 0 (0.0%) | 22 | Africain, Colombien, Chauffée | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin.option_title | str | 252 | 0 (0.0%) | 11 | Pays d'Origine, Traitement de Chauffe, Ursprungsland | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin.value | str | 252 | 0 (0.0%) | 4 | african, colombian, heated | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.default_label | NoneType | 252 | 252 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.default_option_title | str | 252 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.label | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.option_title | str | 252 | 0 (0.0%) | 7 | Couleur Original, Farbursprung, Colour Origin | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.value | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.price | str | 252 | 0 (0.0%) | 187 | 846, 3176, 1479 | Monetary value or price-related setting |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty | dict | 252 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty.default_label | str | 252 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty.label | str | 252 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty.option_title | str | 252 | 0 (0.0%) | 6 | Quantité de pierres, Anzahl der Steine, Quantity of stones | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.qty.value | str | 252 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality.default_label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality.default_option_title | str | 252 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality.option_title | str | 252 | 0 (0.0%) | 6 | Qualité, Qualität, Quality | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.quality.value | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape.default_label | str | 252 | 0 (0.0%) | 4 | Round, Heart, Oval | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape.default_option_title | str | 252 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape.label | str | 252 | 0 (0.0%) | 9 | Rond, Rund, Heart | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape.option_title | str | 252 | 0 (0.0%) | 5 | Formes, Schliffform, Shape | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.shape.value | str | 252 | 0 (0.0%) | 4 | 1, 8, 9 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.default_label | NoneType | 252 | 252 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.default_option_title | str | 252 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.label | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.option_title | str | 252 | 0 (0.0%) | 5 | Nom et Prénom, Name, Naam | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.value | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.default_label | str | 252 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.label | str | 252 | 0 (0.0%) | 11 | Émeraude, Rubis, Saphir | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.option_title | str | 252 | 0 (0.0%) | 4 | Stone Type, Steinarten, Stentyp | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.value | str | 252 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.default_label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.default_option_title | str | 252 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.option_title | str | 252 | 0 (0.0%) | 5 | Carats, Steinkarat insgesamt, Carat | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.value | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.shape | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.shape.default_label | str | 5125 | 0 (0.0%) | 5 | Round, Princess, Heart | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.shape.default_option_title | str | 5125 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.shape.label | str | 5125 | 0 (0.0%) | 34 | Rotondo, Okrągły, Redondo | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.shape.option_title | str | 5125 | 0 (0.0%) | 20 | Forma, Kształt, Formato | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.shape.value | str | 5125 | 0 (0.0%) | 5 | 1, 11, 8 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_name | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_name.default_label | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.stone_name.default_option_title | str | 5125 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.stone_name.label | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_name.option_title | str | 5125 | 0 (0.0%) | 20 | Nome, Imię, Jméno | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.stone_name.value | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_type | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_type.default_label | str | 5125 | 0 (0.0%) | 34 | Diamond, Green Diamond, Yellow Diamond | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.stone_type.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.stone_type.label | str | 5125 | 0 (0.0%) | 243 | Diamante, Diamante Verde, Diamante Giallo | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.stone_type.option_title | str | 5125 | 0 (0.0%) | 21 | Tipo di Pietra, Rodzaj kamienia, Stone Type | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.stone_type.value | str | 5125 | 0 (0.0%) | 34 | diamond-Brillant, greendiamond, yellowdiamond | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.total_carat | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.total_carat.default_label | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.total_carat.default_option_title | str | 5125 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| options.list.element.values.list.element.stone_quality.list.element.total_carat.label | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| options.list.element.values.list.element.stone_quality.list.element.total_carat.option_title | str | 5125 | 0 (0.0%) | 37 | Carato totale della pietra, Masa diamentu (w karatach), Carat Total da Pedra | Localized display name/label for the field: option |
| options.list.element.values.list.element.stone_quality.list.element.total_carat.value | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| options.list.element.values.list.element.store_title | NoneType, str | 51606 | 1868 (3.6%) | 1724 | 4.0 mm, Oro Bianco & Giallo 375, Oro Giallo & Bianco 375 | Localized display name/label for the field: store |
| options.list.element.values.list.element.title | str | 51606 | 0 (0.0%) | 1754 | IT, EU, 4.0 mm | N/A (See parent components for context) |
| options.list.element.without_stone_same_men | NoneType, int | 11069 | 10424 (94.2%) | 1 | 1 | N/A (See parent components for context) |
| product_id | int | 1000 | 0 (0.0%) | 1000 | 106468, 106548, 106265 | Unique identifier for the product |
| product_name | str | 1000 | 0 (0.0%) | 1000 | Fede nuziale donna Bright Line 4 mm, Obrączka ślubna damska Charming Queen 4 mm, Anel Casamento Feminino Golden Infinity 5 mm | Full name of the product |
| product_type | str | 1000 | 0 (0.0%) | 8 | wedding_ring, ring, earring | Broad product category |
| product_type_value | NoneType, str | 1000 | 1 (0.1%) | 7 | 12, 1, 2 | Internal identifier for the product type |
| sku | str | 1000 | 0 (0.0%) | 1000 | GWD-H14319081-W, GWD-H14319100-W, GWD-H14319035-W | Stock Keeping Unit |
| stone | dict | 1000 | 0 (0.0%) | 1 | N/A | List of gemstone configurations currently assigned to the product |
| stone.list | list | 1000 | 252 (25.2%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element | dict | 13126 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.configure_quality | str | 13126 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.list.element.data_stones | dict | 13126 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list | list | 13126 | 33 (0.3%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.carat | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.carat.default_label | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.carat.default_option_title | str | 16927 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.carat.label | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.carat.option_title | str | 16927 | 0 (0.0%) | 15 | Carati, Karat, Quilate | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.carat.value | str | 16927 | 0 (0.0%) | 37 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.certificate | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.certificate.default_label | str | 16927 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.certificate.default_option_title | str | 16927 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.certificate.label | str | 16927 | 0 (0.0%) | 28 | Certificato GL, Certyfikowany przez GL, Certificado GL | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.certificate.option_title | str | 16927 | 0 (0.0%) | 26 | Certificazione, Zaświadczenie, Certificação | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.certificate.value | str | 16927 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.clarity | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.clarity.default_label | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.clarity.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.clarity.label | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.clarity.option_title | str | 16927 | 0 (0.0%) | 26 | Purezza, Czystość Kamienia, Claridade | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.clarity.value | str | 16927 | 0 (0.0%) | 5 | VS, AAA, AAAAA | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.colour | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.colour.default_label | NoneType, str | 16927 | 498 (2.9%) | 23 | H, Black, Violet | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.colour.default_option_title | str | 16927 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.colour.label | NoneType, str | 16927 | 499 (2.9%) | 299 | H, Nero, Viola | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.colour.option_title | str | 16927 | 0 (0.0%) | 24 | Colore, Kolor, COR | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.colour.value | NoneType, str | 16927 | 498 (2.9%) | 23 | H, Black, Violet | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.cut | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.cut.default_label | str | 16927 | 0 (0.0%) | 2 | Excellent, Very Good | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.cut.default_option_title | str | 16927 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.cut.label | str | 16927 | 0 (0.0%) | 49 | Eccellente, Ottimo, Doskonały | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.cut.option_title | str | 16927 | 0 (0.0%) | 23 | Taglio, Szlif Kamienia, CORTE | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.cut.value | str | 16927 | 0 (0.0%) | 2 | 4, 3 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.diameter | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.diameter.default_label | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.diameter.default_option_title | str | 16927 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.diameter.label | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.diameter.option_title | str | 16927 | 0 (0.0%) | 22 | Diametro, Średnica, Diâmetro | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.diameter.value | str | 16927 | 0 (0.0%) | 35 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.id | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin.default_label | NoneType, str | 16927 | 14756 (87.2%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.origin.default_option_title | str | 16927 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.origin.label | NoneType, str | 16927 | 14756 (87.2%) | 46 | Africano, Scaldato, Podgrzany | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin.option_title | str | 16927 | 0 (0.0%) | 52 | Origin / Heat Treatment, Paese d\'Origine, Trattamento termico | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.origin.value | NoneType, str | 16927 | 14756 (87.2%) | 2 | african, heated | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin_colour | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin_colour.default_label | NoneType, str | 16927 | 13685 (80.8%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.origin_colour.default_option_title | str | 16927 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.origin_colour.label | NoneType, str | 16927 | 13685 (80.8%) | 45 | Migliorato, Naturale, Wzmocniony | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.origin_colour.option_title | str | 16927 | 0 (0.0%) | 27 | Origine del Colore, Pochodzenie koloru, Origem da cor | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.origin_colour.value | NoneType, str | 16927 | 13685 (80.8%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.price | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | Monetary value or price-related setting |
| stone.list.element.data_stones.list.element.qty | dict | 16927 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.list.element.data_stones.list.element.qty.default_label | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.qty.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.qty.label | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.qty.option_title | str | 16927 | 0 (0.0%) | 27 | Quantità di pietre, Ilość kamieni, Quantidade de pedras | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.qty.value | str | 16927 | 0 (0.0%) | 70 | 2, 3, 56 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.quality | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.quality.default_label | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.quality.default_option_title | str | 16927 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.quality.label | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.quality.option_title | str | 16927 | 0 (0.0%) | 24 | Qualità, Jakość, Qualidade | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.quality.value | str | 16927 | 0 (0.0%) | 4 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.shape | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.shape.default_label | str | 16927 | 0 (0.0%) | 6 | Round, Princess, Heart | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.shape.default_option_title | str | 16927 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.shape.label | str | 16927 | 0 (0.0%) | 36 | Rotondo, Okrągły, Redondo | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.shape.option_title | str | 16927 | 0 (0.0%) | 20 | Forma, Kształt, Formato | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.shape.value | str | 16927 | 0 (0.0%) | 6 | 1, 11, 8 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_name | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_name.default_label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.stone_name.default_option_title | str | 16927 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.stone_name.label | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_name.option_title | str | 16927 | 0 (0.0%) | 21 | Nome, Imię, Név | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.stone_name.value | NoneType | 16927 | 16927 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_type | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_type.default_label | NoneType, str | 16927 | 1 (0.0%) | 50 | Diamond, Black Diamond, Amethyst | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.stone_type.default_option_title | str | 16927 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.stone_type.label | NoneType, str | 16927 | 1 (0.0%) | 628 | Diamante, Diamante Nero, Ametista | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.stone_type.option_title | str | 16927 | 0 (0.0%) | 21 | Tipo di Pietra, Rodzaj kamienia, Stone Type | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.stone_type.value | str | 16927 | 0 (0.0%) | 51 | diamond-Brillant, blackdiamond, amethyst | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.total_carat | dict | 16927 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.total_carat.default_label | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.total_carat.default_option_title | str | 16927 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| stone.list.element.data_stones.list.element.total_carat.label | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| stone.list.element.data_stones.list.element.total_carat.option_title | str | 16927 | 0 (0.0%) | 39 | Carato totale della pietra, Masa diamentu (w karatach), Carat Total da Pedra | Localized display name/label for the field: option |
| stone.list.element.data_stones.list.element.total_carat.value | str | 16927 | 0 (0.0%) | 139 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| stone.list.element.default_quality | NoneType, str | 13126 | 9027 (68.8%) | 5 | AAA, AAAAA, A | N/A (See parent components for context) |
| stone.list.element.default_title | str | 13126 | 0 (0.0%) | 54 | Diamond, Black Diamond, Amethyst | Localized display name/label for the field: default |
| stone.list.element.is_default | bool | 13126 | 0 (0.0%) | 2 | False, True | Boolean flag/binary status: default |
| stone.list.element.option_id | str | 13126 | 0 (0.0%) | 784 | 291182, 291981, 289253 | Internal system identifier for option |
| stone.list.element.option_type_id | str | 13126 | 0 (0.0%) | 13126 | 2395525, 2395526, 2395527 | Internal system identifier for option_type |
| stone.list.element.price | str | 13126 | 0 (0.0%) | 1734 | 17.00, 7.00, 3.00 | Monetary value or price-related setting |
| stone.list.element.price_type | str | 13126 | 0 (0.0%) | 1 | fixed | Monetary value or price-related setting |
| stone.list.element.sku | str | 13126 | 0 (0.0%) | 51 | diamond-Brillant, blackdiamond, amethyst | Unique Stock Keeping Unit code |
| stone.list.element.stone_gia | NoneType, dict | 13126 | 13108 (99.9%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list | list | 18 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.carat | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.carat.default_label | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.carat.default_option_title | str | 4424 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.carat.label | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.carat.option_title | str | 4424 | 0 (0.0%) | 4 | Carats, Karat, Carat | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.carat.value | str | 4424 | 0 (0.0%) | 9 | 1, 0.99, 0.5 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.certificate | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.certificate.default_label | str | 4424 | 0 (0.0%) | 1 | GIA | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.certificate.default_option_title | str | 4424 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.certificate.label | str | 4424 | 0 (0.0%) | 1 | GIA | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.certificate.option_title | str | 4424 | 0 (0.0%) | 5 | Le Certificat, Zertifizierung, Certification | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.certificate.value | str | 4424 | 0 (0.0%) | 1 | 2 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.clarity | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.clarity.default_label | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.clarity.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.clarity.label | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.clarity.option_title | str | 4424 | 0 (0.0%) | 6 | Clarté, Reinheit, Stone Clarity | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.clarity.value | str | 4424 | 0 (0.0%) | 8 | SI, SI1, VS2 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.colour | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.colour.default_label | str | 4424 | 0 (0.0%) | 7 | J, I, H | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.colour.default_option_title | str | 4424 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.colour.label | str | 4424 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.colour.option_title | str | 4424 | 0 (0.0%) | 7 | Couleurs, Farbe, Colour | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.colour.value | str | 4424 | 0 (0.0%) | 7 | J, I, H | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.cut | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.cut.default_label | str | 4424 | 0 (0.0%) | 4 | Good, Very Good, Fair | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.cut.default_option_title | str | 4424 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.cut.label | str | 4424 | 0 (0.0%) | 23 | Bien, Très Bien, Passable | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.cut.option_title | str | 4424 | 0 (0.0%) | 6 | Taille, Schliff, Cut | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.cut.value | str | 4424 | 0 (0.0%) | 4 | 2, 3, 1 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.diameter | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.diameter.default_label | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.diameter.default_option_title | str | 4424 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.diameter.label | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.diameter.option_title | str | 4424 | 0 (0.0%) | 3 | Diamètre, Durchmesser, Diameter | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.diameter.value | str | 4424 | 0 (0.0%) | 7 | 6.5 mm, 5.0 mm, 6.0x6.0 mm | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.id | str | 4424 | 0 (0.0%) | 1820 | 11036, 11037, 11038 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.origin.default_option_title | str | 4424 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.origin.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin.option_title | str | 4424 | 0 (0.0%) | 1 | Origin / Heat Treatment | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.origin.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin_colour | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin_colour.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.origin_colour.default_option_title | str | 4424 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.origin_colour.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.origin_colour.option_title | str | 4424 | 0 (0.0%) | 7 | Couleur Original, Farbursprung, Colour Origin | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.origin_colour.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.price | str | 4424 | 0 (0.0%) | 2310 | 5428, 5768, 6220 | Monetary value or price-related setting |
| stone.list.element.stone_gia.list.element.qty | dict | 4424 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.list.element.stone_gia.list.element.qty.default_label | str | 4424 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.qty.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.qty.label | str | 4424 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.qty.option_title | str | 4424 | 0 (0.0%) | 6 | Quantité de pierres, Anzahl der Steine, Quantity of stones | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.qty.value | str | 4424 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.quality | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.quality.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.quality.default_option_title | str | 4424 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.quality.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.quality.option_title | str | 4424 | 0 (0.0%) | 6 | Qualité, Qualität, Quality | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.quality.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.shape | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.shape.default_label | str | 4424 | 0 (0.0%) | 3 | Round, Heart, Oval | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.shape.default_option_title | str | 4424 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.shape.label | str | 4424 | 0 (0.0%) | 8 | Rond, Rund, Heart | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.shape.option_title | str | 4424 | 0 (0.0%) | 5 | Formes, Schliffform, Shape | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.shape.value | str | 4424 | 0 (0.0%) | 3 | 1, 8, 9 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_name | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_name.default_label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.stone_name.default_option_title | str | 4424 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.stone_name.label | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_name.option_title | str | 4424 | 0 (0.0%) | 5 | Nom et Prénom, Name, Naam | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.stone_name.value | NoneType | 4424 | 4424 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_type | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_type.default_label | str | 4424 | 0 (0.0%) | 1 | Diamond | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.stone_type.default_option_title | str | 4424 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.stone_type.label | str | 4424 | 0 (0.0%) | 2 | Diamant, Diamond | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.stone_type.option_title | str | 4424 | 0 (0.0%) | 4 | Stone Type, Steinarten, Stentyp | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.stone_type.value | str | 4424 | 0 (0.0%) | 1 | diamond-Brillant | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.total_carat | dict | 4424 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.total_carat.default_label | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.total_carat.default_option_title | str | 4424 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.list.element.stone_gia.list.element.total_carat.label | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | N/A (See parent components for context) |
| stone.list.element.stone_gia.list.element.total_carat.option_title | str | 4424 | 0 (0.0%) | 5 | Carats, Steinkarat insgesamt, Carat | Localized display name/label for the field: option |
| stone.list.element.stone_gia.list.element.total_carat.value | str | 4424 | 0 (0.0%) | 10 | 1, 0.99, 0.98 | N/A (See parent components for context) |
| stone.list.element.stone_group | str | 13126 | 0 (0.0%) | 10 | diamond, semi_precious, precious_stone | N/A (See parent components for context) |
| stone.list.element.stone_quality | NoneType, dict | 13126 | 9839 (75.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list | list | 3287 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.carat | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.carat.default_label | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.carat.default_option_title | str | 5125 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.carat.label | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.carat.option_title | str | 5125 | 0 (0.0%) | 15 | Carati, Karat, Quilate | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.carat.value | str | 5125 | 0 (0.0%) | 28 | 0.01, 0.005, 0.015 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.certificate | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.certificate.default_label | str | 5125 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.certificate.default_option_title | str | 5125 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.certificate.label | str | 5125 | 0 (0.0%) | 27 | Certificato GL, Certyfikowany przez GL, Certificado GL | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.certificate.option_title | str | 5125 | 0 (0.0%) | 26 | Certificazione, Zaświadczenie, Certificação | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.certificate.value | str | 5125 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.clarity | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.clarity.default_label | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.clarity.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.clarity.label | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.clarity.option_title | str | 5125 | 0 (0.0%) | 26 | Purezza, Czystość Kamienia, Claridade | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.clarity.value | str | 5125 | 0 (0.0%) | 10 | VS, VVS, VS1 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.colour | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.colour.default_label | str | 5125 | 0 (0.0%) | 33 | H, Fancy Dark, Fancy Yellow | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.colour.default_option_title | str | 5125 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.colour.label | str | 5125 | 0 (0.0%) | 187 | H, Scuro Fantasia, Giallo Fantasia | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.colour.option_title | str | 5125 | 0 (0.0%) | 24 | Colore, Kolor, COR | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.colour.value | str | 5125 | 0 (0.0%) | 33 | H, Fancy Dark, Fancy Yellow | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.cut | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.cut.default_label | str | 5125 | 0 (0.0%) | 3 | Excellent, Very Good, Good | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.cut.default_option_title | str | 5125 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.cut.label | str | 5125 | 0 (0.0%) | 55 | Eccellente, Ottimo, Doskonały | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.cut.option_title | str | 5125 | 0 (0.0%) | 23 | Taglio, Szlif Kamienia, CORTE | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.cut.value | str | 5125 | 0 (0.0%) | 3 | 4, 3, 2 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.diameter | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.diameter.default_label | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.diameter.default_option_title | str | 5125 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.diameter.label | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.diameter.option_title | str | 5125 | 0 (0.0%) | 22 | Diametro, Średnica, Diâmetro | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.diameter.value | str | 5125 | 0 (0.0%) | 30 | 1.3 mm, 1.0 mm, 1.5 mm | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.id | str | 5125 | 0 (0.0%) | 982 | 6324, 6306, 9087 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.label | str | 5125 | 0 (0.0%) | 138 | VS, VVS, Scuro Fantasia | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin.default_label | NoneType, str | 5125 | 4999 (97.5%) | 2 | African, Heated | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.origin.default_option_title | str | 5125 | 0 (0.0%) | 3 | Origin / Heat Treatment, Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.origin.label | NoneType, str | 5125 | 4999 (97.5%) | 11 | Africain, Chauffée, Afrikanisch | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin.option_title | str | 5125 | 0 (0.0%) | 12 | Origin / Heat Treatment, Pays d'Origine, Traitement de Chauffe | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.origin.value | NoneType, str | 5125 | 4999 (97.5%) | 2 | african, heated | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin_colour | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin_colour.default_label | NoneType, str | 5125 | 3350 (65.4%) | 2 | Enhanced, Natural | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.origin_colour.default_option_title | str | 5125 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.origin_colour.label | NoneType, str | 5125 | 3350 (65.4%) | 30 | Migliorato, Wzmocniony, Realçada | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.origin_colour.option_title | str | 5125 | 0 (0.0%) | 27 | Origine del Colore, Pochodzenie koloru, Origem da cor | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.origin_colour.value | NoneType, str | 5125 | 3350 (65.4%) | 2 | enhanced_color, natural_color | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.price | str | 5125 | 0 (0.0%) | 1649 | 17, 64, 36 | Monetary value or price-related setting |
| stone.list.element.stone_quality.list.element.qty | dict | 5125 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.list.element.stone_quality.list.element.qty.default_label | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.qty.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.qty.label | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.qty.option_title | str | 5125 | 0 (0.0%) | 26 | Quantità di pietre, Ilość kamieni, Quantidade de pedras | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.qty.value | str | 5125 | 0 (0.0%) | 66 | 2, 3, 56 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality.default_label | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality.default_option_title | str | 5125 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality.label | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality.option_title | str | 5125 | 0 (0.0%) | 24 | Qualità, Jakość, Qualidade | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality.value | str | 5125 | 0 (0.0%) | 4 | AAA, AAAA, A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins | NoneType, dict | 5125 | 4999 (97.5%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list | list | 126 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat.default_label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat.default_option_title | str | 252 | 0 (0.0%) | 1 | Carat | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat.label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat.option_title | str | 252 | 0 (0.0%) | 4 | Carats, Karat, Carat | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.carat.value | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate.default_label | str | 252 | 0 (0.0%) | 1 | GL Certified | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate.default_option_title | str | 252 | 0 (0.0%) | 1 | Certification | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate.label | str | 252 | 0 (0.0%) | 6 | Certifié GL, GL Zertifiziert, GL Certified | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate.option_title | str | 252 | 0 (0.0%) | 5 | Le Certificat, Zertifizierung, Certification | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.certificate.value | str | 252 | 0 (0.0%) | 1 | 1 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity.default_label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Clarity | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity.option_title | str | 252 | 0 (0.0%) | 6 | Clarté, Reinheit, Stone Clarity | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.clarity.value | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour.default_label | str | 252 | 0 (0.0%) | 3 | Green, Red, Dark Blue | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour.default_option_title | str | 252 | 0 (0.0%) | 1 | Colour | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour.label | str | 252 | 0 (0.0%) | 18 | Vert, Rose, Bleu Foncé | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour.option_title | str | 252 | 0 (0.0%) | 7 | Couleurs, Farbe, Colour | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.colour.value | str | 252 | 0 (0.0%) | 3 | Green, Red, Dark Blue | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut.default_label | str | 252 | 0 (0.0%) | 1 | Very Good | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut.default_option_title | str | 252 | 0 (0.0%) | 1 | Cut | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut.label | str | 252 | 0 (0.0%) | 6 | Très Bien, Sehr gut, Very Good | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut.option_title | str | 252 | 0 (0.0%) | 6 | Taille, Schliff, Cut | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.cut.value | str | 252 | 0 (0.0%) | 1 | 3 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter.default_label | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter.default_option_title | str | 252 | 0 (0.0%) | 1 | Diameter | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter.label | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter.option_title | str | 252 | 0 (0.0%) | 3 | Diamètre, Durchmesser, Diameter | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.diameter.value | str | 252 | 0 (0.0%) | 10 | 6.5 mm, 7.5 mm, 9.0 mm | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.id | str | 252 | 0 (0.0%) | 120 | 14, 5774, 13 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin.default_label | str | 252 | 0 (0.0%) | 4 | African, Colombian, Heated | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin.default_option_title | str | 252 | 0 (0.0%) | 2 | Country of Origin, Heat Treatment | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin.label | str | 252 | 0 (0.0%) | 22 | Africain, Colombien, Chauffée | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin.option_title | str | 252 | 0 (0.0%) | 11 | Pays d'Origine, Traitement de Chauffe, Ursprungsland | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin.value | str | 252 | 0 (0.0%) | 4 | african, colombian, heated | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.default_label | NoneType | 252 | 252 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.default_option_title | str | 252 | 0 (0.0%) | 1 | Color Origin | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.label | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.option_title | str | 252 | 0 (0.0%) | 7 | Couleur Original, Farbursprung, Colour Origin | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.origin_colour.value | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.price | str | 252 | 0 (0.0%) | 187 | 846, 3176, 1479 | Monetary value or price-related setting |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty | dict | 252 | 0 (0.0%) | 1 | N/A | Quantity or count of items |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty.default_label | str | 252 | 0 (0.0%) | 2 | 1, 2 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Quantity | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty.label | str | 252 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty.option_title | str | 252 | 0 (0.0%) | 6 | Quantité de pierres, Anzahl der Steine, Quantity of stones | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.qty.value | str | 252 | 0 (0.0%) | 2 | 1, 2 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality.default_label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality.default_option_title | str | 252 | 0 (0.0%) | 1 | Quality | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality.label | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality.option_title | str | 252 | 0 (0.0%) | 6 | Qualité, Qualität, Quality | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.quality.value | str | 252 | 0 (0.0%) | 2 | AAA, AAAA | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape.default_label | str | 252 | 0 (0.0%) | 4 | Round, Heart, Oval | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape.default_option_title | str | 252 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape.label | str | 252 | 0 (0.0%) | 9 | Rond, Rund, Heart | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape.option_title | str | 252 | 0 (0.0%) | 5 | Formes, Schliffform, Shape | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.shape.value | str | 252 | 0 (0.0%) | 4 | 1, 8, 9 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.default_label | NoneType | 252 | 252 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.default_option_title | str | 252 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.label | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.option_title | str | 252 | 0 (0.0%) | 5 | Nom et Prénom, Name, Naam | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_name.value | NoneType | 252 | 252 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.default_label | str | 252 | 0 (0.0%) | 3 | Emerald, Ruby, Saphire | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.default_option_title | str | 252 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.label | str | 252 | 0 (0.0%) | 11 | Émeraude, Rubis, Saphir | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.option_title | str | 252 | 0 (0.0%) | 4 | Stone Type, Steinarten, Stentyp | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.stone_type.value | str | 252 | 0 (0.0%) | 3 | emerald, ruby, sapphire | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat | dict | 252 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.default_label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.default_option_title | str | 252 | 0 (0.0%) | 2 | Carat, Total Stone Carat | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.label | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.option_title | str | 252 | 0 (0.0%) | 5 | Carats, Steinkarat insgesamt, Carat | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.quality_origins.list.element.total_carat.value | str | 252 | 0 (0.0%) | 10 | 1, 1.6, 3 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.shape | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.shape.default_label | str | 5125 | 0 (0.0%) | 5 | Round, Princess, Heart | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.shape.default_option_title | str | 5125 | 0 (0.0%) | 1 | Shape | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.shape.label | str | 5125 | 0 (0.0%) | 34 | Rotondo, Okrągły, Redondo | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.shape.option_title | str | 5125 | 0 (0.0%) | 20 | Forma, Kształt, Formato | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.shape.value | str | 5125 | 0 (0.0%) | 5 | 1, 11, 8 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_name | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_name.default_label | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.stone_name.default_option_title | str | 5125 | 0 (0.0%) | 1 | Name | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.stone_name.label | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_name.option_title | str | 5125 | 0 (0.0%) | 20 | Nome, Imię, Jméno | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.stone_name.value | NoneType | 5125 | 5125 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_type | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_type.default_label | str | 5125 | 0 (0.0%) | 34 | Diamond, Green Diamond, Yellow Diamond | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.stone_type.default_option_title | str | 5125 | 0 (0.0%) | 1 | Stone Type | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.stone_type.label | str | 5125 | 0 (0.0%) | 243 | Diamante, Diamante Verde, Diamante Giallo | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.stone_type.option_title | str | 5125 | 0 (0.0%) | 21 | Tipo di Pietra, Rodzaj kamienia, Stone Type | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.stone_type.value | str | 5125 | 0 (0.0%) | 34 | diamond-Brillant, greendiamond, yellowdiamond | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.total_carat | dict | 5125 | 0 (0.0%) | 1 | N/A | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.total_carat.default_label | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.total_carat.default_option_title | str | 5125 | 0 (0.0%) | 2 | Total Stone Carat, Carat | Localized display name/label for the field: default |
| stone.list.element.stone_quality.list.element.total_carat.label | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| stone.list.element.stone_quality.list.element.total_carat.option_title | str | 5125 | 0 (0.0%) | 37 | Carato totale della pietra, Masa diamentu (w karatach), Carat Total da Pedra | Localized display name/label for the field: option |
| stone.list.element.stone_quality.list.element.total_carat.value | str | 5125 | 0 (0.0%) | 120 | 0.02, 0.015, 0.28 | N/A (See parent components for context) |
| stone.list.element.store_title | str | 13126 | 0 (0.0%) | 631 | Diamante, Diamante Nero, Ametista | Localized display name/label for the field: store |
| stone.list.element.title | str | 13126 | 0 (0.0%) | 631 | Diamante, Diamante Nero, Ametista | N/A (See parent components for context) |
| stone.list.element.without_stone_same_men | NoneType | 13126 | 13126 (100.0%) | 0 | N/A | N/A (See parent components for context) |
| store_id | str | 1000 | 0 (0.0%) | 55 | glit, glpl, glpt | Store or Country code |
| type_id | str | 1000 | 0 (0.0%) | 2 | simple, product_set | Product type code |

---
*Note: This table is automatically generated based on the current data sample.*