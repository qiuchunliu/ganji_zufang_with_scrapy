# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class GanjiZufangItem(scrapy.Item):
class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_name = scrapy.Field()  # 房源名字
    house_price = scrapy.Field()  # 价格
    house_model = scrapy.Field()  # 户型
    house_area = scrapy.Field()  # 面积
    house_toward = scrapy.Field()  # 朝向
    house_floor = scrapy.Field()  # 楼层
    house_decoration = scrapy.Field()  # 装修情况
    house_address = scrapy.Field()  # 小区名称和地址
    house_contact_tel = scrapy.Field()  # 联系人电话

