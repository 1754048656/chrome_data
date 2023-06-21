import os

def run_script(mimdumpPort):
    # 请填写参数
    #################################
    # 浏览器环境
    mimdumpPort = mimdumpPort
    #################################

    # 输出重定向到log文件中
    # com = 'python .\\run.py --searchWord=' + searchWord +' --remainder=' + remainder +' --mitmdumpPort=' + mimdumpPort +' --username=' + phoneNum +' --matchWord=' + matchWord +' --commons=' + commons +' >> ..\\logs\\' + searchWord + '.log'
    com = 'python ./run.py --mitmdumpPort=' + mimdumpPort

    print(com)
    os.system(com)