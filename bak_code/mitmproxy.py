import re
import json
import time
import urllib
import datetime
import mitmproxy.http

# mitmproxy抓包配置类
class Addons:

    def __init__(self):
        print("已开启mitmproxy")
        self.tmp_list = [
                        {
                            "id": 100001,
                            "name": "数码"
                        },
                        {
                            "id": 100002,
                            "name": "科技"
                        },
                        {
                            "id": 100003,
                            "name": "互联网"
                        },
                        {
                            "id": 100004,
                            "name": "商业财经"
                        },
                        {
                            "id": 100005,
                            "name": "职场"
                        },
                        {
                            "id": 100006,
                            "name": "教育"
                        },
                        {
                            "id": 100007,
                            "name": "法律"
                        },
                        {
                            "id": 100008,
                            "name": "军事"
                        },
                        {
                            "id": 100009,
                            "name": "汽车"
                        },
                        {
                            "id": 100010,
                            "name": "人文社科"
                        },
                        {
                            "id": 100011,
                            "name": "自然科学"
                        },
                        {
                            "id": 100012,
                            "name": "工程技术"
                        },
                        {
                            "id": 100013,
                            "name": "情感"
                        },
                        {
                            "id": 100014,
                            "name": "心理学"
                        },
                        {
                            "id": 100015,
                            "name": "两性"
                        },
                        {
                            "id": 100016,
                            "name": "母婴亲子"
                        },
                        {
                            "id": 100017,
                            "name": "家居"
                        },
                        {
                            "id": 100018,
                            "name": "健康"
                        },
                        {
                            "id": 100019,
                            "name": "艺术"
                        },
                        {
                            "id": 100020,
                            "name": "音乐"
                        },
                        {
                            "id": 100021,
                            "name": "设计"
                        },
                        {
                            "id": 100022,
                            "name": "影视娱乐"
                        },
                        {
                            "id": 100023,
                            "name": "宠物"
                        },
                        {
                            "id": 100024,
                            "name": "体育电竞"
                        },
                        {
                            "id": 100025,
                            "name": "运动健身"
                        },
                        {
                            "id": 100026,
                            "name": "动漫游戏"
                        },
                        {
                            "id": 100027,
                            "name": "美食"
                        },
                        {
                            "id": 100028,
                            "name": "旅行"
                        },
                        {
                            "id": 100029,
                            "name": "时尚"
                        }
                    ]
        self.dict_tmp = {}
        for item_json in self.tmp_list:
            # item_json = json.loads(item)
            self.dict_tmp[str(item_json['id'])] = item_json['name']
        print(self.dict_tmp)


    def response(self, flow: mitmproxy.http.HTTPFlow):
        print(flow.request.url)
        # https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&offset=20&period=hour
        if 'https://www.zhihu.com/api/v4/creators/rank/hot?domain' in flow.request.url:
            if flow.response.content:
                #https://www.zhihu.com/api/v4/creators/rank/hot?domain=100002&period=hour
                url_text = flow.request.url
                domain = re.compile('api/v4/creators/rank/hot\?domain=(.*?)&', re.S).findall(url_text)[0]

                print('domain => ' + str(self.dict_tmp[str(domain)]))
                # json_tmp_line['type'] = self.dict_tmp[domain]
                data_json = flow.response.json()
                data_list = data_json['data']
                for data_list_item in data_list:
                    json_tmp_line = {}
                    json_tmp_line['type'] = self.dict_tmp[domain]
                    title = data_list_item['question']['title']
                    topics = data_list_item['question']['topics']
                    json_tmp_line['title'] = title
                    json_tmp_line['topics'] = topics
                    json_text = json.dumps(json_tmp_line, ensure_ascii=False)
                    self.write2File('zhihu_data/zhihu_title.txt', json_text + '\n')
                    print(json_text)
                pass

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

addons = [
    Addons()
]
