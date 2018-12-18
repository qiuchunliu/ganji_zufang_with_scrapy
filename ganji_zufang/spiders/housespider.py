# -*- coding: utf-8 -*-
import scrapy
from ganji_zufang.items import HouseItem
import re
import time


class HousespiderSpider(scrapy.Spider):
    name = 'housespider'
    # allowed_domains = ['ganji.com']
    # 因为 yield 里的 url 已经包含 domains 所以如果还有这个 allowed_domains 属性在，
    # 会导致无法调用函数的现象
    # 所以后续应该注意获取到的url是不是完整的
    start_urls = ['http://sh.ganji.com/wblist/zufang/']
    count = 0

    def parse(self, response):
        divs = response.xpath('//div[@class="f-list-item ershoufang-list"]')
        print('*' * 20, len(divs))  # 查看divs 的长度
        for div in divs:
            time.sleep(0.5)
            href = div.xpath('.//a[@class="js-title value title-font"]/@href').get()
            if href[0] != 'h':
                href = 'http:' + href
            print(href)
            yield scrapy.Request(url=href, callback=self.parse_each_house)
        self.count += 1
        print('已经获取第 %02d 页。' % self.count)
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            # print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_each_house(self, response):
        item = HouseItem()
        item['house_name'] = re.sub('\s', '', response.xpath('//p[@class="card-title"]/i/text()').get())
        item['house_price'] = re.sub('\s', '', ''.join(list
                                                       (map
                                                        (lambda x: x.strip(),
                                                         response.xpath('//div[@class="price-wrap"]//text()').getall()
                                                         )
                                                        )
                                                       )
                                     )
        # item['house_price'] = response.xpath('//div[@class="price-wrap"]//text()').getall()
        lis = response.xpath('//ul[@class="er-list f-clear"]//li')
        item['house_model'] = re.sub('\s', '', lis[0].xpath('./span[2]/text()').get())
        item['house_area'] = re.sub('\s', '', lis[1].xpath('./span[2]/text()').get())  # 面积
        item['house_toward'] = re.sub('\s', '', lis[2].xpath('./span[2]/text()').get())  # 朝向
        item['house_floor'] = re.sub('\s', '', lis[3].xpath('./span[2]/text()').get())  # 楼层
        item['house_decoration'] = re.sub('\s', '', lis[4].xpath('./span[2]/text()').get())  # 装修情况
        lii = response.xpath('//ul[@class="er-list-two f-clear"]//li[@class="er-item f-fl"]')
        item['house_address'] = (re.sub('\s', '', lii[0].xpath('./span[2]/a//text()').getall()[1] + ' ' +
                                 lii[1].xpath('./span[2]/text()').get().strip()))  # 小区名称和地址
        item['house_contact_tel'] = (re.sub('\s', '', response.xpath('//div[@class="user-info f-clear small-company"]'
                                                                     '//a[@class="name"]/text()').get() + ' ' +
                                     response.xpath('//a[@class="phone_num js_person_phone"]/text()').get()
                                            )
                                     )  # 联系人电
        # print(item)
        yield item
