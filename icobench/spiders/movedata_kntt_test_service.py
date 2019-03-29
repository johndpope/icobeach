import time
from icobench.util import *
from icobench.model.scrapy import *


class MovedataKnttTestService():
    name = 'icobench_kntt_spider'
    root_path = ""
    print('root_path:' + root_path)

    # 移动数据到测试服数据库
    def move_project_data(self):
        print('move_project_data' + 'move_project_data')
        # 查询所有的抓取到的项目数据，遍历，拿出名字去kntt项目表中查项目是否存在存在跳出，继续走下一条；
        # 不存在新建，将此项目信息添加到kntt项目表中，根据项目名称查询抓取数据的详情表，
        # 同时像kntt的ico表中添加信息，像kntt的团队表中添加团队信息，，像kntt的媒体表添加信息，像kntt官方媒体表中添加信息。

        # 查询抓取表的项目列表信息
        scrapyProjectList = ScrapyProjectListModel().get_by_id(1)
        # 关闭数据库
        scrapy_db.close()
        print('start_time:' + '关闭数据库')
        # 项目名字
        scrapyProjectList_name = scrapyProjectList.name  # 名字
        scrapyProjectList_logo = scrapyProjectList.logo  # logo
        scrapyProjectList_detail_desc = scrapyProjectList.detail_desc  # 详情
        scrapyProjectList_kyc = scrapyProjectList.kyc  # 是否存在kyc
        scrapyProjectList_white_list = scrapyProjectList.white_list  # 是否存在白名单
        scrapyProjectList_limit_countries = scrapyProjectList.limit_countries  # 限制国家
        scrapyProjectList_start_time = scrapyProjectList.start_time  # 开始时间
        scrapyProjectList_end_time = scrapyProjectList.end_time  # 结束时间
        scrapyProjectList_score = scrapyProjectList.score  # 项目评分
        # 根据项目列表id获取项目详情
        project_list_id = scrapyProjectList.id  # 列表id
        print('project_list_id:' + str(project_list_id))
        # 获取详情
        scrapyProjectDetails = ScrapyProjectDetailModel.get_by_project_list_id(ScrapyProjectDetailModel,
                                                                               project_list_id)
        print('scrapyProjectDetails:' + scrapyProjectDetails.name)
        scrapyProjectDetail_slogan = scrapyProjectDetails.slogan  # 宣传语
        scrapyProjectDetail_homepage = scrapyProjectDetails.homepage  # 官网
        scrapyProjectDetail_white_paper = scrapyProjectDetails.white_paper  # 白皮书
        scrapyProjectDetail_video = scrapyProjectDetails.video  # 视频链接
        scrapyProjectDetail_industry = scrapyProjectDetails.industry  # 行业标签
        scrapyProjectDetail_detail_excerpt = scrapyProjectDetails.detail_excerpt  # 摘要
        scrapyProjectDetail_detail_desc = scrapyProjectDetails.detail_desc  # 项目介绍
        scrapyProjectDetail_ico_symbol = scrapyProjectDetails.ico_symbol  # 代币符号
        scrapyProjectDetail_ico_soft_cap = scrapyProjectDetails.ico_soft_cap  # 软顶
        scrapyProjectDetail_ico_hard_cap = scrapyProjectDetails.ico_hard_cap  # 硬顶
        scrapyProjectDetail_ico_initial_price = scrapyProjectDetails.ico_initial_price  # 初始价格
        scrapyProjectDetail_ico_token_supply = scrapyProjectDetails.ico_token_supply  # 代币总量
        scrapyProjectDetail_ico_platform = scrapyProjectDetails.ico_platform  # 平台
        scrapyProjectDetail_ico_type = scrapyProjectDetails.ico_type  # 类型
        scrapyProjectDetail_ico_accepting = scrapyProjectDetails.ico_accepting  # 接受币种
        scrapyProjectDetail_ico_circulating_supply = scrapyProjectDetails.ico_circulating_supply  # 销售百分比
        scrapyProjectDetail_ico_preico_start_date = scrapyProjectDetails.ico_preico_start_date  # 预售开始时间
        scrapyProjectDetail_ico_preico_end_date = scrapyProjectDetails.ico_preico_end_date  # 预售结束时间
        scrapyProjectDetail_ico_preico_price = scrapyProjectDetails.ico_preico_price  # 预售价格
        scrapyProjectDetail_ico_public_start_date = scrapyProjectDetails.ico_public_start_date  # 公募开始时间
        scrapyProjectDetail_ico_preico_price = scrapyProjectDetails.ico_preico_price  # 预售价格
        scrapyProjectDetail_ico_public_end_date = scrapyProjectDetails.ico_public_end_date  # 公募结束时间
        scrapyProjectDetail_ico_public_price = scrapyProjectDetails.ico_public_price  # 公募价格
        scrapyProjectDetail_media = scrapyProjectDetails.media  # 媒体
        scrapyProjectDetail_team = scrapyProjectDetails.team  # 团队
        scrapyProjectDetail_roadmap = scrapyProjectDetails.roadmap  # 媒体


