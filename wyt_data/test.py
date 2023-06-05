import requests

cookies = {
    '__finger': '26bb9371cd9266cac533d4f42f1fd18c',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': '__finger=26bb9371cd9266cac533d4f42f1fd18c',
    'Referer': 'https://wenda.familydoctor.com.cn/question/all/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://wenda.familydoctor.com.cn/question/questiondatalist.do/all/0/58002/',
    cookies=cookies,
    headers=headers,
)




def write2File(file_name, text):
    file = open(file_name, 'a', encoding='utf-8')
    file.write(text)

write2File('wyt_1.json', response.text)
print('完成')