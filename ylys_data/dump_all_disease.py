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

        with open("two_de.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                text_url = text_line.split(' => ')[2]
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                text_url = 'https://www.youlai.cn' + text_url
                print(text_url)
                self.getTwoDepartmentList(text_url, one_department, two_department)


    def getTwoDepartmentList(self, text_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=18
        )
        time.sleep(2)
        #<dl class="textList">
        disease_info = re.compile('<dl class="textList">(.*?)</dl>', re.S).findall(response.text)[0]
        #<a href="/dise/2.html"><i></i>胃溃疡</a>
        disease_info = re.compile('<a href="(.*?)</a>', re.S).findall(disease_info)
        for disease_info_item in disease_info:
            disease_href = disease_info_item.split('"><i></i>')[0]
            disease_name = disease_info_item.split('"><i></i>')[1]
            text_line = one_department + ' => ' + two_department + ' => ' + disease_name + ' => https://www.youlai.cn' + disease_href + '\n'
            print(text_line)
            self.write2File('disease_href_0.txt', text_line)

        time.sleep(1)



    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()