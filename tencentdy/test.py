import requests

cookies = {
    'RK': 'ktH07f4JQs',
    'ptcz': 'f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15',
    'bk_token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
    'bk_uin': '3000001307478811',
}

headers = {
    '17a3c89965b3': '40a33722',
    '236a604fb8a6': '1685670200552',
    '94b9f47267ea': '71f6ecc1ac702c9dda370162e3dad48c0b295f11',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer 130bb675-694e-405a-88a7-a17d3a38912d-yk',
    'Connection': 'keep-alive',
    # 'Cookie': 'RK=ktH07f4JQs; ptcz=f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15; bk_token=130bb675-694e-405a-88a7-a17d3a38912d-yk; bk_uin=3000001307478811',
    'Origin': 'https://h5.baike.qq.com',
    'Referer': 'https://h5.baike.qq.com/mobile/search.html?search=%E6%B6%88%E7%98%A6&VNK=ba8831cc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/json',
    'd5ccfadd2a55': '0449f97bf72cfac493e3abda181b8c29682b04c8',
    'f6ff59b173b4': '0',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-tde-env-id': '',
}

params = {
    'timestamp': '1685671220461',
}

json_data = {
    'header': {
        'version': 2,
        'flag': 0,
    },
    'body': {
        'seq': 35,
        'cmd': 'SearchForInner',
        'token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
        'client': {
            'platform': 1,
            'os': 0,
            'env': '',
            'isTourist': 49,
            'adtag': '',
            'vnk': 'ba8831cc',
            'product': 8,
        },
        'payload': {
            'count': 15,
            'query': '消瘦',
            'type': 0,
            'searchid': 'af9b7420fb5f1401aca6c50eeea36715',
            'docidlistflag': 7,
            'cityname': '',
            'longitude': -110.1,
            'latitude': -40.1,
            'l_filter': {
                'city': '深圳市',
                'enable': True,
            },
        },
        'traceid': '02d00aad-ff24-460a-8994-11a4c8ed314c',
    },
}

response = requests.post(
    'https://h5.baike.qq.com/api/access/json/cmd/SearchForInner',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.json())

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"header":{"version":2,"flag":0},"body":{"seq":35,"cmd":"SearchForInner","token":"130bb675-694e-405a-88a7-a17d3a38912d-yk","client":{"platform":1,"os":0,"env":"","isTourist":49,"adtag":"","vnk":"ba8831cc","product":8},"payload":{"count":15,"query":"消瘦","type":0,"searchid":"af9b7420fb5f1401aca6c50eeea36715","docidlistflag":7,"cityname":"","longitude":-110.1,"latitude":-40.1,"l_filter":{"city":"深圳市","enable":true}},"traceid":"02d00aad-ff24-460a-8994-11a4c8ed314c"}}'.encode()
#response = requests.post(
#    'https://h5.baike.qq.com/api/access/json/cmd/SearchForInner',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)










