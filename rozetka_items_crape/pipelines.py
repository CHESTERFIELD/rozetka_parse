# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class RozetkaItemsCrapePipeline(object):

    def open_spider(self, spider):
        hostname = '127.0.0.1'
        username = 'diplom_user'
        password = 'diplom_password'
        database = 'items_db'
        port = 5432
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if item['name'] != "" and item['link'] != "#":
            self.cur.execute("insert into items_content(name,link) values(%s,%s)",
                             (item['name'], item['link']))
            self.connection.commit()
        return item
