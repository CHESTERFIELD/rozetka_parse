# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from rozetka_items_crape.mysite.rozetka.models import Category, Product


class RozetkaItemsCrapeItem(scrapy.Item):
    pass


class CategoryItem(DjangoItem):
    django_model = Category


class ProductItem(DjangoItem):
    django_model = Product
