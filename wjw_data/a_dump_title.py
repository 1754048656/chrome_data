import json
import time

import requests
from urllib import parse
import re
import random
import uaList

import asyncio
import websockets

class Dump:
    def __init__(self):
        self.nameList = []
        self.cookies = {
            'wzws_sessionid': 'gDExNC4yNDguMTI0LjEyMIFmOTBmY2OgZIA/O4I5MGRhNGI=',
            'sVoELocvxVW0S': '5CU1yaPmSzL9VdJY7ptf89Lp8hjzRmQMji9DKFr6WPdyUW1umdjWaOXIn0PRBBfSb.T58HJie.w_fQcvwfQuIQq',
            'insert_cookie': '96816998',
            'yfx_c_g_u_id_10006654': '_ck23060716263714679133701521441',
            'arialoadData': 'true',
            'ariawapChangeViewPort': 'false',
            'yfx_f_l_v_t_10006654': 'f_t_1686126397461__r_t_1686126397461__v_t_1686139386553__r_c_0',
            'sVoELocvxVW0T': '5REcqmC1qGrLqqqDE2Ip81GBFN37JBuTA.5pD7BbvhzIvF9i7_qU_VUcPRssFy.ZOHRurTFqL0sIrFLWIL1ouQZcxbe7xNLu_PgydKSMAQSAAogtQfe_WgiCHPqWEO74B0NRSIf.4RRh48MPxtPOMSHrMqIVM.AVzUPBcwDrCGlD5otnjX1KJ4dZFugwNeFgZLwfzCqsI8Vj5lkjB7DJ5YnAlZsESCvfsycQwS9aypsUXSvWUysdYonBZY7Yi4X0qTeKCvcOHKKthCRmbl3wCPz',
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

        self.webS()

        # with open("href.txt", 'r', encoding='utf-8') as file:
        #     for item in file:
        #         text_line = item
        #         text_line = text_line.strip()
        #         json_line = json.loads(text_line)
        #
        #         print(json_line)
        #         base_url = 'http://www.nhc.gov.cn'
        #         name = json_line['name']
        #         channelUrl = json_line['channelUrl']
        #         channelUrl = channelUrl.split('.shtml')[0]
        #         for m in range(1, 100):
        #             if m == 1:
        #                 re_channelUrl = channelUrl + '.shtml'
        #             else:
        #                 re_channelUrl = channelUrl + '_' + str(m) + '.shtml'
        #             text_url = base_url + re_channelUrl
        #             res_res = self.getTwoDepartmentList(text_url, name)
        #             if res_res == '-1':
        #                 break
        #             if res_res == '-2':
        #                 error_line = text_line + ' => ' + text_url + '\n'
        #                 self.write2File('error_url.txt', error_line)



    def getTwoDepartmentList(self, text_url, name):
        self.headers['User-Agent'] = uaList.list[random.randint(0, len(uaList.list) - 1)]
        self.cookies['sVoELocvxVW0T'] = self.sVoELocvxVW0T
        print('sVoELocvxVW0T => ' + self.cookies['sVoELocvxVW0T'])
        print('User-Agent => ' + self.headers['User-Agent'])

        print('text_url => ' + text_url)
        response = requests.get(
            text_url,
            cookies=self.cookies,
            headers=self.headers,
            timeout=8,
            verify=False
        )

        # time.sleep(1.5)
        res_text = response.text
        # print(res_text)
        if 'html was not found on this server' in res_text:
            return '-1'

        # <tr bgcolor="#ffffff" class="xx">(.*?)</tr>
        res_list = re.compile('<tr bgcolor="#ffffff" class="xx">(.*?)</tr>', re.S).findall(res_text)
        if len(res_list) == 0:
            return '-2'

        for res_list_item in res_list:
            # print('res_list_item => ' + res_list_item)
            json_line = {}
            json_line['name'] = name

            #<a href="(.*?)</a>
            dis_info = re.compile('<a href="(.*?)\'  >', re.S).findall(res_list_item)[0]
            # print('dis_info => ' + dis_info)
            dis_url = dis_info.split('" target="_blank" title=\'')[0]
            dis_title = dis_info.split('" target="_blank" title=\'')[1].strip()
            print('dis_url => ' + dis_url)
            print('dis_title => ' + dis_title)

            #<td align="left" style="padding-left:5px;">GB 15983-1995</td>
            bianhao = re.compile('<td align="left" style="padding-left:5px;">(.*?)</td>', re.S).findall(res_list_item)[0]
            print('bianhao => ' + bianhao)

            #<td align="center"><p>19960701</p></td>
            time_info = re.compile('<td align="center"><p>(.*?)</p></td>', re.S).findall(res_list_item)[0]
            print('time_info => ' + time_info)

            json_line['dis_title'] = dis_title
            json_line['dis_url'] = dis_url
            json_line['bianhao'] = bianhao
            json_line['time_info'] = time_info

            json_text = json.dumps(json_line, ensure_ascii=False)
            print(json_text)
            self.write2File('b_wjw_url.txt', json_text + '\n')


    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)


    def getsVo(self):
        self._websocket.send('123432')


    def webS(self):
        # 把ip换成自己本地的ip
        start_server = websockets.serve(self.main_logic, 'localhost', 8010)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    # 服务器端主逻辑
    # websocket和path是该函数被回调时自动传过来的，不需要自己传
    async def main_logic(self, websocket, path):
        self._websocket = websocket
        await self.recv_msg(websocket)

    # 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
    async def recv_msg(self, websocket):
        while True:
            recv_text = await websocket.recv()
            if 'sVoELocvxVW0T=' in recv_text:
                # print(recv_text)
                self.sVoELocvxVW0T = recv_text.split('sVoELocvxVW0T=')[1]
            # response_text = f"your submit context: {recv_text}"
            # await websocket.send(recv_text)

Dump()