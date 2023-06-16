import json
import time

import requests
import re
import random
import ua_list

# 去重
class DumpAllTitle:
    def __init__(self):
        for i in range(0, 5):
            dis_file = "a_xywy_QA_" + str(i) + ".txt"
            # print('dis_file => ' + dis_file)
            with open(dis_file, 'r', encoding='utf-8') as file:
                for item in file:
                    text_line = item.strip()
                    # print('------------------------------------')
                    # print('before text_line => ' + text_line)
                    #"question": "自己到了更年期经常会觉得发热、出汗，在网上看了一些药物，想买点来试试，想问问更年期可不可以吃胰激肽原酶肠溶片？","answer": "胰激肽原酶肠溶片可改善人体微循环障碍，更年期的女性是可以吃的，有利于症状缓解。胰激肽原酶常见如胰激肽原酶，这是一种蛋白水解酶，其药用机理是通过激活激肽系统，释放出激肽，来起到保护神经、舒缓血管、抑制血小板聚集和促进纤维蛋白溶解的作用，扩张局部血管管径，改善了更年期微循环障碍引起的潮热汗出、头晕心悸等症状，更年期女性可在医生的指导下合理服用，疗效较优。此外，更年期的女性还可能会伴随有失眠多梦、烦躁易怒等植物神经紊乱症状，故可遵医嘱服用谷维素、维生素B1等药物来改善。"}
                    #"question": "(.*?)}

                    title = re.compile('"title": "(.*?)", "question":', re.S).findall(text_line)[0]
                    question = re.compile('"question": "(.*?)", "answer":', re.S).findall(text_line)[0]
                    answer = re.compile('"answer": "(.*?)"}', re.S).findall(text_line)[0]
                    # print('question => ' + question)
                    # print('answer => ' + answer)
                    # 去掉尖括号
                    regex = re.compile(', "title": "(.*?)"}')
                    text_line = regex.sub('}', text_line)
                    # print('  mind text_line => ' + text_line)

                    json_line = json.loads(text_line)
                    json_line['title'] = title
                    json_line['question'] = question
                    json_line['answer'] = answer
                    # print(' after text_line => ' + text_line)

                    self.write2File('b_xywy_QA_' + str(i) + '.txt', json.dumps(json_line, ensure_ascii=False) + '\n')

        print('完成')




    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

        # self.write2File('a_msd_title.txt', json.dumps(title_list[i], ensure_ascii=False) + '\n')

DumpAllTitle()