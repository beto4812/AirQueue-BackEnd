import scrapy
import urlparse

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["scottishairquality.co.uk"]
	start_urls = ["http://www.scottishairquality.co.uk/latest/summary"]

	def parse(self, response):
		for sel in response.xpath('//tr/td[1]/a'):
			item = DmozItem()
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
			print sel
			pm10 = sel.xpath('tr[1]/td[3]/text()').extract()
			no2 = sel.xpath('tr[2]/td[3]/text()').extract()
			no = sel.xpath('tr[3]/td[3]/text()').extract()
			nox = sel.xpath('tr[4]/td[3]/text()').extract()

			print pm10, no2, no, nox


