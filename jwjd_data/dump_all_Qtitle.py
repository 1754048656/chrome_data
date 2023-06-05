import json
import time

import requests
import re
import random
import uaList
import var


class DumpAllTitle:
    def __init__(self):
        self.nameList = []
        self.tmpNum = 0
        self.cookies = {
            '__bid_n': '1882f0c91a42fba82f4207',
            'Hm_lvt_f46dd4cc550b93aefde9b00265bb533d': '1684411712,1684460792,1684562420',
            '__finger': 'dffc58f4fc8ff7ac5cc47140db9690ff',
            '__customer_area': '%7B%22id%22%3A%20328%2C%20%22pid%22%3A%20257%7D',
            'Hm_lvt_821f19fe5c3397f5b5ef53c7b38cd53a': '1684416533,1684460792,1684562486',
            'FPTOKEN': 'h8bW4dP8wKK0yDmG34ZuNDoqS68zlAo+vBPs5uU7xz11xldV6PIED3+DxVuembRzxtQsOyUp48TvayjVB5xWIazJ3XdyUL/byVwDDAnyRnPxrbmp7SVOVCfwEvbnAosstXxwSFEp3y90jhX2gEiytN+WOFs9J+7fevx6lW/3TBBuHq2uUWw46NLv5mVtRdPEDoYofI+u5R89X/bmVtj8VMDXbxLgRG+go3ENLg1HWg7jcLP1CHedo065TmqMMD99N+DibI28jJmhVtWub5aRyTprHyy5FRzV4nT77Y0rpPLQq9AA8BoTK6ofZgEdu25nNyku8AWNp/sSGKkuiRlFBAk8uy6KWyFzDlDoKnqdy6xhGN3srG1sS5+joZYuGCrhjtBqIclOmaqkg0PoO7DCRw==|jk+CJ0+44KEKm899CWJll0vg54wJvDdkhO124o2zRsA=|10|c3673e9875ef97c7773c48efc67b8a75',
            'Hm_lvt_c921245921d111cf1fa20405202aa5d7': '1684562682',
            'Hm_lpvt_c921245921d111cf1fa20405202aa5d7': '1684562682',
            'Hm_lvt_7b02d24f7ab152a2a63a4bd73dd61f30': '1684562701',
            'Hm_lpvt_7b02d24f7ab152a2a63a4bd73dd61f30': '1684562712',
            'Hm_lpvt_f46dd4cc550b93aefde9b00265bb533d': '1684563798',
            'Hm_lpvt_821f19fe5c3397f5b5ef53c7b38cd53a': '1684563798',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '__bid_n=1882f0c91a42fba82f4207; Hm_lvt_f46dd4cc550b93aefde9b00265bb533d=1684411712,1684460792,1684562420; __finger=dffc58f4fc8ff7ac5cc47140db9690ff; __customer_area=%7B%22id%22%3A%20328%2C%20%22pid%22%3A%20257%7D; Hm_lvt_821f19fe5c3397f5b5ef53c7b38cd53a=1684416533,1684460792,1684562486; FPTOKEN=h8bW4dP8wKK0yDmG34ZuNDoqS68zlAo+vBPs5uU7xz11xldV6PIED3+DxVuembRzxtQsOyUp48TvayjVB5xWIazJ3XdyUL/byVwDDAnyRnPxrbmp7SVOVCfwEvbnAosstXxwSFEp3y90jhX2gEiytN+WOFs9J+7fevx6lW/3TBBuHq2uUWw46NLv5mVtRdPEDoYofI+u5R89X/bmVtj8VMDXbxLgRG+go3ENLg1HWg7jcLP1CHedo065TmqMMD99N+DibI28jJmhVtWub5aRyTprHyy5FRzV4nT77Y0rpPLQq9AA8BoTK6ofZgEdu25nNyku8AWNp/sSGKkuiRlFBAk8uy6KWyFzDlDoKnqdy6xhGN3srG1sS5+joZYuGCrhjtBqIclOmaqkg0PoO7DCRw==|jk+CJ0+44KEKm899CWJll0vg54wJvDdkhO124o2zRsA=|10|c3673e9875ef97c7773c48efc67b8a75; Hm_lvt_c921245921d111cf1fa20405202aa5d7=1684562682; Hm_lpvt_c921245921d111cf1fa20405202aa5d7=1684562682; Hm_lvt_7b02d24f7ab152a2a63a4bd73dd61f30=1684562701; Hm_lpvt_7b02d24f7ab152a2a63a4bd73dd61f30=1684562712; Hm_lpvt_f46dd4cc550b93aefde9b00265bb533d=1684563798; Hm_lpvt_821f19fe5c3397f5b5ef53c7b38cd53a=1684563798',
            'If-Modified-Since': 'Sat, 13 May 2023 10:32:33 GMT',
            'Referer': 'https://www.familydoctor.com.cn/ask/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.page_n = 11141
        with open("dis_" + str(var.server_num) + ".txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                text_disease = text_line.split(' => ')[2]
                text_url = text_line.split(' => ')[3]

                print(text_url)
                self.getTwoDepartmentList(text_url, one_department, two_department, text_disease, text_line)
                self.page_n = 1

    def getTwoDepartmentList(self, text_url, one_department, two_department, text_disease, text_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=28
        )

        try:
            page_size_info = re.compile('下一页</a>(.*?)&amp;" target="_self">尾页</a>', re.S).findall(response.text)[0]
            page_size = page_size_info.split('page=')[1]
        except Exception as e:
            page_size = '1'
            print(e)
        for i in range(self.page_n, int(page_size) + 1):
            # https://www.familydoctor.com.cn/ask/did/87?page=1
            # 去掉<>
            regex = re.compile(r"page=\d+")
            text_url = regex.sub('page=' + str(i), text_url)
            print(text_url)

            for i in range(40):
                try:
                    self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
                    print('User-Agent => ' + self.headers['User-Agent'])
                    response_res = requests.get(
                        text_url,
                        cookies=self.cookies,
                        headers=self.headers,
                        timeout=28
                    )

                    # Q:</b><p><a href="https://www.familydoctor.com.cn/q/20350658.html">麦粒肿是什么症状</a></p>
                    question_info = re.compile('Q:</b><p><a href="(.*?)</a></p>', re.S).findall(response_res.text)
                    for question_info_item in question_info:
                        print(question_info_item)

                        self.getPageQuestion(question_info_item, one_department, two_department, text_disease)
                    time.sleep(6)
                    break
                except Exception as e:
                    time.sleep(15)
                    print(e)


    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

    def getPageQuestion(self, question_info_item, one_department, two_department, text_disease):
        question = question_info_item.split('">')[1]
        question_href = question_info_item.split('">')[0]
        json_line = {}
        json_line['one_department'] = one_department
        json_line['two_department'] = two_department
        json_line['text_disease'] = text_disease
        json_line['question'] = question
        json_line['question_href'] = question_href

        self.write2File('jwjd_href' + str(var.server_num) + '.txt', str(json_line).replace('\'', '\"') + '\n')
        self.tmpNum = self.tmpNum + 1
        print('tmpNum => ' + str(self.tmpNum))
        pass



DumpAllTitle()