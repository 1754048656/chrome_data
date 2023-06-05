import time

import requests
import re
import random
import uaList

class DumpAllTitle:
    def __init__(self):
        self.nameList = []
        self.num = 0
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

        self.base_url = 'https://www.miaoshou.net'

        with open("two_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()

                # print(text_line)
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                text_url = text_line.split(' => ')[2]

                # print(text_url)
                one_t = text_url.split('_')[1]
                two_t = text_url.split('_')[2]
                print(one_t + '_' + two_t)
                self.num = 0
                for i in range(1, 500):
                    url_base = 'https://www.miaoshou.net/question/list_' + one_t + '_' + two_t + '_1' + '_' + str(i) + '.html'
                    print(url_base)
                    res = self.getTwoDepartmentList(url_base, one_department, two_department)
                    if res == 'n':
                        print('跳过，下一个')
                        break
                    # time.sleep(1)


    def getTwoDepartmentList(self, text_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )
        # print(response.text)

        #<p class="mb15">
        # <a href="/question/YqxrB378eQmge6R8.html" target="_blank">
        try:
            qa_href_info = re.compile('<p class="mb15">(.*?)" target="_blank">', re.S).findall(response.text)
            # print(qa_href_info)
            if len(qa_href_info) == 0:
                print('没有了')
                return 'n'
            for qa_href_info_item in qa_href_info:

                json_line = {}
                qa_href_info_item = qa_href_info_item.strip()
                qa_href_info_item = self.base_url + qa_href_info_item.replace('<a href="', '')

                if qa_href_info_item in self.nameList:
                    print('重复加一')
                    self.num = self.num + 1
                    if self.num > 4:
                        return 'n'
                    return 'y'
                self.nameList.append(qa_href_info_item)
                json_line['one_department'] = one_department
                json_line['two_department'] = two_department
                json_line['qa_href'] = qa_href_info_item
                print(json_line)
                self.write2File('qa_href.txt', str(json_line).replace('\'', '\"') + '\n')

        except Exception as e:
            print(e)

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()