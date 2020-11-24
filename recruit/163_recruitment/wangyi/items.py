# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位
    position = scrapy.Field()
    # 所属部门
    department = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    recruit_number = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 工作年限
    working_years = scrapy.Field()
    # 工作地点
    workplace = scrapy.Field()
    # 职位描述
    job_description = scrapy.Field()
    # 职位要求
    job_requirements = scrapy.Field()
    # 兼职/全职
    operation_mode = scrapy.Field()
    # 发布时间
    release_time = scrapy.Field()
