import scrapy

class AirQualitySpider(scrapy.Spider):
    name = "airquality"
    #allowed_domains = ["scottishairquality.co.uk"]
    allowed_domains = ["dmoz.org"]

    start_urls = [
	#"http://www.scottishairquality.co.uk/latest/summary"
	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
	]

#def parse(self, response):
#	for sel in response.xpath('//tr/td[1]'):
#		name = sel.xpath('/a/text()').extract()
#		link = sel.xpath('/a/@href').extract()
#		print name


def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
