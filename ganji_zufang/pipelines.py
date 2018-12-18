# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class GanjiZufangPipeline(object):
    house_count = 0

    def __init__(self):
        self.f = open('ganji_zufang.csv', 'a+', newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(('房源名称', '价格', '户型', '面积', '朝向', '楼层', '装修', '地址', '联系方式'))

    def process_item(self, item, spider):
        self.house_count += 1
        print('正在写入 %04d 个房屋信息。。。' % self.house_count)

        self.writer.writerow((item['house_name'], item['house_price'], item['house_model'],
                              item['house_area'], item['house_toward'], item['house_floor'],
                              item['house_decoration'], item['house_address'], item['house_contact_tel'])
                             )
        print('写入完成')

        return item

    def file_close(self):
        self.f.close()
