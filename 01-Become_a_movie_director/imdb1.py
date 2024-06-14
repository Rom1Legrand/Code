import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

class imdb_spider(scrapy.Spider):
    # Name of your spider
    name = "imdb"

    # Url to start your spider from 
    start_urls = [
        'https://www.imdb.com/chart/boxoffice',
    ]

    # Callback function that will be called when starting your spider
    # It will ranking, the title, the url, the total earnings, the rating and the number of voters of the first <div> with class="quote"

    def parse(self, response):
        elements = response.css("div.sc-b189961a-0.hBZnfJ.cli-children")
        for element in elements:
            yield {
                "ranking" : element.css('h3.ipc-title__text::text').get().split(".")[0]
                ,
                "title" : element.css("h3.ipc-title__text::text").get().split(".")[1].strip()
                ,
                "url" : element.css('a.ipc-title-link-wrapper').attrib["href"]
                ,
                "total_earning" : element.css('span.sc-8f57e62c-2.elpuzG::text').get()
                ,
                "rating" : element.css('span.ipc-rating-star.ipc-rating-star--base.ipc-rating-star--imdb.ratingGroup--imdb-rating::text').get()
                ,
                "voters" : element.css('span.ipc-rating-star--voteCount::text').getall()[1]
            }
        
        #return {"title": title, "rating": rating,"voters": voters,"total_earning":total_earning, "ranking": ranking, "url": url}

    
# Name of the file where the results will be saved
filename = "imdb1.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('01-Become_a_movie_director/'):
        os.remove('01-Become_a_movie_director/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        '01-Become_a_movie_director/' + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(imdb_spider)
process.start()