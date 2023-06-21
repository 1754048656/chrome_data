import datetime
import json
import sys
import time
import subprocess

import redis
from selenium import webdriver
from selenium.webdriver.common.by import By

class Run:

    def __init__(self):
        print('run')

        chromePort = '8800'
        chromeDataFile = '/Users/linsheng/Desktop/chrome_data_0/'
        mitmdumpPort = '9900'

        # 任务开始
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # 开启字段
        s1 = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=' + str(chromePort) + ' --user-data-dir=' + chromeDataFile

        # s2 = 'mitmdump -s mitm_addons.py -p ' + str(mitmdumpPort)
        s2 = 'mitmdump -s mitm_addons.py -q -p ' + str(mitmdumpPort)
        # s2 = 'mitmweb -s mitm_addons.py -q -p ' + str(mitmdumpPort)

        # 重置properties中的CHORME_URL
        CHORME_URL = "127.0.0.1:" + str(chromePort)

        print(s1)
        # 打开浏览器
        self.chrome_process = subprocess.Popen(s1, shell=True)

        # 创建浏览器对象
        options = webdriver.ChromeOptions()
        # 接管chrome浏览器
        options.add_experimental_option("debuggerAddress", CHORME_URL)
        self.driver = webdriver.Chrome(options=options)

        time.sleep(2)
        # 调整窗口大小
        self.driver.set_window_position(350, 0)
        self.driver.set_window_size(1050, 730)

        # 隐式等待
        # self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(6)

        print(s2)
        self.mitmproxy_process = subprocess.Popen(s2, shell=True)
        time.sleep(5)
        # 限定页面加载时间最大为3秒
        self.driver.set_page_load_timeout(8)
        self.run_task()

        time.sleep(9 * 99999)

    # 销毁对象时关闭进程
    def __del__(self):
        try:
            sys.stdout.flush()
            print('关闭浏览器进程')
            # 关闭浏览器进程
            self.chrome_process.terminate()
            # 关闭抓包工具进程
            self.mitmproxy_process.terminate()
        except :
            pass

    def run_task(self):
        self.r = redis.Redis(host='127.0.0.1', port='6379', decode_responses=True)
        with open("zhihu_topic/z_res.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)

                self.scroll_down(text_line)
                time.sleep(5)

        pass

    def scroll_down(self, text_line):
        text_name = text_line.split(' => ')[0]
        text_url = text_line.split(' => ')[1]
        print(text_name)
        print(text_url)
        self.r.set('current_name', text_name)
        try:
            self.driver.get(text_url)
        except Exception as e:
            print('--- 打开页面出错 ---')
            print(e)
        time.sleep(5)
        for t in range(999999):
            to_next = self.r.get('to_next')
            if to_next == 'T':
                print('--- 达到两万个问题 ---')
                self.r.set('to_next', 'F')
                self.r.set('current_num', 0)
                break
            self.driver.execute_script("window.scrollBy(0,500)")
            time.sleep(0.2)
        pass


Run()
