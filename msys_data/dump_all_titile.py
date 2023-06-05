import requests
import re
import random
import uaList

class DumpAllTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            '__finger': '26bb9371cd9266cac533d4f42f1fd18c',
        }

        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': '__finger=26bb9371cd9266cac533d4f42f1fd18c',
            'Referer': 'https://wenda.familydoctor.com.cn/question/all/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        with open("href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                department_info = re.compile('<a href="/question(.*?)</a>', re.S).findall(text_line)[0]
                text_url = 'https://www.miaoshou.net/question' + department_info.split('"  >')[0]
                one_department = department_info.split('"  >')[1]

                print(text_url)
                self.getTwoDepartmentList(text_url, one_department)


    def getTwoDepartmentList(self, text_url, one_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )
        # print(response.text)

        # 二级科室：</span>
        # <div class="fl fenlei_rbox">
        #     <a href="/question/list_1_0_1.html" class="on" >全部</a>
        #     <a href="/question/list_1_312_1.html"  >职业病科</a>
        #         <a href="/question/list_1_42_1.html"  >神经内科</a>
        #         <a href="/question/list_1_41_1.html"  >消化内科</a>
        #         <a href="/question/list_1_40_1.html"  >内分泌科</a>
        #         <a href="/question/list_1_39_1.html"  >风湿免疫科</a>
        #         <a href="/question/list_1_38_1.html"  >呼吸内科</a>
        #         <a href="/question/list_1_37_1.html"  >肾内科</a>
        #         <a href="/question/list_1_36_1.html"  >血液科</a>
        #         <a href="/question/list_1_35_1.html"  >感染科</a>
        #         <a href="/question/list_1_33_1.html"  >老年病科</a>
        #         <a href="/question/list_1_32_1.html"  >普通内科</a>
        #         <a href="/question/list_1_31_1.html"  >心血管内科</a>
        #         <a href="/question/list_1_1_1.html"  >内科</a>
        # </div>
        try:
            two_department_info = re.compile('二级科室：</span>(.*?)</div>', re.S).findall(response.text)[0]
            # print(two_department_info)

            #<a href="/question/list_1_312_1.html"  >职业病科</a>
            #<a href="(.*?)</a>
            two_href = re.compile('<a href=\"(.*?)</a>', re.S).findall(two_department_info)
            # print(two_href)
            for two_href_item in two_href:
                if '全部' not in two_href_item:
                    two_department_href = two_href_item.split('"  >')[0]
                    two_department = two_href_item.split('"  >')[1]
                    line_Line = one_department + ' => ' + two_department + ' => https://www.miaoshou.net' + two_department_href
                    self.write2File('two_href_0.txt', line_Line + '\n')
        except Exception as e:
            line_Line = one_department + ' => ' + one_department + ' => ' + text_url
            self.write2File('two_href_0.txt', line_Line + '\n')
            print(e)


        # https://www.miaoshou.net/question/list_1_0_1_1.html

        # https://www.miaoshou.net/question/list_18_155_1_1.html


    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()