import json
import time

import requests
from urllib import parse
import re
import random
import uaList

class DumpTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            'BAIDUID': '3C9F43BD24AA4B2932F6C727656D78A6:FG=1',
            'BIDUPSID': '3C9F43BD24AA4B2932F6C727656D78A6',
            'PSTM': '1684473847',
            'BD_UPN': '123253',
            'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
            'H_PS_PSSID': '38515_36543_38541_38767_38576_38196_38764_26350_22158',
            'BDSFRCVID': '3K4OJeCT5G09-d6fJ3GRhFn2dgKK0gOTTPjcTR5qJ04BtyCVcmiREG0PtOpvTLPM_EGSogKK0mOTHUAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
            'H_BDCLCKID_SF': 'tbIJoDK5JDD3fP36q45HMt00qxby26PeWbn9aJ5nQI5nhKIzb5jty6t10x7l2jjb523ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMPjamOnaU5p3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6oBjGjP',
            'H_PS_645EC': '1ebfKiDiXlZkodHiG0WD0mSk%2B35CKhiffAiEv9LM4ZSft46m0INvLbLgrN4',
            'BAIDUID_BFESS': '3C9F43BD24AA4B2932F6C727656D78A6:FG=1',
            'BDSFRCVID_BFESS': '3K4OJeCT5G09-d6fJ3GRhFn2dgKK0gOTTPjcTR5qJ04BtyCVcmiREG0PtOpvTLPM_EGSogKK0mOTHUAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
            'H_BDCLCKID_SF_BFESS': 'tbIJoDK5JDD3fP36q45HMt00qxby26PeWbn9aJ5nQI5nhKIzb5jty6t10x7l2jjb523ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMPjamOnaU5p3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6oBjGjP',
            'channel': 'baidusearch',
            'baikeVisitId': '855817f8-f596-4356-8fa8-42a632a48ac9',
            'ab_sr': '1.0.1_ZWM5OWU4Y2U5YzZiZjQ3ZDA2NTliNDY4YmQzMjhkMDdjMWMxODZjZGJjYTliMzg0MTcyMjkwNzZmNjc1ZTdjOWQ1ZTMxYmZlZTkxYzJjYTMyYzNmOGEzMjgwOWI1ZTI2N2I2YmQzMzI0MzY1ZmE4ODkwYzc1Y2M1YmEyOGFiMDdiZTMxZTAwZGU3NzA2MzRkYmRjNzVmN2Q1Yzg5NTg4Ng==',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'BAIDUID=3C9F43BD24AA4B2932F6C727656D78A6:FG=1; BIDUPSID=3C9F43BD24AA4B2932F6C727656D78A6; PSTM=1684473847; BD_UPN=123253; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=38515_36543_38541_38767_38576_38196_38764_26350_22158; BDSFRCVID=3K4OJeCT5G09-d6fJ3GRhFn2dgKK0gOTTPjcTR5qJ04BtyCVcmiREG0PtOpvTLPM_EGSogKK0mOTHUAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbIJoDK5JDD3fP36q45HMt00qxby26PeWbn9aJ5nQI5nhKIzb5jty6t10x7l2jjb523ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMPjamOnaU5p3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6oBjGjP; H_PS_645EC=1ebfKiDiXlZkodHiG0WD0mSk%2B35CKhiffAiEv9LM4ZSft46m0INvLbLgrN4; BAIDUID_BFESS=3C9F43BD24AA4B2932F6C727656D78A6:FG=1; BDSFRCVID_BFESS=3K4OJeCT5G09-d6fJ3GRhFn2dgKK0gOTTPjcTR5qJ04BtyCVcmiREG0PtOpvTLPM_EGSogKK0mOTHUAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbIJoDK5JDD3fP36q45HMt00qxby26PeWbn9aJ5nQI5nhKIzb5jty6t10x7l2jjb523ion3vQUbmjRO206oay6O3LlO83h52aC5NKl0MLPbcq-Q2Xh3YBUL10UnMBMPjamOnaU5p3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj6oBjGjP; channel=baidusearch; baikeVisitId=855817f8-f596-4356-8fa8-42a632a48ac9; ab_sr=1.0.1_ZWM5OWU4Y2U5YzZiZjQ3ZDA2NTliNDY4YmQzMjhkMDdjMWMxODZjZGJjYTliMzg0MTcyMjkwNzZmNjc1ZTdjOWQ1ZTMxYmZlZTkxYzJjYTMyYzNmOGEzMjgwOWI1ZTI2N2I2YmQzMzI0MzY1ZmE4ODkwYzc1Y2M1YmEyOGFiMDdiZTMxZTAwZGU3NzA2MzRkYmRjNzVmN2Q1Yzg5NTg4Ng==',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        self.params = {
            'from': 'dicta',
            'sf_ref': 'med_pc',
            'sf_ch': 'ch_med_pc',
        }
        with open("dis_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                print(text_line)
                department = text_line.split(' => ')[0]
                dis_name = text_line.split(' => ')[1]
                dis_url = text_line.split(' => ')[2]
                #https://www.baidu.com/bh/dict/ydxx_10611358696585305825?from=dicta&sf_ref=med_pc&sf_ch=ch_med_pc
                dis_url = re.compile('dict/(.*?)\?from=dicta').findall(dis_url)[0]

                for i in range(40):
                    try:
                        self.getTwoDepartmentList(dis_url, department, dis_name)
                        break
                    except Exception as e:
                        print(e)

                    time.sleep(15)
                time.sleep(5)

    def getTwoDepartmentList(self,  dis_url, department, dis_name):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        print('User-Agent => ' + self.headers['User-Agent'])
        dis_url = 'https://www.baidu.com/bh/dict/' + dis_url
        response = requests.get(
            dis_url,
            cookies=self.cookies,
            headers=self.headers,
            params=self.params,
            timeout=28
        )

        time.sleep(1.5)

        res_text = response.text
        #componentData: {(.*?)commonData: {
        component = re.compile('componentData: \{(.*?)commonData: \{', re.S).findall(res_text)[0]
        component = '{' + component
        component = component.strip()
        component = component[0:-3]
        component = component.strip()
        component = component.strip(',')
        component = component + '}'
        component = json.loads(component)
        # disease_alias = component['disease']['alias']
        disease_level_data = component['disease']['overview']['level1Data']

        disease_json = {}
        # disease_json['disease_alias'] = disease_alias
        disease_json['department'] = department
        disease_json['dis_name'] = dis_name
        disease_json['level1Data'] = []
        for disease_level_data_item in disease_level_data:
            print('****************************************')
            print('disease_level_data_item => ' + json.dumps(disease_level_data_item, ensure_ascii=False))
            json_tmp = {}
            json_tmp['level1Tag'] = disease_level_data_item['level1Tag']
            json_tmp['level1Text'] = disease_level_data_item['level1Text']
            hasLevel2 = False
            isList = False
            try:
                isList = isinstance(disease_level_data_item['level2Data'], list)
                json_tmp['level2Data'] = []
                hasLevel2 = True
            except Exception as e:
                pass
            if (hasLevel2):
                if (isList):
                    for item in disease_level_data_item['level2Data']:
                        print('item => ' + json.dumps(item, ensure_ascii=False))
                        json_tmp_tmp = {}
                        json_tmp_tmp['level2Tag'] = item['level2Tag']
                        try:
                            json_tmp_tmp['level2Text'] = item['level2Text']
                        except Exception as e:
                            # print('no level2Text')
                            pass
                        try:
                            json_tmp_tmp['level3Data'] = item['level3Data']
                        except Exception as e:
                            # print('no level3Data')
                            pass
                        json_tmp['level2Data'].append(json_tmp_tmp)
                    disease_json['level1Data'].append(json_tmp)
                else:
                    json_tmp_tmp = {}
                    json_tmp_tmp['level2Tag'] = disease_level_data_item['level2Data']['level2Tag']
                    try:
                        json_tmp_tmp['level2Text'] = disease_level_data_item['level2Data']['level2Text']
                    except Exception as e:
                        # print('no level2Text')
                        pass
                    try:
                        json_tmp_tmp['level3Data'] = disease_level_data_item['level2Data']['level3Data']
                    except Exception as e:
                        # print('no level3Data')
                        pass
                    json_tmp['level2Data'].append(json_tmp_tmp)
                    disease_json['level1Data'].append(json_tmp)

        self.write2File('baidu_jk.txt', json.dumps(disease_json, ensure_ascii=False) + '\n')
        print('disease_alias => ' + json.dumps(disease_json, ensure_ascii=False))
        print('----------------------------------------')

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


DumpTitle()