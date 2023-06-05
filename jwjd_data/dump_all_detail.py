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
        self.error_num = 0
        with open('jwjd_href' + str(var.server_num) + '.txt', 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                # one_department = text_line.split(' => ')[0]
                # two_department = text_line.split(' => ')[1]
                # text_disease = text_line.split(' => ')[2]
                # text_url = text_line.split(' => ')[4]
                try:
                    json_tmp = json.loads(text_line)
                except Exception as e:
                    print(e)
                    print('get error')
                    continue
                one_department = json_tmp['one_department']
                two_department = json_tmp['two_department']
                text_disease = json_tmp['text_disease']
                text_url = json_tmp['question_href']
                print(text_url)
                # try:
                #     self.getTwoDepartmentList(text_url, one_department, two_department, text_disease)
                # except Exception as e:
                #     self.write2File('b_jwjd_error_' + str(var.server_num) + '.txt',
                #                     text_line + '\n')
                #     print(e)
                #     self.error_num = self.error_num + 1
                # time.sleep(1)

                for t in range(30):
                    try:
                        res = self.getTwoDepartmentList(text_url, one_department, two_department, text_disease)
                        if res == 'delete':
                            print('-------delete-------')
                            time.sleep(4)
                            break
                        if res == 'hh':
                            time.sleep(18)
                            print('---------hh------')
                            continue
                        time.sleep(4)
                        break
                    except Exception as e:
                        print(e)
                        print('-------other error------' + str(t))
                        self.write2File('b_jwjd_error_' + str(var.server_num) + '.txt', text_line + '\n')
                        time.sleep(4)
                        break


        # self.getTwoDepartmentList('https://www.familydoctor.com.cn/ask/v/507320786.html', '', '', '')

    def getTwoDepartmentList(self, text_url, one_department, two_department, text_disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=8
        )

        if '您所提问的问题已经删除' in response.text:
            return 'delete'

        try:
            #问题
            #<h3 class="quest-title">请问得了麦粒肿这是怎么回事？</h3>
            question_detail = re.compile('<h3 class="quest-title">(.*?)</h3>', re.S).findall(response.text)[0]
            question_detail = question_detail.strip()
        except Exception as e:
            print(e)
            return 'hh'

        if '...' in question_detail:
            question_detail = re.compile('<label>问题：</label>(.*?)</p>', re.S).findall(response.text)[0]
            #<label>问题：</label>
            # <p>
            #     躺下后脑不晕，坐着差点，走路晕（后脑晕）厉害，后脑有沙子响，易心慌，胸闷，气短，两腿无力，X光显示颈椎1234不稳，经颅多普勒显示-椎动脉缺血，请问能影响交感神经吗？
            # </p>
            question_detail = question_detail.split('<p>')[1]
            question_detail = question_detail.strip()
            print('question_detail_1 => ' + question_detail)
        else:
            print('question_detail_0 => ' + question_detail)


        list_final = []
        list_tmp = []
        #答案
        #<a href="https://www.familydoctor.com.cn/ask/doctor/173429" class="answer-doctor">
        #     <em>
        #         <img src="https://img.familydoctor.com.cn/ku/20130830/201308300328117204.jpg" />
        #     </em>
        #     <p>王庆松  医师</p>
        # </a>
        # <a href="http://yyk.familydoctor.com.cn/20137/" class="answer-doctor">
        #     <p>家庭医生在线合作医院 </p>
        #     <p>其他</p>
        #       <p style="color:#00af80">全科</p>
        # </a>
        doctor_info = re.compile('<dl class="answer-info-cont">(.*?)</dt>', re.S).findall(response.text)
        if len(doctor_info) > 0:
            for doctor_info_item in doctor_info:
                json_line = {}
                # print(doctor_info_item)
                doctor_info_item_text = re.compile('<p>(.*?)</p>', re.S).findall(doctor_info_item)

                doctor_name = doctor_info_item_text[0]
                doctor_hospital_label = ''
                doctor_hospital = ''
                if len(doctor_info_item_text) == 3:
                    doctor_hospital_label = doctor_info_item_text[2]
                    doctor_hospital = doctor_info_item_text[1]
                if len(doctor_info_item_text) == 2:
                    #doctor_hospital_label = doctor_info_item_text[2]
                    doctor_hospital = doctor_info_item_text[1]

                doctor_label = re.compile('<p style="color:(.*?)</p>', re.S).findall(doctor_info_item)[0]
                doctor_label = doctor_label.split('>')[1]
                json_line['one_department'] = one_department
                json_line['two_department'] = two_department
                json_line['text_disease'] = text_disease
                json_line['doctor_name'] = doctor_name
                json_line['doctor_label'] = doctor_label
                json_line['doctor_hospital'] = doctor_hospital
                json_line['doctor_hospital_label'] = doctor_hospital_label

                json_line['question'] = question_detail
                list_tmp.append(json_line)
                # print(json_line)

        # 如果有两个答案，就存成两条
        # <p class="answer-words">麦粒肿，它是属于眼睑腺体的一种比较急性化脓性炎症，得了麦粒肿，那么切忌的是进行挤压或者是用未消毒的针挑，还有就是过早切开。这是因为眼睑血管是比较丰富的，还有就是其静脉和眼眶静脉以及颜面静脉，它们是相通的，而且没有静脉瓣可以阻止其血液的回流，与此同时又与颅腔静脉相通，假如炎症一旦扩散的话，轻者引起眶蜂窝织炎，那么重者就会导致海绵窦血栓形成败血症。</p>
        # <p class="answer-words">(.*?)</p>
        answer = re.compile('<p class="answer-words">(.*?)</p>', re.S).findall(response.text)
        if len(answer) > 0:
            i = 0
            for answer_item in answer:
                # print(answer_item)
                json_line_tmp = list_tmp[i]
                answer_item = answer_item.strip()
                json_line_tmp['answer'] = answer_item
                list_final.append(json_line_tmp)
                i = i + 1

        for list_final_item in list_final:
            print(list_final_item)

            self.write2File('jwjd_QA_' + str(var.server_num) + '.txt', json.dumps(list_final_item, ensure_ascii=False) + '\n')

        time.sleep(1)

    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)



DumpAllTitle()