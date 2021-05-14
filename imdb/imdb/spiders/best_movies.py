# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/top/', headers={
                'User-Agent' : self.user_agent
            })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        # For more pages ---> WARNING IT DOESN'T WORK THE IMDB PAGE HAS CHANGED
        #Rule(LinkExtractor(restrict_xpaths="//a[@class='next-page]'"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        title = response.xpath("//div[@class='title_wrapper']/h1/text()").get()
        year = response.xpath("//span[@id='titleYear']/a/text()").get()
        duration = response.xpath("normalize-space((//time)[1]/text())").get()
        genre = response.xpath("//div[@class='subtext']/a[1]/text()").get()
        rating = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        movie_url = response.url
        yield {
            "title" : title,
            "year" : year,
            "duration" : duration,
            "genre" :  genre,
            "rating" : rating,
            "movie_url" : movie_url,
            "user_agent" : response.request.headers['User-Agent']
        }