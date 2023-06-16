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
            'Hm_lvt_7b5243e28e06e5637ee9bdfbc0f4e734': '1686568374',
            'Hm_lvt_6ab8f0ec2ab13c47d7b02f7c4fa00c44': '1686568419',
            'Hm_lvt_141a64e5e06ba763181e9639a4634d84': '1686574660',
            'Hm_lpvt_141a64e5e06ba763181e9639a4634d84': '1686574686',
            'Hm_lpvt_7b5243e28e06e5637ee9bdfbc0f4e734': '1686710076',
            'Hm_lpvt_6ab8f0ec2ab13c47d7b02f7c4fa00c44': '1686710076',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'Hm_lvt_7b5243e28e06e5637ee9bdfbc0f4e734=1686568374; Hm_lvt_6ab8f0ec2ab13c47d7b02f7c4fa00c44=1686568419; Hm_lvt_141a64e5e06ba763181e9639a4634d84=1686574660; Hm_lpvt_141a64e5e06ba763181e9639a4634d84=1686574686; Hm_lpvt_7b5243e28e06e5637ee9bdfbc0f4e734=1686710076; Hm_lpvt_6ab8f0ec2ab13c47d7b02f7c4fa00c44=1686710076',
            'Pragma': 'no-cache',
            'Referer': 'https://www.bohe.cn/voice/list/new/53.html',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        self.list_tmp = []
        self.num_tmp = 0
        self.session = requests.Session()  # 创建session

        with open("dis_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                department = text_line.split(' => ')[0]
                disease = text_line.split(' => ')[1]
                disease_url = text_line.split(' => ')[2]
                # print(department)
                # print(disease)
                # print(disease_url)

                for o in range(1, 11):
                    disease_tmp = disease_url.split('.html')[0] + '_' + str(o) + '.html'
                    print(department)
                    print(disease)
                    print(disease_tmp)
                    res_info = self.getTwoDepartmentList(disease_tmp, department, disease)
                    if res_info == '-3':
                        print('-----next-----')
                        self.num_tmp = 0
                        break
                    time.sleep(2)

    def getTwoDepartmentList(self, disease_tmp, department, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = self.session.get(disease_tmp, cookies=self.cookies, headers=self.headers, allow_redirects=False, timeout=8)
        res_text = response.text

        #<span class="title-con"><a href="(.*?)</a></span>
        question_info_list = re.compile('<span class="title-con"><a href="(.*?)</a></span>', re.S).findall(res_text)
        if len(question_info_list) == 0:
            return '-3'
        u = 0
        for question_info_list_item in question_info_list:

            # print(question_info_list_item)
            question_url = question_info_list_item.split('" class="a-hover">')[0]
            question = question_info_list_item.split('" class="a-hover">')[1]

            json_line = {}
            json_line['department'] = department
            json_line['disease'] = disease
            json_line['question'] = question
            json_line['question_url'] = question_url

            if question_url in self.list_tmp:
                self.num_tmp = self.num_tmp + 1
                if self.num_tmp > 3:
                    return '-3'
                return '-1'
            else:
                self.list_tmp.append(question_url)


            json_text = json.dumps(json_line, ensure_ascii=False) + '\n'
            print(json_text)
            self.write2File('a_question_url.txt', json_text)

            u = u+1

        return '-0'


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()