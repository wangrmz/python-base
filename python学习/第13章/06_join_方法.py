# join 方法的作用：阻塞当前进程，等 join 前面的进程执行完，再继续往下执行。
# join(timeout)，其中 timeout 是可选参数，表示等多久，单位是秒。

# 注意点：
#   1.p.join() 不是让进程 p 等，而是让“执行这行 join 代码的那个进程”去等，等的是 p 这个进程。
#   2.当达到了 timeout 所指定的时间后，进程并不会终止，只是“不再等”了。
#   3.join 必须在 start 之后
import os
import time
from multiprocessing import Process

def speak():
    for index in range(10):
        print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = Process(target=speak)
    # 这里是os申请一个进程，随即开始执行
    # p1.join()：这里会报错，can only join a started process，只能join一个已开启的进程
    p2 = Process(target=study)
    # 这里是os申请一个进程，随即开始执行
    p1.start()
    #  p1.join():等待p1执行完毕
    # 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位；
    # 一个进程里可以有多个线程，进程内部共享资源；进程之间不共享资源，进程类似工厂，线程类似工厂内部流水线
    # 让主进程等 p1 5秒钟，join阻塞的是当前执行的进程，这里也就是主进程，
    p1.join(5)


    p2.start()
    # p1.join() # 让主进程等 p1 进程执行完毕后，主进程再继续执行。
    # p2.join() # 让主进程等 p2 进程执行完毕后，主进程再继续执行。
    print('我是主进程中的【最后一行】打印')