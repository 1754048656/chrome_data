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
            'RK': 'ktH07f4JQs',
            'ptcz': 'f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15',
            'bk_token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
            'bk_uin': '3000001307478811',
        }
        self.headers = {
            '17a3c89965b3': '7e0a51b7',
            '236a604fb8a6': '1685531281292',
            '94b9f47267ea': 'dac172b777777efcdfc493869fac085592309c5c',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': 'Bearer 130bb675-694e-405a-88a7-a17d3a38912d-yk',
            'Connection': 'keep-alive',
            # 'Cookie': 'RK=ktH07f4JQs; ptcz=f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15; bk_token=130bb675-694e-405a-88a7-a17d3a38912d-yk; bk_uin=3000001307478811',
            'Origin': 'https://h5.baike.qq.com',
            'Referer': 'https://h5.baike.qq.com/mobile/overview_detail.html?id=sy20844010zya6kf&name=%E4%B9%8F%E5%8A%9B&m=e95bfa918211c355909c512dc6b7d047&m=e95bfa918211c355909c512dc6b7d047&tab=gaishu&searchid=1e8d0071b86b4da73e3829a54017de2f&VNK=311b81c4&TNK=f29c1e3c',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'content-type': 'application/json',
            'd5ccfadd2a55': 'e416355c070fd96435360b23cbdc49af7bb48a76',
            'f6ff59b173b4': '0',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'x-tde-env-id': '',
        }

        self.params = {
            'timestamp': '1685602121834',
        }

        self.json_data = {
            'header': {
                'version': 2,
                'flag': 0,
            },
            'body': {
                'seq': 96,
                'cmd': 'BatchGetDiseaseTabData',
                'token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
                'client': {
                    'platform': 1,
                    'os': 0,
                    'env': '',
                    'isTourist': 49,
                    'adtag': '',
                    'vnk': 'f29c1e3c#gaishu',
                    'product': 8,
                },
                'payload': {
                    'tabs': [
                        '概述',
                        '病因',
                        '表现',
                        '就医',
                        '治疗',
                        '防护',
                    ],
                    'disease': '',
                    'id': 'sy10745010lprfi4',
                },
                # 'traceid': '4f9a1aa3-51b6-485d-9ffd-bafa417ec83e',
                'traceid': '0bbd3884-0a2f-4ccf-a751-80be672cc5f8',
            },
        }

        # file = open("res.txt", "r", encoding="utf-8")
        # data = file.read()
        # # print(data)
        # data_info = data.split('symptoms: [')
        # for data_info_item in data_info:
        #     # print(data_info_item)
        #     name_info = re.compile('name: "(.*?)"').findall(data_info_item)
        #
        #     department = name_info.pop()
        #     for name_info_item in name_info:
        #         json_line = {}
        #         json_line['department'] = department
        #         # print('name_info_item => ' + name_info_item)
        #         json_line['disease'] = name_info_item
        #         print('-----------------------------')
        #         print('json_line => ' + str(json_line))
        #         tmp_line = json.dumps(json_line, ensure_ascii=False)
        #         self.write2File('href_dis.txt', tmp_line + '\n')
        #
        # file.close()

        with open("id_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)
                json_line = json.loads(text_line)

                for i in range(40):
                    try:
                        self.getTwoDepartmentList(json_line)
                        time.sleep(4)
                        break
                    except Exception as e:
                        print(e)

                    time.sleep(18)

    def getTwoDepartmentList(self,  json_tmp):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        self.json_data['body']['payload']['id'] = json_tmp['id']
        print('json_data => ' + json.dumps(self.json_data, ensure_ascii=False))
        response = requests.post(
            'https://h5.baike.qq.com/api/access/json/cmd/BatchGetDiseaseTabData',
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            json=self.json_data,
            timeout=28
        )
        time.sleep(1.5)

        # print(response.text)
        json_line = response.json()
        tabsData = json_line['body']['payload']['tabsData']

        # json_tmp = {}
        # json_tmp['department'] = json_line['department']
        # json_tmp['disease'] = json_line['disease']
        list_tabs = ['防护', '治疗', '病因', '表现', '概述', '就医']
        for list_tabs_item in list_tabs:
            md_text = tabsData[list_tabs_item]['tabData']['tid4']['md_text']
            if md_text == '':
                md_text = tabsData[list_tabs_item]['tabData']['tid0']['md_definition']

            md_text = self.format_text(md_text)
            json_tmp[list_tabs_item] = md_text
            print('md_text => ' + list_tabs_item + ' => ' + md_text)

        # print('tabsData => ' + json.dumps(tabsData, ensure_ascii=False))
        json_text = json.dumps(json_tmp, ensure_ascii=False)
        self.write2File('txyd_detail.txt', json_text + '\n')



        # content_info = re.compile('{"contentId": "(.*?)", "udNum"').findall(json_text)
        # for content_info_item in content_info:
        #     print('content_info_item => ' + content_info_item)
        #     url_href = content_info_item.split('", "name": "')[0]
        #     dis_name = content_info_item.split('", "name": "')[1]
        #     line_tmp = text_line + ' => ' + dis_name + ' => https://www.baidu.com/bh/dict/' + url_href + '?from=dicta&sf_ref=med_pc&sf_ch=ch_med_pc'
        #     self.write2File('dis_url.txt', line_tmp + '\n')

        # print('res_json => ' + json_text)

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


    def format_text(self, topic_header_text):

        # 去掉尖括号
        regex = re.compile('<(.*?)>')
        topic_header_text = regex.sub('', topic_header_text)

        # 去掉末尾的
        # topic_header_text = topic_header_text.split('<')[0]
        # topic_header_text = topic_header_text.split('$(document)')[0]

        # '      '
        # topic_header_text = topic_header_text.replace('      ', '，')
        # topic_header_text = topic_header_text.replace('     ', '，')
        # topic_header_text = topic_header_text.replace('    ', '，')
        # topic_header_text = topic_header_text.replace('   ', '，')
        # topic_header_text = topic_header_text.replace('  ', '，')
        topic_header_text = topic_header_text.replace('	', '')
        # topic_header_text = topic_header_text.replace('  ', '')
        topic_header_text = topic_header_text.replace('&nbsp;', '')
        topic_header_text = topic_header_text.replace('\n', '')
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
        topic_header_text = topic_header_text.strip()
        topic_header_text = topic_header_text.strip('，')

        return topic_header_text

DumpTitle()