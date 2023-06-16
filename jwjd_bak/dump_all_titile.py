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
            list_tmp = []
            dis_file = "disease_" + str(i) + ".txt"
            print('dis_file => ' + dis_file)
            with open(dis_file, 'r', encoding='utf-8') as file:
                for item in file:
                    text_line = item
                    print(text_line)
                    dis_url = text_line.split(' => ')[3]
                    if dis_url in list_tmp:
                        print('跳过')
                        continue
                    else:
                        list_tmp.append(dis_url)
                        self.write2File('dis_' + str(i) + '.txt', text_line)





    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

        # self.write2File('a_msd_title.txt', json.dumps(title_list[i], ensure_ascii=False) + '\n')

DumpAllTitle()