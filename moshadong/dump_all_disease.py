import json
import time

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

        with open("a_msd_title.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                json_line = json.loads(text_line)
                sub_list = json_line['sub']
                print(json_line)
                sub_label = 'yes'
                for sub_list_item in sub_list:
                    # print('-----------*************************************-----------')
                    # print('sub_list_item => ' + str(sub_list_item))
                    sub_title_url = sub_list_item['sub_title_url']
                    print('sub_title_url => ' + sub_title_url)

                    sub_list_item = self.deep_method(sub_title_url, sub_list_item)
                    print('sub_list_item => ' + str(sub_list_item))
                    print('-----------*************************************-----------')
                    if sub_list_item == 'no':
                        sub_label = 'no'
                        break

                if sub_label == 'yes':
                    self.write2File('a_msd_detail.txt', json.dumps(json_line, ensure_ascii=False) + '\n')
                else:
                    self.write2File('b_msd_detail_error.txt', text_line)

    def deep_method(self, sub_title_url, sub_list_item):
        topic__accordion = ''

        for i in range(20):
            self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
            print('User-Agent => ' + self.headers['User-Agent'])
            try:
                response = requests.get(
                    sub_title_url,
                    cookies=self.cookies,
                    headers=self.headers,
                    timeout=9
                )
                # <div class="topic__accordion"><section class="topic__section">
                topic__accordion = re.compile('topic__accordion">(.*?)<section class="topic__section">', re.S).findall(response.text)[0]
                break
            except Exception as e:
                print(e)
            time.sleep(12)
        if topic__accordion != '':
            topic__accordion = topic__accordion.strip()
            sub_content = ''
            # 如果不包含 topic__header--section 则直接去掉尖括号
            if 'topic__header--section'not in topic__accordion:
                sub_content = self.format_text(topic__accordion)
                sub_list_item['sub_content'] = sub_content

            else:
                # 拿出第一个再去掉尖括号
                topic_header_text = topic__accordion.split('topic__header--section')[0]
                sub_content = self.format_text(topic_header_text)
                sub_list_item['sub_content'] = sub_content

                sub_list_item = self.getTopicHeaders(topic__accordion, sub_list_item)

            time.sleep(4)
            return sub_list_item
        else:
            return 'no'


    def write2File(self, file_name, text):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(text)

    def getTopicHeaders(self, topic__accordion, sub_list_item):
        topic_header_list = topic__accordion.split('topic__header--section')
        topic_header_list.pop(0)
        print('=======================================')
        sub_list_item['third_list'] = []
        sub_list_item.pop('third')
        for topic_header_list_item in topic_header_list:
            topic_name = topic_header_list_item.split('</h2>')[0]
            topic_name = topic_name.split('</span>')[1]
            # 去掉尖括号
            regex = re.compile('<(.*?)>')
            topic_name = regex.sub('', topic_name)
            topic_name = topic_name.strip()

            third_json = {}
            third_json['third_title'] = topic_name
            print('topic_name => ' + topic_name)
            topic_content = topic_header_list_item.split('</h2>')[1]

            # 如果不包含 topic__header--subsection 则直接去掉尖括号
            if 'topic__header--subsection' not in topic_content:
                topic_content = self.format_text(topic_content)
                print('topic_content => ' + topic_content)
                third_json['third_content'] = topic_content

            else:
                # 拿出第一个再去掉尖括号
                tmp_topic_content = topic_content.split('topic__header--subsection')[0]
                tmp_topic_content = self.format_text(tmp_topic_content)
                print('topic_content => ' + tmp_topic_content)
                third_json['third_content'] = tmp_topic_content
                third_json = self.getSubTopicHeaders(topic_content, third_json)
            sub_list_item['third_list'].append(third_json)


        sub_list_item_tmp = json.dumps(sub_list_item, ensure_ascii=False)
        print(sub_list_item_tmp)
        return sub_list_item

    def format_text(self, topic_header_text):
        # 去掉<span class="tooltip-content">(.*?)</a>
        regex = re.compile('<span class="tooltip-content">(.*?)</a>')
        topic_header_text = regex.sub('', topic_header_text)

        # 去掉尖括号
        regex = re.compile('<(.*?)>')
        topic_header_text = regex.sub('', topic_header_text)

        # 去掉末尾的
        topic_header_text = topic_header_text.split('<')[0]
        topic_header_text = topic_header_text.split('$(document)')[0]

        # '      '
        topic_header_text = topic_header_text.replace('      ', '，')
        topic_header_text = topic_header_text.replace('     ', '，')
        topic_header_text = topic_header_text.replace('    ', '，')
        topic_header_text = topic_header_text.replace('   ', '，')
        topic_header_text = topic_header_text.replace('  ', '，')
        topic_header_text = topic_header_text.replace('，、 ', '、')
        topic_header_text = topic_header_text.replace('，, ', '，')
        topic_header_text = topic_header_text.replace('。，', '。')
        topic_header_text = topic_header_text.replace('，。', '。')
        topic_header_text = topic_header_text.replace('，，', '，')
        topic_header_text = topic_header_text.replace('：，', '：')
        topic_header_text = topic_header_text.replace('，）', '）')
        topic_header_text = topic_header_text.replace('），', '）')
        topic_header_text = topic_header_text.replace('，)，', ')，')
        topic_header_text = topic_header_text.replace('，)。', ')。')
        topic_header_text = topic_header_text.strip()
        topic_header_text = topic_header_text.strip('，')

        return topic_header_text

    def getSubTopicHeaders(self, topic_content, third_json):
        topic_header_list = topic_content.split('topic__header--subsection')
        topic_header_list.pop(0)

        third_json['forth'] = []

        for topic_header_list_item in topic_header_list:
            #</span> 荚膜 </h3>
            topic_sub_name = re.compile('</span>(.*?)</h3>', re.S).findall(topic_header_list_item)[0]
            topic_sub_name = topic_sub_name.strip()
            forth_json = {}
            forth_json['forth_title'] = topic_sub_name
            print('topic_sub_name => ' + topic_sub_name)

            topic_sub_content = topic_header_list_item.split('</h3>')[1]
            topic_sub_content = self.format_text(topic_sub_content)
            forth_json['forth_content'] = topic_sub_content
            print('topic_sub_content => ' + topic_sub_content)
            print('---------------------------------------')
            third_json['forth'].append(forth_json)

        return third_json


DumpAllTitle()