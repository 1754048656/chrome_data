import json
import time

import requests
import re
import random
import uaList
from sVo import SvoData

class DumpTitle:
    def __init__(self):
        self.nameList = []
        self.cookies = {
    'wzws_sessionid': 'gDExNC4yNDguMTI0LjEyMIFmOTBmY2OgZIA/O4I5MGRhNGI=',
    'sVoELocvxVW0S': '5CU1yaPmSzL9VdJY7ptf89Lp8hjzRmQMji9DKFr6WPdyUW1umdjWaOXIn0PRBBfSb.T58HJie.w_fQcvwfQuIQq',
    'insert_cookie': '96816998',
    'yfx_c_g_u_id_10006654': '_ck23060716263714679133701521441',
    'yfx_f_l_v_t_10006654': 'f_t_1686126397461__r_t_1686190691241__v_t_1686214207043__r_c_1',
    'arialoadData': 'true',
    'sVoELocvxVW0T': '5REmWKD1rsmLqqqDEb2J7MquL5tGHp8BF6eYX5ia6uv2hDzIWHbCsh0u2da0FvBTYVpK0wqP4obBY17f0PLYBH2vdehMK3Y74QT5WJwqJdyTJE9c_14w3YJkPrheg6Rw2AOESxjg.P1idt8nhEVb5.GIsR5ylFLcQkoQF0oIF0eaHNy4X.6a3ugYlDq6MPeZZVbBcp6iGt_LkCZ.dRcArIzj3tptfdWoukkwpYOIjxps40jcE3qyim4Xg16kN4aypaF0CwJuzMpRgDntYcpJOIDNnMRL8spJH_FJrGTeJEsYG',
}
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'wzws_sessionid=gDExNC4yNDguMTI0LjEyMIFmOTBmY2OgZIA/O4I5MGRhNGI=; sVoELocvxVW0S=5CU1yaPmSzL9VdJY7ptf89Lp8hjzRmQMji9DKFr6WPdyUW1umdjWaOXIn0PRBBfSb.T58HJie.w_fQcvwfQuIQq; insert_cookie=96816998; yfx_c_g_u_id_10006654=_ck23060716263714679133701521441; arialoadData=true; ariawapChangeViewPort=false; yfx_f_l_v_t_10006654=f_t_1686126397461__r_t_1686126397461__v_t_1686137112305__r_c_0; sVoELocvxVW0T=5RErNmK1qFpGqqqDE2FzaeALfJ6sWSk8WIVX7eT0yKo2zrDwYmtgUVgZ8ybNSYQ9ptLUysv1b1ZSdNKsj7pOCbQpBoIe9Cufbg6m87ogipRopuSPr8oxPTLeZLdpbC9VlS6_FC7aMSuiKaYThbPiylXLpLQZ5QNb3ZSDMGPDCuBXfYynpGI3UTY3JqK5shYJW_ldgQAWyCNsketP5bJlvyGUJ0ACHxNrOduchP4J524c8MCNOqkVaKhLD.qGA5..bqEphl1UyFUuTlGVwAEZX1h',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        time.sleep(2)

        #/wjw/s9491/200802/38800.shtml
        #http://www.nhc.gov.cn/ewebeditor/uploadfile/2018/04/20180414155505490.pdf
        with open("b_wjw_url.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                json_line = json.loads(text_line)

                dis_title = json_line['dis_title']
                dis_url = 'http://www.nhc.gov.cn' + json_line['dis_url']
                print('dis_title => ' + dis_title)
                print('dis_url => ' + dis_url)
                try:
                    self.getTwoDepartmentList(dis_url, json_line)
                    time.sleep(0.9)
                except Exception as e:
                    self.write2File('b_error_pdf.txt', text_line + '\n')
                    print(e)

    def getTwoDepartmentList(self, dis_url, json_line):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        self.cookies['sVoELocvxVW0T'] = SvoData.sVoELocvxVW0T
        print('sVoELocvxVW0T => ' + self.cookies['sVoELocvxVW0T'])
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(
            dis_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=12,
            verify=False
        )

        res_text = response.text
        # print(res_text)
        #<div class="con" id="xw_box">(.*?)</div>
        pdf_info = re.compile('<div class="con" id="xw_box">(.*?)</div>', re.S).findall(res_text)[0]
        #href="7ab2722f726541a6aae5bf427406764b/files/595e704eb44143d8b37db4d6e0633a6a.pdf">
        pdf_url = re.compile('href="(.*?)"', re.S).findall(pdf_info)[0]
        # try:
        # pdf_url = re.compile('href="(.*?)"', re.S).findall(pdf_info)[0] + 'PDF'
        # except Exception as e:
        #     pdf_url = re.compile('href="(.*?)pdf"', re.S).findall(pdf_info)[0] + 'pdf'
        #     print(e)
        print('pdf_url => ' + pdf_url)
        json_line['pdf_url'] = pdf_url
        json_line['dis_url'] = dis_url

        json_text = json.dumps(json_line, ensure_ascii=False)

        self.write2File('b_dump_pdf.txt', json_text + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


# DumpTitle()