if __name__ == '__main__':
    print('' + '')
    # 查询所有，进行循环
    # scrapyProjectLists = ScrapyProjectListModel().get_list()
    # # 关闭数据库
    # scrapy_db.close()
    # print('scrapyProjectListCount：' + str(len(scrapyProjectLists)))
    # for scrapyProjectList in scrapyProjectLists:
    #     print('scrapyProjectList：' + str(scrapyProjectList))
    #     # 项目名字
    #     scrapyProjectList_name = scrapyProjectList.name
    #     print('scrapyProjectList_name：' + scrapyProjectList_name)
    #     # 关闭数据库
    #     scrapy_db.close()

    # 查询抓取表的项目列表信息
    scrapyProjectList = ScrapyProjectListModel().get_by_id(3)
    # 根据项目列表id获取项目详情
    project_list_id = scrapyProjectList.id
    print('project_list_id:' + str(project_list_id))
    scrapyProjectDetails = ScrapyProjectDetailModel.get_by_project_list_id(ScrapyProjectDetailModel, project_list_id)
    print('scrapyProjectDetails:' + scrapyProjectDetails.name)
    # 取出媒体数据数组
    scrapyProjectDetail_media_arr = scrapyProjectDetails.media
    print('scrapyProjectDetail_media_arr:' + scrapyProjectDetail_media_arr)
    # 将数组转为list
    scrapyProjectDetail_media_list = list(eval(scrapyProjectDetail_media_arr))
    for scrapyProjectDetail_media in scrapyProjectDetail_media_list:
        print('scrapyProjectDetail_media:' + str(scrapyProjectDetail_media))
        # 取媒体名字
        media_name = scrapyProjectDetail_media['name']
        print('media_name:' + media_name)
        media_link = scrapyProjectDetail_media['link']
        print('media_link:' + media_link)

    scrapyProjectDetail_team_arr = scrapyProjectDetails.team  # 团队
    # 将数组转为list
    scrapyProjectDetail_team_list = list(eval(scrapyProjectDetail_team_arr))
    for scrapyProjectDetail_team in scrapyProjectDetail_team_list:
        print('scrapyProjectDetail_team:' + str(scrapyProjectDetail_team))
        team_name = scrapyProjectDetail_team['name']
        print('team_name:' + team_name)
        team_avatar = scrapyProjectDetail_team['avatar']
        print('team_avatar:' + team_avatar)
        team_title = scrapyProjectDetail_team['title']
        print('team_title:' + team_title)
        team_socials = scrapyProjectDetail_team['socials']
        print('team_socials:' + team_socials)

    scrapyProjectDetail_roadmap_arr = scrapyProjectDetails.roadmap  # 路线
    # 将数组转为list
    scrapyProjectDetail_roadmap_list = list(eval(scrapyProjectDetail_roadmap_arr))
    for scrapyProjectDetail_roadmap in scrapyProjectDetail_roadmap_list:
        print('scrapyProjectDetail_roadmap:' + str(scrapyProjectDetail_roadmap))
        roadmap_time = scrapyProjectDetail_roadmap['roadmap_time']
        print('roadmap_time:' + roadmap_time)
        roadmap_target = scrapyProjectDetail_roadmap['roadmap_target']
        print('roadmap_target:' + roadmap_target)


