import requests

cookies = {
    'wzws_sessionid': 'gDExNC4yNDguMTI0LjEyMIFmOTBmY2OgZIA/O4I5MGRhNGI=',
    'sVoELocvxVW0S': '5CU1yaPmSzL9VdJY7ptf89Lp8hjzRmQMji9DKFr6WPdyUW1umdjWaOXIn0PRBBfSb.T58HJie.w_fQcvwfQuIQq',
    'insert_cookie': '96816998',
    'yfx_c_g_u_id_10006654': '_ck23060716263714679133701521441',
    'arialoadData': 'true',
    'yfx_f_l_v_t_10006654': 'f_t_1686126397461__r_t_1686276306150__v_t_1686278599787__r_c_2',
    'sVoELocvxVW0T': '5REhW2K1cuxGqqqDEvXZ.7GU2_Ua3YukrvYsggMmhE1PURaqVjH1aRaEjLAZyAW1cWkaKTKcyFPt1bRH.qJztOuZTM4427IfMPtz_zG3NbjxWZ1nfbi4lqcK3_Arzdc73vdettghP1SZQ6OcLq4.eMlIIoFsI_VvH0XscbxLn7VWV8TV9RYyPFBumgnyL_oMMkSQv12.Rrq1qhMftfBoSTs69kjuRJw_4bBb_fXSmde8aBWeJbdzi2E_e2IwPPlMZWl6SuJu1gSqptlhLXAedAIEzwIJUsT9JbKZTavsAOruE2L4upI6qqn8j1_5SSU4qrb6vkEbS_8j_E.A5suCYAf',
}

headers = {
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

response = requests.get(
    'http://www.nhc.gov.cn/ewebeditor/uploadfile/2014/12/20141212170935617.pdf',
    cookies=cookies,
    headers=headers,
    verify=False,
)

with open("pdf_dir/example.pdf", "wb") as f:
    f.write(response.content)