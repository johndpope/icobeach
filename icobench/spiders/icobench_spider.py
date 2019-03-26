import scrapy
import os
from icobench.util import *
from icobench.items import *
from icobench.model.scrapy import *


class IcobenchSpider(scrapy.Spider):
    name = 'icobench_spider'
    root_path = ""
    print('root_path:' + root_path)

    def start_requests(self):

        model = 2
        if model == 1:
            urls = [
                'https://icobench.com/icos?page=1'
            ]
            print('start_requests:' + 'start_requests')
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
        if model == 2:
            print('retry_requests:' + 'retry_requests')
            print("wired")
            current_path = os.path.abspath(__file__)
            # 获取当前文件的父目录
            father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
            self.root_path = os.path.dirname(father_path)
            filename = self.root_path + '/html/status.text'
            self.root_url = "https://icobench.com"
            m_list = []
            for key in range(1, 447):
                m_list.append(key)

            print(m_list)
            with open(filename, 'r') as f:
                line = f.readline().strip('\n').strip()
                while line != None and line != '':
                    print("line", line)
                    m_list.remove(int(line))
                    # m_list[int(line)-1]
                    line = f.readline().strip('\n').strip()

            print(m_list)
            for page_id in m_list:
                print('page_id:', page_id)
                page_url = self.root_url + "/icos?page=" + str(page_id)
                print(page_url)
                yield scrapy.Request(page_url, callback=self.ico_parse)
                # TimeUtil().sleep_random_extime()

    def retry_requests(self):
        print('retry_requests_aaa:')
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        root_path = os.path.dirname(father_path)
        filename = root_path + '/html/status.text'
        self.root_url = "https://icobench.com"
        m_list = []
        for key in range(1, 447):
            m_list.append(key)

        print(m_list)
        with open(filename, 'r') as f:
            line = f.readline().strip('\n').strip()
            while line != None and line != '':
                print("line", line)
                m_list.remove(int(line))
                # m_list[int(line)-1]
                line = f.readline().strip('\n').strip()

        print(m_list)
        for page_id in m_list:
            print('page_id:', page_id)
            page_url = self.root_url + "/icos?page=" + str(page_id)
            print(page_url)
            yield scrapy.Request(page_url, callback=self.ico_parse)
            TimeUtil().sleep_random_extime()

    # https://icobench.com/ico/somesing
    # https://icobench.com/images/icos/icons/somesing.jpg
    def parse(self, response):
        print('parse:' + 'parse')
        self.root_url = "https://icobench.com"

        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        self.root_path = os.path.dirname(father_path)
        print('当前目录:' + current_path)
        print('当前父目录:' + father_path)
        print('root目录:' + self.root_path)

        pages = response.xpath("//*[@id='category']/div/div[2]/div[3]/div/a")

        page_size = int(pages[len(pages) - 2].xpath("text()").extract()[0])
        print("page_size:", page_size)
        print("url:", response.url)
        self.ico_parse(response)

        # https://icobench.com/icos?page=1
        for page_id in range(2, page_size + 1):
            page_url = self.root_url + "/icos?page=" + str(page_id)
            print(page_url)
            yield scrapy.Request(page_url, callback=self.ico_parse)
            TimeUtil().sleep_random_extime()

    def ico_parse(self, response):
        print("ico_parse:", "ico_parse")

        url = response.url
        page_id = url.split('=')[1]
        filename = self.root_path + '/html/' + page_id + ".html"

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        ico_list = response.xpath("//td[@class='ico_data']")
        print("ico_list:", ico_list)
        for ico_data in ico_list:
            # 子页面连接
            page_href = self.root_url + ico_data.xpath("div[@class='image_box']/a/@href").extract()[0].strip()
            # 图标
            icon_url = self.root_url + ico_data.xpath("div[@class='image_box']/a/@style").extract()[0].split('\'')[
                1].strip()
            # 项目名
            project_name = ico_data.xpath("div[@class='content']/a/text()").extract()[0].strip()
            project = ico_data.xpath("div[@class='content']/p/text()").extract()
            print("project", project)
            # 项目简介
            project_detail = project[0].strip()
            # 定义变量
            project_kyc_value = 0
            project_whitelist_value = 0
            project_countries = ''
            if len(project) > 1:
                # 是否存在kyc
                project_kyc = project[1].strip()
                if project_kyc == 'Yes':
                    project_kyc_value = 1
                print("project_kyc:", project_kyc)
            if len(project) > 3:
                # 是否存在白名单
                project_whitelist = project[3].strip()
                if project_whitelist == 'Yes':
                    project_whitelist_value = 1
                print("project_whitelist:", project_whitelist)
            if len(project) > 5:
                # 限制的国家
                project_countries = project[5].strip()
                print("project_countries:", project_countries)
            # ico开始时间
            start_time = ico_data.xpath("div[@class='shw']//div[@class='row']/text()").extract()[0].strip()
            # ico结束时间
            end_time = ico_data.xpath("div[@class='shw']//div[@class='row']/text()").extract()[1].strip()
            # 项目评分
            rate = ico_data.xpath("div[@class='shw']//div[@class='row']//div/text()").extract()[0].strip()

            print("page_href:", page_href)
            print("icon_url:", icon_url)
            print("project_name:", project_name)
            print("project_detail:", project_detail)
            print("start_time:", start_time)
            print("end_time:", end_time)
            print("rate:", rate)

            # 将数据存到数据库里
            scrapy_project_list_model = ScrapyProjectListModel(
                name=project_name,
                page_href=page_href,
                logo=icon_url,
                detail_desc=project_detail,
                kyc=project_kyc_value,
                white_list=project_whitelist_value,
                limit_countries=project_countries,
                start_time=start_time,
                end_time=end_time,
                score=rate
            )
            ScrapyProjectListModel().update_model(scrapy_project_list_model)
            # 关闭数据库
            scrapy_db.close()
            print("ScrapyProjectListModel", ScrapyProjectListModel.name)

        status_name = self.root_path + "/html/status.text"
        with open(status_name, 'a') as f:
            f.write(page_id + "\n")
        self.log('Saved page_id %s' % page_id)

        # yield scrapy.Request(page_href, callback=self.detail_parse)
        # TimeUtil().sleep_random_extime()

    def detail_parse(self, response):
        project_name = response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[2]/h1/text()").extract()[
            0].strip()
        print("project_name:", project_name)

        root_url = "https://icobench.com"
        filename = self.root_path + '/html/' + project_name + '.html'

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # 宣传语
        # project_slogan = response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[2]/h2/text()").extract()[0]
        # print(project_slogan)
        # # 简介
        # detail_excerpt = response.xpath("//*[@id='profile_header']/div/div[1]/p/text()").extract()[0]
        # # 行业标签
        # industry_list = response.xpath("//*[@id='profile_header']/div/div[1]/div[2]/a/text()")
        # industry=""
        # for ind in industry_list:
        #     industry=industry+","+ ind
        # # 视频
        # video = response.xpath("//*[@id='profile_header']/div/div[1]/div[3]/@onclick").extract()[0].split('\'')[1]
        # # 白皮书
        # white_paper = response.xpath("//*[@id='profile_content']/div/div[1]/div[1]/div/a[6]/@href").extract()[0]
        # # 详细介绍
        # detail_desc = response.xpath("//*[@id='about']/p/text()")
        #
        # ico=IcobenchItem()
        # ico['project_name']=project_name
        # ico['project_slogan'] = project_slogan
        # ico['detail_excerpt'] = detail_excerpt
        # ico['industry'] = industry
        # ico['white_paper'] = white_paper
        # ico['detail_desc'] = detail_desc
        # ico['video'] = video
        #
        #
        # print(ico)

        # icobench = IcoItem()
        #
        # ico_list_key = response.xpath("//*[@id='profile_header']/div/div[2]/div[3]/div/div[1]/text()")
        # ico_list_value = response.xpath("//*[@id='profile_header']/div/div[2]/div[3]/div/div[2]/b/text()")
        #
        # for list1,list2 in zip(ico_list_key,ico_list_value):
        #     list1 = list1.strip()
        #     list2 = list2.strip()
        #     list1=list1.replace(' ','_')
        #     print(list1)
        #     if list1 in icobench:
        #         icobench[list1]=list2
        # print(icobench)

        # financial_key = response.xpath("//*[@id='financial']/div/div/div[@class='row']/div[1]")
        # financial_value = response.xpath("//*[@id='financial']/div/div/div[@class='row']/div[2]")


if __name__ == '__main__':
    # 初始化服务
    # service = IcobenchSpider()
    # print('service:', service)
    # service.start_requests()
    # print('service:', '结束')

    def create_tables():
        with scrapy_db:
            scrapy_db.create_tables([ScrapyProjectListModel])


    create_tables()

    m_dict = {}
    for key in range(1, 447):
        m_dict[str(key)] = key

    print(m_dict)
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    root_path = os.path.dirname(father_path)
    filename = root_path + '/html/status.text'
    # with open(filename, 'r') as f:
    #     line = f.readline().strip('\n').strip()
    #     while line != None and line != '' :
    #         print("line",line)
    #         m_dict.pop(line)
    #         line = f.readline().strip('\n').strip()
    #
    #     print(m_dict)
    #
    #     keys = m_dict.keys()
    #     for index in keys:
    #         print(index)

    m_list = []
    for key in range(1, 447):
        m_list.append(key)

    print(m_list)
    with open(filename, 'r') as f:
        line = f.readline().strip('\n').strip()
        while line != None and line != '':
            print("line", line)
            m_list.remove(int(line))
            # m_list[int(line)-1]
            line = f.readline().strip('\n').strip()

    print(m_list)
    for index in m_list:
        print(index)
