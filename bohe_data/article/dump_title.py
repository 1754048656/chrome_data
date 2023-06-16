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
        self.tmp_list = []
        self.tmp_num = 0

        with open("res.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                tmp_url = text_line.split(' => ')[0]
                one_department = text_line.split(' => ')[1]

                self.getTwoDepartmentList(tmp_url, one_department)


    def getTwoDepartmentList(self, tmp_url, one_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(tmp_url, cookies=self.cookies, headers=self.headers)
        res_text = response.text

        #全部</a>
        disease_info = re.compile('全部</a>(.*?)</div>', re.S).findall(res_text)[0]
        disease_list = re.compile('<a href="(.*?)</a>', re.S).findall(disease_info)
        for disease_list_item in disease_list:
            # print(disease_list_item)
            disease_url = disease_list_item.split('" class=""> ')[0]
            disease_name = disease_list_item.split('" class=""> ')[1]
            print(disease_name)
            print(disease_url)

            # json_line = {}
            # json_line['department'] = one_department
            # json_line['disease_name'] = disease_name
            # json_line['disease_url'] = disease_url

            json_text = one_department + ' => ' + disease_name + ' => ' + disease_url + '\n'
            self.write2File('url.txt', json_text)


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()