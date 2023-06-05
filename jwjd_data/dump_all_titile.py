import requests
import re
import random
import uaList

class DumpAllTitle:
    def __init__(self):
        self.nameList = []
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

        with open("keshi.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[2]
                text_url = text_line.split(' => ')[1]

                #https://www.familydoctor.com.cn/q/9/d
                text_url = text_url.split('category/')[1]
                text_url = text_url.replace('/', '')
                text_url = 'https://www.familydoctor.com.cn/q/' + text_url + '/d'
                print(text_url)
                self.getTwoDepartmentList(text_url, one_department, two_department)


    def getTwoDepartmentList(self, text_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )
        # print(response.text)
        # <a href="https://www.familydoctor.com.cn/ask/did/728">麦粒肿</a>
        # https://www.familydoctor.com.cn/ask/did/728?page=1&
        disease = re.compile('<a href="https://www.familydoctor.com.cn/ask/did/(.*?)</a>', re.S).findall(response.text)
        for disease_item in disease:
            # 728">麦粒肿
            disease_name = disease_item.split('">')[1]
            disease_url = disease_item.split('">')[0]
            disease_url = 'https://www.familydoctor.com.cn/ask/did/' + disease_url + '?page=1'
            print(disease_name)

            text_line = one_department + ' => ' + two_department + ' => ' + disease_name + ' => ' + disease_url
            self.write2File('disease.txt', text_line + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()