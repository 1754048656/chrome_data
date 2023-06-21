from multiprocessing import Process, Queue, set_start_method
import time,random,os

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[46m%s 生产了 %s\033[0m' %(os.getpid(),res))
    q.put(None) #发送结束信号


if __name__ == '__main__':
    set_start_method('fork')

    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #开始
    p1.start()
    print('进程间通信-队列-主进程')