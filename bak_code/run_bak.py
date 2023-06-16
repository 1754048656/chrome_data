import datetime
import os
import argparse
import sys
import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By

#   -i http://pypi.douban.com/simple --trusted-host pypi.douban.com       pip命令安装的时候后面加上


class Run:

    def __init__(self):
        print('run')

        chromePort = '8800'
        # chromeDataFile = 'C:\\Users\\JT\\Desktop\\chrome_userdata_0\\'
        chromeDataFile = '/Users/linsheng/Desktop/chrome_data_0/'
        mitmdumpPort = '9900'

        # 任务开始
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # file = open('../logs/' + self.searchWord + '_统计.txt', 'w')
        # file.write('程序开始时间: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # file.write('\n')

        # 开启字段
        # s1 = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe --remote-debugging-port=' + str(chromePort) + ' --user-data-dir=' + chromeDataFile
        s1 = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=' + str(chromePort) + ' --user-data-dir=' + chromeDataFile
        # s1 = 'chrome --headless --remote-debugging-address=127.0.0.1 --remote-debugging-port=' + str(chromePort) + ' --disable-gpu  --user-data-dir=' + chromeDataFile

        # s2 = 'mitmdump -s mitmproxy_addons.py -p ' + str(mitmdumpPort)
        # s2 = 'mitmdump -s mitmproxy_addons.py -q -p ' + str(mitmdumpPort)
        s2 = 'mitmweb -s mitmproxy_addons.py -q -p ' + str(mitmdumpPort)

        # 重置properties中的CHORME_URL
        CHORME_URL = "127.0.0.1:" + str(chromePort)

        print(s1)
        # 打开浏览器
        # os.system('' + s1)
        self.chrome_process = subprocess.Popen(s1, shell=True)
        # self.chrome_process = subprocess.Popen(s1, creationflags=subprocess.CREATE_NEW_CONSOLE)


        # 这种方式会被知乎检测到
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

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
        # os.system('' + s2)
        self.mitmproxy_process = subprocess.Popen(s2, shell=True)
        # self.mitmproxy_process = subprocess.Popen(s2, creationflags=subprocess.CREATE_NEW_CONSOLE)
        # self.mitmproxy_process = subprocess.Popen(s2, creationflags=subprocess.CREATE_NO_WINDOW)
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

Run()
