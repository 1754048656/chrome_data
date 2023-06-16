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
        self.session = requests.Session()  # 创建session
        with open("bohe_q.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                json_line = json.loads(text_line)
                one_department = json_line['one_department']
                two_department = json_line['two_department']
                question = json_line['question']
                question_url = json_line['question_url']


                print(one_department)
                print(two_department)
                print(question)
                print(question_url)

                self.getTwoDepartmentList(question_url, one_department, two_department, question)
                time.sleep(1)


    def getTwoDepartmentList(self, question_url, one_department, two_department, question):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = self.session.get(question_url, cookies=self.cookies, headers=self.headers, allow_redirects=False,
                                    timeout=8)
        # response = requests.get(question_url, cookies=self.cookies, headers=self.headers)
        res_text = response.text

        #问题描述
        #<div class="iask-user-des-content">(.*?)</div>
        ask_desc = re.compile('<div class="iask-user-des-content">(.*?)</div>', re.S).findall(res_text)[0]
        ask_desc = ask_desc.strip()
        print('ask_desc => ' + ask_desc)

        #病人
        #<span class="iask-user-info-name">(.*?)</span>
        user_info = re.compile('<span class="iask-user-info-name">(.*?)</span>', re.S).findall(res_text)[0]
        user_info = user_info.strip()
        print('user_info => ' + user_info)

        #时间
        #<span class="iask-user-info-time">(.*?)</span>
        time_info = re.compile('<span class="iask-user-info-time">(.*?)</span>', re.S).findall(res_text)[0]
        time_info = time_info.strip()
        print('time_info => ' + time_info)

        #医生信息
        #<div class="detail-doctor-answer flr">(.*?)</div>
        doctor_info = re.compile('<div class="detail-doctor-answer flr">(.*?)</div>', re.S).findall(res_text)[0]
        # print('doctor_info => ' + doctor_info)

        #医生名称
        #<span class="doctor-name fll">张越</span>
        doctor_name = re.compile('<span class="doctor-name fll">(.*?)</span>', re.S).findall(doctor_info)[0]
        print('doctor_name => ' + doctor_name)

        #医生职位
        #<span class="doctor-professional fll">(.*?)</span>
        doctor_label = re.compile('<span class="doctor-professional fll">(.*?)</span>', re.S).findall(doctor_info)[0]
        print('doctor_label => ' + doctor_label)

        #医生医院
        #<span class="doctor-hospital fll">(.*?)</span>
        doctor_hospital = re.compile('<span class="doctor-hospital fll">(.*?)</span>', re.S).findall(doctor_info)[0]
        print('doctor_hospital => ' + doctor_hospital)

        #<div class="doctor-answer-description pc_articleContent">(.*?)</div>
        doctor_answer = re.compile('<div class="doctor-answer-description pc_articleContent">(.*?)</div>', re.S).findall(res_text)[0]
        doctor_answer = self.format_text(doctor_answer)
        print('doctor_answer => ' + doctor_answer)

        json_tmp = {}
        json_tmp['one_department'] = one_department
        json_tmp['two_department'] = two_department
        json_tmp['title'] = question
        json_tmp['question'] = ask_desc
        json_tmp['patient'] = user_info
        json_tmp['time'] = time_info
        json_tmp['doctor_name'] = doctor_name
        json_tmp['doctor_label'] = doctor_label
        json_tmp['doctor_hospital'] = doctor_hospital
        json_tmp['doctor_answer'] = doctor_answer

        json_text = json.dumps(json_tmp, ensure_ascii=False) + '\n'
        print(json_text)


    def format_text(self, topic_header_text):
        # 去掉尖括号
        regex = re.compile('<(.*?)>')
        topic_header_text = regex.sub('', topic_header_text)
        topic_header_text = topic_header_text.strip()
        return topic_header_text


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()