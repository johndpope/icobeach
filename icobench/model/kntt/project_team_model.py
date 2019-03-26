from icobench.model.kntt.base_kntt_model import BaseKnttModel, qishi_db
from peewee import *
import datetime

"""
ProjectTeamModel项目model层   
"""


class ProjectTeamModel(BaseKnttModel):
    project_id = IntegerField(null=True)  # 项目id
    name = CharField(null=True)  # 名称
    avatar = TextField(null=True)  # 头像
    socials = TextField(null=True)  # 个人主页
    title = TextField(null=True)  # 个人主页
    language = CharField(default='en', null=True)  # 个人主页
    created_at = DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.datetime.now)  # 更新时间

    """
    计算总数
    By Ada
    2019-03-21
    """

    def get_count(self):
        return ProjectTeamModel.select().count()

    """
    根据项目id查询信息
    By Ada
    2019-03-21
    """

    def get_by_project_id(self, project_id):
        for Model in ProjectTeamModel.select().where(ProjectTeamModel.project_id == project_id):
            return Model
        return None

    """
    跟新和新建
    By Ada
    2019-03-21
    """

    def updata_model(self, model):
        if model is not None:
            ProjectTeamModel.replace(name=model.name,
                                     project_id=model.project_id,
                                     avatar=model.avatar,
                                     socials=model.socials,
                                     title=model.title,
                                     language=model.language,
                                     ) \
                .on_conflict(
                # 更新
                update={
                    ProjectTeamModel.name: model.name,
                    ProjectTeamModel.project_id: model.project_id,
                    ProjectTeamModel.avatar: model.avatar,
                    ProjectTeamModel.socials: model.socials,
                    ProjectTeamModel.title: model.title,
                    ProjectTeamModel.language: model.language,
                }) \
                .execute()
        return Model

    class Meta:
        table_name = "t_project_team_info"  # 表名
