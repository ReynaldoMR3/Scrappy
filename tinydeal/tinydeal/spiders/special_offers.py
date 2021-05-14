# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']

    def start_requests(self):
    	yield scrapy.Request(url='https://web.archive.org/web/20190225123327/https://tinydeal.com/specials.html', callback=self.parse, headers={
    			'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    		})

    def parse(self, response):
    	products = response.xpath("//ul[@class='productlisting-ul']/div/li")

    	for product in products:
    		title = product.xpath(".//a[@class='p_box_title']/text()").get()
    		url = response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get())
    		discounted_price = product.xpath(".//div[@class='p_box_price']/span[1]/text()").get()
    		original_price = product.xpath(".//div[@class='p_box_price']/span[2]/text()").get()

    		yield {
    			"title" : title,
    			"url" : url,
    			"discounted_price" : discounted_price,
    			"original_price" : original_price,
    			"User-Agent" : response.request.headers['User-Agent']
    		}

    	next_page = response.xpath("//a[@class='nextPage']/@href").get()

    	if next_page:

    		yield scrapy.Request(url=next_page, callback=self.parse, headers={
    			'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    		})