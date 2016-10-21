# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GreenBookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address= scrapy.Field()
    tel= scrapy.Field()
    mail = scrapy.Field()
    website = scrapy.Field()

