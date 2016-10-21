# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request


class GreenbookSpider(CrawlSpider):
    name = "greenbook"
    allowed_domains = ["thegreenbook.com"]
    start_urls = (
        'http://www.thegreenbook.com/',
    )

    rules = (
        Rule(SgmlLinkExtractor(allow=r'http://www.thegreenbook.com/products/search'),callback='parse2'),
        Rule(SgmlLinkExtractor(allow=r'http://www.thegreenbook.com/products/[^/]+/$'), callback='parse_item'),
    )

    def parse_item(self, response):
        # i = GreenBookItem()
        # url=response.url
        # i['name'] = response.xpath('//h1/text()').extract()[0]
        # i['address']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[4]
        # i['tel']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[3]
        # i['mail']=u''.join(response.xpath('//div[@id="articleContent"]/descendant::text()').extract())
        # i['website']=''
        
        self.logger.info('I am here!!!!!!!!!!!!!!')
        return {'count':1}
        
    def parse_start_urls(self, response):
        #hxs = HtmlXPathSelector(response)

        #items = []
        import pdb
        urls = response.xpath('//@href').re(r'.*/products/search/.*')
        # pdb.set_trace()
        for url in urls:
            self.logger.info('search:'+url)
            yield Request(url,headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"})
        
    def parse2(self, response):
        #hxs = HtmlXPathSelector(response)

        #items = []
        #import pdb
        urls = response.xpath('//@href').re(r'^/products/.*')
        # pdb.set_trace()
        for url in urls:
            self.logger.info('joinurl:'+url)
            yield Request('http://www.thegreenbook.com'+url,headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"})
