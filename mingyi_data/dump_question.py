import json
import time

import requests
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
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
        self.base_url = 'https://m.myzx.cn/'
        with open("res.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                json_line = json.loads(text_line)
                department = json_line['department']
                disease = json_line['disease']
                dis_url = json_line['dis_url']

                self.getTwoDepartmentList(dis_url, department, disease)
                time.sleep(2)

    def getTwoDepartmentList(self, tmp_url, department, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(tmp_url, cookies=self.cookies, headers=self.headers)
        res_text = response.text
        # print(res_text)
        # time.sleep(5)


        #<div class="tags-wraper tags-wraper2">(.*?)<div class="tabs-more-btn">
        disease_info = re.compile('<div class="tags-wraper tags-wraper2">(.*?)</div>', re.S).findall(res_text)[0]

        #<a href="/voice/1_0_2009_1" class="tag-item " data-id="2009">感冒</a>
        disease_list = re.compile('<a href="(.*?)</a>', re.S).findall(disease_info)
        if len(disease_list) == 0:
            json_line = {}
            json_line['department'] = department
            json_line['disease'] = department
            json_line['dis_url'] = tmp_url

            json_text = json.dumps(json_line, ensure_ascii=False)
            print(json_text)
            self.write2File('mingyi_url.txt', json_text + '\n')

            return '--'

        for disease_list_item in disease_list:
            disease_list_item = disease_list_item.strip()
            dis_url = disease_list_item.split('class="tag-item "')[0]
            dis_url = dis_url.split('"')[0]
            dis_url = dis_url.strip()
            dis_url = self.base_url + dis_url
            disease = disease_list_item.split('class="tag-item "')[1]
            disease = disease.split('>')[1]
            disease = disease.strip()
            print(dis_url)
            print(disease)
            print('-------------------')

            json_line = {}
            json_line['department'] = department
            json_line['disease'] = disease
            json_line['dis_url'] = dis_url

            json_text = json.dumps(json_line, ensure_ascii=False)
            print(json_text)
            self.write2File('mingyi_url.txt', json_text + '\n')



    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()