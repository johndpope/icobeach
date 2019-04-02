from icobench.model.kntt.base_kntt_model import BaseKnttModel, qishi_db
from peewee import *
import datetime

"""
ProjectIcoModel项目model层   
"""


class ProjectIcoModel(BaseKnttModel):
    # CharField：字符串类型
    name = CharField(unique=True, null=True)  # 名称
    project_id = IntegerField(null=True)  # 项目id
    status = IntegerField(null=True)  # 状态（0：准备中；1：进行中；2：已结束；3：未发行；4：已流通；5：终止）
    symbol = CharField(null=True)  # 名称     TextField(unique=True, null=True)
    start_date = DateTimeField(null=True)  # 开始日期
    end_date = DateTimeField(null=True)  # 结束日期
    soft_cap = CharField(null=True)  # 目标下限
    hard_cap = CharField(null=True)  # 目标上限
    initial_price = CharField(null=True)  # 初始价格
    token_supply = CharField(null=True)  # 代币数
    platform = CharField(null=True)  # 平台
    type = CharField(null=True)  # 类型
    accepting = CharField(null=True)  # 接受币种
    circulating_supply = CharField(null=True)  # 流通百分比
    restriction = CharField(null=True)  # 投资限制
    whitelist_start_date = DateTimeField(null=True)  # 白名单开始时间
    whitelist_end_date = DateTimeField(null=True)  # 白名单结束时间
    kyc = IntegerField(default=0, null=True)  # KYC:是否存在kyc;0:否；1：是
    kyc_start_date = DateTimeField(null=True)  # KYC开始时间
    kyc_end_date = DateTimeField(null=True)  # KYC结束时间
    kyc_url = CharField(null=True)  # KYC地址
    private_start_date = DateTimeField(null=True)  # 私募开始时间
    private_end_date = DateTimeField(null=True)  # 私募结束时间
    private_price = CharField(null=True)  # 私募价格
    private_lower_limit = CharField(null=True)  # 私募下限/账号
    private_upper_limit = CharField(null=True)  # 私募上限/账号
    preico_start_date = DateTimeField(null=True)  # 预售开始时间
    preico_end_date = DateTimeField(null=True)  # 预售结束时间
    preico_url = CharField(null=True)  # 预售地址
    preico_price = CharField(null=True)  # 预售价格
    preico_lower_limit = CharField(null=True)  # 预售下限/账号
    preico_upper_limit = CharField(null=True)  # 预售上限/账号
    public_start_date = DateTimeField(null=True)  # 公募开始时间
    public_end_date = DateTimeField(null=True)  # 公募结束时间
    public_url = CharField(null=True)  # 公募地址
    public_price = CharField(null=True)  # 公募价格
    public_lower_limit = CharField(null=True)  # 公募下限/账号
    public_upper_limit = CharField(null=True)  # 公募上限/账号/账号
    created_at = DateTimeField(default=datetime.datetime.now)  # 创建时间
    updated_at = DateTimeField(default=datetime.datetime.now)  # 更新时间

    """
    计算总数量
    By Ada
    2019-03-21
    """

    def get_count(self):
        return ProjectIcoModel.select().count()

    """
    根据id获取信息
    By Ada
    2019-03-21
    """

    def get_by_id(self, id):
        for Model in ProjectIcoModel.select().where(ProjectIcoModel.id == id):
            return Model
        return None

    """
    根据项目id查询信息
    By Ada
    2019-03-21
    """
    def get_by_project_id(self,project_id):
        for Model in ProjectIcoModel.select().where(ProjectIcoModel.project_id == project_id):
            return Model
        return None

    """
    跟新和新建
    By Ada
    2019-03-21
    """

    def update_model(self, model):
        if model is not None:
            ProjectIcoModel.replace(name=model.name,
                                    project_id=model.project_id,
                                    status=model.status,
                                    symbol=model.symbol,
                                    start_date=model.start_date,
                                    end_date=model.end_date,
                                    soft_cap=model.soft_cap,
                                    hard_cap=model.hard_cap,
                                    initial_price=model.initial_price,
                                    token_supply=model.token_supply,
                                    platform=model.platform,
                                    type=model.type,
                                    accepting=model.accepting,
                                    circulating_supply=model.circulating_supply,
                                    restriction=model.restriction,
                                    whitelist_start_date=model.whitelist_start_date,
                                    whitelist_end_date=model.whitelist_end_date,
                                    kyc=model.kyc,
                                    kyc_start_date=model.kyc_start_date,
                                    kyc_end_date=model.kyc_end_date,
                                    kyc_url=model.kyc_url,
                                    private_start_date=model.private_start_date,
                                    private_end_date=model.private_end_date,
                                    private_price=model.private_price,
                                    private_lower_limit=model.private_lower_limit,
                                    private_upper_limit=model.private_upper_limit,
                                    preico_start_date=model.preico_start_date,
                                    preico_end_date=model.preico_end_date,
                                    preico_url=model.preico_url,
                                    preico_price=model.preico_price,
                                    preico_lower_limit=model.preico_lower_limit,
                                    preico_upper_limit=model.preico_upper_limit,
                                    public_start_date=model.public_start_date,
                                    public_end_date=model.public_end_date,
                                    public_url=model.public_url,
                                    public_price=model.public_price,
                                    public_lower_limit=model.public_lower_limit,
                                    public_upper_limit=model.public_upper_limit,
                                    ) \
                .on_conflict(
                # 更新
                update={
                    ProjectIcoModel.name: model.name,
                    ProjectIcoModel.project_id: model.project_id,
                    ProjectIcoModel.status: model.status,
                    ProjectIcoModel.symbol: model.symbol,
                    ProjectIcoModel.start_date: model.start_date,
                    ProjectIcoModel.end_date: model.end_date,
                    ProjectIcoModel.soft_cap: model.soft_cap,
                    ProjectIcoModel.hard_cap: model.hard_cap,
                    ProjectIcoModel.initial_price: model.initial_price,
                    ProjectIcoModel.token_supply: model.token_supply,
                    ProjectIcoModel.platform: model.platform,
                    ProjectIcoModel.type: model.type,
                    ProjectIcoModel.accepting: model.accepting,
                    ProjectIcoModel.circulating_supply: model.circulating_supply,
                    ProjectIcoModel.restriction: model.restriction,
                    ProjectIcoModel.whitelist_start_date: model.whitelist_start_date,
                    ProjectIcoModel.whitelist_end_date: model.whitelist_end_date,
                    ProjectIcoModel.kyc: model.kyc,
                    ProjectIcoModel.kyc_start_date: model.kyc_start_date,
                    ProjectIcoModel.kyc_end_date: model.kyc_end_date,
                    ProjectIcoModel.kyc_url: model.kyc_url,
                    ProjectIcoModel.private_start_date: model.private_start_date,
                    ProjectIcoModel.private_end_date: model.private_end_date,
                    ProjectIcoModel.private_price: model.private_price,
                    ProjectIcoModel.private_lower_limit: model.private_lower_limit,
                    ProjectIcoModel.private_upper_limit: model.private_upper_limit,
                    ProjectIcoModel.preico_start_date: model.preico_start_date,
                    ProjectIcoModel.preico_end_date: model.preico_end_date,
                    ProjectIcoModel.preico_url: model.preico_url,
                    ProjectIcoModel.preico_price: model.preico_price,
                    ProjectIcoModel.preico_lower_limit: model.preico_lower_limit,
                    ProjectIcoModel.preico_upper_limit: model.preico_upper_limit,
                    ProjectIcoModel.public_start_date: model.public_start_date,
                    ProjectIcoModel.public_end_date: model.public_end_date,
                    ProjectIcoModel.public_url: model.public_url,
                    ProjectIcoModel.public_price: model.public_price,
                    ProjectIcoModel.public_lower_limit: model.public_lower_limit,
                    ProjectIcoModel.public_upper_limit: model.public_upper_limit,
                    ProjectIcoModel.updated_at: model.updated_at,
                }) \
                .execute()
        return Model

    class Meta:
        table_name = "t_project_ico"  # 表名