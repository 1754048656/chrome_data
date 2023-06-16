# import random
#
# import requests
#
# def get_uid(self, uid):
#     headers = {
#         "Accept": "application/json, text/plain, */*",
#         "Referer": "https://www.douyin.com/",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Proxy-Tunnel": str(random.randint(1, 10000))  # 设置IP切换头
#     }
#     response = requests.get(url, headers=headers)
#     print(response.text)
#     user_info = response.json()
#     if not user_info:
#         return None
#     sec_uid = user_info.get("sec_uid")
#     nickname = user_info.get("nickname")
#     return sec_uid, nickname