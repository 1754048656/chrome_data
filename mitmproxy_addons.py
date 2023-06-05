import re
import json
import time
import urllib
import datetime
from urllib import parse

import mitmproxy.http

# mitmproxy抓包配置类
class Addons:

    def __init__(self):
        print("start mitmproxy")
        self.tmpList = {}
        self.list = []
        with open("tencentdy/href_test.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)
                json_line = json.loads(text_line)
                department = json_line['department']
                disease = json_line['disease']

                self.tmpList[disease] = department
            print(self.tmpList)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # print(flow.request.url)
        # https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=20&period=hour
        if 'https://h5.baike.qq.com/api/access/json/cmd/SearchForInner' in flow.request.url:
            if flow.response.content:
                print(flow.request.url)
                res_info = flow.response.text
                # /pages/yidian/medpedia/overview/main?id=sy10745010lprfi4&name
                id_info = re.compile('/pages/yidian/medpedia/overview/main\?id=(.*?)&m=').findall(res_info)[0]
                id_text = id_info.split('&name=')[0]
                name_text = id_info.split('&name=')[1]
                name_text = parse.unquote(name_text)

                print('id_text => ' + id_text)
                print('name_text => ' + name_text)

                # print('self.tmpList[name_text]' + self.tmpList[name_text])
                json_tmp = {}
                json_tmp['department'] = self.tmpList[name_text]
                json_tmp['disease'] = name_text
                json_tmp['id'] = id_text
                if id_text in self.list:
                    pass
                else:
                    self.list.append(id_text)
                    self.write2File('tencentdy/id_href.txt', json.dumps(json_tmp, ensure_ascii=False) + '\n')

                # #https://www.zhihu.com/api/v4/creators/rank/hot?domain=100002&period=hour
                # url_text = flow.request.url
                # domain = re.compile('api/v4/creators/rank/hot\?domain=(.*?)&', re.S).findall(url_text)[0]
                #
                # print('domain => ' + str(self.dict_tmp[str(domain)]))
                # # json_tmp_line['type'] = self.dict_tmp[domain]
                # data_json = flow.response.json()
                # data_list = data_json['data']
                # for data_list_item in data_list:
                #     json_tmp_line = {}
                #     json_tmp_line['type'] = self.dict_tmp[domain]
                #     title = data_list_item['question']['title']
                #     topics = data_list_item['question']['topics']
                #     json_tmp_line['title'] = title
                #     json_tmp_line['topics'] = topics
                #     json_text = json.dumps(json_tmp_line, ensure_ascii=False)
                #     self.write2File('zhihu_data/zhihu_title.txt', json_text + '\n')
                #     print(json_text)
                pass

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


addons = [
    Addons()
]
