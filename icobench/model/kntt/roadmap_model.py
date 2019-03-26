from icobench.model.kntt.base_kntt_model import BaseKnttModel, qishi_db
from peewee import *
import datetime

"""
ProjectRoadmapModel项目model层   
"""


class ProjectRoadmapModel(BaseKnttModel):
    project_id = IntegerField(null=True)  # 项目id
    time = CharField(null=True)  # 时间
    target = CharField(null=True)  # 目标
    status = CharField(null=True)  # 状态（0：未知；1：按时完成；2：逾期完成；3：未完成）
    language = CharField(default='en', null=True)  # 个人主页
    created_at = DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.datetime.now)  # 更新时间

    """
    计算总数
    By Ada
    2019-03-21
    """

    def get_count(self):
        return ProjectRoadmapModel.select().count()

    """
    根据项目id查询信息
    By Ada
    2019-03-21
    """

    def get_by_project_id(self, project_id):
        for Model in ProjectRoadmapModel.select ().where(ProjectRoadmapModel.project_id == project_id):
            return Model
        return None

    """
    更新和创建
    By Ada
    2019-03-21
    """

    def updata_model(self, model):
        if model is not None:
            ProjectRoadmapModel.replace(project_id=model.project_id,
                                        time=model.time,
                                        target=model.target,
                                        status=model.status,
                                        language=model.language,
                                        ) \
                .on_conflict(
                # 更新
                update={
                    ProjectRoadmapModel.project_id: model.project_id,
                    ProjectRoadmapModel.time: model.time,
                    ProjectRoadmapModel.target: model.target,
                    ProjectRoadmapModel.status: model.status,
                    ProjectRoadmapModel.language: model.language,
                }) \
                .execute()
        return Model

    class Meta:
        table_name = "t_roadmap_info"  # 表名
