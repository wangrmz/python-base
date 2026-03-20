# 定义一个协程函数
import asyncio
import time


async def work(n, delay):
    print(f'work{n}开始')
    print(f'work{n}执行中')
    # 模拟一个IO等待
    await asyncio.sleep(delay)
    print(f'work{n}结束')
    return f'work{n}的返回值'


async def mian():
    print('mian')

    start = time.time()
    # 调用三次work函数，分别调用三个协程对象，调用协程函数就会得到协程对象
    # asyncio.create_task 会把一个协程对象包装成一个可被事件循环调度的任务，并注册到事件循环中去
    task1 = asyncio.create_task(work(1,2))
    task2 = asyncio.create_task(work(2,2))
    task3 = asyncio.create_task(work(3,2))



    # 此处会等待coroutine1执行完成
    res1 = await task1
    print(res1)

    # 此处会等待上面的coroutine1执行完成，在等待coroutine2完成
    res2 = await task2
    print(res2)

    # 此处会等待上面的coroutine2执行完成，在等待coroutine3完成
    res3 = await task3
    print(res3)

    end = time.time()-start
    print(end)
    print('mian结束')
    return '我是main的返回值'


# 将协程对象交给事件循环
result = asyncio.run(mian())
print(result)


# 程序执行过程
# mian
# work1开始
# work1执行中
# work2开始
# work2执行中
# work3开始
# work3执行中
# work1结束
# work2结束
# work3结束
# work1的返回值
# work2的返回值
# work3的返回值
# 2.0010948181152344
# mian结束
# 我是main的返回值













