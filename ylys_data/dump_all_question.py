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

        with open("disease_href_0.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                disease = text_line.split(' => ')[2]
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                disease_url = text_line.split(' => ')[3]
                disease_url = disease_url
                #https://www.youlai.cn/dise/asklist/34_10.html
                disease_num = re.compile('https://www\.youlai\.cn/dise/(.*?)\.html', re.S).findall(disease_url)[0]
                disease_url = 'https://www.youlai.cn/dise/asklist/' + disease_num + '_1.html'
                print(disease_url)
                self.getTwoDepartmentList(disease_url, one_department, two_department, disease)


    def getTwoDepartmentList(self, text_url, one_department, two_department, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        for i in range(1, 11):
            base_url = text_url.split('_1')[0]
            base_url = base_url + '_' + str(i) + '.html'
            print(base_url)

            response = requests.get(
                base_url,
                cookies=self.cookies,
                headers=self.headers,
                timeout=18
            )
            time.sleep(1)

            #<h3><a href="/ask/6A3F15gauAP.html" target="_blank">三个月宝宝发育指标</a></h3>
            #<h3><a href="/ask/B064BFgaJSa.html" target="_blank">右眼内眼角有个肉疙瘩怎么回事</a></h3>
            question_info = re.compile('<h3><a href="(.*?)</a></h3>', re.S).findall(response.text)
            if len(question_info) == 0:
                return '0'
            for question_info_item in question_info:
                question_href = question_info_item.split('" target="_blank">')[0]
                question = question_info_item.split('" target="_blank">')[1]
                text_line = one_department + ' => ' + \
                            two_department + ' => ' + \
                            disease + ' => ' + \
                            question + ' => ' + \
                            question_href + ' => '
                print(text_line)
                self.write2File('a_question_href.txt', text_line + '\n')




    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()