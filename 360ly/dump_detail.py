import json
import time

from urllib import parse
import requests
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            'QiHooGUID': 'D6A0A64BB0C8CAE3EA2DF144E5CF6D3D.1685104120808',
            '__guid': '98597507.3715389439386620400.1685104131895.04',
        }
        self.headers = {
            'authority': 'ly.so.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            # 'cookie': 'QiHooGUID=D6A0A64BB0C8CAE3EA2DF144E5CF6D3D.1685104120808; __guid=98597507.3715389439386620400.1685104131895.04',
            'referer': 'https://ly.so.com/sku/yidian/index?tab=0&tab_type=%E6%8C%89%E7%A7%91%E5%AE%A4&content_type=%E7%96%BE%E7%97%85%E7%B1%BB&tab_value=%E7%94%B7%E7%A7%91',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        with open("b_dis_href.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                department = text_line.split(' => ')[0]
                dis_name = text_line.split(' => ')[1]

                disease = dis_name
                dis_name = parse.quote(dis_name)
                href_text = 'https://ly.so.com/api/v1/yidian/detail?cancelToken={"promise":{}}&contentName=&contentNameTerm=' + disease
                self.getTwoDepartmentList(href_text, department, dis_name, disease, text_line)
                time.sleep(2)

    def getTwoDepartmentList(self, href_text, department, dis_name, disease, text_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        self.headers['referer'] = 'https://ly.so.com/sku/yidian/index?tab=0&tab_type=%E6%8C%89%E7%A7%91%E5%AE%A4&content_type=%E7%96%BE%E7%97%85%E7%B1%BB&tab_value=' + dis_name
        print(href_text)
        print('User-Agent => ' + self.headers['User-Agent'])
        try:
            response = requests.get(
                href_text,
                cookies=self.cookies,
                headers=self.headers,
                timeout=28
            )
            time.sleep(1.5)
            json_line = response.json()
            tabList = json_line['data']['result']['tabs']['tab']
            # print(tabList)
            json_text = {}
            json_text['department'] = department
            json_text['disease'] = disease
            json_text['name_list'] = []

            print('department => ' + department)
            print('disease => ' + disease)
            for tabList_item in tabList:
                name = tabList_item['name']
                htmlContent = tabList_item['htmlContent']
                tmp_line = {}
                tmp_line['name'] = name
                tmp_line['name_content_list'] = []
                print('name => ' + name)
                # print('htmlContent => ' + htmlContent)
                h3_title_list = htmlContent.split('<h3>')
                h3_title_list.pop(0)
                for h3_title_list_item in h3_title_list:
                    tmp_line_line = {}
                    h3_title = h3_title_list_item.split('</h3>')[0]
                    h3_title = self.format_text(h3_title)
                    h3_content = h3_title_list_item.split('</h3>')[1]
                    tmp_line_line['title'] = h3_title
                    print('h3_title => ' + h3_title)


                    h3_content = self.format_text(h3_content)
                    tmp_line_line['content'] = h3_content
                    print('h3_content => ' + h3_content)
                    tmp_line['name_content_list'].append(tmp_line_line)

                print('-----------------------------')
                json_text['name_list'].append(tmp_line)

            json_text = json.dumps(json_text, ensure_ascii=False)
            print("json_text => " + json_text)
            self.write2File('360ly_detail.txt', json_text + '\n')

        except Exception as e:
            self.write2File('error.txt', text_line)
            print(e)


        # https://ly.so.com/detail/yidian?title=xxx
        # https://ly.so.com/api/v1/yidian/detail?cancelToken={"promise":{}}&contentName=&contentNameTerm=泌乳素瘤

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
        topic_header_text = topic_header_text.replace('  ', '')
        topic_header_text = topic_header_text.replace('&nbsp;', '')
        topic_header_text = topic_header_text.replace(' \n', '')
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