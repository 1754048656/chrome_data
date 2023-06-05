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
            'QiHooGUID': 'D6A0A64BB0C8CAE3EA2DF144E5CF6D3D.1685104120808',
            '__guid': '98597507.3715389439386620400.1685104131895.04',
        }
        self.headers = {
            'authority': 'ly.so.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': 'QiHooGUID=D6A0A64BB0C8CAE3EA2DF144E5CF6D3D.1685104120808; __guid=98597507.3715389439386620400.1685104131895.04',
            'referer': 'https://ly.so.com/sku/yidian/index?tab=0&tab_type=%E6%8C%89%E7%A7%91%E5%AE%A4&content_type=%E7%96%BE%E7%97%85%E7%B1%BB&tab_value=%E7%94%B7%E7%A7%91',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open("href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = re.compile('value": "(.*?)"', re.S).findall(text_line)[0]
                print(text_line)

                href_text = 'https://ly.so.com/api/v1/yidian/sku?cancelToken={"promise":{}}&content_type=疾病类&tab_type=按科室&tab_value=' + text_line
                self.getTwoDepartmentList(href_text, text_line)
                time.sleep(2)

    def getTwoDepartmentList(self, href_text, department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            href_text,
            cookies=self.cookies,
            headers=self.headers,
            timeout=28
        )
        time.sleep(1.5)
        json_line = response.json()
        json_text = json.dumps(json_line, ensure_ascii=False)

        print('res_json => ' + json_text)
        entity_list = json_line['data']['entity_list']
        for entity_list_item in entity_list:
            dis_name_list = entity_list_item['list']
            for dis_name in dis_name_list:
                one_line = department + ' => ' + dis_name + ' => https://ly.so.com/sku/yidian/index?tab=0&tab_type=%E6%8C%89%E7%A7%91%E5%AE%A4&content_type=%E7%96%BE%E7%97%85%E7%B1%BB&tab_value=' + parse.quote(dis_name) + '\n'
                print(one_line)
                self.write2File('dis_href.txt', one_line)


        # https://ly.so.com/detail/yidian?title=xxx
        # https://ly.so.com/api/v1/yidian/detail?cancelToken={"promise":{}}&contentName=&contentNameTerm=泌乳素瘤

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)




DumpTitle()