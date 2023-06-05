import json
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

        with open("b_msd_title.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                #print(text_line)
                #<a class="section__item" href="/professional/infectious-diseases">
                #     传染病
                # </a>
                department_info = re.compile('<a class="section__item" href="(.*?)<', re.S).findall(text_line)
                for department_info_item in department_info:
                    department_href = department_info_item.split('">')[0]
                    department_name = department_info_item.split('">')[1]
                    department_href = 'https://www.msdmanuals.cn' + department_href
                    print(department_name + ' => ' + department_href)
                    self.getTwoDepartmentList(department_href, department_name)

    def getTwoDepartmentList(self, text_url, department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=28
        )
        time.sleep(1.5)

        title_list = []
        #疾病名称和url
        medicalsection__caption = re.compile("<div class='medicalsection__caption'>(.*?)</div>", re.S).findall(response.text)
        for medicalsection__caption_i in medicalsection__caption:
            first_title = {}

            medical_info = re.compile('<a href="(.*?)</a>', re.S).findall(medicalsection__caption_i)[0]
            # medical_href = medical_info.split('">')[0]
            medical_name = medical_info.split('">')[1]
            # medical_href = 'https://www.msdmanuals.cn' + medical_href
            medical_name = medical_name.strip()
            first_title['department'] = department
            first_title['medical_name'] = medical_name
            # first_title['medical_href'] = medical_href
            first_title['sub'] = []
            title_list.append(first_title)

        # 第二级title
        medicalsection__column = re.compile("<div class='medicalsection__column'>(.*?)</div>", re.S).findall(response.text)
        i = 0
        for medicalsection__column_i in medicalsection__column:
            #根据<li class='medicalsection__link切割
            t = 0
            sub_title = medicalsection__column_i.split("<li class='medicalsection__link")
            sub_title.pop(0)
            for sub_title_item in sub_title:
                sub_title_a_info = re.compile('<a href="(.*?)</a>', re.S).findall(sub_title_item)[0]
                subtitle_url = sub_title_a_info.split('">')[0]
                subtitle_name = sub_title_a_info.split('">')[1]
                sub_json = {}
                sub_json['sub_title'] = subtitle_name
                sub_json['sub_title_url'] = 'https://www.msdmanuals.cn' + subtitle_url

                # third_title
                # 先找 a 标签的数量，如果只有一个，则为单标签
                #<a href="/professional/infectious-diseases/biology-of-infectious-disease/introduction-to-the-biology-of-infectious-diseases">感染性疾病生理基础介绍</a>
                #<a href="(.*?)</a>
                # third_title_a = re.compile('<a href="(.*?)</a>', re.S).findall(sub_title_item)
                # if len(third_title_a) == 1:
                #     pass
                # else:
                sub_json = self.get_third_title(sub_title_item, sub_json)
                title_list[i]['sub'].append(sub_json)
                t = t + 1
                # 展示一个sub_json
                # print('sub_json => ' + str(sub_json))
                time.sleep(1)

            print('i => ' + str(title_list[i]))
            self.write2File('a_msd_title.txt', json.dumps(title_list[i], ensure_ascii=False) + '\n')
            i = i + 1


    def get_third_title(self, sub_title_item, sub_json):
        # 根据medicalsection__link__inside切割
        third_title_info = sub_title_item.split('medicalsection__link__inside')
        third_title_info.pop(0)
        # print('sub => ' + str(sub_json))
        sub_json['third'] = []
        for third_title_info_item in third_title_info:
            third_title_a_info = re.compile('<a href="(.*?)</a>', re.S).findall(third_title_info_item)
            third_title_name = third_title_a_info[0].split('">')[1]
            third_json = {}
            third_json['third_title'] = third_title_name

            if len(third_title_a_info) == 1:
                pass
            else:
                third_json = self.get_forth_title(third_title_info_item, third_json)

            sub_json['third'].append(third_json)
        return sub_json


    def get_forth_title(self, third_title_info_item, third_json):
        third_json['forth'] = []
        third_title_a_info = re.compile('<a href="(.*?)</a>', re.S).findall(third_title_info_item)
        third_title_a_info.pop(0)
        for item in third_title_a_info:
            forth_name = item.split('">')[1]
            third_json['forth'].append(forth_name)

        return third_json


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)




DumpAllTitle()