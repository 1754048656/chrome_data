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

        with open("url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                department = text_line.split(' => ')[0]
                disease = text_line.split(' => ')[1]
                disease_url = text_line.split(' => ')[2]

                for t in range(1, 11):
                    disease_url_tmp = disease_url.split('.html')[0]
                    disease_url_tmp = disease_url_tmp + '_' + str(t) + '.html'
                    print(disease_url_tmp)
                    res_info = self.getTwoDepartmentList(disease_url, department, disease)
                    if res_info == '-3':
                        print('-----next-----')
                        self.tmp_num = 0
                        break
                    time.sleep(2)

    def getTwoDepartmentList(self, disease_url, department, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(disease_url, cookies=self.cookies, headers=self.headers, allow_redirects=False, timeout=8)
        res_text = response.text

        #<div class="ma-modone-right">(.*?)<p class="video-play-num flr">
        question_info = re.compile('<div class="ma-modone-right">(.*?)</a>', re.S).findall(res_text)
        one_question = question_info[0]
        if one_question in self.tmp_list:
            self.tmp_num = self.tmp_num + 1
            if self.tmp_num > 2:
                return '-3'
            return '-1'
        else:
            self.tmp_list.append(one_question)
        for question_info_item in question_info:
            question_info_item = question_info_item.strip()
            question = question_info_item.split('title">')[1]
            question_url = re.compile('<a href="(.*?)" class', re.S).findall(question_info_item)[0]
            print(question)
            # print(question_url)

            json_line = {}
            json_line['department'] = department
            json_line['disease'] = disease
            json_line['question'] = question
            json_line['question_url'] = question_url

            json_text = json.dumps(json_line, ensure_ascii=False)
            print(json_text)
            self.write2File('article_url.txt', json_text + '\n')



    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()