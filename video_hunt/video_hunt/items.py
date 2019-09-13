# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class VideoHuntItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class VideoTitleItem(scrapy.Item):
    title = scrapy.Field()          # 视频的标题
    url = scrapy.Field()            # 视频的网页链接
    label = scrapy.Field()          # 视频的标签
    create_time = scrapy.Field()    # 发表时间
    update_time = scrapy.Field()    # 发表时间
    info = scrapy.Field()           # 视频的描述

class VideoItem(scrapy.Item):
    title = scrapy.Field()          # 该集视频的标题
    url = scrapy.Field()            # 视频的网页链接
    create_time = scrapy.Field()    # 发表时间
    update_time = scrapy.Field()    # 发表时间
    info = scrapy.Field()           # 视频的描述
    source_id = scrapy.Field()      # 视频的主名称id


