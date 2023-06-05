import requests
import re

cookies = {
    'Backend-club-xywy-web-release-2': 'APALBOAK',
    'HMF_CI': '9e450f2e87048bf6731ccf4d4c4080ec8cb3b81d6daf0a9d1788ef4358f39630367550c1b67db511ae1024bfa4eb810d30f9ad6e5bed7b93fb3c35a65e70efdeb0',
    'clientac': '1684134133493963450',
    'visit_dt': '2023-4-15',
    'Hm_lvt_ece4b14847cde20fb4a1e4d486fc8846': '1684134134',
    '__bid_n': '1881e3782aa66f63ac4207',
    'FPTOKEN': 'hAA4nze60P+Owx2Z4y7JLdhE/fNoFwv7OFpaJBs5EDIw8EHbenUIiGR2L2AfbTVEa6Bz8BppZBYxiTH+paXjH3lHq4UQq9aQHGg7xbkrQdPVU8nRqgjYf+rJgtAwU69ko6W606AZZqQTTC9+0/fnQCiEoTZeB/NUMIVKljH2Q2Hql3rqQCig6zwNAs644yiSdlh6YwHX2BUDPJZVdEnhQjXn0xSekdD9iJXERgCc2vgMzVlBZLm99MkPD04JLR0Z77rEzqZ4zMvSTAvmBtipdGR5iBe3EeltvCUrNI6sYcYsICku+p8Fy5hwedlfWHgOpi/c7H3+Kb+SIHls8orNo+NGeBLphNXFrR6cBwQFLqIZ5MOafwTrvcQWyTQqZgxhjoSyiOpqSBbP5g3ylDZsushkw9XnvHB9KoD3XAWnNGLZJICI1+4lJv/H6DrDI7uX|VtHtJFQKib7ZoJVgtJHrDL5/eRQtXb4D+GxMT4mfB0g=|10|fb47865587c6deb73d5e92e75ecfa3db',
    'HMY_JC': 'd7c6c3a232b14a04426ca9a39e3a1b62d87e3a7bc4ae6ffbd227bc485030b52224,',
    'HBB_HC': '1169061eacb8100242e5af2a7e15d4f0a78bc8f7ea539a374425a0f554a1445dae08ff95d7598d8875bb43ee1a52b2ee87',
    'Hm_lpvt_ece4b14847cde20fb4a1e4d486fc8846': '1684135007',
    'xywylastUrl': 'https%253A%252F%252Fclub.xywy.com%252Fwenda%252F196507793.htm',
    'xywylastRef': 'https%253A%252F%252Fclub.xywy.com%252Fbig_297.htm',
    'XYWYDATAxywy': '1684134133-1999754206@168413413380122723214845@10',
    'XYWYDATADAYxywy': '1684134133-1684166400@10',
    'XYWYDATASESSIONxywy': '168413413380112211507@10@1684135006@1',
    'ajsDataSession': '1684134133805460742@10@1684135006@1',
    'tj_lastUrl': 'https%3A//club.xywy.com/wenda/196507793.htm',
    'tj_lastUrl_time': '1684135006771',
}

uaList = [
    # macOS
    'Chrome 9	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Safari	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Safari	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Safari 11	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15 QQBrowserLite/1.3.0',
    'Chrome 9	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Chrome 59	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Safari 11	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5',
    'Firefox 9	Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Safari	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',

    # win10
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Chrome	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Microsoft Edge	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Chrome 8	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Chrome	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Firefox 7	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',

    # win7
    'Chrome	Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Chrome 9	Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Chrome 8	Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
    'Firefox 9	Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Chrome 58	Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Chrome 51	Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.1.2',
    'Chrome	Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400',
    'Chrome 9	Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Internet Explorer 11	Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; SE 2.X MetaSr 1.0) like Gecko',
    'Chrome 9	Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'

    # Linux
    'Chrome 8	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Chrome	Mozilla/5.0 (X11; U; U; Linux x86_64; zh-my) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 Puffin/8.3.1.41624AP',
    'Opera 28	Mozilla/5.0 (Linux; BRAVIA 4K 2015 Build/LMY48E.S265) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36 OPR/28.0.1754.0',
    'Safari	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 HeyTapBrowser/40.7.29.1',
    'Chrome 9	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36 Edg/93.0.961.33',
    'Chrome 9	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Safari/537.36',
    'Opera 46	Mozilla/5.0 (Linux; Andr0id 9; BRAVIA 4K UR3 Build/PTT1.190515.001.S104) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 OPR/46.0.2207.0 OMI/4.13.5.431.DIA5HBBTV.250 Model/Sony-BRAVIA-4K-UR3',
]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'Backend-club-xywy-web-release-2=APALBOAK; HMF_CI=9e450f2e87048bf6731ccf4d4c4080ec8cb3b81d6daf0a9d1788ef4358f39630367550c1b67db511ae1024bfa4eb810d30f9ad6e5bed7b93fb3c35a65e70efdeb0; clientac=1684134133493963450; visit_dt=2023-4-15; Hm_lvt_ece4b14847cde20fb4a1e4d486fc8846=1684134134; __bid_n=1881e3782aa66f63ac4207; FPTOKEN=hAA4nze60P+Owx2Z4y7JLdhE/fNoFwv7OFpaJBs5EDIw8EHbenUIiGR2L2AfbTVEa6Bz8BppZBYxiTH+paXjH3lHq4UQq9aQHGg7xbkrQdPVU8nRqgjYf+rJgtAwU69ko6W606AZZqQTTC9+0/fnQCiEoTZeB/NUMIVKljH2Q2Hql3rqQCig6zwNAs644yiSdlh6YwHX2BUDPJZVdEnhQjXn0xSekdD9iJXERgCc2vgMzVlBZLm99MkPD04JLR0Z77rEzqZ4zMvSTAvmBtipdGR5iBe3EeltvCUrNI6sYcYsICku+p8Fy5hwedlfWHgOpi/c7H3+Kb+SIHls8orNo+NGeBLphNXFrR6cBwQFLqIZ5MOafwTrvcQWyTQqZgxhjoSyiOpqSBbP5g3ylDZsushkw9XnvHB9KoD3XAWnNGLZJICI1+4lJv/H6DrDI7uX|VtHtJFQKib7ZoJVgtJHrDL5/eRQtXb4D+GxMT4mfB0g=|10|fb47865587c6deb73d5e92e75ecfa3db; HMY_JC=d7c6c3a232b14a04426ca9a39e3a1b62d87e3a7bc4ae6ffbd227bc485030b52224,; HBB_HC=1169061eacb8100242e5af2a7e15d4f0a78bc8f7ea539a374425a0f554a1445dae08ff95d7598d8875bb43ee1a52b2ee87; Hm_lpvt_ece4b14847cde20fb4a1e4d486fc8846=1684135007; xywylastUrl=https%253A%252F%252Fclub.xywy.com%252Fwenda%252F196507793.htm; xywylastRef=https%253A%252F%252Fclub.xywy.com%252Fbig_297.htm; XYWYDATAxywy=1684134133-1999754206@168413413380122723214845@10; XYWYDATADAYxywy=1684134133-1684166400@10; XYWYDATASESSIONxywy=168413413380112211507@10@1684135006@1; ajsDataSession=1684134133805460742@10@1684135006@1; tj_lastUrl=https%3A//club.xywy.com/wenda/196507793.htm; tj_lastUrl_time=1684135006771',
    'Referer': 'https://club.xywy.com/big_297.htm',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Chrome	Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
#<div class="reply-doc-tit"><span class="name">周恒</span><span class="lable">副主任医师</span><span>内科</span></div>
#<div class="reply-doc-tit"><span class="name">(.*?)</span></div>
response = requests.get('https://club.xywy.com/wenda/196535355.htm',cookies=cookies, headers=headers, timeout=8)
# print(response.text)

try:
    res = re.compile('<span class="name">(.*?)<div class="reply-doc-bt">', re.S).findall(response.text)[0]
    # print('res => ' + res)
    #医生名称
    doctor_name = res.split('</span>')[0]
    print('医生名称 => ' + doctor_name)
    #医生职称
    #<span class="lable">主治医师</span>
    doctor_label = re.compile('<span class="lable">(.*?)</span>', re.S).findall(res)[0]
    print('医生职称 => ' + doctor_label)
    #医生科室
    #<span>内科</span>
    doctor_department = re.compile('<span>(.*?)</span>', re.S).findall(res)[0]
    print('医生科室 => ' + doctor_department)

    # <div class="reply-doc-bt">
    #     <span class="label">三级甲等</span>
    #     <span>武汉大学人民医院</span>
    # </div>
    hospital_info = re.compile('<div class="reply-doc-bt">(.*?)</div>', re.S).findall(response.text)[0]
    # print('hospital_info => ' + hospital_info)
    #医生医院
    #<span>武汉大学人民医院</span>
    hospital_name = re.compile('<span>(.*?)</span>', re.S).findall(hospital_info)[0]
    print('医生医院 => ' + hospital_name)
    #医院标签
    #<span class="label">三级甲等</span>
    hospital_label = re.compile('<span class="label">(.*?)</span>', re.S).findall(hospital_info)[0]
    print('医院标签 => ' + hospital_label)
except Exception as e:
    print(e)

try:
    # <div class="m-ques-para clearfix no-border">
    #     <p class="fl age">性别：女</p>
    #     <p class="fl">年龄：32</p>
    #     <!-- <p class="fr">2021-03-25 14:57:07</p> -->
    # </div>
    patient_info = re.compile('<div class="m-ques-para clearfix no-border">(.*?)</div>', re.S).findall(response.text)[0]
    # print('patient_info =>' + patient_info)
    #患者年龄
    #<p class="fl age"></p>
    patient_age = re.compile('<p class="fl">(.*?)</p>', re.S).findall(patient_info)[0]
    print('患者年龄 => ' + patient_age.split('年龄：')[1])
    #患者性别
    #<p class="fl"></p>
    patient_gender = re.compile('<p class="fl age">(.*?)</p>', re.S).findall(patient_info)[0]
    print('患者性别 => ' + patient_gender.split('性别：')[1])
    #问诊时间
    #<p class="fr">2021-03-25 14:57:07</p>
    patient_time = re.compile('<p class="fr">(.*?)</p>', re.S).findall(patient_info)[0]
    print('问诊时间 => ' + patient_time)
except Exception as e:
    print(e)