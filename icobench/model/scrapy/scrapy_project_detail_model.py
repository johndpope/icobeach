from icobench.model.scrapy.base_scrapy_model import BaseScrapyModel
from peewee import *
import datetime

"""
ScrapyProjectDetailModel项目model层   
"""


class ScrapyProjectDetailModel(BaseScrapyModel):
    # CharField：字符串类型
    project_list_id = CharField(unique=True, null=True)  # 项目列表id
    name = CharField(unique=True, null=True)  # 名称
    slogan = TextField(null=True)  # 宣传语
    logo = TextField(null=True)  # logo
    homepage = TextField(null=True)  # 官网
    white_paper = TextField(null=True)  # 白皮书
    video = TextField(null=True)  # 视频链接
    industry = TextField(null=True)  # 行业标签
    detail_excerpt = TextField(null=True)  # 摘要
    detail_desc = TextField(null=True)  # 项目介绍
    # ico信息
    ico_symbol = CharField(null=True)  # 代币符号
    ico_soft_cap = CharField(null=True)  # 软顶
    ico_hard_cap = CharField(null=True)  # 硬顶
    ico_initial_price = CharField(null=True)  # 初始价格
    ico_token_supply = CharField(null=True)  # 代币总量
    ico_platform = CharField(null=True)  # 平台
    ico_type = CharField(null=True)  # 类型
    ico_accepting = CharField(null=True)  # 接受币种
    ico_circulating_supply = CharField(null=True)  # 销售百分比
    ico_preico_start_date = CharField(null=True)  # 预售开始时间
    ico_preico_end_date = CharField(null=True)  # 预售结束时间
    ico_preico_price = CharField(null=True)  # 预售价格
    ico_public_start_date = CharField(null=True)  # 公募开始时间
    ico_public_end_date = CharField(null=True)  # 公募结束时间
    ico_public_price = CharField(null=True)  # 公募价格
    # 媒体信息
    media = TextField(null=True)  # 媒体
    # media_name = CharField(null=True)  # 媒体名称
    # media_link = CharField(null=True)  # 媒体链接
    # 团队信息
    team = TextField(null=True)  # 团队
    # team_name = CharField(null=True)  # 团队成员名称
    # team_avatar = CharField(null=True)  # 头像
    # team_socials = CharField(null=True)  # 社交媒体
    # team_title = CharField(null=True)  # 职位
    # 路线信息
    roadmap = TextField(null=True)  # 媒体
    # roadmap_time = CharField(null=True)  # 时间
    # roadmap_target = CharField(null=True)  # 目标

    create_date = DateTimeField(default=datetime.datetime.now)
    update_date = DateTimeField(default=datetime.datetime.now)

    """
    计算总数量
    By Ada
    2019-01-29
    """

    def get_count(self):
        return ScrapyProjectDetailModel.select().count()

    """
    根据id获取信息
    By Ada
    2019-01-29
    """

    def get_by_id(self, id):
        for Model in ScrapyProjectDetailModel.select().where(ScrapyProjectDetailModel.id == id):
            return Model
        return None

    """
        根据id获取信息
        By Ada
        2019-01-29
        """

    def get_by_project_list_id(self, project_list_id):
        print('project_list_id_model:' + str(project_list_id))
        for Model in ScrapyProjectDetailModel.select().where(ScrapyProjectDetailModel.project_list_id == project_list_id):
            return Model
        return None

    """
    跟新和新建
    By Ada
    2019-01-29
    """

    def update_model(self, model):
        print('model_update_model1:' + str(model))
        if model is not None:
            print('model:' + str(model))
            ScrapyProjectDetailModel.replace(name=model.name,
                                             project_list_id=model.project_list_id,
                                             slogan=model.slogan,
                                             logo=model.logo,
                                             homepage=model.homepage,
                                             white_paper=model.white_paper,
                                             video=model.video,
                                             detail_excerpt=model.detail_excerpt,
                                             detail_desc=model.detail_desc,
                                             ico_symbol=model.ico_symbol,
                                             ico_soft_cap=model.ico_soft_cap,
                                             ico_hard_cap=model.ico_hard_cap,
                                             ico_initial_price=model.ico_initial_price,
                                             ico_token_supply=model.ico_token_supply,
                                             ico_platform=model.ico_platform,
                                             ico_type=model.ico_type,
                                             ico_accepting=model.ico_accepting,
                                             ico_circulating_supply=model.ico_circulating_supply,
                                             ico_preico_start_date=model.ico_preico_start_date,
                                             ico_preico_end_date=model.ico_preico_end_date,
                                             ico_preico_price=model.ico_preico_price,
                                             ico_public_start_date=model.ico_public_start_date,
                                             ico_public_end_date=model.ico_public_end_date,
                                             ico_public_price=model.ico_public_price,
                                             media=model.media,
                                             # media_name=model.media_name,
                                             # media_link=model.media_link,
                                             team=model.team,
                                             # team_name=model.team_name,
                                             # team_avatar=model.team_avatar,
                                             # team_socials=model.team_socials,
                                             # team_title=model.team_title,
                                             roadmap=model.roadmap,
                                             # roadmap_time=model.roadmap_time,
                                             # roadmap_target=model.roadmap_target,
                                             ) \
                .on_conflict(
                # 更新
                update={
                    ScrapyProjectDetailModel.project_list_id: model.project_list_id,
                    ScrapyProjectDetailModel.slogan: model.slogan,
                    ScrapyProjectDetailModel.logo: model.logo,
                    ScrapyProjectDetailModel.homepage: model.homepage,
                    ScrapyProjectDetailModel.white_paper: model.white_paper,
                    ScrapyProjectDetailModel.video: model.video,
                    ScrapyProjectDetailModel.detail_excerpt: model.detail_excerpt,
                    ScrapyProjectDetailModel.detail_desc: model.detail_desc,
                    ScrapyProjectDetailModel.ico_symbol: model.ico_symbol,
                    ScrapyProjectDetailModel.ico_soft_cap: model.ico_soft_cap,
                    ScrapyProjectDetailModel.ico_hard_cap: model.ico_hard_cap,
                    ScrapyProjectDetailModel.ico_initial_price: model.ico_initial_price,
                    ScrapyProjectDetailModel.ico_token_supply: model.ico_token_supply,
                    ScrapyProjectDetailModel.ico_platform: model.ico_platform,
                    ScrapyProjectDetailModel.ico_type: model.ico_type,
                    ScrapyProjectDetailModel.ico_accepting: model.ico_accepting,
                    ScrapyProjectDetailModel.ico_circulating_supply: model.ico_circulating_supply,
                    ScrapyProjectDetailModel.ico_preico_start_date: model.ico_preico_start_date,
                    ScrapyProjectDetailModel.ico_preico_end_date: model.ico_public_end_date,
                    ScrapyProjectDetailModel.ico_preico_price: model.ico_preico_price,
                    ScrapyProjectDetailModel.ico_public_start_date: model.ico_public_start_date,
                    ScrapyProjectDetailModel.ico_public_end_date: model.ico_public_end_date,
                    ScrapyProjectDetailModel.ico_public_price: model.ico_public_price,
                    ScrapyProjectDetailModel.media: model.media,
                    # ScrapyProjectDetailModel.media_name: model.media_name,
                    # ScrapyProjectDetailModel.media_link: model.media_link,
                    ScrapyProjectDetailModel.team: model.team,
                    # ScrapyProjectDetailModel.team_name: model.team_name,
                    # ScrapyProjectDetailModel.team_avatar: model.team_avatar,
                    # ScrapyProjectDetailModel.team_socials: model.team_socials,
                    # ScrapyProjectDetailModel.team_title: model.team_title,
                    ScrapyProjectDetailModel.roadmap: model.roadmap,
                    # ScrapyProjectDetailModel.roadmap_time: model.roadmap_time,
                    # ScrapyProjectDetailModel.roadmap_target: model.roadmap_target,
                }) \
                .execute()
            print('model_update_model2:' + str(model))
        return model

    class Meta:
        table_name = "t_project_detail_info"  # 表名
