import datetime
import json
import sys
import time
import argparse
import subprocess

import redis
from selenium import webdriver
from selenium.webdriver.common.by import By

class Run:

    def __init__(self, mitmdumpPort, chromePort):
        print('run')

        chromePort = chromePort
        chromeDataFile = '/Users/linsheng/Desktop/chrome_data_2/'
        mitmdumpPort = mitmdumpPort

        # 任务开始
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # 开启字段
        s1 = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=' + str(chromePort) + ' --user-data-dir=' + chromeDataFile

        # s2 = 'mitmdump -s c_mitm_addons.py -p ' + str(mitmdumpPort)
        s2 = 'mitmdump -s c_mitm_addons.py -q -p ' + str(mitmdumpPort)
        # s2 = 'mitmweb -s c_mitm_addons.py -q -p ' + str(mitmdumpPort)

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
        self.driver.set_window_position(50, 0)
        self.driver.set_window_size(1050, 730)

        # 隐式等待
        # self.driver.implicitly_wait(5)

        print(s2)
        self.mitmproxy_process = subprocess.Popen(s2, shell=True)
        time.sleep(5)
        # 限定页面加载时间最大为3秒
        self.driver.set_page_load_timeout(8)
        try:
            # self.run_task()
            pass
        except Exception as e:
            print(e)
            print('--- something wrong ---')
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
        with open("topics_question.txt", 'r', encoding='utf-8') as file:

            for item in file:
                text_line = item
                text_line = text_line.strip()

                tmp_first_topic = text_line.split(' => ')[0]
                text_name = text_line.split(' => ')[1]
                text_url = text_line.split(' => ')[2]

                print(tmp_first_topic)
                print(text_name)
                print(text_url)

                # https://www.zhihu.com/topic/19616487/top-answers
                tmp_text_url = 'https://www.zhihu.com/topic/' + str(text_url) + '/top-answers'

                try:
                    self.driver.get(tmp_text_url)
                except Exception as e:
                    print('--- 打开页面出错 ---')
                    print(e)

                time.sleep(5)
                self.scroll_down(tmp_first_topic, text_name)
                time.sleep(5)

        pass

    def scroll_down(self, tmp_first_topic, text_name):
        self.r.set('tmp_first_topic', tmp_first_topic)
        self.r.set('current_name', text_name)
        scroll_bottom_num = 0
        scroll_bottom = 0
        for t in range(9999):
            print('t => ' + str(t))
            to_next = self.r.get('to_next')
            current_num = self.r.get('current_num')

            # 判断窗口高度
            if t % 9 == 0:
                print('scroll_bottom_num => ' + str(scroll_bottom_num))
                tmp_scroll_bottom = self.currentWindowHeight()
                if tmp_scroll_bottom == scroll_bottom:
                    scroll_bottom_num = scroll_bottom_num + 1
                    print('当前窗口高度未增加')
                else:
                    scroll_bottom_num = 0
                    print('窗口高度增加')
                    scroll_bottom = tmp_scroll_bottom

            # next
            if (to_next == 'T' and int(current_num) >= 20000) or scroll_bottom_num >= 15:
                print('--- 达到两万个问题 ---')
                time.sleep(5)
                self.r.set('to_next', 'F')
                self.r.set('current_num', 0)
                break

            # scroll
            self.driver.execute_script("window.scrollBy(0,600)")
            time.sleep(0.1)
        pass


    def simple_scroll(self):
        for t in range(999999):
            to_next = self.r.get('to_next')
            if to_next == 'T':
                print('--- 切换下一个 ---')
                self.r.set('to_next', 'F')
                break
            self.driver.execute_script("window.scrollBy(0,450)")
            time.sleep(1)

            # /html/body/div[3]/div[1]/div/div/div[2]/a[1]
            try:
                gengduo = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/a[1]')
                gengduo.click()
            except Exception:
                print('-=-=-=-=-=-=-')
                pass
        pass

    def write2File(self, file_name, text):
        file = open(file_name, 'a')
        file.write(text)

    def currentWindowHeight(self):
        # 获取到网页的整体高度
        hight = 'return document.body.clientHeight'
        h = self.driver.execute_script(hight)
        print('h => ' + str(h))
        return h

parser = argparse.ArgumentParser(description='manual to this script')
# parser.add_argument('--searchWord', type=str, default="双色")
# 自动选择合适的配置（端口号，文件路径，copy配置文件等）
parser.add_argument('--mitmdumpPort', type=int, default=9900)

# parser.add_argument('--chromeDataFile', type=str, default="C://Users//Administrator//Desktop//chrome_data_")
args = parser.parse_args()

chromePort = int('1' + str(args.mitmdumpPort))
# chromeDataFile = args.chromeDataFile

Run(chromePort=chromePort, mitmdumpPort=args.mitmdumpPort)

