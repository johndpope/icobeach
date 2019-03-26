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
        scrapyProjectList_name = scrapyProjectList.name
        scrapyProjectList_logo = scrapyProjectList.logo






if __name__ == '__main__':
    print('' + '')
    scrapyProjectList = ScrapyProjectListModel().get_by_id(1)
    # 项目名字
    scrapyProjectList_name = scrapyProjectList.name