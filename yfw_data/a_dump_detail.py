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

        #https://www.yaofangwang.com/yongyao/changwei/list_1.shtml
        with open("yfw_title.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                json_line = json.loads(text_line)
                department = json_line['department']
                title = json_line['title']
                title_url = json_line['title_url']
                title_url_tmp = self.baseUrl + title_url
                print(department)
                print(title)
                print(title_url_tmp)
                print('----------------------')
                self.getTwoDepartmentList(title_url_tmp, department, title)

                print('-===-=-=-=-=-=-=-=-=-=-=-=')
                time.sleep(1)

    def getTwoDepartmentList(self, title_url_tmp, department, title):
        # self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(title_url_tmp, cookies=self.cookies, headers=self.headers)
        response.encoding = 'utf8'
        res_text = response.text

        #<span>(.*?)</span>\|   时间
        time_info = re.compile('<span>(.*?)</span>\|', re.S).findall(res_text)[0]
        print('time_info\n' + time_info)

        #<div class="newsdesc js-article-content">(.*?)<div class="newsinfo nb clearfix dash_bom">  内容
        content_info = re.compile('<div class="newsdesc js-article-content">(.*?)<div class="newsinfo nb clearfix dash_bom">', re.S).findall(res_text)[0]
        # print('content_info \n' + content_info.strip())

        #<div class='font-small-title' id='small-title(.*?)</div>
        # title_info = re.compile("<div class='font-small-title' id='small-title(.*?)</div>", re.S).findall(content_info)
        # for title_info_item in title_info:
        #     title_name = title_info_item.split('\'>')[1]
        #     print('title_name\n' + title_name)

        json_line = {}
        json_line['department'] = department
        json_line['title'] = title
        json_line['content_list'] = []

        #标题和内容
        if "<div class='font-small-title' id='small-title" in content_info:
            #</p><div class='font-small-title' id='small-title
            title_content = content_info.split("<div class='font-small-title' id='small-title")
            title_content.pop(0)
            for title_content_item in title_content:
                # print(title_content_item)
                title_con = title_content_item.split("'>")[1]
                title = title_con.split('</div>')[0]
                content = title_con.split('</div>')[1]
                content = self.format_text(content)
                json_tmp = {}
                json_tmp['title'] = title
                json_tmp['content'] = content
                print(json_tmp)
                json_line['content_list'].append(json_tmp)
        else:
            print('</p><p></p><p></p><p></p><p></p><p>')
            content_list = content_info.split('</p><p>')
            for content_list_item in content_list:
                content_list_item = self.format_text(content_list_item)
                print(content_list_item)
                json_line['content_list'].append(content_list_item)


        self.write2File('yfw_detail.txt', json.dumps(json_line, ensure_ascii=False) + '\n')

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
        # topic_header_text = topic_header_text.strip('">')
        topic_header_text = topic_header_text.strip()
        # if 'gon">' in topic_header_text:
        #     topic_header_text = topic_header_text.split('gon">')[1]

        return topic_header_text

DumpTitle()