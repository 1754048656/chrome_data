import json
import time

import requests
from urllib import parse
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            'XSRF-TOKEN': 'eyJpdiI6IlpkM3k1Yk1Remd3SkFza0RSaEVOTXc9PSIsInZhbHVlIjoiekErVGxWazJkcVowTVBRWmdJOHlBVGNMUGlHTFwvM0c1blwvY3hIVFJ0dUFGV0h0ZENSOGJkN3FzZitCYW52V0xiIiwibWFjIjoiMGY5ZTE3NGY3ZDY2YTNiZTZiZTlhNWFjZjcxNmI1ZmQwODE2OGI1N2IzZjQ4MTAzYjZlYzcyZGNhZjFjOWJkNSJ9',
            'laravel_session': 'eyJpdiI6IjBNU25abGlPbDYrWmFhXC9DTmtwdEpRPT0iLCJ2YWx1ZSI6Imw4N3NwTmtpQSs1MEdXTGc5NTQzcjA3MitJMmRJQm5ESmE1cnVlM1dxRDBreXR2b016dXh4dVA4bW8rZHBCQkQiLCJtYWMiOiIyYzlmOTU5M2I5MzY3MjI5ODMzOTcxZDEyZjJkODE2NDU1NTU5OTAxZTUwNGQwNmYwMzMyNWQ1ZjJhNGZhYjYxIn0%3D',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlpkM3k1Yk1Remd3SkFza0RSaEVOTXc9PSIsInZhbHVlIjoiekErVGxWazJkcVowTVBRWmdJOHlBVGNMUGlHTFwvM0c1blwvY3hIVFJ0dUFGV0h0ZENSOGJkN3FzZitCYW52V0xiIiwibWFjIjoiMGY5ZTE3NGY3ZDY2YTNiZTZiZTlhNWFjZjcxNmI1ZmQwODE2OGI1N2IzZjQ4MTAzYjZlYzcyZGNhZjFjOWJkNSJ9; laravel_session=eyJpdiI6IjBNU25abGlPbDYrWmFhXC9DTmtwdEpRPT0iLCJ2YWx1ZSI6Imw4N3NwTmtpQSs1MEdXTGc5NTQzcjA3MitJMmRJQm5ESmE1cnVlM1dxRDBreXR2b016dXh4dVA4bW8rZHBCQkQiLCJtYWMiOiIyYzlmOTU5M2I5MzY3MjI5ODMzOTcxZDEyZjJkODE2NDU1NTU5OTAxZTUwNGQwNmYwMzMyNWQ1ZjJhNGZhYjYxIn0%3D',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open("gyc_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)

                json_line = json.loads(text_line)

                department = json_line['department']
                disease = json_line['disease']
                disease_url = json_line['disease_href']
                print(disease_url)

                self.getTwoDepartmentList(disease_url, disease, department)

    def getTwoDepartmentList(self, disease_url, disease, department):


        response = requests.get(
            disease_url,
            cookies=self.cookies,
            headers=self.headers,
            verify=False,
            timeout=12
        )

        time.sleep(1.5)
        res_text = response.text

        json_line = {}
        json_line['department'] = department
        json_line['disease'] = disease

        # <div class="disease_details_item">(.*?)</div>
        # print(res_text)
        res_info = re.compile('<div class="disease_details_item">(.*?)</div>', re.S).findall(res_text)
        for res_info_item in res_info:
            res_info_item = res_info_item.strip()
            # print('res_info_item => ' + res_info_item)
            try:
                sub_title = res_info_item.split('</span>')[0]
                content = res_info_item.split('</span>')[1]
                content = self.format_text(content)
            except Exception as e:
                sub_title = '典籍论述'
                content = self.format_text(res_info_item)
                print(e)

            sub_title = self.format_text(sub_title)
            # print('sub_title => ' + sub_title)
            # print('content => ' + content)
            json_line[sub_title] = content

        print('--------------------')
        json_text = json.dumps(json_line, ensure_ascii=False)
        print(json_text)
        self.write2File('gyc_detail.txt', json_text + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


    def format_text(self, topic_header_text):

        # 去掉尖括号
        regex = re.compile('<(.*?)>')
        topic_header_text = regex.sub('', topic_header_text)

        # 去掉末尾的
        # topic_header_text = topic_header_text.split('<')[0]
        # topic_header_text = topic_header_text.split('$(document)')[0]

        # '      '
        # topic_header_text = topic_header_text.replace('      ', '，')
        # topic_header_text = topic_header_text.replace('     ', '，')
        # topic_header_text = topic_header_text.replace('    ', '，')
        # topic_header_text = topic_header_text.replace('   ', '，')
        # topic_header_text = topic_header_text.replace('  ', '，')
        # topic_header_text = topic_header_text.replace('</div>', '')
        # topic_header_text = topic_header_text.replace('<p>', '')
        # topic_header_text = topic_header_text.replace('</p>', '')

        # topic_header_text = topic_header_text.replace('  ', '')
        # topic_header_text = topic_header_text.replace('&nbsp;', '')
        # topic_header_text = topic_header_text.replace('\n', '')
        # topic_header_text = topic_header_text.replace('，、 ', '、')
        # topic_header_text = topic_header_text.replace('，, ', '，')
        # topic_header_text = topic_header_text.replace('。，', '。')
        # topic_header_text = topic_header_text.replace('，。', '。')
        # topic_header_text = topic_header_text.replace('，，', '，')
        # topic_header_text = topic_header_text.replace('：，', '：')
        # topic_header_text = topic_header_text.replace('，）', '）')
        # topic_header_text = topic_header_text.replace('），', '）')
        # topic_header_text = topic_header_text.replace('，)，', ')，')
        # topic_header_text = topic_header_text.replace('，)。', ')。')
        # topic_header_text = topic_header_text.strip()
        # topic_header_text = topic_header_text.strip('">')
        topic_header_text = topic_header_text.strip()
        topic_header_text = topic_header_text.strip('：')

        # if 'gon">' in topic_header_text:
        #     topic_header_text = topic_header_text.split('gon">')[1]

        return topic_header_text

DumpTitle()