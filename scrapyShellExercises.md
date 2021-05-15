### scrapy shell exercises

Init
```
scrapy shell
```

Fetch URL and update local objects
```
 fetch("https://www.worldometers.info/world-population/population-by-country/")
```


```
2021-05-11 22:02:49 [scrapy.core.engine] INFO: Spider opened
2021-05-11 22:02:50 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.worldometers.info/robots.txt> (referer: None)
2021-05-11 22:02:50 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.worldometers.info/world-population/population-by-country/> (referer: None)
```


Fetch URL with request

    r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")

    fetch(r)

    2021-05-11 22:04:33 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.worldometers.info/world-population/population-by-country/> (referer: None)



Get HTML

    In [4]: response.body
    Out[4]: b'\n<!DOCTYPE html><!--[if IE 8]> <html lang="en" class="ie8"> <![endif]--><!--[if IE 9]> <html lang="en" class="ie9"> <![endif]--><!--[if !IE]><!--> <html lang="en"> <!--<![endif]--> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Population by Country (2021) - Worldometer</title><meta name="description" content="List of countries and dependencies in the world ranked by population, from the most populated. Growth rate, median age, fertility rate, area, density, population density, urbanization, urban population, share of world population."><link rel="shortcut icon" href="/favicon/favicon.ico"


Getting the title with tags

    title = response.xpath("//h1")

    In [4]: title
    Out[4]: [<Selector xpath='//h1' data='<h1>Countries in the world by populat...'>]


Getting the text in the title

    In [5]: title = response.xpath("//h1/text()")

    In [6]: title
    Out[6]: [<Selector xpath='//h1/text()' data='Countries in the world by population ...'>]
    In [7]: title.get()
    Out[7]: 'Countries in the world by population (2021)'


Getting the title with css

    In [9]: title_css = response.css("h1::text")

    In [10]: title_css
    Out[10]: [<Selector xpath='descendant-or-self::h1/text()' data='Countries in the world by population ...'>]

*Note: the css selector is not recommended because scrapy converts the xpath selector so it cant use css, this affects the performance of the spider*

Getting all the countries

    In [13]: countries = response.xpath("//td/a/text()").getall()

    In [14]: countries
    Out[14]: 
    ['China',
     'India',
     'United States',
     'Indonesia',
     'Pakistan',
     'Brazil',
     'Nigeria',
     'Bangladesh',
     ...
    ]

## Steps for creating projects and spiders

Start project:

    scrappy startproject <project_name>

Generate spider

    scrappy genspider <name> <url>

Generate spider with crawler template

    scrappy genspider -t crawl <name> <url>


