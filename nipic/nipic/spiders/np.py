# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request

from nipic.items import NipicItem


class NpSpider(scrapy.Spider):
    name = "np"
    allowed_domains = ["nipic.com"]
    start_urls = ['http://www.nipic.com/']

    def parse(self, response):
        #获取所有的一级导航菜单的url
        navUrls = response.xpath("//div[@class='fl nav-item-wrap']/a/@href").extract()
        #print(navUrls)
        newNavUrls = navUrls[1:4]  # ['/design/index.html', '/photo/index.html', '/media/index.html']
        #print(newNavUrls)
        for i in newNavUrls:
            # 获取完整的url ---> http://www.nipic.com/design/index.html
            navUrl = response.urljoin(i)
            #print(navUrl)
            # 交由下一个回调函数处理
            yield Request(url=navUrl, callback=self.secondNavCallback)

    # 处理二级导航菜单
    def secondNavCallback(self, response):
        # 得到所有二级菜单的url
        secondNavUrls = response.xpath("//div[@class='menu-box-bd']/dl/dt/div/a/@href").extract()
        #print(secondNavUrls)
        for i in secondNavUrls:
            secondNavUrl = response.urljoin(i)
            yield Request(url=secondNavUrl, callback=self.imagePageCallback)

    # 处理点击二级菜单后的图片列表页
    def imagePageCallback(self, response):
        # 得到所有的分页页码
        pages = response.xpath("//div[@class='common-page-box mt10 align-center']/a/em/text()").extract()
        #print(pages)
        # 获取分页链接  /design/acg/index.html?page=2
        pageUrls = response.xpath("//div[@class='common-page-box mt10 align-center']/a/@href").extract()
        #print(pageUrls)
        pageUrl = pageUrls[0:1]
        #print(pageUrl)
        # 得到完整链接
        pageUrlBase = response.urljoin(pageUrl[0])
        #print(pageUrlBase)
        # 截取公共部分
        commonPageUrl = pageUrlBase[0:-1]
        # 得到最大的页码
        maxPage = pages[-1]
        for i in range(2,int(maxPage)+1):
            # 拼接分页链接
            url = commonPageUrl + str(i)
            #print(url)
            yield Request(url=url, callback=self.imageListCallback)

    # 处理每一页的每一张图片
    def imageListCallback(self, response):
        # 获取图片的url
        imageUrls = response.xpath("//div[@class='search-result overflow-hidden']/ul/li/a/@href").extract()
        #print(len(imageUrls))
        for url in imageUrls:
            imageUrl = url
            #print(imageUrl)
            yield Request(url= imageUrl, callback=self.imageDetailCallback)

    # 正式得到图片
    def imageDetailCallback(self, response):
        # 创建 NipicItem 对象
        nipicItem = NipicItem()
        # 得到图片
        image = response.xpath("//div[@id='static']/img/@src").extract()
        #print(image)
        nipicItem["url"] = image
        yield nipicItem

