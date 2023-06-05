import json
import time

import requests
from urllib import parse
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            'XSRF-TOKEN': 'eyJpdiI6IlpkM3k1Yk1Remd3SkFza0RSaEVOTXc9PSIsInZhbHVlIjoiekErVGxWazJkcVowTVBRWmdJOHlBVGNMUGlHTFwvM0c1blwvY3hIVFJ0dUFGV0h0ZENSOGJkN3FzZitCYW52V0xiIiwibWFjIjoiMGY5ZTE3NGY3ZDY2YTNiZTZiZTlhNWFjZjcxNmI1ZmQwODE2OGI1N2IzZjQ4MTAzYjZlYzcyZGNhZjFjOWJkNSJ9',
            'laravel_session': 'eyJpdiI6IjBNU25abGlPbDYrWmFhXC9DTmtwdEpRPT0iLCJ2YWx1ZSI6Imw4N3NwTmtpQSs1MEdXTGc5NTQzcjA3MitJMmRJQm5ESmE1cnVlM1dxRDBreXR2b016dXh4dVA4bW8rZHBCQkQiLCJtYWMiOiIyYzlmOTU5M2I5MzY3MjI5ODMzOTcxZDEyZjJkODE2NDU1NTU5OTAxZTUwNGQwNmYwMzMyNWQ1ZjJhNGZhYjYxIn0%3D',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlpkM3k1Yk1Remd3SkFza0RSaEVOTXc9PSIsInZhbHVlIjoiekErVGxWazJkcVowTVBRWmdJOHlBVGNMUGlHTFwvM0c1blwvY3hIVFJ0dUFGV0h0ZENSOGJkN3FzZitCYW52V0xiIiwibWFjIjoiMGY5ZTE3NGY3ZDY2YTNiZTZiZTlhNWFjZjcxNmI1ZmQwODE2OGI1N2IzZjQ4MTAzYjZlYzcyZGNhZjFjOWJkNSJ9; laravel_session=eyJpdiI6IjBNU25abGlPbDYrWmFhXC9DTmtwdEpRPT0iLCJ2YWx1ZSI6Imw4N3NwTmtpQSs1MEdXTGc5NTQzcjA3MitJMmRJQm5ESmE1cnVlM1dxRDBreXR2b016dXh4dVA4bW8rZHBCQkQiLCJtYWMiOiIyYzlmOTU5M2I5MzY3MjI5ODMzOTcxZDEyZjJkODE2NDU1NTU5OTAxZTUwNGQwNmYwMzMyNWQ1ZjJhNGZhYjYxIn0%3D',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open("res.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)
                department = text_line.split(' => ')[0]
                test_url_tmp = text_line.split(' => ')[1]
                test_url = test_url_tmp.split('.html')[0]
                # test_url = test_url.strip('.')
                print('test_url_tmp => ' + test_url_tmp)

                # for i in range(30):
                #     try:
                #
                #         time.sleep(4)
                #         break
                #     except Exception as e:
                #         print(e)
                #     print('-----------wait-----------')
                #     time.sleep(12)
                self.getTwoDepartmentList(test_url, test_url_tmp, department)

    def getTwoDepartmentList(self, test_url, test_url_tmp, deparment):


        # response = requests.get(
        #     # 'http://www.dtqcw.net/disease/fubu/p1.html',
        #     test_url_tmp,
        #     cookies=self.cookies,
        #     headers=self.headers,
        #     verify=False,
        #     timeout=12
        # )
        #
        # time.sleep(1.5)
        # res_text = response.text
        #
        # page_info = re.compile('class="active">(.*?)aria-label="Next"', re.S).findall(res_text)[0]
        # # print('page_info => ' + page_info)
        # # <li><a href="(.*?)</a></li>
        # page_num_info = re.compile('<li><a href="(.*?)</a></li>', re.S).findall(page_info)
        # page_num = page_num_info[len(page_num_info) - 1]
        # page_num = page_num.split('">')[1]
        # print('page_num => ' + page_num)

        for t in range(1, 155):
            self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
            print('User-Agent => ' + self.headers['User-Agent'])

            page_url = test_url + '/p' + str(t) + '.html'

            res = ''
            for m in range(30):
                try:
                    res = self.getUrl(page_url, deparment)
                    time.sleep(4)
                    break
                except Exception as e:
                    print(e)
                print('-----------wait-----------')
                time.sleep(12)
            if res == '-1':
                print('没有了, 换下一个')
                break



    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

    def getUrl(self, page_url, department):
        response = requests.get(
            # 'http://www.dtqcw.net/disease/fubu/p1.html',
            page_url,
            cookies=self.cookies,
            headers=self.headers,
            verify=False,
            timeout=12
        )

        print('current_page_num => ' + page_url)

        res_info = response.text
        # print('res_info => ' + res_info)
        disease_info = re.compile('<ul class="disease_list">(.*?)</ul>', re.S).findall(res_info)[0]
        # print('disease_info => ' + disease_info)
        if 'title=' not in disease_info:
            return '-1'

        # <li><a href="(.*?)</a></li>
        disease_text_list = re.compile('<li><a href="(.*?)</a></li>', re.S).findall(disease_info)
        for disease_text_list_item in disease_text_list:
            # print('disease_text_list_item => ' + disease_text_list_item)
            disease_href = disease_text_list_item.split('" title="')[0]
            disease_name = disease_text_list_item.split('" title="')[1]
            disease_name = disease_name.split('">')[1]

            json_tmp = {}
            json_tmp['department'] = department
            json_tmp['disease'] = disease_name
            json_tmp['disease_href'] = disease_href

            print('disease_href => ' + disease_href)
            print('disease_name => ' + disease_name)

            self.write2File('gyc_href.txt', json.dumps(json_tmp, ensure_ascii=False) + '\n')
        time.sleep(3)
        pass





DumpTitle()