# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
    	countries = response.xpath("//table/tbody/tr")

    	for country in countries:
    		country_name = country.xpath(".//td[1]/a/text()").get()
    		gdp_debt = country.xpath(".//td[2]/text()").get()
    		

    		yield {
    			"country_name" : country_name,
    			"gdp_debt" : gdp_debt
    		}
        
