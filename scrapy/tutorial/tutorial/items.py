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

	pm_10 = scrapy.Field() #Particulate Matter (10 micrometer)
	no = scrapy.Field() #Nitric oxide
	no_x = scrapy.Field() #Nitrogen oxides
	no_2 = scrapy.Field() #Nitrogen Dioxide
	pm_1 = scrapy.Field() #Particulate Matter (1 micrometer)
	pm_2p5 = scrapy.Field()  # Particulate Matter (2.5 micrometer)
	v_pm_2p5 = scrapy.Field()  # Volatile Particulate Matter (2.5 micrometer)
	nv_pm_2p5 = scrapy.Field()  # Volatile Particulate Matter (2.5 micrometer)
	v_pm_10 = scrapy.Field()  # Volatile Particulate Matter (10 micrometer)
	so_2 = scrapy.Field()  # Volatile Particulate Matter (10 micrometer)
	co = scrapy.Field()  # Carbon monoxide


	coordinates = scrapy.Field() #Lat, Long
	lastUpdated = scrapy.Field()
	_id = scrapy.Field()

