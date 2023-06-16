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

        with open("bohe_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                two_de_url = text_line.split(' => ')[2]

                print(one_department)
                print(two_department)
                print(two_de_url)

                for p in range(1, 11):
                    # print(p)
                    two_url = two_de_url.split('.html')[0] + '-' + str(p) + '.html'
                    print(two_url)
                    res_info = ''
                    try:
                        res_info = self.getTwoDepartmentList(two_url, one_department, two_department)
                    except Exception as e:
                        print(e)
                        break
                    if '-3' in res_info:
                        self.tmp_num = 0
                        print('----next----')
                        break
                    time.sleep(2)

    def getTwoDepartmentList(self, two_de_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(two_de_url, cookies=self.cookies, headers=self.headers)
        res_text = response.text

        #<div class="question">
        question_list = re.compile('<div class="question">(.*?)</div>', re.S).findall(res_text)
        if question_list[0] in self.tmp_list:
            self.tmp_num = self.tmp_num + 1
            if self.tmp_num > 3:
                return '-3'
            return '-1'
        self.tmp_list.append(question_list[0])
        for question_list_item in question_list:
            question_list_item = question_list_item.strip()
            #<a href="(.*?)</a>
            question_info = re.compile('<a href="(.*?)</a>', re.S).findall(question_list_item)[0]
            question_url = question_info.split('" target="_blank">')[0]
            question = question_info.split('" target="_blank">')[1]
            print(question_url)
            print(question)

            json_line = {}
            json_line['one_department'] = one_department
            json_line['two_department'] = two_department
            json_line['question'] = question
            json_line['question_url'] = question_url

            json_text = json.dumps(json_line, ensure_ascii=False) + '\n'
            self.write2File('bohe_q.txt', json_text)

        return '-0'


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()