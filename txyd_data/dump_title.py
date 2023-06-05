import requests

cookies = {
    'RK': 'ktH07f4JQs',
    'ptcz': 'f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15',
    'bk_token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
    'bk_uin': '3000001307478811',
}

headers = {
    '17a3c89965b3': 'c82268e4',
    '236a604fb8a6': '1685523579132',
    '94b9f47267ea': '0be38797eb4986e8d2bd4393361958e9de65cabf',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer 130bb675-694e-405a-88a7-a17d3a38912d-yk',
    'Connection': 'keep-alive',
    # 'Cookie': 'RK=ktH07f4JQs; ptcz=f7ccf2ffa0c98ffaadd652f3a8a377c1792faca8ba218a387e2e6d34635f7c15; bk_token=130bb675-694e-405a-88a7-a17d3a38912d-yk; bk_uin=3000001307478811',
    'Origin': 'https://h5.baike.qq.com',
    'Referer': 'https://h5.baike.qq.com/mobile/overview_detail.html?id=sy20355010zw7aww&name=%E6%B5%91%E8%BA%AB%E9%85%B8%E7%97%9B&m=b4629323ae9c65ae51a7e3ca714b7b05&m=b4629323ae9c65ae51a7e3ca714b7b05&tab=bingyin&searchid=89fd85256e6900bf0f3d99becdb1c4ae&VNK=7059db02&TNK=9dd63b17',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/json',
    'd5ccfadd2a55': '08df1a6f0985a80bc650dc92ae03e6223b45c671',
    'f6ff59b173b4': '0',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-tde-env-id': '',
}

params = {
    'timestamp': '1685523717153',
}

json_data = {
    'header': {
        'version': 2,
        'flag': 0,
    },
    'body': {
        'seq': 57,
        'cmd': 'BatchGetDiseaseTabData',
        'token': '130bb675-694e-405a-88a7-a17d3a38912d-yk',
        'client': {
            'platform': 1,
            'os': 0,
            'env': '',
            'isTourist': 49,
            'adtag': '',
            'vnk': '9dd63b17#bingyin',
            'product': 8,
        },
        'payload': {
            'tabs': [
                '概述',
                '病因',
                '表现',
                '就医',
                '治疗',
                '防护',
            ],
            'disease': '浑身酸痛',
            'id': 'sy20355010zw7aww',
        },
        'traceid': 'e9c932cd-7350-43f9-a374-a122b86f90b2',
    },
}

response = requests.post(
    'https://h5.baike.qq.com/api/access/json/cmd/BatchGetDiseaseTabData',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"header":{"version":2,"flag":0},"body":{"seq":57,"cmd":"BatchGetDiseaseTabData","token":"130bb675-694e-405a-88a7-a17d3a38912d-yk","client":{"platform":1,"os":0,"env":"","isTourist":49,"adtag":"","vnk":"9dd63b17#bingyin","product":8},"payload":{"tabs":["概述","病因","表现","就医","治疗","防护"],"disease":"浑身酸痛","id":"sy20355010zw7aww"},"traceid":"e9c932cd-7350-43f9-a374-a122b86f90b2"}}'.encode()
#response = requests.post(
#    'https://h5.baike.qq.com/api/access/json/cmd/BatchGetDiseaseTabData',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)