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
            'BAIDUID': '3C9F43BD24AA4B2932F6C727656D78A6:FG=1',
            'BIDUPSID': '3C9F43BD24AA4B2932F6C727656D78A6',
            'PSTM': '1684473847',
            'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
            'BA_HECTOR': '002k0525050580848504a04c1i78jn81n',
            'ZFY': 'MFwwAaA81PWeQPje:AImBCi:AODgkU:A7JktZPXypYs:A1g:C',
            'BAIDUID_BFESS': '3C9F43BD24AA4B2932F6C727656D78A6:FG=1',
            'H_PS_PSSID': '38515_36543_38541_38767_38576_38196_38637_38764_26350_22158',
            'PSINO': '2',
            'delPer': '0',
        }
        self.headers = {
            'authority': 'jiankang.baidu.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': 'BAIDUID=3C9F43BD24AA4B2932F6C727656D78A6:FG=1; BIDUPSID=3C9F43BD24AA4B2932F6C727656D78A6; PSTM=1684473847; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=002k0525050580848504a04c1i78jn81n; ZFY=MFwwAaA81PWeQPje:AImBCi:AODgkU:A7JktZPXypYs:A1g:C; BAIDUID_BFESS=3C9F43BD24AA4B2932F6C727656D78A6:FG=1; H_PS_PSSID=38515_36543_38541_38767_38576_38196_38637_38764_26350_22158; PSINO=2; delPer=0',
            'referer': 'https://jiankang.baidu.com/widescreen/entitylist?tabType=2&navType=3',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        self.params = {
            'tabType': '2',
            'navType': '3',
            'itemType': '感染科',
        }
        with open("href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                print(text_line)

                self.getTwoDepartmentList(text_line)
                time.sleep(2)

    def getTwoDepartmentList(self,  text_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        self.params['itemType'] = text_line
        response = requests.get(
            'https://jiankang.baidu.com/widescreen/api/entitylist',
            cookies=self.cookies,
            headers=self.headers,
            params=self.params,
            timeout=28
        )
        time.sleep(1.5)
        json_line = response.json()
        json_text = json.dumps(json_line, ensure_ascii=False)
        content_info = re.compile('{"contentId": "(.*?)", "udNum"').findall(json_text)
        for content_info_item in content_info:
            print('content_info_item => ' + content_info_item)
            url_href = content_info_item.split('", "name": "')[0]
            dis_name = content_info_item.split('", "name": "')[1]
            line_tmp = text_line + ' => ' + dis_name + ' => https://www.baidu.com/bh/dict/' + url_href + '?from=dicta&sf_ref=med_pc&sf_ch=ch_med_pc'
            self.write2File('dis_url.txt', line_tmp + '\n')

        # print('res_json => ' + json_text)

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()