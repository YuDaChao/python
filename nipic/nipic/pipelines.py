# -*- coding: utf-8 -*-

import urllib.request

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NipicPipeline(object):
    def process_item(self, item, spider):
        #print(item["url"])
        # 获取图片的路径和名称
        url = item["url"][0]
        fileName = "F:/python/" + url[-26:]
        print("正在爬取图片 : ", url , " ----> ", fileName)
        urllib.request.urlretrieve(url, filename=fileName)
        return item
