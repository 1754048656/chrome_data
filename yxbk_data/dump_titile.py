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
            'VEE': 'wikitext',
            'Hm_lvt_8e1450316c96d3e524f02e4c301c03a2': '1685949150,1685967300',
            'Hm_lpvt_8e1450316c96d3e524f02e4c301c03a2': '1685967715',
        }
        self.headers = {
            'authority': 'www.yixue.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'VEE=wikitext; Hm_lvt_8e1450316c96d3e524f02e4c301c03a2=1685949150,1685967300; Hm_lpvt_8e1450316c96d3e524f02e4c301c03a2=1685967715',
            'referer': 'https://www.yixue.com/index.php?title=%E5%88%86%E7%B1%BB:%E5%85%A8%E8%BA%AB%E7%97%87%E7%8A%B6&pagefrom=%E5%AE%9D%E5%AE%9D%E7%BC%BA%E4%B9%8F%E5%AE%89%E5%85%A8%E6%84%9F',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open("b_dis_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                print(text_line)
                department = text_line.split(' => ')[0]
                text_url = text_line.split(' => ')[1]

                self.getTwoDepartmentList(text_url, department)
                time.sleep(2)

    def getTwoDepartmentList(self, text_url, deparment):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )

        time.sleep(1.5)
        res_text = response.text

        #  <li><a href=(.*?)</a></li>
        disease_info = re.compile('<li><a href=(.*?)">').findall(res_text)
        for disease_info_item in disease_info:
            if '分类:症状' in disease_info_item:
                print('next -----')
                continue
            disease_info_item = disease_info_item.strip()

            json_line = {}
            urlencode = disease_info_item.split('" title="')[0]
            dis_name = disease_info_item.split('" title="')[1]
            json_line['department'] = deparment
            json_line['disease'] = dis_name
            json_line['urlencode'] = urlencode
            print(json_line)
            self.write2File('b_dis_url.txt', json.dumps(json_line, ensure_ascii=False) + '\n')

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()