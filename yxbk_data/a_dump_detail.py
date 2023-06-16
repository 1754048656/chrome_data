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
            'VEE': 'wikitext',
            'Hm_lvt_8e1450316c96d3e524f02e4c301c03a2': '1685949150,1685967300',
            'Hm_lpvt_8e1450316c96d3e524f02e4c301c03a2': '1685967715',
        }
        self.headers = {
            'authority': 'www.yixue.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'VEE=wikitext; Hm_lvt_8e1450316c96d3e524f02e4c301c03a2=1685949150,1685967300; Hm_lpvt_8e1450316c96d3e524f02e4c301c03a2=1685967715',
            'referer': 'https://www.yixue.com/index.php?title=%E5%88%86%E7%B1%BB:%E5%85%A8%E8%BA%AB%E7%97%87%E7%8A%B6&pagefrom=%E5%AE%9D%E5%AE%9D%E7%BC%BA%E4%B9%8F%E5%AE%89%E5%85%A8%E6%84%9F',
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

        # with open("dis_url.txt", 'r', encoding='utf-8') as file:
        with open("b_dis_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                json_line = json.loads(text_line)
                department = json_line['department']
                disease = json_line['disease']
                urlencode = json_line['urlencode']
                urlencode = urlencode.split('"/')[1]
                print('department => ' + department)
                print('disease => ' + disease)
                print('urlencode => ' + urlencode)

                try:
                    self.getTwoDepartmentList(urlencode, department, disease)
                    time.sleep(3)
                except Exception as e:
                    print(e)
                    self.write2File('c_error_line.txt', item)
                    print('------error_line------')


    def getTwoDepartmentList(self, urlencode, department, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        'https://www.yixue.com/index.php?title=Asperger%E7%BB%BC%E5%90%88%E5%BE%81&action=edit'
        text_url = 'https://www.yixue.com/index.php?title=' + urlencode + '&action=edit'
        print('text_url => ' + text_url)
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )

        time.sleep(1.5)
        res_text = response.text

        # json_tmp = {}
        # json_tmp['department'] = department
        # json_tmp['disease'] = disease
        # json_tmp['detail_list'] = []
        # json_tmp['keywords_list'] = []

        #name="wpTextbox1">(.*?)</textarea>
        res = re.compile('name="wpTextbox1">(.*?)</textarea>', re.S).findall(res_text)[0]
        # print(res)
        print('-------------')

        json_line = {}

        json_line['department'] = department
        json_line['disease'] = disease
        json_line['detail_list'] = []
        json_line['keywords_list'] = []

        if '\n==' in res:
            first_content = res.split('\n==')[0]
            # print('first_content => ' + first_content)
            json_l = {}
            first_content = first_content.strip('\n')
            first_content = first_content.replace('\n\n', '')
            first_content = first_content.replace('[[', '')
            first_content = first_content.replace(']]', '')
            json_l['简介'] = first_content
            json_line['detail_list'].append(json_l)

            last_content = ''
            if res.count('\n==') >= 2:
                last_list = res.split('\n==')
                last_content = last_list[len(last_list) - 1]
                if '参看==' in last_content:
                    last_content = '-1'
            # print('last_content => ' + last_content)
            if last_content != '-1':
                json_p = {}
                last_content = last_content.strip('\n')
                last_content = last_content.replace('\n\n', '')
                last_content = last_content.replace('[[', '')
                last_content = last_content.replace(']]', '')
                json_p['end'] = last_content
                json_line['detail_list'].append(json_p)

        # 替换三个 = 的
        res = res.replace('===', '')
        res = res.replace('&lt;br />', '')
        # detail_info = re.compile('===(.*?)===', re.S).findall(res)
        # for detail_info_item in detail_info:
        #     # print('detail_info_item => ' + detail_info_item)
        #     # 替换符号
        #     regex = re.compile('==' + detail_info_item + '==')
        #     res = regex.sub('==' + detail_info_item + '>>', res)

        # print('res => ' + res)
        # ==Asperger综合征的原因==
        detail_info = re.compile('==(.*?)==', re.S).findall(res)
        for detail_info_item in detail_info:
            # print('detail_info_item => ' + detail_info_item)
            # 替换符号
            regex = re.compile('==' + detail_info_item + '==')
            res = regex.sub('==' + detail_info_item + '>>', res)
        # print(res)


        tmp_info = res.split('==')
        tmp_info.pop(0)
        for tmp_info_item in tmp_info:
            if '参看>>' in tmp_info_item:
                continue
            # print('tmp_info_item => ' + tmp_info_item)
            tmp_title = tmp_info_item.split('>>')[0]
            tmp_content = tmp_info_item.split('>>')[1]

            json_m = {}
            tmp_content = tmp_content.strip('\n')
            tmp_content = tmp_content.replace('\n\n', '')
            tmp_content = tmp_content.replace('[[', '')
            tmp_content = tmp_content.replace(']]', '')
            json_m[tmp_title] = tmp_content
            json_line['detail_list'].append(json_m)






        #[[综合征]]
        res_list = re.compile('\[\[(.*?)]]', re.S).findall(res)
        for res_list_item in res_list:
            if '分类:全身症状' in res_list_item:
                continue
            # print('res_list_item => ' + res_list_item)
            json_line['keywords_list'].append(res_list_item)

        json_str = json.dumps(json_line, ensure_ascii=False)
        print(json_str + '\n')

        self.write2File('c_yxbk_data.txt', json_str + '\n')

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()