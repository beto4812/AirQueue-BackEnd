import scrapy
import urlparse

from scrapy.crawler import CrawlerProcess
from items import SensorReading


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["scottishairquality.co.uk"]
    start_urls = ["http://www.scottishairquality.co.uk/latest/summary"]

    def parse(self, response):
        for sel in response.xpath('//tr/td[1]/a'):
            # item = DmozItem()
            name = sel.xpath('text()').extract()
            link = sel.xpath('@href').extract()

            concat = "http://www.scottishairquality.co.uk/latest/" + link[0]

            # print  name[0], link[0]
            print "-VISITING: " + concat
            # item['link'] = link
            # item['name'] = name
            # yield item
            yield scrapy.Request(concat, callback=self.parse_station_data)

    def process_row(self, row, reading):
        pollutant = row.xpath('td[1]').extract()



        key = {
            '<td>PM<sub>10</sub> particulate matter (Hourly measured)</td>': 'pm_10',
            '<td>Nitric oxide (NO)</td>': 'no',
            '<td>Nitrogen oxides as nitrogen dioxide (NOXasNO<sub>2</sub>)</td>': 'no_x',
            '<td>Nitrogen dioxide (NO<sub>2</sub>)</td>': 'no_2',
            '<td>PM1 particulate matter (Hourly measured)</td>': 'pm_1',
            '<td>PM<sub>2.5</sub> particulate matter (Hourly measured)</td>': 'pm_2p5',
            '<td>Volatile PM<sub>2.5</sub> (Hourly measured)</td>': 'v_pm_2p5',
            '<td>Non-volatile PM<sub>2.5</sub> (Hourly measured)</td>': 'nv_pm_2p5',
            '<td>Volatile PM<sub>10</sub> (Hourly measured)</td>': 'v_pm_10',
            '<td>Sulphur dioxide (SO<sub>2</sub>)</td>': 'so_2',
            '<td>Carbon monoxide</td>': 'co',
            '<td>Ozone (O<sub>3</sub>)</td>': 'o3'
        }.get(pollutant[0])

        val = row.xpath('td[3]/text()').extract()
        if key:
            if val[0] != "No data ":
                reading[key] = val

    def parse_station_data(self, response):
        for sel in response.xpath('//tbody'):
            # reading = SensorReading()
            print "-SEL "
            print sel

            reading = SensorReading()

            reading['source'] = "scottishairquality.co.uk"  # Static for this spider
            reading['sourceID'] = sel.xpath('//div[@class="media margin-bottom"]/p[1]/b').extract()
            if sel.xpath('//div[@class="media margin-bottom"]/p[2]/span').extract() != "":
                reading['air_quality_index'] = sel.xpath('//div[@class="media margin-bottom"]/p[2]/span').extract()
            reading['coordinates'] = sel.xpath('//div[@class="media margin-bottom"]/a/@href').extract()
            reading['lastUpdated'] = sel.xpath('//div[@class="media margin-bottom"]/p[3]').extract()
            reading['site_map'] = sel.xpath('//div[@class="media margin-bottom"]/a/img/ @src').extract()

            rows = sel.xpath('tr')
            for row in rows:
                print row
                self.process_row(row, reading)

            yield reading
            #if(no and no[0] != 'No data '): reading['no'] = no
            #if(source and source[0] != 'No data '): reading['source'] = source
            #if(sourceID and sourceID[0] != 'No data '): reading['sourceID'] = sourceID[0].split(':')[1][1:-4]
            #if(pm10 and pm10[0] != 'No data ' and pm10[1]): reading['pm10'] = pm10
            #if(no2 and no2[0] != 'No data '): reading['no2'] = no2
            #if(nox and nox[0] != 'No data '): reading['nox'] = nox
            #if(coordinates and coordinates[0] != 'No data '): reading['coordinates'] = coordinates
            #if(lastUpdated and lastUpdated[0] != 'No data '): reading['lastUpdated'] = [lastUpdated[0].split(': ')[0], lastUpdated[0].split(': ')[1].split(' ')[1][:-4]]

            # yield reading

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES': {'pipelines.SensorReadingPipeline': 100}
})

process.crawl(DmozSpider)
process.start() # the script will block here until the crawling is finished