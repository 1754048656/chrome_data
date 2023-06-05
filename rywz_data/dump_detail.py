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
            'PHPSESSID': '4e2vc32j1oim7kv23m1a92ohnd4re8fu',
            '6Dly_2132_saltkey': 'uU60B20B',
            '6Dly_2132_lastvisit': '1685692423',
            'Hm_lvt_f838732f69e738aab432abc4b4f201ac': '1685696043',
            '6Dly_2132_sid': 'o8DZff',
            '6Dly_2132_lastact': '1685704636%09finddoctor.php%09',
            'Hm_lpvt_f838732f69e738aab432abc4b4f201ac': '1685704657',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': 'PHPSESSID=4e2vc32j1oim7kv23m1a92ohnd4re8fu; 6Dly_2132_saltkey=uU60B20B; 6Dly_2132_lastvisit=1685692423; Hm_lvt_f838732f69e738aab432abc4b4f201ac=1685696043; 6Dly_2132_sid=o8DZff; 6Dly_2132_lastact=1685704636%09finddoctor.php%09; Hm_lpvt_f838732f69e738aab432abc4b4f201ac=1685704657',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.renyiwenzhen.com/finddoctor.php?action=anjb&ckid=52',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        self.params = {
            'action': 'anjb',
            'ckid': '3',
        }
        with open("dis_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                print(text_line)
                department = text_line.split(' => ')[0]
                disease = text_line.split(' => ')[1]
                url_text = text_line.split(' => ')[2]

                print('url_text => ' + url_text)
                print('department => ' + department)
                print('disease => ' + disease)

                for m in range(30):
                    try:
                        self.getTwoDepartmentList(url_text, department, disease)
                        time.sleep(4)
                        break
                    except Exception as e:
                        print(e)
                    time.sleep(18)
                    print('------wait------')

    def getTwoDepartmentList(self,  url_text, deparment, disease):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        # self.params['ckid'] = ckid_text

        response = requests.get(
            url_text,
            cookies=self.cookies,
            headers=self.headers,
            verify=False,
            timeout=18
        )

        # print(response.text)

        #<div class="jmsg_m(.*?)</div>

        res_text = response.text.split('<div class="jmsg_t">')[1]
        # print('-------------------------------')
        # print(res_text)
        # print('-------------------------------')
        res_text = res_text.split('<div class="tipp">')[0]
        # print('res_text => ' + res_text)
        # disease_info = re.compile('div class="jmsg_m(.*?)</p></div>').findall(res_text)
        res_list = res_text.split('<div class="jmsg_m')
        res_list.pop(0)

        json_line = {}

        tab_list = [
            '概述',
            '症状',
            '病因',
            '检查',
            '治疗',
        ]

        json_line['department'] = deparment
        json_line['disease'] = disease

        n = 0
        for res_list_item in res_list:
            res_list_item = self.format_text(res_list_item)
            json_line[tab_list[n]] = res_list_item
            print(tab_list[n] + ' => \n' + res_list_item)
            print('--------------------')

            n = n+1

        json_tmp = json.dumps(json_line, ensure_ascii=False)
        print(json_tmp)
        self.write2File('rywz_detail.txt', json_tmp + '\n')
        #
        # print('len(disease_info) => ' + str(len(disease_info)))
        # n = 0
        # for disease_info_item in disease_info:
        #     print('disease_info_item => ' + disease_info_item)
        #     # print('tab_list[n] => ' + tab_list[n])
        #     # self.write2File('dis_detail.txt', text_line + '\n')
        #     n = n + 1

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

    def format_text(self, topic_header_text):

        # 去掉尖括号
        # regex = re.compile('<(.*?)>')
        # topic_header_text = regex.sub('', topic_header_text)

        # 去掉末尾的
        # topic_header_text = topic_header_text.split('<')[0]
        # topic_header_text = topic_header_text.split('$(document)')[0]

        # '      '
        # topic_header_text = topic_header_text.replace('      ', '，')
        # topic_header_text = topic_header_text.replace('     ', '，')
        # topic_header_text = topic_header_text.replace('    ', '，')
        # topic_header_text = topic_header_text.replace('   ', '，')
        # topic_header_text = topic_header_text.replace('  ', '，')
        topic_header_text = topic_header_text.replace('</div>', '')
        topic_header_text = topic_header_text.replace('<p>', '')
        topic_header_text = topic_header_text.replace('</p>', '')

        # topic_header_text = topic_header_text.replace('  ', '')
        # topic_header_text = topic_header_text.replace('&nbsp;', '')
        # topic_header_text = topic_header_text.replace('\n', '')
        # topic_header_text = topic_header_text.replace('，、 ', '、')
        # topic_header_text = topic_header_text.replace('，, ', '，')
        # topic_header_text = topic_header_text.replace('。，', '。')
        # topic_header_text = topic_header_text.replace('，。', '。')
        # topic_header_text = topic_header_text.replace('，，', '，')
        # topic_header_text = topic_header_text.replace('：，', '：')
        # topic_header_text = topic_header_text.replace('，）', '）')
        # topic_header_text = topic_header_text.replace('），', '）')
        # topic_header_text = topic_header_text.replace('，)，', ')，')
        # topic_header_text = topic_header_text.replace('，)。', ')。')
        # topic_header_text = topic_header_text.strip()
        topic_header_text = topic_header_text.strip('">')
        topic_header_text = topic_header_text.strip()

        if 'gon">' in topic_header_text:
            topic_header_text = topic_header_text.split('gon">')[1]

        return topic_header_text


DumpTitle()