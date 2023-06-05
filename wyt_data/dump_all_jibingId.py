import json

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


        with open("href_jibing_one_two.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                href_num = text_line.split(' => ')[2]
                jiBing = text_line.split(' => ')[3]

                # print('one_department => ' + one_department)
                # print('two_department => ' + two_department)
                # print('href_num => ' + href_num)
                # print('jiBing => ' + jiBing)
                # print('------------------------------')
                text_url = 'https://wenda.familydoctor.com.cn/question/questiondatalist.do/jibing/' + str(href_num) + '/1/10000/'
                self.getJiBingList(text_url, one_department, two_department, jiBing)


    def getJiBingList(self, text_url, one_department, two_department, jiBing):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )

        res_text = response.text
        res_text = json.loads(res_text)
        res_text = res_text['data']['records']
        # print(res_text)
        for res_text_item in res_text:
            id = res_text_item['id']
            overtid = res_text_item['overtid']
            title = res_text_item['title']
            content = res_text_item['content']
            #add_overtid = one_department + '=>' + two_department + '=>' + jiBing + '=>' + id + '=>' + overtid + '=>' + title + '=>' + content
            #print(add_overtid)
            json_info = {}
            json_info['one_department'] = one_department
            json_info['two_department'] = two_department
            json_info['disease'] = jiBing
            json_info['id'] = id
            json_info['overtid'] = overtid
            json_info['title'] = title
            json_info['content'] = content
            print(res_text_item)
            self.write2File('href_overId.txt', str(json_info).replace('\'', '\"') + '\n')

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllJiBingID()