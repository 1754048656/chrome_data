import requests

cookies = {
    '_zap': '3fdfebd8-e96f-4fee-9061-0bd8739ff5a6',
    'd_c0': 'AGBXK-uy2RaPTsdGmEfBq2IiQfQNAd7QIiU=|1685346647',
    'captcha_session_v2': '2|1:0|10:1685346648|18:captcha_session_v2|88:aFczTUFaNU5SUTV0OVl3QjZVbHJaMkY0YUZRMjZmWFo5VXUzSVRQbVV6N1F3SzluSmFTREVYQmJURkc2cndFeQ==|ca0c85ad883b09f8665f5e099be0a561300ed38aa6b440d6e38698d6a126c52b',
    '__snaker__id': 'XEJbjv2w14W111Vd',
    'gdxidpyhxdE': 'Ou26CmrJUHCeqwIPsdhw60arAiDj9tgRNEx9%5C5Q%2FYsAzn%2FgGQE%5C6La%5CLQAtVb6Gxq7h4yhCkSEU800LD%5CT7Ag5xTWJ3wcryUTCYJPlO%2FUj%2BbTvf%2Fn%2Fnk0nWTI6xRPUMNQnbxcaIsX6xiDmN0%2BjOS2SYIqauQBSpWtWZnapku0ezwRfgz%3A1685347563498',
    'YD00517437729195%3AWM_NI': 'FS1tAY9gsgr2R5%2FTYuEfbZngMKqFFWn6hfQDljEVaKjqZ0qzLPfgan72fenOYHiU8I3BE%2FDhcjPq11w%2FtL0zC8xgBEpDvpfNC7DUT2cm15USHeaw3rX3N7uPWyTGLuz0TFE%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee82b76fb4eeb6adcf60a3ac8bb7c15f839f8a83d86495a8fcadf1529392a6a7d82af0fea7c3b92a868dff95c453fbb9bd88f13a92ebe1b5dc7f87baaebbed6d8f95bfa7c55daeeaa887d450b0b68bb7e441aaaf96d1f4729090aa88e466f5eeaa86ed459b98a7b6bb43f19e8bd0c764a1b6a092b43bb5f1bcadb37281e8b888c14fb49cba91e54681e98cb6d73aa1b3ffd6d8598cbbaf98b27a9ced82d8f85c95a79ca8cf7fbaf09ca7c837e2a3',
    'YD00517437729195%3AWM_TID': '8nn3yQkXXW1ARVFRVVOFwSxsa6dVdmVU',
    'q_c1': 'ef9b2fda5dae49a1bb59a9b19ec183ed|1685346681000|1685346681000',
    'tst': 'r',
    'z_c0': '2|1:0|10:1685346684|4:z_c0|92:Mi4xQ09Wb0dRQUFBQUFBWUZjcjY3TFpGaGNBQUFCZ0FsVk5lYWRoWlFBZC1ENmxwYWFiZkZCVUotUzFoTV9MUzNnS2xn|8831e7e3edb71386dc378c6be6a9cb6bf90f189874b732cfc1a2ad0d3d2a6bb2',
    '_xsrf': '412aa997-4b5c-4bb0-9ae9-635189d2c693',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1685346662,1685348624,1685349119,1686905835',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1686917487',
    'KLBRSID': 'fe0fceb358d671fa6cc33898c8c48b48|1686917587|1686913720',
}

headers = {
    'Host': 'www.zhihu.com',
    # 'Cookie': '_zap=3fdfebd8-e96f-4fee-9061-0bd8739ff5a6; d_c0=AGBXK-uy2RaPTsdGmEfBq2IiQfQNAd7QIiU=|1685346647; captcha_session_v2=2|1:0|10:1685346648|18:captcha_session_v2|88:aFczTUFaNU5SUTV0OVl3QjZVbHJaMkY0YUZRMjZmWFo5VXUzSVRQbVV6N1F3SzluSmFTREVYQmJURkc2cndFeQ==|ca0c85ad883b09f8665f5e099be0a561300ed38aa6b440d6e38698d6a126c52b; __snaker__id=XEJbjv2w14W111Vd; gdxidpyhxdE=Ou26CmrJUHCeqwIPsdhw60arAiDj9tgRNEx9%5C5Q%2FYsAzn%2FgGQE%5C6La%5CLQAtVb6Gxq7h4yhCkSEU800LD%5CT7Ag5xTWJ3wcryUTCYJPlO%2FUj%2BbTvf%2Fn%2Fnk0nWTI6xRPUMNQnbxcaIsX6xiDmN0%2BjOS2SYIqauQBSpWtWZnapku0ezwRfgz%3A1685347563498; YD00517437729195%3AWM_NI=FS1tAY9gsgr2R5%2FTYuEfbZngMKqFFWn6hfQDljEVaKjqZ0qzLPfgan72fenOYHiU8I3BE%2FDhcjPq11w%2FtL0zC8xgBEpDvpfNC7DUT2cm15USHeaw3rX3N7uPWyTGLuz0TFE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee82b76fb4eeb6adcf60a3ac8bb7c15f839f8a83d86495a8fcadf1529392a6a7d82af0fea7c3b92a868dff95c453fbb9bd88f13a92ebe1b5dc7f87baaebbed6d8f95bfa7c55daeeaa887d450b0b68bb7e441aaaf96d1f4729090aa88e466f5eeaa86ed459b98a7b6bb43f19e8bd0c764a1b6a092b43bb5f1bcadb37281e8b888c14fb49cba91e54681e98cb6d73aa1b3ffd6d8598cbbaf98b27a9ced82d8f85c95a79ca8cf7fbaf09ca7c837e2a3; YD00517437729195%3AWM_TID=8nn3yQkXXW1ARVFRVVOFwSxsa6dVdmVU; q_c1=ef9b2fda5dae49a1bb59a9b19ec183ed|1685346681000|1685346681000; tst=r; z_c0=2|1:0|10:1685346684|4:z_c0|92:Mi4xQ09Wb0dRQUFBQUFBWUZjcjY3TFpGaGNBQUFCZ0FsVk5lYWRoWlFBZC1ENmxwYWFiZkZCVUotUzFoTV9MUzNnS2xn|8831e7e3edb71386dc378c6be6a9cb6bf90f189874b732cfc1a2ad0d3d2a6bb2; _xsrf=412aa997-4b5c-4bb0-9ae9-635189d2c693; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1685346662,1685348624,1685349119,1686905835; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1686917487; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1686917587|1686913720',
    'x-zse-93': '101_3_3.0',
    'x-zst-81': '3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZKXY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTFiVy2LL1TvxMPCLqZrg0oHg9_JN1K6LGFgXOFGgYr7HCY_SMHgC9wwwpDwcTVMOB9vpBeUoVFUXGBqY1_cVfeDSsu9g_87g1zcUO67omag3q5B208BXLJ_tOyJOqm03CeXXLzhN8ICVYsU3LFrCLXBo9VhHBDuwyoGN_VGpsQAN_5JO0Og_z3cPK8gYyYCV926c1XgNK9CXGPDC_jJO02ipBoTLYfcXObrrLk0ts-uCBs4xGQQ90QQNp2G2YThH9cCN16U3Y2GpCBcSY6refo7YVZbeCYgw0wJxOwrOs',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'x-ab-pb': 'Cgo7ArcDiwUnB/gMEgUBAAAAAA==',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-96': '2.0_nKD=X8bocUSYw6pT3r3jixw09t2nt6NCtV7dFVtOYf/LrGOGVPD3GbI74Lehiz3Y',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zhihu.com/question/361471558',
    'accept-language': 'zh-CN,zh;q=0.9',
}

params = {
    'cursor': 'a3fb1c4d2c1ca19a43b8a4c6282283c4',
    'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled',
    'limit': '3',
    'offset': '',
    'order': 'default',
    'platform': 'desktop',
    'session_id': '1686917486525166562',
}

response = requests.get('https://www.zhihu.com/api/v4/questions/361471558/feeds', params=params, cookies=cookies, headers=headers)

print(response.text)