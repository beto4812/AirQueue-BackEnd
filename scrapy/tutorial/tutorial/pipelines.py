# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo
import datetime
import boto3

class SensorReadingPipeline(object):
    collection_name = 'sensor_readings'

    def process_item(self, item, spider):
        print "SensorReadingPipeline"
        if 'sourceID' in item:
            item['sourceID'] = item['sourceID'][0].split(':')[1][1:-4]
        if 'lastUpdated' in item:
            updated = item['lastUpdated'][0].split()
            item['lastUpdated'] = str(datetime.datetime.strptime(updated[3]+" "+updated[4][:-4], "%d/%m/%Y %H:%M"))
        if 'no_2' in item:
            item['no_2'] = [item['no_2'][0].split(' ')[0], item['no_2'][0].split(' ')[1]]
        if 'no' in item:
            item['no'] = [item['no'][0].split(' ')[0], item['no'][0].split(' ')[1]]
        if 'no_x' in item:
            item['no_x'] = [item['no_x'][0].split(' ')[0], item['no_x'][0].split(' ')[1]]
        if 'pm_10' in item:
            item['pm_10'] = [item['pm_10'][0].split(' ')[0], item['pm_10'][0].split(' ')[1],
                             item['pm_10'][1].strip().replace('(', '').replace(')', '')]
        if 'v_pm_10' in item:
            item['v_pm_10'] = [item['v_pm_10'][0].split(' ')[0], item['v_pm_10'][0].split(' ')[1],
                               item['v_pm_10'][1].strip().replace('(', '').replace(')', '')]
        if 'pm_2p5' in item:
            item['pm_2p5'] = [item['pm_2p5'][0].split(' ')[0], item['pm_2p5'][0].split(' ')[1],
                              item['pm_2p5'][1].strip().replace('(', '').replace(')', '')]
        if 'nv_pm_2p5' in item:
            item['nv_pm_2p5'] = [item['nv_pm_2p5'][0].split(' ')[0], item['nv_pm_2p5'][0].split(' ')[1],
                                  item['nv_pm_2p5'][1].strip().replace('(', '').replace(')', '')]
        if 'v_pm_2p5' in item:
            item['v_pm_2p5'] = [item['v_pm_2p5'][0].split(' ')[0], item['v_pm_2p5'][0].split(' ')[1],
                                  item['v_pm_2p5'][1].strip().replace('(', '').replace(')', '')]
        if 'so_2' in item:
            item['so_2'] =  [item['so_2'][0].split(' ')[0], item['so_2'][0].split(' ')[1]]

        if 'co' in item:
            item['co'] =  [item['co'][0].split(' ')[0], item['co'][0].split(' ')[1]]


        if item['coordinates']:
            coord = item['coordinates'][0].replace(',', ' ').replace('=', ' ').split()
            item['coordinates'] = [coord[1],coord[2]]
        item['date_inserted'] = str(datetime.datetime.utcnow())
        item['sourceID_lastUpdated'] = item['sourceID'] + str(item['lastUpdated'])

        self.db[self.collection_name].insert(dict(item))
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('airquality')

        table.put_item(
                Item = dict(item)
        )

        return item

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        print self.mongo_uri, self.mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
