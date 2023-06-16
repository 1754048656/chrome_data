import json

import requests

cookies = {
    'Hm_lvt_086e860fd41dcb45bb007e07a0961bd8': '1686318320,1686537818',
    'JSESSIONID': '3F5E82779BF196B79C6CB720E334AFF8',
    'Hm_lpvt_086e860fd41dcb45bb007e07a0961bd8': '1686538111',
    'AWSALB': 'oUBNRfRjz7P5f/P2cwfV4SulH84Wg+Sh50/ReNfWBC4l+QpTNrRr3rm6N8UQEo696zxsuAC7ddhSWvQ688emxNi1YhEyu3i6dI0FYZqfjiGDC/Ap41P75FvjHV/d',
    'AWSALBCORS': 'oUBNRfRjz7P5f/P2cwfV4SulH84Wg+Sh50/ReNfWBC4l+QpTNrRr3rm6N8UQEo696zxsuAC7ddhSWvQ688emxNi1YhEyu3i6dI0FYZqfjiGDC/Ap41P75FvjHV/d',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'Hm_lvt_086e860fd41dcb45bb007e07a0961bd8=1686318320,1686537818; JSESSIONID=3F5E82779BF196B79C6CB720E334AFF8; Hm_lpvt_086e860fd41dcb45bb007e07a0961bd8=1686538111; AWSALB=oUBNRfRjz7P5f/P2cwfV4SulH84Wg+Sh50/ReNfWBC4l+QpTNrRr3rm6N8UQEo696zxsuAC7ddhSWvQ688emxNi1YhEyu3i6dI0FYZqfjiGDC/Ap41P75FvjHV/d; AWSALBCORS=oUBNRfRjz7P5f/P2cwfV4SulH84Wg+Sh50/ReNfWBC4l+QpTNrRr3rm6N8UQEo696zxsuAC7ddhSWvQ688emxNi1YhEyu3i6dI0FYZqfjiGDC/Ap41P75FvjHV/d',
    'Origin': 'https://www.yiigle.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.yiigle.com/Paper/Search?type=Guid&q=%E6%8C%87%E5%8D%97&searchType=pt',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'type': 'Guid',
    'sortField': '',
    'page': 1,
    'searchType': 'pt',
    'pageSize': 6000,
    'queryString': '指南',
    'query': '',
    'searchText': '指南',
    'searchLog': '指南',
    'isAggregations': 'N',
    'logintoken': 'f892bb1509da491a939cb13165b71a45',
}

response = requests.post('https://www.yiigle.com/apiVue/search/searchList', cookies=cookies, headers=headers, json=json_data)

res_json = response.json()
# print(res_json)
json_str = json.dumps(res_json, ensure_ascii=False)

file = open('dump_title.txt', 'a')
file.write(json_str)
