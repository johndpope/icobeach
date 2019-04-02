import time
from icobench.util import *
from icobench.model.scrapy import *
from icobench.model.kntt import *
import datetime


class MovedataKnttTestService():
    # name = 'movedata_kntt_test_service'
    # root_path = ""
    # print('root_path:' + root_path)

    def trans_qiniu(self, img_url):
        f_name = UUIDUtil().get_uuid()
        print(f_name)
        status = QiniuUtil().upload_url(img_url, f_name)
        if status is False:
            status = QiniuUtil().upload_url2file(img_url, f_name)
            if status is False:
                img = ""
            else:
                img = "http://img.lvluozhibao.com/" + f_name
        else:
            img = "http://img.lvluozhibao.com/" + f_name
        return img

    # 移动数据到测试服数据库
    def move_project_data(self):
        print('move_project_data' + 'move_project_data')
        # 查询所有的抓取到的项目数据，遍历，拿出名字去kntt项目表中查项目是否存在存在跳出，继续走下一条；
        # 不存在新建，将此项目信息添加到kntt项目表中，根据项目名称查询抓取数据的详情表，
        # 同时像kntt的ico表中添加信息，像kntt的团队表中添加团队信息，，像kntt的媒体表添加信息，像kntt官方媒体表中添加信息。

        # # 查询抓取表的项目列表信息
        # scrapyProjectList = ScrapyProjectListModel().get_by_id(1)
        # 关闭数据库
        scrapy_db.close()

        # 查询所有，进行循环
        scrapyProjectLists = ScrapyProjectListModel().get_list()
        # 关闭数据库
        scrapy_db.close()
        print('scrapyProjectListCount：' + str(len(scrapyProjectLists)))
        for scrapyProjectList in scrapyProjectLists:
            print('start_time:' + '关闭数据库')
            # 项目名字
            scrapyProjectList_name = scrapyProjectList.name  # 名字
            # 判断kntt数据库中是否存在此项目
            project_model = ProjectModel.get_by_name(self, scrapyProjectList_name)
            # 关闭数据库
            qishi_db.close()
            if project_model is None:
                scrapyProjectList_logo = scrapyProjectList.logo  # logo
                scrapyProjectList_kyc = scrapyProjectList.kyc  # 是否存在kyc
                # scrapyProjectList_white_list = scrapyProjectList.white_list  # 是否存在白名单
                scrapyProjectList_limit_countries = scrapyProjectList.limit_countries  # 限制国家
                scrapyProjectList_start_time = scrapyProjectList.start_time  # 开始时间
                if scrapyProjectList_start_time != '':
                    scrapyProjectList_start_time = TimeUtil.en_datetime_to_zh_datetime(self,
                                                                                       scrapyProjectList_start_time),
                scrapyProjectList_end_time = scrapyProjectList.end_time  # 结束时间
                if scrapyProjectList_end_time != '':
                    scrapyProjectList_end_time = TimeUtil.en_datetime_to_zh_datetime(self, scrapyProjectList_end_time),
                scrapyProjectList_score = scrapyProjectList.score  # 项目评分
                # 根据项目列表id获取项目详情
                project_list_id = scrapyProjectList.id  # 列表id
                print('project_list_id:' + str(project_list_id))
                # 获取详情
                scrapyProjectDetails = ScrapyProjectDetailModel.get_by_project_list_id(ScrapyProjectDetailModel,
                                                                                       project_list_id)
                # 关闭数据库
                scrapy_db.close()
                if scrapyProjectDetails is not None:
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
                    if scrapyProjectDetail_ico_preico_start_date != '':
                        scrapyProjectDetail_ico_preico_start_date = TimeUtil.str_time_todatatime(self,
                                                                                                 scrapyProjectDetail_ico_preico_start_date),
                    else:
                        scrapyProjectDetail_ico_preico_start_date = None
                    print('scrapyProjectDetail_ico_preico_start_date:' + str(scrapyProjectDetail_ico_preico_start_date))

                    scrapyProjectDetail_ico_preico_end_date = scrapyProjectDetails.ico_preico_end_date  # 预售结束时间
                    if scrapyProjectDetail_ico_preico_end_date != '':
                        scrapyProjectDetail_ico_preico_end_date = TimeUtil.str_time_todatatime(self,
                                                                                               scrapyProjectDetail_ico_preico_end_date),
                    else:
                        scrapyProjectDetail_ico_preico_end_date = None
                    print('scrapyProjectDetail_ico_preico_end_date:' + str(scrapyProjectDetail_ico_preico_end_date))
                    scrapyProjectDetail_ico_preico_price = scrapyProjectDetails.ico_preico_price  # 预售价格
                    scrapyProjectDetail_ico_public_start_date = scrapyProjectDetails.ico_public_start_date  # 公募开始时间
                    if scrapyProjectDetail_ico_public_start_date != '':
                        scrapyProjectDetail_ico_public_start_date = TimeUtil.str_time_todatatime(self,
                                                                                                 scrapyProjectDetail_ico_public_start_date),
                    else:
                        scrapyProjectDetail_ico_public_start_date = None
                    print('scrapyProjectDetail_ico_public_start_date:' + str(scrapyProjectDetail_ico_public_start_date))
                    scrapyProjectDetail_ico_public_end_date = scrapyProjectDetails.ico_public_end_date  # 公募结束时间
                    if scrapyProjectDetail_ico_public_end_date != '':
                        scrapyProjectDetail_ico_public_end_date = TimeUtil.str_time_todatatime(self,
                                                                                               scrapyProjectDetail_ico_public_end_date),
                    else:
                        scrapyProjectDetail_ico_public_end_date = None
                    print('scrapyProjectDetail_ico_public_end_date:' + str(scrapyProjectDetail_ico_public_end_date))
                    scrapyProjectDetail_ico_public_price = scrapyProjectDetails.ico_public_price  # 公募价格
                    # 取出媒体数据数组
                    scrapyProjectDetail_media_arr = scrapyProjectDetails.media  # 媒体
                    print('scrapyProjectDetail_media_arr:' + scrapyProjectDetail_media_arr)

                    scrapyProjectDetail_team_arr = scrapyProjectDetails.team  # 团队

                    scrapyProjectDetail_roadmap_arr = scrapyProjectDetails.roadmap  # 路线

                    print('scrapyProjectDetail_video:' + scrapyProjectDetail_video)
                    # 组合项目信息数据
                    test_kntt_project_list_model = ProjectModel(
                        name=scrapyProjectList_name,
                        ico='1',
                        lab=scrapyProjectDetail_industry,
                        slogan=scrapyProjectDetail_slogan,
                        detail_title=scrapyProjectList_name,
                        logo=self.trans_qiniu(scrapyProjectList_logo),
                        homepage=scrapyProjectDetail_homepage,
                        white_paper=scrapyProjectDetail_white_paper,
                        video=self.trans_qiniu(scrapyProjectDetail_video),
                        industry=scrapyProjectDetail_industry,
                        detail_excerpt=scrapyProjectDetail_detail_excerpt,
                        detail_desc=scrapyProjectDetail_detail_desc,
                        score=scrapyProjectList_score,
                        country=scrapyProjectList_limit_countries,
                    )
                    print('test_kntt_project_list_model:' + str(test_kntt_project_list_model))
                    ProjectModel().update_model(test_kntt_project_list_model)
                    # 关闭数据库
                    qishi_db.close()
                    # 根据项目名称查询app数据库的项目id
                    project_list = ProjectModel.get_by_name(self, scrapyProjectList_name)
                    project_list_id = project_list.id
                    print('project_list_id:' + str(project_list_id))

                    # 组合项目ico信息数据
                    test_kntt_project_ico_model = ProjectIcoModel(
                        name=scrapyProjectList_name,
                        project_id=project_list_id,
                        status='0',
                        symbol=scrapyProjectDetail_ico_symbol,
                        start_date=scrapyProjectList_start_time,
                        end_date=scrapyProjectList_end_time,
                        soft_cap=scrapyProjectDetail_ico_soft_cap,
                        hard_cap=scrapyProjectDetail_ico_hard_cap,
                        initial_price=scrapyProjectDetail_ico_initial_price,
                        token_supply=scrapyProjectDetail_ico_token_supply,
                        platform=scrapyProjectDetail_ico_platform,
                        type=scrapyProjectDetail_ico_type,
                        accepting=scrapyProjectDetail_ico_accepting,
                        circulating_supply=scrapyProjectDetail_ico_circulating_supply,
                        kyc=scrapyProjectList_kyc,
                        preico_start_date=scrapyProjectDetail_ico_preico_start_date,
                        preico_end_date=scrapyProjectDetail_ico_preico_end_date,
                        preico_price=scrapyProjectDetail_ico_preico_price,
                        public_start_date=scrapyProjectDetail_ico_public_start_date,
                        public_end_date=scrapyProjectDetail_ico_public_end_date,
                        public_price=scrapyProjectDetail_ico_public_price,
                    )
                    print('test_kntt_project_ico_model:' + str(test_kntt_project_ico_model))
                    ProjectIcoModel().update_model(test_kntt_project_ico_model)
                    # 关闭数据库
                    qishi_db.close()

                    # 掉更新媒体信息
                    self.update_project_media_mes(scrapyProjectDetail_media_arr, project_list_id)

                    # 掉更新团队信息
                    self.update_project_team_mes(scrapyProjectDetail_team_arr, project_list_id)

                    # 掉更新路线信息
                    self.update_project_roadmap_mes(scrapyProjectDetail_roadmap_arr, project_list_id)

    def update_project_media_mes(self, scrapyProjectDetail_media_arr, project_list_id):
        # 将数组转为list
        scrapyProjectDetail_media_list = list(eval(scrapyProjectDetail_media_arr))
        # 循环取出媒体信息
        for scrapyProjectDetail_media in scrapyProjectDetail_media_list:
            print('scrapyProjectDetail_media:' + str(scrapyProjectDetail_media))
            # 取媒体名字
            media_name = scrapyProjectDetail_media['name']
            print('media_name:' + media_name)
            media_link = scrapyProjectDetail_media['link']
            print('media_link:' + media_link)
            #  组合媒体信息
            test_kntt_project_media_model = ProjectMediaModel(
                project_id=project_list_id,
                name=media_name,
                link=media_link,
                language='en',
            )
            print('test_kntt_project_media_model:' + str(test_kntt_project_media_model))
            ProjectMediaModel().update_model(test_kntt_project_media_model)
            # 关闭数据库
            qishi_db.close()

    def update_project_team_mes(self, scrapyProjectDetail_team_arr, project_list_id):
        # 将数组转为list
        scrapyProjectDetail_team_list = list(eval(scrapyProjectDetail_team_arr))
        # 循环取出信息
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

            #  组合团队信息
            test_kntt_project_team_model = ProjectTeamModel(
                project_id=project_list_id,
                name=team_name,
                avatar=self.trans_qiniu(team_avatar),
                socials=team_socials,
                title=team_title,
                language='en',
            )
            print('test_kntt_project_team_model:' + str(test_kntt_project_team_model))
            ProjectTeamModel().update_model(test_kntt_project_team_model)
            # 关闭数据库
            qishi_db.close()

    def update_project_roadmap_mes(self, scrapyProjectDetail_roadmap_arr, project_list_id):
        # 将数组转为list
        scrapyProjectDetail_roadmap_list = list(eval(scrapyProjectDetail_roadmap_arr))
        # 循环取出信息
        for scrapyProjectDetail_roadmap in scrapyProjectDetail_roadmap_list:
            print('scrapyProjectDetail_roadmap:' + str(scrapyProjectDetail_roadmap))
            roadmap_time = scrapyProjectDetail_roadmap['roadmap_time']
            print('roadmap_time:' + roadmap_time)
            roadmap_target = scrapyProjectDetail_roadmap['roadmap_target']
            print('roadmap_target:' + roadmap_target)

            #  组合路线信息
            test_kntt_project_roadmap_model = ProjectRoadmapModel(
                project_id=project_list_id,
                time=roadmap_time,
                target=roadmap_target,
                status='1',
                language='en',
            )
            print('test_kntt_project_roadmap_model:' + str(test_kntt_project_roadmap_model))
            ProjectRoadmapModel().update_model(test_kntt_project_roadmap_model)
            # 关闭数据库
            qishi_db.close()


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

    # # 查询抓取表的项目列表信息
    # scrapyProjectList = ScrapyProjectListModel().get_by_id(3)
    # # 根据项目列表id获取项目详情
    # project_list_id = scrapyProjectList.id
    # print('project_list_id:' + str(project_list_id))
    # scrapyProjectDetails = ScrapyProjectDetailModel.get_by_project_list_id(ScrapyProjectDetailModel, project_list_id)
    # print('scrapyProjectDetails:' + scrapyProjectDetails.name)
    # # 取出媒体数据数组
    # scrapyProjectDetail_media_arr = scrapyProjectDetails.media
    # print('scrapyProjectDetail_media_arr:' + scrapyProjectDetail_media_arr)
    # # 将数组转为list
    # scrapyProjectDetail_media_list = list(eval(scrapyProjectDetail_media_arr))
    # for scrapyProjectDetail_media in scrapyProjectDetail_media_list:
    #     print('scrapyProjectDetail_media:' + str(scrapyProjectDetail_media))
    #     # 取媒体名字
    #     media_name = scrapyProjectDetail_media['name']
    #     print('media_name:' + media_name)
    #     media_link = scrapyProjectDetail_media['link']
    #     print('media_link:' + media_link)
    #
    # scrapyProjectDetail_team_arr = scrapyProjectDetails.team  # 团队
    # # 将数组转为list
    # scrapyProjectDetail_team_list = list(eval(scrapyProjectDetail_team_arr))
    # for scrapyProjectDetail_team in scrapyProjectDetail_team_list:
    #     print('scrapyProjectDetail_team:' + str(scrapyProjectDetail_team))
    #     team_name = scrapyProjectDetail_team['name']
    #     print('team_name:' + team_name)
    #     team_avatar = scrapyProjectDetail_team['avatar']
    #     print('team_avatar:' + team_avatar)
    #     team_title = scrapyProjectDetail_team['title']
    #     print('team_title:' + team_title)
    #     team_socials = scrapyProjectDetail_team['socials']
    #     print('team_socials:' + team_socials)
    #
    # scrapyProjectDetail_roadmap_arr = scrapyProjectDetails.roadmap  # 路线
    # # 将数组转为list
    # scrapyProjectDetail_roadmap_list = list(eval(scrapyProjectDetail_roadmap_arr))
    # for scrapyProjectDetail_roadmap in scrapyProjectDetail_roadmap_list:
    #     print('scrapyProjectDetail_roadmap:' + str(scrapyProjectDetail_roadmap))
    #     roadmap_time = scrapyProjectDetail_roadmap['roadmap_time']
    #     print('roadmap_time:' + roadmap_time)
    #     roadmap_target = scrapyProjectDetail_roadmap['roadmap_target']
    #     print('roadmap_target:' + roadmap_target)

    # 查询抓取表的项目列表信息      测试七牛上传
    # scrapyProjectList = ScrapyProjectListModel().get_by_id(3)
    # scrapyProjectList_logo = scrapyProjectList.logo
    # print('scrapyProjectList_logo:' + scrapyProjectList_logo)
    # scrapyProjectList_logo = MovedataKnttTestService.trans_qiniu(scrapyProjectList, scrapyProjectList_logo)
    # print('scrapyProjectList_logo:' + scrapyProjectList_logo)
    # scrapyProjectList_video = 'https://www.youtube.com/embed/DCBABbhNUfY'
    # print('scrapyProjectList_video:' + scrapyProjectList_video)
    # scrapyProjectList_video = MovedataKnttTestService.trans_qiniu(scrapyProjectList, scrapyProjectList_video)
    # print('scrapyProjectList_video:' + scrapyProjectList_video)

    # init service

    service = MovedataKnttTestService()
    service.move_project_data()

    # ProjectModel = ProjectModel.get_by_id(ProjectModel,'1')
    # print('ProjectModel' + ProjectModel.name)

    # project_list = ProjectModel.get_by_name(ProjectModel,'ghjghjhf');
    # print('project_list' + str(project_list.id))

    # time = '2019-04-02'
    # # date = datetime.time.strftime('%Y-%m-%d %H:%M:%S')
    # date = TimeUtil.str_time_todatatime('',time)
    # print('date' + str(date))

    # time = '18 Feb 2019'
    # time_format = datetime.datetime.strptime(time, '%d %b %Y')
    # print('time_format' + str(time_format))
