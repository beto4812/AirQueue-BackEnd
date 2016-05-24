import scrapy
import urlparse

from tutorial.items import SensorReading

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["scottishairquality.co.uk"]
	start_urls = ["http://www.scottishairquality.co.uk/latest/summary"]

	def parse(self, response):
		for sel in response.xpath('//tr/td[1]/a'):
			#item = DmozItem()
			name = sel.xpath('text()').extract()
			link = sel.xpath('@href').extract()

			concat = "http://www.scottishairquality.co.uk/latest/" + link[0]
				
			print  name[0], link[0]
			print concat
			#item['link'] = link
			#item['name'] = name
			#yield item
			yield scrapy.Request(concat, callback=self.parse_station_data)


	def parse_station_data(self, response):
		for sel in response.xpath('//tbody'):
			reading = SensorReading()
			print sel
			source = "scottishairquality.co.uk" #Static for this spider
			sourceID = sel.xpath('//div[@class="media margin-bottom"]/p[1]/b').extract()
			coordinates = sel.xpath('//div[@class="media margin-bottom"]/a/@href').extract()
			lastUpdated = sel.xpath('//div[@class="media margin-bottom"]/p[3]').extract()
			pm10 = sel.xpath('tr[1]/td[3]/text()').extract()
			no2 = sel.xpath('tr[2]/td[3]/text()').extract()
			no = sel.xpath('tr[3]/td[3]/text()').extract()
			nox = sel.xpath('tr[4]/td[3]/text()').extract()
			
			reading['source'] = source
			reading['sourceID'] = sourceID
			reading['pm10'] = pm10
			reading['no2'] = no2
			reading['no'] = no
			reading['nox'] = nox
			reading['coordinates'] = coordinates
			reading['lastUpdated'] = lastUpdated
		
			yield reading	
