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
            'arialoadData': 'true',
            'yfx_f_l_v_t_10006654': 'f_t_1686126397461__r_t_1686276306150__v_t_1686278599787__r_c_2',
            'sVoELocvxVW0T': '5REhW2K1cuxGqqqDEvXZ.7GU2_Ua3YukrvYsggMmhE1PURaqVjH1aRaEjLAZyAW1cWkaKTKcyFPt1bRH.qJztOuZTM4427IfMPtz_zG3NbjxWZ1nfbi4lqcK3_Arzdc73vdettghP1SZQ6OcLq4.eMlIIoFsI_VvH0XscbxLn7VWV8TV9RYyPFBumgnyL_oMMkSQv12.Rrq1qhMftfBoSTs69kjuRJw_4bBb_fXSmde8aBWeJbdzi2E_e2IwPPlMZWl6SuJu1gSqptlhLXAedAIEzwIJUsT9JbKZTavsAOruE2L4upI6qqn8j1_5SSU4qrb6vkEbS_8j_E.A5suCYAf',
        }
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            # 'Cookie': 'wzws_sessionid=gDExNC4yNDguMTI0LjEyMIFmOTBmY2OgZIA/O4I5MGRhNGI=; sVoELocvxVW0S=5CU1yaPmSzL9VdJY7ptf89Lp8hjzRmQMji9DKFr6WPdyUW1umdjWaOXIn0PRBBfSb.T58HJie.w_fQcvwfQuIQq; insert_cookie=96816998; yfx_c_g_u_id_10006654=_ck23060716263714679133701521441; arialoadData=true; yfx_f_l_v_t_10006654=f_t_1686126397461__r_t_1686276306150__v_t_1686278599787__r_c_2; sVoELocvxVW0T=5REhW2K1cuxGqqqDEvXZ.7GU2_Ua3YukrvYsggMmhE1PURaqVjH1aRaEjLAZyAW1cWkaKTKcyFPt1bRH.qJztOuZTM4427IfMPtz_zG3NbjxWZ1nfbi4lqcK3_Arzdc73vdettghP1SZQ6OcLq4.eMlIIoFsI_VvH0XscbxLn7VWV8TV9RYyPFBumgnyL_oMMkSQv12.Rrq1qhMftfBoSTs69kjuRJw_4bBb_fXSmde8aBWeJbdzi2E_e2IwPPlMZWl6SuJu1gSqptlhLXAedAIEzwIJUsT9JbKZTavsAOruE2L4upI6qqn8j1_5SSU4qrb6vkEbS_8j_E.A5suCYAf',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.nhc.gov.cn/wjw/pyl/201412/8e3234e7084646b6aea803a1525cb6f6.shtml',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        time.sleep(2)

        for t in range(200):
            time.sleep(3)
            print(str(t))
            # SvoData.mywebs.send('keyi_' + str(t))

        #/wjw/s9491/200802/38800.shtml
        #http://www.nhc.gov.cn/ewebeditor/uploadfile/2018/04/20180414155505490.pdf
        # with open("b_dump_pdf.txt", 'r', encoding='utf-8') as file:
        #     for item in file:
        #         text_line = item
        #         text_line = text_line.strip()
        #         json_line = json.loads(text_line)
        #         # print(json_line)
        #
        #         dis_title = json_line['dis_title']
        #         dis_url = json_line['dis_url']
        #         #http://www.nhc.gov.cn/wjw/s9495/202003/8343429db2a84c73b14fefaa43554511.shtml
        #         # regex = re.compile('/(.*?)\.shtml')
        #         # dis_url_tmp = regex.sub('', dis_url)
        #         dis_url_list = dis_url.split('/')
        #         last_dis = dis_url_list.pop(len(dis_url_list) - 1)
        #         dis_url_tmp = ''
        #         for item in dis_url_list:
        #             if item == '':
        #                 continue
        #             if item == 'http:':
        #                 dis_url_tmp = dis_url_tmp + item + '//'
        #             else:
        #                 dis_url_tmp = dis_url_tmp + item + '/'
        #         pdf_url = json_line['pdf_url']
        #
        #         if 'ewebeditor' in pdf_url:
        #             dis_url_final = 'http://www.nhc.gov.cn' + pdf_url
        #         else:
        #             dis_url_final = dis_url_tmp + pdf_url
        #         print(dis_title)
        #         print(dis_url_tmp + last_dis)
        #         print(dis_url_final)
        #         # print('dis_title => ' + dis_title)
        #         # print('dis_url_tmp => ' + dis_url_tmp)
        #         # print('pdf_url => ' + pdf_url)
        #         print('------------------------')
        #
        #         # try:
        #         self.getTwoDepartmentList(dis_url_final, dis_title)
        #         time.sleep(3)
        #         # except Exception as e:
        #         #     self.write2File('b_error_pdf.txt', text_line + '\n')
        #         #     print(e)
        #         #     time.sleep(5)

    def getTwoDepartmentList(self, dis_url_final, dis_title):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        self.cookies['sVoELocvxVW0T'] = SvoData.sVoELocvxVW0T
        print('sVoELocvxVW0T => ' + self.cookies['sVoELocvxVW0T'])
        print('User-Agent => ' + self.headers['User-Agent'])

        response = requests.get(
            dis_url_final,
            cookies=self.cookies,
            headers=self.headers,
            timeout=150,
            verify=False
        )

        # （代替 GBZ/T 160.66—2004）
        # dis_title_tmp = dis_title.split('（')[0]
        dis_title_tmp = dis_title.replace('/', ' ')
        print(dis_title_tmp)
        with open("pdf_dir/" + dis_title_tmp + ".pdf", "wb") as f:
            f.write(response.content)


        # # print(res_text)
        # #<div class="con" id="xw_box">(.*?)</div>
        # pdf_info = re.compile('<div class="con" id="xw_box">(.*?)</div>', re.S).findall(res_text)[0]
        # #href="7ab2722f726541a6aae5bf427406764b/files/595e704eb44143d8b37db4d6e0633a6a.pdf">
        # pdf_url = re.compile('href="(.*?)"', re.S).findall(pdf_info)[0]
        # # try:
        # # pdf_url = re.compile('href="(.*?)"', re.S).findall(pdf_info)[0] + 'PDF'
        # # except Exception as e:
        # #     pdf_url = re.compile('href="(.*?)pdf"', re.S).findall(pdf_info)[0] + 'pdf'
        # #     print(e)
        # print('pdf_url => ' + pdf_url)
        # json_line['pdf_url'] = pdf_url
        # json_line['dis_url'] = dis_url
        #
        # json_text = json.dumps(json_line, ensure_ascii=False)
        #
        # self.write2File('b_dump_pdf.txt', json_text + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


# DumpTitle()