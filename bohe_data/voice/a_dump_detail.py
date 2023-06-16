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

        with open("a_question_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                json_line = json.loads(text_line)

                department = json_line['department']
                disease = json_line['disease']
                question = json_line['question']
                question_url = json_line['question_url']

                print(question_url)

                self.getTwoDepartmentList(question_url, json_line)


    def getTwoDepartmentList(self, question_url, json_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = self.session.get(question_url, cookies=self.cookies, headers=self.headers, allow_redirects=False, timeout=8)
        res_text = response.text

        department = json_line['department']
        disease = json_line['disease']
        question = json_line['question']

        #语音内容
        #<div class="dis-txt-info pc_articleContent">(.*?)</div>
        articleContent = re.compile('<div class="dis-txt-info pc_articleContent">(.*?)</div>', re.S).findall(res_text)[0]
        articleContent = self.format_text(articleContent)

        #医生名字
        #class="doctor-name">(.*?)</a>
        doctor_name = re.compile('class="doctor-name">(.*?)</a>', re.S).findall(res_text)[0]

        #职位
        #<p class="posit">(.*?)</p>
        doctor_posit = re.compile('<p class="posit">(.*?)</p>', re.S).findall(res_text)[0]

        #医院
        #<div class="hospital">(.*?)</p>
        doctor_hospital = re.compile('<div class="hospital">(.*?)</p>', re.S).findall(res_text)[0]
        doctor_hospital = self.format_text(doctor_hospital)

        print(department)
        print(disease)
        print(question)
        print(articleContent)
        print(doctor_name)
        print(doctor_posit)
        print(doctor_hospital)

        json_tmp = {}
        json_tmp['department'] = department
        json_tmp['disease'] = disease
        json_tmp['question'] = question
        json_tmp['answer'] = articleContent
        json_tmp['doctor_name'] = doctor_name
        json_tmp['doctor_posit'] = doctor_posit
        json_tmp['doctor_hospital'] = doctor_hospital

        json_text = json.dumps(json_tmp, ensure_ascii=False) + '\n'

        self.write2File('voice_detail.txt', json_text)



    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


    def format_text(self, topic_header_text):
        # 去掉尖括号
        regex = re.compile('<(.*?)>')
        topic_header_text = regex.sub('', topic_header_text)
        topic_header_text = topic_header_text.strip()
        return topic_header_text

DumpTitle()