from icobench.model.kntt.base_kntt_model import BaseKnttModel, qishi_db
from peewee import *
import datetime

"""
ProjectMediaModel项目model层   
"""


class ProjectMediaModel(BaseKnttModel):
    project_id = IntegerField(null=True)  # 项目id
    name = CharField(null=True)  # 媒体名字
    image = CharField(null=True)  # 图片
    link = CharField(null=True)  # 链接
    language = CharField(null=True)  # 链接
    created_at = DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.datetime.now)  # 更新时间

    """
    计算总数
    By Ada
    2019-03-22
    """

    def get_count(self):
        return ProjectMediaModel.select().count()

    """
    根据项目id获取信息
    By Ada
    2019-03-22
    """

    def get_by_project_id(self, project_id):
        for Model in ProjectMediaModel.select().where(ProjectMediaModel.project_id == project_id):
            return Model
        return None

    """
    更新和创建信息
    By Ada
    2019-03-22
    """

    def updata_model(self, model):
        if model is not None:
            ProjectMediaModel.replace(project_id=model.project_id,
                                      name=model.name,
                                      image=model.image,
                                      link=model.link,
                                      language=model.language,
                                      ) \
                .on_conflict(
                # 更新
                update={
                    ProjectMediaModel.project_id: model.project_id,
                    ProjectMediaModel.name: model.name,
                    ProjectMediaModel.image: model.image,
                    ProjectMediaModel.link: model.link,
                    ProjectMediaModel.language: model.language,
                }) \
                .execute()
        return Model

    class Meta:
        table_name = "t_project_media"  # 表名
