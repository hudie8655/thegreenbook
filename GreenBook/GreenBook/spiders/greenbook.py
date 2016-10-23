# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from GreenBook.items import GreenBookItem


class GreenbookSpider(CrawlSpider):
    name = "greenbook"
    allowed_domains = ["thegreenbook.com"]
    start_urls = (
        'http://www.thegreenbook.com/',
    )

    #rules = (
        #Rule(LinkExtractor(allow=r'http://www.thegreenbook.com/products/search'),callback='parse2'),
     #   Rule(LinkExtractor(allow=r'http://www.thegreenbook.com/products/[a-zA-Z-]+/$'), callback='parse_item'),
    #)

#TODO:
#1.用代理访问
#2。获取各项信息
#3。修改代码关系
#4。获取下一页
    def parse_item(self, response):
        items=[]

        # url=response.url
        companys = response.css('div.companyInformation')
        for c in companys:
            i = GreenBookItem()
            i['name'] = c.css('a[itemprop="CompanyName"]::text').extract_first().strip()
            items.append(i)
        # i['address']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[4]
        # i['tel']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[3]
        # i['mail']=u''.join(response.xpath('//div[@id="articleContent"]/descendant::text()').extract())
        # i['website']=''
        self.logger.info('I am here!!!!!!!!!!!!!!')
        yield items

        #TODO:
        #怎么获取下一页呢？？
        
    def parse(self,response):
        #hxs = HtmlXPathSelector(response)

        #items = []
        urls = response.xpath('//@href').re(r'.*/products/search/.*')
        # pdb.set_trace()
        for url in urls:
            self.logger.info('search:'+url)
            yield Request(url,callback=self.parse2,dont_filter=True)#headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
        
    def parse2(self, response):
        #hxs = HtmlXPathSelector(response)

        #items = []
        #import pdb
        urls = response.xpath('//@href').re(r'^/products/.*')
        # pdb.set_trace()
        for url in urls:
            self.logger.info('joinurl:'+url)
            yield Request('http://www.thegreenbook.com'+url,callback=self.parse_item,dont_filter=True)#,headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
