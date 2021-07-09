import scrapy

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001/']
    start_urls=['http://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001/']

    def parse(self,response):
        #define the fields for your item here like:
        #name = scrapy.Fielde()
        #title,preview,writer
        pass