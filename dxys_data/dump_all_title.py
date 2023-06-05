import requests
import json
import time
import re
cookies = {
    'csrfToken': 'oNj0tjaalI3OXBBrpaJmFciw',
    'dxy_da_cookie-id': '869108451621547f5f80229bcfd8d3f81683880299819',
    'Hm_lvt_f21c182642df0697ca3ebaf7a82b8fc4': '1683880300',
    '_ga': 'GA1.2.1769602490.1683880300',
    '_gid': 'GA1.2.1516081062.1683880300',
    'DOTCOM_CSRFTOKEN': '65db0780-ef40-4781-84f9-6ae522beca87',
    'Hm_lpvt_f21c182642df0697ca3ebaf7a82b8fc4': '1683880504',
}

headers = {
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://dxy.com/articles',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'csrfToken=oNj0tjaalI3OXBBrpaJmFciw; dxy_da_cookie-id=869108451621547f5f80229bcfd8d3f81683880299819; Hm_lvt_f21c182642df0697ca3ebaf7a82b8fc4=1683880300; _ga=GA1.2.1769602490.1683880300; _gid=GA1.2.1516081062.1683880300; DOTCOM_CSRFTOKEN=65db0780-ef40-4781-84f9-6ae522beca87; Hm_lpvt_f21c182642df0697ca3ebaf7a82b8fc4=1683880504',
}

list = [
  {
    "id": 6948,
    "name": "儿科",
    "href": "https://dxy.com/diseases/6948"
  },
  {
    "id": 2781,
    "name": "妇科",
    "href": "https://dxy.com/diseases/2781"
  },
  {
    "id": 25431,
    "name": "产科",
    "href": "https://dxy.com/diseases/25431"
  },
  {
    "id": 751,
    "name": "皮肤科",
    "href": "https://dxy.com/diseases/751"
  },
  {
    "id": 6785,
    "name": "内分泌科",
    "href": "https://dxy.com/diseases/6785"
  },
  {
    "id": 6523,
    "name": "消化内科",
    "href": "https://dxy.com/diseases/6523"
  },
  {
    "id": 3329,
    "name": "神经内科",
    "href": "https://dxy.com/diseases/3329"
  },
  {
    "id": 6133,
    "name": "心血管内科",
    "href": "https://dxy.com/diseases/6133"
  },
  {
    "id": 7485,
    "name": "骨科",
    "href": "https://dxy.com/diseases/7485"
  },
  {
    "id": 4907,
    "name": "普外科",
    "href": "https://dxy.com/diseases/4907"
  },
  {
    "id": 7984,
    "name": "感染科",
    "href": "https://dxy.com/diseases/7984"
  },
  {
    "id": 5413,
    "name": "普通内科",
    "href": "https://dxy.com/diseases/5413"
  },
  {
    "id": 1645,
    "name": "肾脏内科",
    "href": "https://dxy.com/diseases/1645"
  },
  {
    "id": 2129,
    "name": "呼吸内科",
    "href": "https://dxy.com/diseases/2129"
  },
  {
    "id": 1846,
    "name": "耳鼻咽喉科",
    "href": "https://dxy.com/diseases/1846"
  },
  {
    "id": 531,
    "name": "泌尿外科",
    "href": "https://dxy.com/diseases/531"
  },
  {
    "id": 675,
    "name": "口腔科",
    "href": "https://dxy.com/diseases/675"
  },
  {
    "id": 3880,
    "name": "眼科",
    "href": "https://dxy.com/diseases/3880"
  },
  {
    "id": 2393,
    "name": "血液科",
    "href": "https://dxy.com/diseases/2393"
  },
  {
    "id": 4617,
    "name": "肿瘤科",
    "href": "https://dxy.com/diseases/4617"
  },
  {
    "id": 5160,
    "name": "神经外科",
    "href": "https://dxy.com/diseases/5160"
  },
  {
    "id": 5087,
    "name": "肝胆胰腺外科",
    "href": "https://dxy.com/diseases/5087"
  },
  {
    "id": 710,
    "name": "精神心理科",
    "href": "https://dxy.com/diseases/710"
  },
  {
    "id": 1459,
    "name": "风湿免疫科",
    "href": "https://dxy.com/diseases/1459"
  },
  {
    "id": 5618,
    "name": "心胸外科",
    "href": "https://dxy.com/diseases/5618"
  },
  {
    "id": 5393,
    "name": "甲状腺乳腺外科",
    "href": "https://dxy.com/diseases/5393"
  },
  {
    "id": 9235,
    "name": "影像检验科",
    "href": "https://dxy.com/diseases/9235"
  },
  {
    "id": 6095,
    "name": "美容整形科",
    "href": "https://dxy.com/diseases/6095"
  },
  {
    "id": 8742,
    "name": "疼痛科 麻醉科",
    "href": "https://dxy.com/diseases/8742"
  },
  {
    "id": 21780,
    "name": "性病科",
    "href": "https://dxy.com/diseases/21780"
  }
]


def diseases_detail(item):
    response = requests.get(item['href'], cookies=cookies, headers=headers)
    res = re.compile('<script>window.\$\$data=(.*?)</script>', re.S).findall(response.text)
    print(res)
    # 写到文件中
    # file = open('diseases_' + item['name'] + '.txt', 'a', encoding='utf-8')
    # file.write(str(res) + '\n')
    # pass


for item in list:
    print(item['name'] + ' ' + item['href'])
    diseases_detail(item)
    time.sleep(10)
