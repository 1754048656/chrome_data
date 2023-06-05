import json
import time

import requests
import re
import random
import uaList

class DumpAllJiBingID:
    def __init__(self):
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


        with open("href_overId.txt", 'r', encoding='utf-8') as file:
            for item in file:
                #{
                # "one_department": "内科",
                # "two_department": "呼吸内科",
                # "disease": "胸痛",
                # "id": 26683,
                # "overtid": "2023051817313786740",
                # "title": "患上支气管炎会胸痛吗",
                # "content": "单纯支气管炎引起胸痛的症状比较少，由于支气管炎的感染位置在气管内，不易侵入胸膜，肺炎容易侵入胸膜，胸痛。如果有胸痛症状，完善胸片或胸部CT检查，看看是否有胸部积液。如果没有肺炎，而且是中老年人，完善心电图，除心肌缺血或心肌梗死外；此外，还取决于局部皮肤是否发红和泡疹，除了带状疱疹。"
                # }
                try:
                    text_line = item.strip()
                    # print(text_line)
                    json_line = json.loads(text_line)
                    # print(json_line)
                    overtid = json_line['overtid']
                    href_overtid = 'https://wenda.familydoctor.com.cn/question/' + overtid + '.html'



                    # one_department = text_line.split(' => ')[0]
                    # two_department = text_line.split(' => ')[1]
                    # href_num = text_line.split(' => ')[2]
                    # jiBing = text_line.split(' => ')[3]

                    # print('one_department => ' + one_department)
                    # print('two_department => ' + two_department)
                    # print('href_num => ' + href_num)
                    # print('jiBing => ' + jiBing)
                    # print('------------------------------')


                    # text_url = 'https://wenda.familydoctor.com.cn/question/questiondatalist.do/jibing/' + str(href_num) + '/1/10000/'
                    self.getJiBingList(href_overtid, json_line)
                except Exception as e:
                    print(e)


    def getJiBingList(self, text_url, json_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )
        res_text = response.text
        #print(res_text)
        #<span class="doc-name"><a>刘凯</a></span>/ <span class="doc-duty">副主任医师</span> <span class="doc-dep">达孜区人民医院</span>
        #<a class="cate cate1"
        #<span class="doc-name">(.*?)<a class="cate cate1"
        doctor_info = re.compile('<span class="doc-name">(.*?)<a class="cate cate1"', re.S).findall(res_text)[0]
        #print('doctor_info => ' + doctor_info)
        #<a>刘凯</a>
        doctor_name = re.compile('<a>(.*?)</a>', re.S).findall(doctor_info)[0]
        print('doctor_name => ' + doctor_name)
        #<span class="doc-duty">副主任医师</span>
        doctor_label = re.compile('<span class="doc-duty">(.*?)</span>', re.S).findall(doctor_info)[0]
        print('doctor_label => ' + doctor_label)
        #<span class="doc-dep">达孜区人民医院</span>
        doctor_hospital = re.compile('<span class="doc-dep">(.*?)</span>', re.S).findall(doctor_info)[0]
        print('doctor_hospital => ' + doctor_hospital)
        json_line['doctor_name'] = doctor_name
        json_line['doctor_label'] = doctor_label
        json_line['doctor_hospital'] = doctor_hospital

        self.write2File('all_QA_0.txt', str(json_line).replace('\'', '\"') + '\n')

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllJiBingID()
