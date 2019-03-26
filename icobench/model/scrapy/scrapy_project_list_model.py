from icobench.model.scrapy.base_scrapy_model import BaseScrapyModel
from peewee import *
import datetime

"""
ScrapyProjectListModel项目model层   
"""


class ScrapyProjectListModel(BaseScrapyModel):
    # CharField：字符串类型
    name = CharField(unique=True, null=True)  # 名称
    page_href = CharField(null=True)  # 项目子页面连接
    logo = TextField(null=True)  # logo
    detail_desc = TextField(null=True)  # 项目介绍
    kyc = IntegerField(default=0, null=True)  # 是否kyc ；0：否；1：是
    white_list = IntegerField(default=0, null=True)  # 是否白名单 ；0：否；1：是
    limit_countries = CharField(null=True)  # 限制的国家
    start_time = CharField(null=True)
    end_time = CharField(null=True)
    score = CharField(null=True)
    create_date = DateTimeField(default=datetime.datetime.now)
    update_date = DateTimeField(default=datetime.datetime.now)

    """
    计算总数量
    By Ada
    2019-01-29
    """

    def get_count(self):
        return ScrapyProjectListModel.select().count()

    """
    根据id获取信息
    By Ada
    2019-01-29
    """

    def get_by_id(self, id):
        for Model in ScrapyProjectListModel.select().where(ScrapyProjectListModel.id == id):
            return Model
        return None

    """
    获取所有信息
    By
    Ada
    2019 - 03 - 14
    """
    def get_list(self):
        return ScrapyProjectListModel.select()
        # .offset(20).limit(40)
        # for Model in ScrapyProjectListModel.select().limit(2):
        #     return Model
        # return None


    """
    跟新和新建
    By Ada
    2019-01-29
    """

    def update_model(self, model):
        if model is not None:
            ScrapyProjectListModel.replace(name=model.name,
                                           page_href=model.page_href,
                                           logo=model.logo,
                                           detail_desc=model.detail_desc,
                                           kyc=model.kyc,
                                           white_list=model.white_list,
                                           limit_countries=model.limit_countries,
                                           start_time=model.start_time,
                                           end_time=model.end_time,
                                           score=model.score
                                           ) \
                .on_conflict(
                # 更新
                update={
                    ScrapyProjectListModel.page_href: model.page_href,
                    ScrapyProjectListModel.logo: model.logo,
                    ScrapyProjectListModel.detail_desc: model.detail_desc,
                    ScrapyProjectListModel.kyc: model.kyc,
                    ScrapyProjectListModel.white_list: model.white_list,
                    ScrapyProjectListModel.limit_countries: model.limit_countries,
                    ScrapyProjectListModel.start_time: model.start_time,
                    ScrapyProjectListModel.end_time: model.end_time,
                    ScrapyProjectListModel.score: model.score
                }) \
                .execute()
        return model

    class Meta:
        table_name = "t_project_list_info"  # 表名
