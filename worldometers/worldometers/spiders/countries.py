# -*- coding: utf-8 -*-
import scrapy
import logging
#from scrapy.shell import inspect_response
#from scrapy.utils.response import open_in_browser
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")

        for country in countries:
        	# when executiong an xpath expression against a selector you start with .//
        	name = country.xpath(".//text()").get()
        	link = country.xpath(".//@href").get()


        	# absolute_url = f"https://www.worldometers.info{link}"
        	#absolute_url = response.urljoin(link)


        	#yield scrapy.Request(url=absolute_url)

        	yield response.follow(url=link, callback=self.parse_country, meta={'country_name' : name})


    import pdb; pdb.set_trace()  # breakpoint f697c0ee //
    def parse_country(self, response):
        logging.info(response.status)
        logging.warning(response.status)
        #open_in_browser(response) # Warning! opens all the links crawled in browser WARNING!
        #inspect_response(response, self)
    	# name = response.request.meta['country_name']
    	# #logging.info(response.url)
    	# rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

    	# for row in rows:
    	# 	year = row.xpath(".//td[1]/text()").get()
    	# 	population = row.xpath(".//td[2]/strong/text()").get()

    	# 	yield {
    	# 		'name' : name,
    	# 		'year' : year,
    	# 		'population' : population
    	# 	}




