# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
	link = scrapy.Field()
	name = scrapy.Field()

class SensorReading(scrapy.Item):
	source = scrapy.Field() #Source of reading (e.g scottishairquality.co.uk)
	sourceID = scrapy.Field() #Id assigned as in source
	pm10 = scrapy.Field() #Particulate Matter
	no2 = scrapy.Field() #Nitrogen Dioxide
	no = scrapy.Field() #Nitric oxide
	nox = scrapy.Field() #Nitrogen oxides
	coordinates = scrapy.Field() #Lat, Long
	lastUpdated = scrapy.Field() 

