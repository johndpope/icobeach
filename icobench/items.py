# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IcoItem(scrapy.Item):
    # 国家
    Country = scrapy.Field()
    # ico
    # 代币符号
    Token = scrapy.Field()
    # 开始时间
    # 软顶
    Soft_cap = scrapy.Field()
    # 硬顶
    Hard_cap = scrapy.Field()
    # 平台
    Platform = scrapy.Field()
    # 接受币种
    Accepting = scrapy.Field()
    # 投资限制
    Minimum_investment = scrapy.Field()
    # 预售开始时间
    preICO_start = scrapy.Field()
    # 预售结束时间
    preICO_end = scrapy.Field()
    # 预售价格
    PreICO_Price = scrapy.Field()
    Price_in_preICO = scrapy.Field()
    # 公募开始时间
    ICO_start = scrapy.Field()
    # 公募结束时间
    ICO_end = scrapy.Field()
    # 公募价格
    Price = scrapy.Field()
    Price_in_ICO = scrapy.Field()

    Restricted_areas = scrapy.Field()

    Bonus = scrapy.Field()

    Bounty = scrapy.Field()


    pass


class financialItem(scrapy.Item):
    # ico
    # 代币符号
    Token = scrapy.Field()
    # 开始时间
    start_date = scrapy.Field()
    # 结束时间
    end_date = scrapy.Field()
    # 软顶
    Soft_cap = scrapy.Field()
    # 硬顶
    Hard_cap = scrapy.Field()
    # 初始价格
    initial_price = scrapy.Field()
    # 代币总量
    token_supply = scrapy.Field()
    # 平台
    Platform = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 接受币种
    Accepting = scrapy.Field()
    # 流通百分比
    circulating_supply = scrapy.Field()
    # 投资限制
    Minimum_investment = scrapy.Field()
    # 是否kyc
    kyc = scrapy.Field()
    # 预售开始时间
    preICO_start = scrapy.Field()
    # 预售结束时间
    preICO_end = scrapy.Field()
    # 预售价格
    PreICO_Price = scrapy.Field()
    Price_in_preICO = scrapy.Field()
    # 公募开始时间
    ICO_start = scrapy.Field()
    # 公募结束时间
    ICO_end = scrapy.Field()
    # 公募价格
    Price = scrapy.Field()
    Price_in_ICO = scrapy.Field()

    Restricted_areas = scrapy.Field()

    Bonus = scrapy.Field()

    Bounty = scrapy.Field()

    pass


class IcobenchItem(scrapy.Item):
    # 项目名
    project_name = scrapy.Field()
    # 宣传语
    project_slogan = scrapy.Field()
    # 简介
    detail_excerpt = scrapy.Field()
    # 行业标签
    industry = scrapy.Field()
    # 视频
    video = scrapy.Field()
    # 白皮书
    white_paper = scrapy.Field()
    # 详细介绍
    detail_desc = scrapy.Field()
    # 官网
    homepage = scrapy.Field()
    # 图标
    logo= scrapy.Field()





    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
