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

    # asyncio.gather 把多个协程对象同时丢给事件循环，并在全部执行完后，一次性拿到所有结果。
    result = asyncio.gather(work(1,2),work(2,2),work(3,2))

    print(result)
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













