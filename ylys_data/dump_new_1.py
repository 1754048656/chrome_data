import json
import time

import requests
import re
import random
import uaList

# 格式处理
class DumpAllTitle:
    def __init__(self):
        with open('d_ylys_QA.txt', 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item.strip()
                json_line = json.loads(text_line)
                question = json_line['question']
                answer = json_line['answer']
                # 去掉尖括号
                pattern = r"\\u[0-9a-f]{4}"
                pattern_0 = r"\\x[0-9a-f]{2}"
                # regex = re.compile(pattern)
                # question = regex.sub('', question)
                #
                # regex = re.compile(pattern_0)
                # question = regex.sub('', question)

                regex = re.compile('\\\\')
                question = regex.sub('', question)

                regex = re.compile('\\\\')
                answer = regex.sub('', answer)

                json_line['question'] = question
                json_line['answer'] = answer

                self.write2File('t_ylys_QA.txt', json.dumps(json_line, ensure_ascii=False) + '\n')

        print('完成')




    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

        # self.write2File('a_msd_title.txt', json.dumps(title_list[i], ensure_ascii=False) + '\n')

DumpAllTitle()