# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
sys.path.append('../')
from utils.mysql import DbManager
from .items import *


class VideoHuntPipeline(object):
    def process_item(self, item, spider):
        # db = DbManager()
        # sql = "insert into source_detail(title,url) values(%s,%s);"
        # values = [item['title'], item['url']]
        # result = db.queryStr(sql, values)
        # db = DbManager()
        # sql = "insert into source(title,url) values(%s,%s);"
        # values = [item['title'], item['url']]
        # result = db.queryStr(sql, values)

        # 保存item到数据库
        # 总视频的标题
        if isinstance(item, VideoTitleItem):
            print("save VideoTitleItem")
            db = DbManager()
            sql = "insert into source(title,url) values(%s,%s);"
            values = [item['title'], item['url']]
            result = db.queryStr(sql, values)

            sql = "select id from source where title = %d and url = %d;"
            id = db.fetchone(sql, values)
        # 该视频某一集
        elif isinstance(item, VideoItem):
            print("save VideoItem")
            db = DbManager()
            sql = "insert into source_detail(title, url,source_id) values(%s,%s,%s);"
            values = [item['title'], item['url'], item['source_id']]
            result = db.queryStr(sql, values)

        # item_string = str(item)
        # file = open("items.txt", "w", encoding="utf-8")  # 以追加的方式打开文件，不存在则创建
        # # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，
        # # 将其编码改为utf-8
        # file.write(item_string)
        # file.write('\n')
        # file.close()
        # print(item_string)  # 在控制台输出

        return item  # 会在控制台输出原item数据，可以选择不写

