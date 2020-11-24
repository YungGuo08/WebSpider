# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentRecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名
    position_name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 事业群
    business_group = scrapy.Field()
    # 招聘类型
    recruitment_type = scrapy.Field()
    # 产品名称
    product_name = scrapy.Field()
    # 工作职责
    responsibility = scrapy.Field()
    # 工作要求
    requirement = scrapy.Field()
    # 发布时间
    release_time = scrapy.Field()
