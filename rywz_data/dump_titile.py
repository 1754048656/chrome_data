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
            'PHPSESSID': '4e2vc32j1oim7kv23m1a92ohnd4re8fu',
            '6Dly_2132_saltkey': 'uU60B20B',
            '6Dly_2132_lastvisit': '1685692423',
            'Hm_lvt_f838732f69e738aab432abc4b4f201ac': '1685696043',
            '6Dly_2132_sid': 'o8DZff',
            '6Dly_2132_lastact': '1685704636%09finddoctor.php%09',
            'Hm_lpvt_f838732f69e738aab432abc4b4f201ac': '1685704657',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'PHPSESSID=4e2vc32j1oim7kv23m1a92ohnd4re8fu; 6Dly_2132_saltkey=uU60B20B; 6Dly_2132_lastvisit=1685692423; Hm_lvt_f838732f69e738aab432abc4b4f201ac=1685696043; 6Dly_2132_sid=o8DZff; 6Dly_2132_lastact=1685704636%09finddoctor.php%09; Hm_lpvt_f838732f69e738aab432abc4b4f201ac=1685704657',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.renyiwenzhen.com/finddoctor.php?action=anjb&ckid=52',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        self.params = {
            'action': 'anjb',
            'ckid': '3',
        }
        with open("href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                print(text_line)
                ckid_text = text_line.split(' => ')[0]
                department = text_line.split(' => ')[1]

                self.getTwoDepartmentList(ckid_text, department)
                time.sleep(2)

    def getTwoDepartmentList(self,  ckid_text, deparment):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        self.params['ckid'] = ckid_text

        response = requests.get(
            'http://www.renyiwenzhen.com/finddoctor.php',
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            verify=False,
            timeout=18
        )

        time.sleep(1.5)
        res_text = response.text

        #  <a target="_blank" href="http://www.renyiwenzhen.com/finddoctor-jbdetail-97.html" title="点击查看 宫颈息肉 详情">
        disease_info = re.compile(' <a target="_blank" href="(.*?) 详情">').findall(res_text)
        for disease_info_item in disease_info:
            disease_url = disease_info_item.split('" title="点击查看 ')[0]
            disease_name = disease_info_item.split('" title="点击查看 ')[1]

            text_line = deparment + ' => ' + disease_name + ' => ' + disease_url
            print(text_line)
            self.write2File('dis_url.txt', text_line + '\n')

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()