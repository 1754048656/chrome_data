import datetime
import json
import sys
import time
import subprocess

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

        # s2 = 'mitmdump -s mitmproxy_addons.py -p ' + str(mitmdumpPort)
        # s2 = 'mitmdump -s mitmproxy_addons.py -q -p ' + str(mitmdumpPort)
        s2 = 'mitmweb -s mitmproxy_addons.py -q -p ' + str(mitmdumpPort)

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
        time.sleep(9)
        with open("tencentdy/href_test.txt", 'r', encoding='utf-8') as file:
            for item in file:
                text_line = item
                text_line = text_line.strip()
                # print(text_line)
                json_line = json.loads(text_line)
                department = json_line['department']
                disease = json_line['disease']
                url_text = 'https://h5.baike.qq.com/mobile/search.html?search=' + disease
                print(url_text)
                self.driver.get(url_text)

                time.sleep(5)
        pass


Run()
