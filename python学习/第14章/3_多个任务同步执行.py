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
    # 调用三次work函数，分别调用三个协程对象
    coroutine1 = work(1, 2)
    coroutine2 = work(2, 2)
    coroutine3 = work(3, 2)

    # 此处会等待coroutine1执行完成
    res1 = await coroutine1
    print(res1)

    # 此处会等待上面的coroutine1执行完成，在等待coroutine2完成
    res2 = await coroutine2
    print(res2)

    # 此处会等待上面的coroutine2执行完成，在等待coroutine3完成
    res3 = await coroutine3
    print(res3)

    end = time.time()-start
    print(end)
    print('mian结束')
    return '我是main的返回值'


# 将协程对象交给事件循环
result = asyncio.run(mian())
print(result)













