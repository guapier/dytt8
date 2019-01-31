# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dytt8Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 电影名
    category = scrapy.Field()  # 类别
    country = scrapy.Field()  # 产地
    douban_rate = scrapy.Field()  # 豆瓣评分
    language = scrapy.Field()  # 语言
    publish_date = scrapy.Field()  # 上映日期
    IMDb_rate = scrapy.Field()  # IMDB评分
    movie_time = scrapy.Field()  # 片长
    director = scrapy.Field()  # 导演
    main_actor = scrapy.Field()  # 主演
    introduce = scrapy.Field()  # 简介
    download_url = scrapy.Field()  # 下载地址
