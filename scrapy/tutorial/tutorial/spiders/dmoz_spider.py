import scrapy
import urlparse

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["scottishairquality.co.uk"]
	start_urls = ["http://www.scottishairquality.co.uk/latest/summary"]

	def parse(self, response):
        	#filename = response.url.split("/")[-2] + '.html'
		#with open(filename, 'wb') as f:
		#f.write(response.body)
		for sel in response.xpath('//tr/td[1]/a'):
			item = DmozItem()
			#print sel.extract()
			name = sel.xpath('text()').extract()
			link = sel.xpath('@href').extract()

			#urlparse.urljoin(link, link)
			
			#join = response.urljoin(link)

			#print join		

			concat = "http://www.scottishairquality.co.uk/latest/" + link[0]
				
			print  name[0], link[0]
			print concat
			item['link'] = link
			item['name'] = name
			#yield item
			#yield scrapy.Request(url, callback=self.parse_station_data)


	def parse_station_data(self, response):
		for sel in reponse.xpath('//tr'):
			print sel




