import requests
import json
import time
import re

class HandleJson:

  def __init__(self):
    self.dxys_json = {
      'dxys': []
    }
    self.dxys_list = []
    self.list = [
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

    self.num = 0

    for item in self.list:
      self.handleData(item['name'])

    print("文章总数 => " + str(self.num))
    self.dxys_json['dxys'] = self.dxys_list
    # 写到文件中
    file = open('dxys_QA.json', 'a', encoding='utf-8')
    file.write(str(self.dxys_json).replace('\'', '\"'))

  def handleData(self, param):
    with open("diseases_" + param + "_detail.txt", 'r', encoding='utf-8') as file:
      for item in file:
        detail_str = item.strip()

        try:
          self.regexStr(detail_str, param)
        except Exception as e:
          print(e)

    # file = open("diseases_性病科_article.json", 'r', encoding='utf-8')
    # self.regexStr(file.readline())

  def regexStr(self, detail_str, param):
    try:
      detail_str = detail_str.replace('\\\\n', '')
      detail_str = detail_str.replace('\\\"', '')
      detail_str = detail_str.replace('\\\'', '')
      detail_str = detail_str.replace('\\', '')
      detail_str = detail_str.replace('[\'', '')
      detail_str = detail_str.replace('\']', '')
    except Exception as e:
      print(e)
    detail_str = json.loads(detail_str)

    #获取文章名称
    title = detail_str['tdk']['title']
    title = title.split("症状_")[0]
    #print(title)

    #定义一个文章的json
    json_item = {}
    json_item['subject'] = param
    json_item['title'] = title

    #字段分离
    article = detail_str['disease']['article']
    for article_item in article:
      field = article_item['title']
      detail = article_item['detail']
      if len(detail) > 12:
        json_item[field] = self.getQuestions(detail)

    self.num = self.num + 1
    print(title)
    self.dxys_list.append(json_item)



    # article = article_detail['disease']['article']
    # data_json = {}
    #
    #
    # for article_item in article:
    #   title = article_item['title']
    #   detail = article_item['detail']
    #   if len(detail) > 12:
    #     data_json[title] = detail
    # print(data_json)
    #
    # # print(detail_str)
    # # self.write2File('diseases_性病科_article_test.json', detail_str)
    # self.write2File('detail_' + param + '.txt', str(data_json))
    # self.num = self.num + 1
    # print('当前文章数 => ' + str(self.num))


  def write2File(self, file_name, text):
    file = open(file_name, 'a', encoding='utf-8')
    file.write(text)

  def getQuestions(self, detail):

    #获取每一个问题和答案
    detail_str = str(detail)
    qa_list_tmp = []
    qa_list = detail_str.split("<h2")
    for qa_list_item in qa_list:
      if qa_list_item != '':
        json_qa = {}
        #print(qa_list_item)
        question = qa_list_item.split('</h2>')[0]
        question = question.split('>')[1]
        answer = qa_list_item.split('</h2>')[1]
        # 去掉尖括号,最后做
        regex = re.compile('<(.*?)>')
        answer = regex.sub('', answer)

        #去掉[1]
        regex = re.compile('\[\d+,\d+\]|\[\d\]')
        answer = regex.sub('', answer)

        json_qa['question'] = question
        json_qa['answer'] = answer
        qa_list_tmp.append(json_qa)
    return qa_list_tmp

    # # 匹配问题的
    # # "<h2 searchId=6-1>支原体感染有哪些预防办法？</h2>
    # res = re.compile('<h2(.*?)</h2>', re.S).findall(str(detail))
    # for res_item in res:
    #   res_item_tmp = res_item.split('>')[1]
    #   print(res_item_tmp)
    # pass


HandleJson()