# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")

        for product in products:
        	url = response.urljoin(product.xpath(".//descendant::div[@class='p-title']/a[1]/@href").get())
        	img_url = product.xpath(".//descendant::img[1]/@data-src").get()
        	name = product.xpath(".//descendant::div[@class='p-title']/a[1]/@title").get()
        	price = product.xpath(".//descendant::div[@class='p-price']/div[1]/span/text()").get()

        	yield {
        		'url' : url,
        		'img_url': img_url,
        		'name' : name,
        		'price' : price
        	}

        next_page = response.xpath("//ul[@class='pagination']/li[position()=last()]/a/@href").get()

        if next_page:
        	yield scrapy.Request(url=next_page, callback=self.parse)