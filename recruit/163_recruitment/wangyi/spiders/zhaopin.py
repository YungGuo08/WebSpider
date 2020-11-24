import scrapy
import json
import time


from wangyi.items import WangyiItem


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/api/hr163/position/queryPage']

    def __init__(self):

        self.headers = {
            'content-type': 'application/json',
            'origin': 'https://hr.163.com',
            'referer': 'https://hr.163.com/job-list.html',
        }

        self.data = {
            'currentPage': '1',
            'pageSize': '4100'
        }

    def start_requests(self):
        url = 'https://hr.163.com/api/hr163/position/queryPage'
        yield scrapy.Request(url, method='POST', headers=self.headers, body=json.dumps(self.data), callback=self.parse)

    def parse(self, response):
        data_json = json.loads(response.text)
        data_list = data_json['data']['list']
        for data in data_list:
            item = WangyiItem()
            item['position'] = data['name']
            item['department'] = data['firstDepName']
            item['position_type'] = data['firstPostTypeName']
            item['recruit_number'] = data['recruitNum']
            item['education'] = data['reqEducationName']
            item['working_years'] = data['reqWorkYearsName']
            item['workplace'] = data['workPlaceNameList'][0]
            item['job_description'] = data['description']
            item['job_requirements'] = data['requirement']
            # 全职0，实习1，派遣2
            if data['workType'] == '0':
                item['operation_mode'] = '全职'
            elif data['workType'] == '1':
                item['operation_mode'] = '实习'
            elif data['workType'] == '2':
                item['operation_mode'] = '派遣'
            time_ = time.localtime(data['updateTime'] / 1000)
            item['release_time'] = time.strftime('%Y-%m-%d', time_)
            yield item
