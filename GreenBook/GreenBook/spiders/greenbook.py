# -*- coding: utf-8 -*-
import scrapy


class GreenbookSpider(scrapy.Spider):
    name = "greenbook"
    allowed_domains = ["thegreenbook.com"]
    start_urls = (
        'http://www.thegreenbook.com/',
    )

    def parse(self, response):
        pass
