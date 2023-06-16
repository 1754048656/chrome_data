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

        with open("res.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()

                url_tmp = text_line.split(' => ')[0]
                department = text_line.split(' => ')[1]
                print(url_tmp)
                print(department)

                self.getTwoDepartmentList(url_tmp, department)
                time.sleep(2)

    def getTwoDepartmentList(self, url_tmp, department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        session = requests.Session()  # 创建session
        response = session.get(url_tmp, cookies=self.cookies, headers=self.headers, timeout=8)
        res_text = response.text

        #<div class="select-dise select-depart posr clr mt-20">(.*?)</div>
        res_info = re.compile('<div class="select-dise select-depart posr clr mt-20">(.*?)</div>', re.S).findall(res_text)[0]
        # print(res_info)
        #<a class="sel-dep-sort-link  Js_listHide" style="display: none;" href="https://www.bohe.cn/voice/list/hot/2_22875.html">
        #     手术疤痕
        # </a>
        dis_name_list = re.compile('<a class="sel-dep-sort-link  Js_listHide" style="display: none;" href="(.*?)</a>', re.S).findall(res_info)
        for dis_name_list_item in dis_name_list:
            dis_name_list_item = dis_name_list_item.strip()
            dis_url = dis_name_list_item.split('">')[0].strip()
            dis_name = dis_name_list_item.split('">')[1].strip()
            # print(dis_url)
            # print(dis_name)

            line_tmp = department + ' => ' + dis_name + ' => ' + dis_url + '\n'
            print(line_tmp)
            self.write2File('dis_url.txt', line_tmp)



    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

DumpTitle()