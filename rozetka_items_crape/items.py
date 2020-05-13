# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RozetkaItemsCrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    count_of_pages = scrapy.Field()


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
