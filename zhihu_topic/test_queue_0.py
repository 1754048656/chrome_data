from multiprocessing import Process, Queue, set_start_method
import time,random,os


def consumer(q):
    while True:
        res=q.get()
        if res is None: break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))


if __name__ == '__main__':
    set_start_method('fork')

    q=Queue()

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    c1.start()
    print('进程间通信-队列-主进程')