import json
import time

import requests
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
        self.baseUrl = 'https://www.yaofangwang.com'
        self.cookies = {
            'real_ip': '114.248.124.120',
            'HMF_CI': '3f8441885ce9e6e1e5458fac19655fca20e721ff20ff100dbe7f45e294db66356b39be53550ae932fead7a22d18247429c0f965541bf3b97d5e2906e66acec2fea',
            'Hm_lvt_e5f454eb1aa8e839f8845470af4667eb': '1686205729',
            'isContact': '0',
            'Hm_lpvt_e5f454eb1aa8e839f8845470af4667eb': '1686209995',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'real_ip=114.248.124.120; HMF_CI=3f8441885ce9e6e1e5458fac19655fca20e721ff20ff100dbe7f45e294db66356b39be53550ae932fead7a22d18247429c0f965541bf3b97d5e2906e66acec2fea; Hm_lvt_e5f454eb1aa8e839f8845470af4667eb=1686205729; isContact=0; Hm_lpvt_e5f454eb1aa8e839f8845470af4667eb=1686209995',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        file = open("res.txt", "r", encoding="utf-8")
        data = file.read()
        #<span class="fll si-list-title-word"></div>
        data_list = re.compile('<span class="fll si-list-title-word">(.*?)</div>', re.S).findall(data)
        for data_list_item in data_list:
            data_list_item = data_list_item.strip()
            # print(data_list_item)
            one_department = data_list_item.split('</span>')[0]

            #<a href="(.*?)</a>
            #https://www.bohe.cn/ask/list-217.html" target="_blank">男科
            two_department_info = re.compile('<a href="(.*?)</a>', re.S).findall(data_list_item)
            for two_department_info_item in two_department_info:
                two_de_url = two_department_info_item.split('" target="_blank">')[0]
                two_department = two_department_info_item.split('" target="_blank">')[1]
                print(one_department)
                print(two_de_url)
                print(two_department)
                one_line = one_department + ' => ' + two_department + ' => ' + two_de_url + '\n'
                self.write2File('bohe_url.txt', one_line)
            print('-------------------------------')


    def getTwoDepartmentList(self, med_url, department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(med_url, cookies=self.cookies, headers=self.headers)
        res_text = response.text

        # <h1>很抱歉，无法找到该页面！</h1>
        if '<h1>很抱歉，无法找到该页面！</h1>' in res_text:
            return '-1'

        #<a style="float:left;margin-bottom:7px" title="断血流片的功效与作用" href="/yongyao/2025786.shtml" class="title"
        title_info = re.compile('<a style="float:left;margin-bottom:7px" title="(.*?)" class="title"').findall(res_text)
        for title_info_item in title_info:
            # print('title_info_item => ' + title_info_item)
            title = title_info_item.split('" href="')[0]
            title_url = title_info_item.split('" href="')[1]

            json_line = {}
            json_line['department'] = department
            json_line['title'] = title
            json_line['title_url'] = title_url

            json_text = json.dumps(json_line, ensure_ascii=False)
            print(json_text)
            self.write2File('a_yfw_title.txt', json_text + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()