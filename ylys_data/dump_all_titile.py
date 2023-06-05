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

        with open("href_0.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                text_url = text_line.split(' => ')[0]
                one_department = text_line.split(' => ')[1]

                self.getTwoDepartmentList(text_url, one_department)


    def getTwoDepartmentList(self, text_url, one_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=18
        )
        # print(response.text)
        #<span>二级：</span>
        # <p>
        # <a href="/dise/pk_1_0_1.html" ">全部</a>
        # <a href="/dise/pk_1_12_1.html" class="cur"> 消化内科</a>
        # <a href="/dise/pk_1_13_1.html" > 心血管内科</a>
        # <a href="/dise/pk_1_14_1.html" > 神经内科</a>
        # <a href="/dise/pk_1_15_1.html" > 呼吸内科</a>
        # <a href="/dise/pk_1_16_1.html" > 内分泌科</a>
        # <a href="/dise/pk_1_17_1.html" > 血液内科</a>
        # <a href="/dise/pk_1_18_1.html" > 肾内科</a>
        # <a href="/dise/pk_1_19_1.html" > 风湿免疫科</a>
        # <a href="/dise/pk_1_20_1.html" > 感染内科</a>
        # <a href="/dise/pk_1_77_1.html" > 普通内科</a>
        # <a href="/dise/pk_1_78_1.html" > 变态反应科</a>
        # <a href="/dise/pk_1_132_1.html" > 肝病科</a>
        # </p>
        department_info = re.compile('<span>二级：</span>(.*?)</p>', re.S).findall(response.text)[0]
        department_list = re.compile('<a href="(.*?)</a>', re.S).findall(department_info)
        for department_list_item in department_list:
            if '全部' in department_list_item:
                continue
            print(department_list_item)
            text_url = department_list_item.split('" > ')[0]
            two_department = department_list_item.split('" > ')[1]
            text_line = one_department + ' => ' + two_department + ' => ' + text_url + '\n'
            print(text_line)
            self.write2File('two_de.txt', text_line)



    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()