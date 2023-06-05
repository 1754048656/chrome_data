import time

import requests
import re
import random
import uaList

class DumpAllTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            '__jsluid_s': '36c191eb0c23ad80299c0d4687e67c20',
            'Hm_lvt_8b53bc0f3e59f56a58a92a894280e28d': '1684725612',
            'utrace': 'ECBFEC320A6DEFAEC150EC04807517B1',
            'Hm_lpvt_8b53bc0f3e59f56a58a92a894280e28d': '1684725658',
        }
        self.headers = {
            'authority': 'www.youlai.cn',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': '__jsluid_s=36c191eb0c23ad80299c0d4687e67c20; Hm_lvt_8b53bc0f3e59f56a58a92a894280e28d=1684725612; utrace=ECBFEC320A6DEFAEC150EC04807517B1; Hm_lpvt_8b53bc0f3e59f56a58a92a894280e28d=1684725658',
            'referer': 'https://www.youlai.cn/dise/pk_1_0_1.html',
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

        with open("a_question_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                disease = text_line.split(' => ')[2]
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                question = text_line.split(' => ')[3]
                question_url = text_line.split(' => ')[4]
                #https://www.youlai.cn/ask/796E93gPx5Y.html
                question_url = 'https://www.youlai.cn' + question_url
                question_url = question_url.replace(' =>', '')
                print(question_url)
                self.getTwoDepartmentList(question_url, one_department, two_department, disease, question)


    def getTwoDepartmentList(self, text_url, one_department, two_department, disease, question):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=28
        )
        time.sleep(1)

        json_line = {}
        json_line['one_department'] = one_department
        json_line['two_department'] = two_department
        json_line['disease'] = disease
        json_line['question'] = question

        try:

            #<div class="docYes">(.*?)</div>
            answer_info = re.compile('<div class="docYes">(.*?)</div>', re.S).findall(response.text)[0]
            # 去掉<>
            regex = re.compile('<(.*?)>')
            answer = regex.sub('', answer_info)
            answer = answer.strip()
            # print('answer => ' + answer)

            #医生信息<div class="doc_left"></div>
            doctor_info = re.compile('<div class="doc_left">(.*?)</div>', re.S).findall(response.text)[0]
            #医生名称<h5>崔馨<span>副主任医师</span>
            doctor_name = re.compile('<h5>(.*?)<span>', re.S).findall(doctor_info)[0]
            #<span>副主任医师</span>
            doctor_label = re.compile('<span>(.*?)</span>', re.S).findall(doctor_info)[0]
            #医院<span>中国人民解放军总医院</span></h5>
            doctor_hospital = re.compile('<span>(.*?)</span>', re.S).findall(doctor_info)[1]


            json_line['answer'] = answer
            json_line['doctor_name'] = doctor_name
            json_line['doctor_label'] = doctor_label
            json_line['doctor_hospital'] = doctor_hospital

            print(json_line)
            self.write2File('a_ylys_QA.txt', str(json_line).replace('\'', '\"') + '\n')
        except Exception as e:
            json_line['question_href'] = text_url
            self.write2File('a_ylys_error.txt', str(json_line).replace('\'', '\"') + '\n')
            print(e)
        time.sleep(1)

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()