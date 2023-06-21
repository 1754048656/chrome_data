import re
import json
import time
import redis
import urllib
import datetime
from urllib import parse

import mitmproxy.http

# mitmproxy抓包配置类
class Addons:

    def __init__(self):
        print("start mitmproxy")
        #初始化redis
        self.r = redis.Redis(host='127.0.0.1', port='6379', decode_responses=True)

        #变量
        self.tmpList = []
        # self.r.set('current_num', 0)
        # self.r.set('to_next', 'F')

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # print(flow.request.url)

        #答案
        if '/api/v4/questions/' in flow.request.url and '/feeds?cursor' in flow.request.url:
            if flow.response.content:
                print(flow.request.url)
                res_json = flow.response.json()
                # print(res_json)
                data_list = res_json['data']
                for data_list_item in data_list:
                    title = data_list_item['target']['question']['title']
                    content = data_list_item['target']['content']
                    print(title)
                    print(content)
                    print('=============')

        # if 'https://www.zhihu.com/question/' in flow.request.url:
        #     if flow.response.content:
        #         print(flow.request.url)
        #         res_text = flow.response.text
        #         # print(res_text)
        #         res_text = re.compile('<script id="js-initialData" type="text/json">(.*?)</script>', re.S).findall(res_text)[0]
        #         json_line = json.loads(res_text)
        #
        #         questions = json_line['initialState']['entities']['questions']
        #         for questions_item in questions:
        #             title = questions[questions_item]['title']
        #             topics = questions[questions_item]['topics']
        #             topic_list = []
        #             for topics_item in topics:
        #                 topic_list.append(topics_item['name'])
        #
        #             print(title)
        #             print(topic_list)
        #             print('==========')
        #
        #         answers = json_line['initialState']['entities']['answers']
        #         for answers_item in answers:
        #             print(answers_item)
        #
        #             excerpt = answers[answers_item]['excerpt']
        #             print(excerpt)
        #             print('-------')


        #问题
        # if '/api/v5.1/topics/' in flow.request.url:
        #     if flow.response.content:
        #         print(flow.request.url)
        #         res_json = flow.response.json()
        #         data_list = res_json['data']
        #         for data_list_item in data_list:
        #
        #             try:
        #                 id = data_list_item['target']['id']
        #                 url = data_list_item['target']['url']
        #                 url = url.split('com/')[1]
        #                 question_id = data_list_item['target']['question']['id']
        #             except Exception as e:
        #                 print('--')
        #                 print('Exception res => ' + json.dumps(res_json, ensure_ascii=False))
        #                 break
        #             url = 'https://www.zhihu.com/question/' + str(question_id) + '/' + url
        #             url = url.replace('answers', 'answer')
        #             question_title = data_list_item['target']['question']['title']
        #             print(url)
        #             print(question_title)
        #             # print('--------------')
        #
        #             json_line = {}
        #             json_line['tmp_first_topic'] = self.r.get('tmp_first_topic')
        #             json_line['topic'] = self.r.get('current_name')
        #             json_line['question_title'] = question_title
        #             json_line['url'] = url
        #
        #             json_text = json.dumps(json_line, ensure_ascii=False)
        #             print(json_text)
        #             print('self.current_num => ' + str(self.r.get('current_num')))
        #             current_num = self.r.get('current_num')
        #             current_num = int(current_num)
        #             if current_num >= 20000:
        #                 self.r.set('to_next', 'T')
        #                 self.tmpList = []
        #                 break
        #             if url in self.tmpList:
        #                 print('----- 重复了 -----')
        #                 continue
        #
        #             current_num = int(current_num) + 1
        #             self.r.set('current_num', current_num)
        #
        #             self.tmpList.append(url)
        #             self.write2File('topics_question.txt', json_text + '\n')
        #     pass



        #拿到所有话题
        #https://www.zhihu.com/node/TopicsPlazzaListV2
        # if 'TopicsPlazzaList' in flow.request.url:
        #     if flow.response.content:
        #         print(flow.request.url)
        #         res_json = flow.response.json()
        #         print('=========')
        #         topic_list = res_json['msg']
        #         for topic_list_item in topic_list:
        #             # print(topic_list_item)
        #             # href="/topic/19551387">
        #             topic_url = re.compile('href="/topic/(.*?)">', re.S).findall(topic_list_item)[0]
        #             print(topic_url)
        #             # <strong>生活方式</strong>
        #             topic_name = re.compile('<strong>(.*?)</strong>', re.S).findall(topic_list_item)[0]
        #             print(topic_name)
        #             print('========================')
        #             # self.write2File('topics.txt', topic_name + ' => ' + topic_url + '\n')



        # https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=20&period=hour
        # if 'https://h5.baike.qq.com/api/access/json/cmd/SearchForInner' in flow.request.url:
        #     if flow.response.content:
        #         print(flow.request.url)
        #         res_info = flow.response.text
                # /pages/yidian/medpedia/overview/main?id=sy10745010lprfi4&name
                # id_info = re.compile('/pages/yidian/medpedia/overview/main\?id=(.*?)&m=').findall(res_info)[0]
                # id_text = id_info.split('&name=')[0]
                # name_text = id_info.split('&name=')[1]
                # name_text = parse.unquote(name_text)
                #
                # print('id_text => ' + id_text)
                # print('name_text => ' + name_text)
                #
                # # print('self.tmpList[name_text]' + self.tmpList[name_text])
                # json_tmp = {}
                # json_tmp['department'] = self.tmpList[name_text]
                # json_tmp['disease'] = name_text
                # json_tmp['id'] = id_text
                # if id_text in self.list:
                #     pass
                # else:
                #     self.list.append(id_text)
                #     self.write2File('tencentdy/id_href.txt', json.dumps(json_tmp, ensure_ascii=False) + '\n')
                #
                # # #https://www.zhihu.com/api/v4/creators/rank/hot?domain=100002&period=hour
                # # url_text = flow.request.url
                # # domain = re.compile('api/v4/creators/rank/hot\?domain=(.*?)&', re.S).findall(url_text)[0]
                # #
                # # print('domain => ' + str(self.dict_tmp[str(domain)]))
                # # # json_tmp_line['type'] = self.dict_tmp[domain]
                # # data_json = flow.response.json()
                # # data_list = data_json['data']
                # # for data_list_item in data_list:
                # #     json_tmp_line = {}
                # #     json_tmp_line['type'] = self.dict_tmp[domain]
                # #     title = data_list_item['question']['title']
                # #     topics = data_list_item['question']['topics']
                # #     json_tmp_line['title'] = title
                # #     json_tmp_line['topics'] = topics
                # #     json_text = json.dumps(json_tmp_line, ensure_ascii=False)
                # #     self.write2File('zhihu_data/zhihu_title.txt', json_text + '\n')
                # #     print(json_text)
                # pass

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

addons = [
    Addons()
]
