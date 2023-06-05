import json
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

        with open("error_msys_qa_0.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()

                json_line = json.loads(text_line)
                qa_href = json_line['text_url']
                one_department = json_line['one_department']
                two_department = json_line['two_department']

                self.getTwoDepartmentList(qa_href, one_department, two_department)


    def getTwoDepartmentList(self, text_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        print(text_url)
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=8
        )
        # print(response.text)

        #<div class="fl pl10">
        #     <p class="main-row"><span class="name">杨威</span><span class="title">副主任医师</span></p>
        #     <p class="vice-row"><span class="hospital">南宁市第二人民医院</span><i class="vertical-line"></i><span class="department">骨科</span></p>
        # </div>
        # doctor_info = re.compile('<div class="fl pl10">(.*?)</div>', re.S).findall(response.text)[0]
        #
        # # print(doctor_info)
        # doctor_info = doctor_info.strip()
        json_line = {}
        json_line['one_department'] = one_department
        json_line['two_department'] = two_department
        try:
            #医生名称
            doctor_name = re.compile('<span class="name">(.*?)</span>', re.S).findall(response.text)[0]
            print('doctor_name => ' + doctor_name)
            #医生标签
            doctor_label = ''
            doctor_hospital = ''
            doctor_department = ''
            try:
                doctor_label = re.compile('<span class="title">(.*?)</span>', re.S).findall(response.text)[0]
                print('doctor_label => ' + doctor_label)
                #医生医院
                doctor_hospital = re.compile('<span class="hospital">(.*?)</span>', re.S).findall(response.text)[0]
                print('doctor_hospital => ' + doctor_hospital)
                #医生科室
                doctor_department = re.compile('<span class="department">(.*?)</span>', re.S).findall(response.text)[0]
                print('doctor_department => ' + doctor_department)
            except Exception as e:
                print(e)

            #question
            question = re.compile('<i class="icon-question">问</i><span class="vertical-middle pl5">(.*?)</span>', re.S).findall(response.text)[0]
            print('question => ' + question)
            #<h2 class="answer-item__section-title">病情分析：</h2>
            #<div class="answer-item__section-content">老年性关节炎的患者建议平时应戒烟戒酒，同时还应加强营养，保证每日有足够量的蛋白、维生素以及膳食纤维的摄入。</div>
            answer_info_h = re.compile('<h2 class="answer-item__section-title">(.*?)</h2>', re.S).findall(response.text)
            answer_info_d = re.compile('<div class="answer-item__section-content">(.*?)</div>', re.S).findall(response.text)
            answer = ''
            if len(answer_info_h) == 2 and len(answer_info_d) == 2:
                answer = answer_info_h[0] + answer_info_d[0] + answer_info_h[1] + answer_info_d[1]
            print('answer => ' + answer)

            #<span class="gender">
            #     女，
            # </span>
            # <span class="age">60岁</span>
            patient_gender = re.compile('<span class="gender">(.*?)</span>', re.S).findall(response.text)[0]
            patient_gender = patient_gender.strip()
            patient_gender = patient_gender.replace('，', '')
            print('patient_gender => ' + patient_gender)
            patient_age = re.compile('<span class="age">(.*?)</span>', re.S).findall(response.text)[0]
            print('patient_age => ' + patient_age)
            #<p class="views-count">2023-05-11</p>
            patient_time = re.compile('<p class="views-count">(.*?)</p>', re.S).findall(response.text)[0]
            print('time => ' + patient_time)


            json_line['doctor_name'] = doctor_name
            json_line['doctor_label'] = doctor_label
            json_line['doctor_hospital'] = doctor_hospital
            json_line['doctor_department'] = doctor_department
            json_line['question'] = question
            json_line['answer'] = answer
            json_line['patient_gender'] = patient_gender
            json_line['patient_age'] = patient_age
            json_line['time'] = patient_time

            self.write2File('b_msys_qa_0.txt', str(json_line).replace('\'', '\"') + '\n')

        except Exception as e:
            json_line['text_url'] = text_url
            self.write2File('error_msys_qa_1.txt', str(json_line).replace('\'', '\"') + '\n')
            print(e)

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()