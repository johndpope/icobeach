import scrapy
import os
from icobench.util import *
from icobench.items import *
from icobench.model.scrapy import *
import time


class IcobenchDetailSpider(scrapy.Spider):
    name = 'icobench_detail_spider'
    root_path = ""
    print('root_path:' + root_path)

    def start_requests(self):

        model = 1
        if model == 1:
            # 踩多条数据
            # scrapyProjectLists = ScrapyProjectListModel().get_list()
            # for scrapyProjectList in scrapyProjectLists:
            #     page_href = scrapyProjectList.page_href
            #     print('page_href:' + page_href)
            #     print('start_time:' + '111')
            #     yield scrapy.Request(url=page_href, callback=self.detail_parse, meta={"scrapyProjectListId": scrapyProjectList.id})
            #     # 关闭数据库
            #     scrapy_db.close()
            #     print('start_time:' + '关闭数据库')
            #     time.sleep(30)

            # 踩一条数据
            scrapyProjectList = ScrapyProjectListModel().get_by_id(53)
            page_href = scrapyProjectList.page_href
            print('page_href:' + page_href)
            yield scrapy.Request(url=page_href, callback=self.detail_parse,
                                 meta={"scrapyProjectListId": scrapyProjectList.id})
            # 关闭数据库
            scrapy_db.close()
        if model == 2:
            print('retry_requests:' + 'retry_requests')
            print("wired")
            current_path = os.path.abspath(__file__)
            # 获取当前文件的父目录
            father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
            self.root_path = os.path.dirname(father_path)
            filename = self.root_path + '/html/details/status.text'
            m_list = []
            scrapyProjectListCount = ScrapyProjectListModel().get_count()
            for key in range(1, scrapyProjectListCount):
                m_list.append(key)
                # 关闭数据库
                scrapy_db.close()
            print(m_list)
            with open(filename, 'r') as f:
                line = f.readline().strip('\n').strip()
                while line != None and line != '':
                    print("line", line)
                    m_list.remove(int(line))
                    # m_list[int(line)-1]
                    line = f.readline().strip('\n').strip()

            print(m_list)
            for project_list_id in m_list:
                print('project_list_id:', project_list_id)
                project_list = ScrapyProjectListModel().get_by_id(project_list_id)
                if project_list is not None:
                    page_url = project_list.page_href
                    print(page_url)
                    yield scrapy.Request(url=page_url, callback=self.detail_parse,
                                        meta={"scrapyProjectListId": project_list_id})
                # 关闭数据库
                scrapy_db.close()

    def detail_parse(self, response):
        meta_data = response.meta
        print('meta_data:' + str(meta_data))
        scrapyProjectList_id = 0
        if "scrapyProjectListId" in meta_data.keys():
            scrapyProjectList_id = response.meta['scrapyProjectListId']
        print('scrapyProjectList_id:' + str(scrapyProjectList_id))
        print('detail_parse:' + 'detail_parse')
        # 项目名称
        project_name_div = response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[2]/h1")
        project_name = ''
        if project_name_div != '[]':
            project_name = response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[2]/h1/text()").extract()[
                0].strip()
        else:
            project_name = response.xpath("// *[ @ id = 'profile_header']/div/div[2]/div[1]/div[2]/h1/text()").extract()[
                0].strip()

        print("project_name:", project_name)
        # 存储文件相关
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        self.root_path = os.path.dirname(father_path)
        print('当前目录:' + current_path)
        print('当前父目录:' + father_path)
        print('root目录:' + self.root_path)
        root_url = "https://icobench.com"
        filename = self.root_path + '/html/details/' + project_name + '.html'
        # 将踩到的html放到指定文件下面
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # 宣传语
        slogan = response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[2]/h2/text()").extract()[0].strip()
        print('slogan:', slogan)
        # logo
        logo = root_url + response.xpath("//*[@id='profile_header']/div/div[1]/div[1]/div[1]/img/@src").extract()[
            0].strip()
        print('logo:', logo)
        # 官网
        # homepage = response.xpath("//*[@id='profile_header']/div/div[2]/div[5]/a[8]/@href").extract()[0].strip()
        # # // *[ @ id = "profile_header"] / div / div[2] / div[5]
        # print('homepage:', homepage)
        # 白皮书
        white_paper_div = response.xpath("//*[@id='profile_content']/div/div[1]/div[2]/div/a")
        print('white_paper_div:', white_paper_div)
        # 计算白皮书div下有多少个a标签
        white_paper_div_len = int(len(white_paper_div))
        print('white_paper_div_len:', white_paper_div_len)
        white_paper = root_url + response.xpath(
            "//*[@id='profile_content']/div/div[1]/div[2]/div/a[" + str(white_paper_div_len) + "]/@href").extract()[0]
        print('white_paper:', white_paper)
        # 视频链接
        video = ''
        video_div = response.xpath("//*[@id='profile_header']/div/div[1]/div[3]")
        print('video_div:', video_div)
        if video_div != '[]':
            video = response.xpath("//*[@id='profile_header']/div/div[1]/div[3]/@onclick").extract()[0].split('\'')[1]

        # 行业标签
        industry_div = response.xpath("//*[@id='profile_header']/div/div[1]/div[2]/a")
        print('industry_div:', industry_div)
        industry_div_len = int(len(industry_div))
        print('industry_div_len:', industry_div_len)
        industry = ''
        for industry_len_num in range(1, industry_div_len + 1):
            print('industry_len_num:', industry_len_num)
            industry = industry + response.xpath("// *[ @ id = 'profile_header'] / div / div[1] / div[2] / a[" + str(
                industry_len_num) + "]/text()").extract()[0] + ','
        print('industry:', industry)
        # 简介
        detail_excerpt = response.xpath("//*[@id='profile_header']/div/div[1]/p/text()").extract()[0].strip()
        print('detail_excerpt:', detail_excerpt)
        # 详细介绍
        detail_desc = response.xpath("//*[@id='about']").extract()[0].strip()
        print('detail_desc:', detail_desc)
        # 软顶
        # 抓(Investment info)div
        ico_investment_info_div = response.xpath("//*[@id='financial']/div/div[2]/div")
        print('ico_investment_info_div:', ico_investment_info_div)
        # 计算(Investment info)中有多少个div
        ico_investment_info_div_len = int(len(ico_investment_info_div))
        print('ico_investment_info_div_len:', ico_investment_info_div_len)
        ico_distributed_in = 0
        # 软顶
        ico_soft_cap = ''
        # 硬顶
        ico_hard_cap = ''
        # 销售百分比
        ico_circulating_supply = ''
        # 接受币种
        ico_accepting = ''
        if ico_investment_info_div_len > 1:
            # 循环抓取
            for ico_investment_info_div_len_num in range(2, ico_investment_info_div_len):
                print('ico_investment_info_div_len_num:', ico_investment_info_div_len_num)
                # 抓取divider  class
                divider_class = response.xpath(
                    "//*[@id='financial']/div/div[2]/div[" + str(
                        ico_investment_info_div_len_num) + "]/@class").extract()[0]
                if divider_class != 'divider':
                    # 抓取div中的名字
                    ico_div_name = response.xpath(
                        "//*[@id='financial']/div/div[2]/div[" + str(
                            ico_investment_info_div_len_num) + "]/div[1]/text()").extract()[
                        0].strip()
                    print('ico_div_name:', ico_div_name)
                    # 判断抓取到的名字是否为Soft cap，是抓取名字对应的值   软顶
                    if ico_div_name == 'Soft cap':
                        ico_soft_cap = response.xpath("//*[@id='financial']/div/div[2]/div[" + str(
                            ico_investment_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_soft_cap:', ico_soft_cap)
                    # 判断抓取到的名字是否为Hard cap，是抓取名字对应的值   硬顶
                    if ico_div_name == 'Hard cap':
                        ico_hard_cap = response.xpath("//*[@id='financial']/div/div[2]/div[" + str(
                            ico_investment_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_hard_cap:', ico_hard_cap)
                    # 判断抓取到的名字是否为Distributed in ICO，是抓取名字对应的值    销售百分比
                    if ico_div_name == 'Distributed in ICO':
                        ico_circulating_supply = response.xpath("//*[@id='financial']/div/div[2]/div[" + str(
                            ico_investment_info_div_len_num) + "]/div[2]/text()").extract()[0].strip()
                        ico_circulating_supply = float(ico_circulating_supply.strip('%').replace(',', ''))  # 去掉s 字符串中的 %
                        print('ico_circulating_supply:', ico_circulating_supply)
                        # 变成小数
                        ico_distributed_in = ico_circulating_supply / 100.0
                        print('ico_distributed_in:', ico_distributed_in)
                    # 判断抓取到的名字是否为Accepting，是抓取名字对应的值  接受币种
                    if ico_div_name == 'Accepting':
                        ico_accepting = response.xpath("//*[@id='financial']/div/div[2]/div[" + str(
                            ico_investment_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_accepting:', ico_accepting)

        # 判断预售开始时间是否存在
        ico_preico_date_label_value = response.xpath("//*[@id='profile_header']/div/div[2]/div[4]/div[1]/div/label")
        print('ico_preico_date_label_value:', ico_preico_date_label_value)
        if ico_preico_date_label_value != []:
            ico_preico_date_label = \
                response.xpath("//*[@id='profile_header']/div/div[2]/div[4]/div[1]/div/label/text()").extract()[
                    0].strip()
        else:
            ico_preico_date_label = ''
        # 预售开始时间
        ico_preico_start_date = ''
        # 预售结束时间
        ico_preico_end_date = ''
        if ico_preico_date_label == 'PreICO time':
            # 预售开始时间
            ico_preico_date = \
                response.xpath("//*[@id='profile_header']/div/div[2]/div[4]/div[1]/div/small/text()").extract()[
                    0].strip()
            ico_preico_date = ico_preico_date.split(" - ")
            print('ico_preico_date:', ico_preico_date)
            # 预售开始时间
            ico_preico_start_date = ico_preico_date[0]
            print('ico_preico_start_date:', ico_preico_start_date)
            # 预售结束时间
            ico_preico_end_date = ico_preico_date[1]
            print('ico_preico_end_date:', ico_preico_end_date)

        # 代币总量  ico_token_supply=Tokens for sale/Distributed in ICO 即销售代币数/销售百分比
        tokens_for_sale = 0;
        # 计算(Token info)中有多少个div
        ico_token_info_div = response.xpath("// *[ @ id = 'financial'] / div / div[1]/div")
        ico_token_info_div_len = int(len(ico_token_info_div))
        print('ico_token_info_div_len:', ico_token_info_div_len)
        # 代币符号
        ico_symbol = ''
        # 平台
        ico_platform = ''
        # 类型
        ico_type = ''
        # 初始价格
        ico_initial_price = ''
        # 预售价格
        ico_preico_price = ''
        if ico_token_info_div_len > 1:
            # 循环抓取
            for ico_token_info_div_len_num in range(2, ico_token_info_div_len):
                print('ico_token_info_div_len_num:', ico_token_info_div_len_num)
                # 抓取div中的名字
                ico_token_info_div_name = response.xpath(
                    "//*[@id='financial']/div/div[1]/div[" + str(
                        ico_token_info_div_len_num) + "]/div[1]/text()")
                print('ico_token_info_div_name_div:', ico_token_info_div_name)
                # 判断div中的值不是空
                if ico_token_info_div_name != []:
                    ico_token_info_div_name = ico_token_info_div_name.extract()[0].strip()
                    print('ico_token_info_div_name:', ico_token_info_div_name)
                    # 判断抓取到的名字是否为Platform，是抓取名字对应的值  代币符号
                    if ico_token_info_div_name == 'Token':
                        # 代币符号
                        ico_symbol = response.xpath("//*[@id='financial']/div[1]/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_symbol:', ico_symbol)
                    # 判断抓取到的名字是否为Platform，是抓取名字对应的值  平台
                    if ico_token_info_div_name == 'Platform':
                        ico_platform = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_platform:', ico_platform)
                    # 判断抓取到的名字是否为Type，是抓取名字对应的值  类型
                    if ico_token_info_div_name == 'Type':
                        ico_type = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_type:', ico_type)
                    # 判断抓取到的名字是否为Price in ICO，是抓取名字对应的值  初始价格
                    if ico_token_info_div_name == 'Price in ICO':
                        # 初始价格  =public_price
                        ico_initial_price = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_initial_price:', ico_initial_price)
                    # 判断抓取到的名字是否为Pirce，是抓取名字对应的值  初始价格
                    if ico_token_info_div_name == 'Pirce':
                        # 初始价格  =public_price
                        ico_initial_price = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_initial_price:', ico_initial_price)
                    # 判断抓取到的名字是否为Tokens for sale，是抓取名字对应的值  销售代币数
                    if ico_token_info_div_name == 'Tokens for sale':
                        # 销售代币数   =Tokens for sale/Distributed in ICO 即销售代币数/销售百分比
                        tokens_for_sale = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('tokens_for_sale:', tokens_for_sale)
                    # 判断抓取到的名字是否为PreICO price，是抓取名字对应的值  预售价格
                    if ico_token_info_div_name == 'PreICO price':
                        ico_preico_price = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_preico_price:', ico_preico_price)
                    # 判断抓取到的名字是否为Price_in_preICO，是抓取名字对应的值  预售价格
                    if ico_token_info_div_name == 'Price_in_preICO':
                        ico_preico_price = response.xpath("//*[@id='financial']/div/div[1]/div[" + str(
                            ico_token_info_div_len_num) + "]/div[2]/text()").extract()[
                            0].strip()
                        print('ico_preico_price:', ico_preico_price)
        # 代币总量
        if ico_distributed_in == 0:
            ico_token_supply = 0
        else:
            if tokens_for_sale == 0:
                ico_token_supply = 0
            else:
                ico_token_supply = int(tokens_for_sale.replace(',', '')) / ico_distributed_in
        print('ico_token_supply:', ico_token_supply)

        # 判断公募开始时间是否存在
        # 公募开始时间
        ico_public_start_date = ''
        # 公募结束时间
        ico_public_end_date = ''
        for ico_public_date_len_num in range(1, 3):
            print('ico_public_date_len_num:', ico_public_date_len_num)
            ico_public_date_label = response.xpath(
                "//*[@id='profile_header']/div/div[2]/div[4]/div[" + str(
                    ico_public_date_len_num) + "]/div/label")
            if ico_public_date_label != []:
                ico_public_date_label_value = response.xpath(
                    "//*[@id='profile_header']/div/div[2]/div[4]/div[" + str(
                        ico_public_date_len_num) + "]/div/label/text()").extract()[
                    0].strip()
            else:
                ico_public_date_label_value = ''
            if ico_public_date_label_value == 'ICO Time':
                # 公募开始时间
                ico_public_date = response.xpath(
                    "//*[@id='profile_header']/div/div[2]/div[4]/div[" + str(
                        ico_public_date_len_num) + "]/div/small/text()").extract()[
                    0].strip()
                ico_public_date = ico_public_date.split(" - ")
                print('ico_public_date:', ico_public_date)
                # 公募开始时间
                ico_public_start_date = ico_public_date[0]
                print('ico_public_start_date:', ico_public_start_date)
                # 公募结束时间
                ico_public_end_date = ico_public_date[1]
                print('ico_public_end_date:', ico_public_end_date)
            break

        # 官方媒体
        media_len_a = response.xpath("//*[@id='profile_header']/div/div[2]/div[5]/a")
        media_len = int(len(media_len_a))
        print('media_len:', media_len)
        media_name = ''
        media_link = ''
        homepage = ''
        # 定义一个媒体字典
        media_dict = {}
        for media_len_num in range(1, media_len + 1):
            print('media_len_num:', media_len_num)
            media_name = media_name + response.xpath("//*[@id='profile_header']/div/div[2]/div[5]/a[" + str(
                media_len_num) + "]/text()").extract()[0].strip() + ','
            print('media_name:', media_name)
            media_link = media_link + response.xpath("//*[@id='profile_header']/div/div[2]/div[5]/a[" + str(
                media_len_num) + "]/@href").extract()[0] + ','
            media_dict[media_name] = media_link
            print('media_link:', media_link)
            # 官网
            if media_name == 'WWW':
                homepage = response.xpath(
                    "//*[@id='profile_header']/div/div[2]/div[5]/a[" + str(media_len_num) + "]/@href").extract()[
                    0].strip()
                print('homepage:', homepage)
        print('media_dict:', media_dict)

        # 团队信息
        team_h3 = response.xpath("// *[ @ id = 'team'] / h3")
        team_h3_len = int(len(team_h3))
        # 定义一个团队字典
        team_dict = {}
        print('team_h3_len:', team_h3_len)
        if team_h3_len == 1:
            # 团队信息
            team_len_div = response.xpath("//*[@id='team']/div[1]/div")
            team_len = int(len(team_len_div))
            print('team_len:', team_len)
            for team_len_num in range(1, team_len + 1):
                print('team_len_num:', team_len_num)
                # 抓取头像
                team_avatar = response.xpath("//*[@id='team']/div[1]/div[" + str(
                    team_len_num) + "]/a/div/@style").extract()[0]
                # 截取头像中的连接
                team_avatar = root_url + team_avatar.split("('")[1].split("')")[0]
                print('team_avatar:', team_avatar)
                # 获取名字
                team_name = response.xpath("//*[@id='team']/div[1]/div[" + str(
                    team_len_num) + "]/h3/text()").extract()[0].strip()
                print('team_name:', team_name)
                # 职位
                team_title_div = response.xpath("//*[@id='team']/div[1]/div[" + str(
                    team_len_num) + "]/h4")
                # 获取长度
                team_title_div_len = int(len(team_title_div))
                team_title = ''
                if team_title_div_len != 0:
                    team_title = response.xpath("//*[@id='team']/div[1]/div[" + str(
                        team_len_num) + "]/h4/text()").extract()[0].strip()
                    print('team_title:', team_title)
                # 社交媒体
                team_socials_div = response.xpath("//*[@id='team']/div[1]/div[" + str(
                    team_len_num) + "]/div/a")
                # // *[ @ id = "team"] / div[1] / div[6] / div
                # 获取长度
                team_socials_div_len = int(len(team_socials_div))
                team_socials = ''
                if team_socials_div_len != 0:
                    team_socials = response.xpath("//*[@id='team']/div[1]/div[" + str(
                        team_len_num) + "]/div/a/@href").extract()[0]
                    print('team_socials:', team_socials)
                team_dict[team_name] = team_name
                team_dict[team_name + '_avatar'] = team_avatar
                team_dict[team_name + '_title'] = team_title
                team_dict[team_name + '_socials'] = team_socials
        else:
            for team_h3_len_num in range(1, team_h3_len + 1):
                print('team_h3_len_num:', team_h3_len_num)
                team_h3_value = response.xpath("// *[ @id='team']/h3[" + str(team_h3_len_num) + "]/text()").extract()[
                    0].strip()
                print('team_h3_value:', team_h3_value)
                # 如果抓到的值为Team，对该div下的内容进行抓取
                if team_h3_value == 'Team':
                    # 团队信息
                    team_len_div = response.xpath("//*[@id='team']/div[" + str(team_h3_len_num) + "]/div")
                    team_len = int(len(team_len_div))
                    print('team_len:', team_len)
                    for team_len_num in range(1, team_len + 1):
                        print('team_len_num:', team_len_num)
                        # 抓取头像
                        team_avatar = response.xpath("//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                            team_len_num) + "]/a/div/@style").extract()[0]
                        # 截取头像中的连接
                        team_avatar = root_url + team_avatar.split("('")[1].split("')")[0]
                        print('team_avatar:', team_avatar)
                        # 获取名字
                        team_name = response.xpath("//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                            team_len_num) + "]/h3/text()").extract()[0].strip()
                        print('team_name:', team_name)
                        # 职位
                        team_title = response.xpath("//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                            team_len_num) + "]/h4/text()").extract()[0].strip()
                        print('team_title:', team_title)
                        # 社交媒体
                        team_socials_div = response.xpath(
                            "//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                                team_len_num) + "]/div")
                        team_socials_div_len = int(len(team_socials_div))
                        # 定义社交媒体
                        team_socials = ''
                        if team_socials_div_len != 0:
                            team_socials_class = \
                                response.xpath("//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                                    team_len_num) + "]/div/@class").extract()[0]
                            print('team_socials_class:', team_socials_class)
                            if team_socials_class == 'socials':
                                team_socials = response.xpath(
                                    "//*[@id='team']/div[" + str(team_h3_len_num) + "]/div[" + str(
                                        team_len_num) + "]/div/a/@href").extract()[0]
                                print('team_socials:', team_socials)
                            else:
                                team_socials = ''
                                print('team_socials:', team_socials)
                        team_dict[team_name] = team_name
                        team_dict[team_name + '_avatar'] = team_avatar
                        team_dict[team_name + '_title'] = team_title
                        team_dict[team_name + '_socials'] = team_socials
        print('team_dict:', team_dict)

        # 线路
        # 线路下一共有多少个div
        roadmap_div = response.xpath("//*[@id='milestones']/div/div")
        roadmap_div_len = int(len(roadmap_div))
        print('roadmap_div_len:', roadmap_div_len)
        # 定义一个线路字典
        roadmap_dict = {}
        for roadmap_div_len_num in range(1, roadmap_div_len + 1):
            print('roadmap_div_len_num:', roadmap_div_len_num)
            # 时间
            roadmap_time = response.xpath(
                "// *[ @id='milestones']/div/div[" + str(roadmap_div_len_num) + "]/div[2]/div[2]/text()").extract()[
                0].strip()
            print('roadmap_time:', roadmap_time)
            # 目标
            roadmap_target = \
                response.xpath(
                    "//*[@id='milestones']/div/div[" + str(roadmap_div_len_num) + "]/div[2]/p/text()").extract()[
                    0].strip()
            print('roadmap_target:', roadmap_target)
            roadmap_dict[roadmap_time] = roadmap_target
        print('roadmap_dict:', roadmap_dict)

        # 将数据存到数据库里
        scrapy_project_detail_model = ScrapyProjectDetailModel(
            project_list_id=scrapyProjectList_id,
            name=project_name,  # 项目名称
            slogan=slogan,  # 宣传语
            logo=logo,  # logo
            homepage=homepage,  # 官网
            white_paper=white_paper,  # 白皮书
            video=video,  # 视频链接
            industry=industry,  # 行业标签
            detail_excerpt=detail_excerpt,  # 简介
            detail_desc=detail_desc,  # 详细介绍
            ico_soft_cap=ico_soft_cap,  # 软顶
            ico_hard_cap=ico_hard_cap,  # 硬顶
            ico_circulating_supply=ico_circulating_supply,  # 销售百分比
            ico_accepting=ico_accepting,  # 接受币种
            ico_preico_start_date=ico_preico_start_date,  # 预售开始时间
            ico_preico_end_date=ico_preico_end_date,  # 预售结束时间
            ico_token_supply=ico_token_supply,  # 代币总量
            ico_symbol=ico_symbol,  # 代币符号
            ico_platform=ico_platform,  # 平台
            ico_type=ico_type,  # 类型
            ico_initial_price=ico_initial_price,  # 初始价格
            ico_preico_price=ico_preico_price,  # 预售价格
            ico_public_start_date=ico_public_start_date,  # 公募开始时间
            ico_public_end_date=ico_public_end_date,  # 公募结束时间
            ico_public_price=ico_initial_price,  # 公募价格
            media=media_dict,  # 媒体
            team=team_dict,  # 团队
            roadmap=roadmap_dict,  # 路线
        )
        print('scrapy_project_detail_model:' + str(scrapy_project_detail_model))
        ScrapyProjectDetailModel().update_model(scrapy_project_detail_model)
        # 关闭数据库
        scrapy_db.close()
        print("ScrapyProjectListModel", ScrapyProjectListModel.name)
        print('start_time:' + '222')

        status_name = self.root_path + "/html/details/status.text"
        with open(status_name, 'a') as f:
            f.write(str(scrapyProjectList_id) + "\n")
        self.log('Saved page_id %s' % scrapyProjectList_id)


if __name__ == '__main__':
    def create_tables():
        with scrapy_db:
            scrapy_db.create_tables([ScrapyProjectDetailModel])


    create_tables()

    # 获取信息
    # scrapyProjectList = ScrapyProjectListModel().get_by_id('1')
    # page_href = scrapyProjectList.page_href
    # print('page_href:' + page_href)

    # ico_distributed_in = "20%"
    # ico_distributed_in = float(ico_distributed_in.strip('%'))  # 去掉s 字符串中的 %
    # ico_distributed_in = ico_distributed_in / 100.0
    # print('ico_distributed_in:', ico_distributed_in)
    # tokens_for_sale = "30,000,000,000"
    # ico_token_supply = int(tokens_for_sale.replace(',', '')) / ico_distributed_in
    # print('ico_token_supply:', ico_token_supply)
    #
    # ico_preico_date = '2019-02-18 - 2019-03-19'
    # ico_preico_date = ico_preico_date.split(" - ")
    # print('ico_preico_date:', ico_preico_date)
    # print('ico_preico_date:', ico_preico_date[0])

    # len_num = 1
    # for len_num in range(1, 3):
    #     print('len_num:', len_num)
    ico_circulating_supply = '9125%'
    demo = ico_circulating_supply.strip('%')
    print("111:"+ico_circulating_supply.strip('%'))
    print("2222:"+demo.replace(',', ''))
    ico_circulating_supply = float(demo.replace(',', ''))  # 去掉s 字符串中的 %