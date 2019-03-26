from icobench.model.kntt.base_kntt_model import BaseKnttModel, qishi_db
from peewee import *
import datetime

"""
ProjectModel项目model层   
"""


class ProjectModel(BaseKnttModel):
    # CharField：字符串类型
    name = CharField(unique=True, null=True)  # 名称
    ico = IntegerField(default=0, null=True)  # 是否ICO ；0：否；1：是
    lab = TextField(unique=True, null=True)  # 标签（以“,”分割）
    slogan = TextField(unique=True, null=True)  # 标签（以“,”分割）
    detail_title = TextField(unique=True, null=True)  # 项目标题
    logo = TextField(unique=True, null=True)  # logo
    homepage = TextField(unique=True, null=True)  # 官网
    white_paper = TextField(unique=True, null=True)  # 白皮书
    video = TextField(unique=True, null=True)  # 视频链接
    industry = TextField(unique=True, null=True)  # 行业标签
    project_img = TextField(unique=True, null=True)  # 项目大图
    detail_excerpt = TextField(unique=True, null=True)  # 摘要
    detail_desc = TextField(unique=True, null=True)  # 项目介绍
    score = DecimalField(unique=True, null=True)  # 分数
    consents_num = IntegerField(default=0, null=True)  # 点赞数目
    reading_num = IntegerField(default=0, null=True)  # 阅读量
    comments_num = IntegerField(default=0, null=True)  # 点评数量
    follow_num = IntegerField(default=0, null=True)  # 关注数量
    is_vip = IntegerField(default=0, null=True)  # 是否是VIP（0：否；1：是）
    recommend = IntegerField(default=0, null=True)  # 是否放入推荐池，0：不放入；1：放入
    language = CharField(unique=True, null=True)  # 语言类型（国际语言编码）
    country = CharField(unique=True, null=True)  # 国家
    kyc_restriction = CharField(unique=True, null=True)  # KYC限制
    is_exchange = IntegerField(default=0, null=True)  # 是否是交易所（0：否；1：是）
    voting_rules = TextField(unique=True, null=True)  # 投票规则
    is_mining = IntegerField(default=0, null=True)  # 是否支持挖矿（0：否；1：是）
    seq = IntegerField(default=0, null=True)  # 值越大越靠前

    """
    计算总数量
    By Ada
    2019-01-29
    """

    def get_count(self):
        return ProjectModel.select().count()

    """
    根据id获取信息
    By Ada
    2019-01-29
    """

    def get_by_id(self, id):
        for Model in ProjectModel.select().where(ProjectModel.id == id):
            return Model
        return None

    """
    跟新和新建
    By Ada
    2019-01-29
    """

    def updata_model(self, model):
        if model is not None:
            ProjectModel.replace(name=model.name,
                                 ico=model.ico,
                                 lab=model.lab,
                                 slogan=model.slogan,
                                 detail_title=model.detail_title,
                                 logo=model.logo,
                                 homepage=model.homepage,
                                 white_paper=model.white_paper,
                                 video=model.video,
                                 industry=model.industry,
                                 project_img=model.project_img,
                                 detail_excerpt=model.detail_excerpt,
                                 detail_desc=model.detail_desc,
                                 score=model.score,
                                 consents_num=model.consents_num,
                                 reading_num=model.reading_num,
                                 comments_num=model.comments_num,
                                 follow_num=model.follow_num,
                                 is_vip=model.is_vip,
                                 recommend=model.recommend,
                                 language=model.language,
                                 country=model.country,
                                 kyc_restriction=model.kyc_restriction,
                                 is_exchange=model.is_exchange,
                                 voting_rules=model.voting_rules,
                                 is_mining=model.is_mining,
                                 seq=model.seq,
                                 )\
                .on_conflict(
                # 更新
                update={
                    ProjectModel.ico: model.ico,
                    ProjectModel.lab: model.lab,
                    ProjectModel.slogan: model.slogan,
                })\
                .execute()
        return Model


class Meta:
    table_name = "t_project_info"  # 表名
