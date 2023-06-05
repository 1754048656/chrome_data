import requests
import re
import random
import uaList

class DumpAllTitle:
    def __init__(self):
        self.cookies = {
            '__finger': '26bb9371cd9266cac533d4f42f1fd18c',
        }

        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': '__finger=26bb9371cd9266cac533d4f42f1fd18c',
            'Referer': 'https://wenda.familydoctor.com.cn/question/all/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }


        # with open("href.txt", 'r', encoding='utf-8') as file:
        #     for item in file:
        #         text_line = item.strip()
        #         text_url = text_line.split(' => ')[0]
        #         one_department = text_line.split(' => ')[1]
        #
        #         self.getJiBingList(text_url, one_department)

        with open("href_keshi.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                one_department = text_line.split(' => ')[0]
                two_department = text_line.split(' => ')[1]
                text_url = text_line.split(' => ')[2]

                self.getJiBingList(text_url, one_department, two_department)


    def getJiBingList(self, text_url, one_department, two_department):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
        )

        #<div class="cate fl">二级科室</div>
        #     <div class="room fl">
        #         <a href="https://wenda.familydoctor.com.cn/question/keshi/1/"  >不限</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/30/"  class="on">呼吸内科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/31/"  >心血管内科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/32/"  >神经内科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/33/"  >消化内科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/34/"  >内分泌科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/35/"  >风湿免疫科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/36/"  >肾内科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/37/"  >呼吸睡眠中心</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/38/"  >血液病科</a>
        #                 <a href="https://wenda.familydoctor.com.cn/question/keshi/39/"  >普内科</a>
        #     </div>
        # </div>
        # <div class="cate-room clear clearfix">
        # /keshi/32/"  >神经内科</a>
        # two_department_text = re.compile('<div class="cate fl">二级科室</div>(.*?)<div class="cate-room clear clearfix">', re.S).findall(response.text)
        # if len(two_department_text) > 0:
        #     # print('two_department_text => Y')
        #     keshiList = re.compile('keshi/(.*?)</a>', re.S).findall(two_department_text[0])
        #     for keshiList_item in keshiList:
        #         keshiTmp = keshiList_item.split('/"  >')
        #         if 'class="hide' in keshiList_item:
        #             keshiTmp = keshiList_item.split('/"  class="hide ">')
        #         if '不限' not in keshiTmp[0]:
        #             keshiList_item = keshiTmp[0]
        #             two_department = keshiTmp[1]
        #             keshiList_item = 'https://wenda.familydoctor.com.cn/question/keshi/' + keshiList_item
        #             tmp = one_department + ' => ' + two_department + ' => ' + keshiList_item + '\n'
        #             print(tmp)
        #             self.write2File('href_keshi.txt', tmp)
        # else:
        #     keshiList = re.compile('keshi/(.*?)/', re.S).findall(text_url)
        #     for keshiList_item in keshiList:
        #         keshiList_item = 'https://wenda.familydoctor.com.cn/question/keshi/' + keshiList_item
        #         tmp = one_department + ' => ' + one_department + ' => ' + keshiList_item + '\n'
        #         print(tmp)
        #         self.write2File('href_keshi.txt', tmp)






        # jibing/3257/"  >矽肺</a>
        # jibing/(.*?)</a>
        res = re.compile('jibing/(.*?)</a>', re.S).findall(response.text)
        for res_item in res:
            # 去掉<>
            regex = re.compile('/\"(.*?)>')
            res_item = regex.sub(' => ', res_item)
            res_item = one_department + ' => ' + two_department + ' => ' + res_item
            print(res_item)
            self.write2File('href_jibing_one_two.txt', res_item + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

DumpAllTitle()

#https://wenda.familydoctor.com.cn/question/questiondatalist.do/jibing/5/1/10000/