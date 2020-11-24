# -*- coding: utf-8 -*-

import scrapy
import json

from tencent_recruitment.items import TencentRecruitmentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=6100']

    def parse(self, response):
        data_list = json.loads(response.text)['Data']['Posts']
        for data in data_list:
            item = TencentRecruitmentItem()
            try:
                # 职位名
                item['position_name'] = data['RecruitPostName'].split('-')[1]
            except:
                item['position_name'] = data['RecruitPostName']
            # 国家
            item['country'] = data['CountryName']
            # 城市
            item['city'] = data['LocationName']
            # 职位类别
            item['category'] = data['CategoryName']
            # 事业群
            if data['BGName'] == 'CDG':
                item['business_group'] = '企业发展事业群'
            elif data['BGName'] == 'CSIG':
                item['business_group'] = '云与智慧产业事业群'
            elif data['BGName'] == 'IEG':
                item['business_group'] = '互动娱乐事业群'
            elif data['BGName'] == 'PCG':
                item['business_group'] = '平台与内容事业群'
            elif data['BGName'] == 'WXG':
                item['business_group'] = '微信事业群'
            elif data['BGName'] == 'TEG':
                item['business_group'] = '技术工程事业群'
            elif data['BGName'] == 'S1':
                item['business_group'] = '职能系统－职能线'
            elif data['BGName'] == 'S2':
                item['business_group'] = '职能系统－财经线'
            elif data['BGName'] == 'S3':
                item['business_group'] = '职能系统－HR与管理线'
            elif data['BGName'] == 'TME':
                item['business_group'] = '腾讯音乐'
            else:
                item['business_group'] = ''
            # 招聘类型
            if data['SourceID'] == 0:
                item['recruitment_type'] = '校招实习生'
            elif data['SourceID'] == 1:
                item['recruitment_type'] = '社招'
            elif data['SourceID'] == 2:
                item['recruitment_type'] = '校招应届生'
            else:
                item['recruitment_type'] = ''
            # 工作职责
            item['responsibility'] = data['Responsibility']
            # 发布时间
            item['release_time'] = data['LastUpdateTime']
            pot_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId=' + data['PostId']
            yield scrapy.Request(url=pot_url, callback=self.parse_details, meta={'item': item})

    def parse_details(self, response):
        item = response.meta['item']
        data = json.loads(response.text)['Data']
        item['product_name'] = data['ProductName']
        item['requirement'] = data['Requirement']
        yield item
