from turtle import ScrolledCanvas
import requests
import pandas as pd
import json
import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urljoin

class BookingSpider(scrapy.Spider):
    # Name of my spider
    name = "Booking"
    allowed_domains = ["booking.com"]

    def start_requests(self):
        yield scrapy.Request('https://www.booking.com', callback=self.form_input)
        
    def form_input(self, response):
        
        villes = ["Mont Saint Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes les Mimosas","Cassis","Marseille", "Aix en Provence","Avignon","Uzes","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
        for ville in villes:
            yield scrapy.FormRequest.from_response(response, formdata={'ss': ville}, callback=self.after_search, meta={'city':ville})

        
    def after_search(self, response):

        hotels = response.css('div.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')  
        ville = response.request.meta["city"]
        for hotel in hotels:

                #name= hotel.xpath('div[1]/div[2]/div/div/div[1]/div/div[1]/div/h3/a/div[1]/text()').get()
                #link=hotel.xpath('div[1]/div[2]/div/div/div[1]/div/div[1]/div/h3/a').attrib["href"]
                name=hotel.css('div.fcab3ed991.a23c043802::text').get()
                link=hotel.css('a.e13098a59f::attr(href)').get()
                score=hotel.css('div.b5cd09854e.d10a6220b4::text').get()
                #score=hotel.xpath('div[1]/div[2]/div/div/div[2]/div[1]/a/span/div/div[1]/text()').get()
                description=hotel.css('div.d8eab2cf7f::text').get()

                dico= {
                'name': name,
                'url': link,
                'score': score,
                'description': description,
                'city':ville
            }
                yield response.follow(url=link, callback=self.parse_hotel, meta={"dico":dico})

    def parse_hotel(self, response):

            all_data = response.request.meta["dico"]
            gps= response.css('a.jq_tooltip.loc_block_link_underline_fix.bui-link.show_on_map_hp_link.show_map_hp_link').attrib['data-atlas-latlng']

            all_data["gps"] = gps
        
            yield all_data



# Name of the file where the results will be saved
filename = "ScrapBooking.json"

# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)
if filename in os.listdir():
    os.remove(filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
'USER_AGENT': 'Chrome/97.0',
'LOG_LEVEL': logging.INFO,
"FEEDS": {
    filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(BookingSpider)
process.start()
