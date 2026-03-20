import asyncio


# await 关键字的作用：
# 1. 挂起：await 会暂停当前协程的执行。
#
# 2. 等待：遇到 await 关键字，事件循环会立即安排 await 后面的对象去执行，并等待该对象执行完成，并且可以拿到执行结果。
#    - 关键点：在执行 await 后面的对象时，会出现两种情况：
#     - 情况一：如果在执行该对象中的代码时，遇到了【await I/O操作】（需要等待外部资源返回结果的操作）
#     例如：网络请求、文件读写等。
#     那 CPU 的控制权就会交给事件循环。
#     事件循环会去调度循环中的其他任务（如果有的话）。
#     - 情况二：如果该对象中的代码，不包含任何【await I/O操作】。
#     例如：print打印、数学计算、逻辑计算等。
#     此时事件循环不会到 CPU 控制权，无法调度循环中的其他任务，不会发生任务切换。
#
# 3. 恢复：当 await 后的对象执行完毕，事件循环会恢复之前被挂起的协程，该协程会从当时挂起的位置继续执行，并拿到返回值。

# 注意：awit后面只能写【可等待对象】 1、 future对象 2、协程对象 3、task对象
async def work():
    print('工作开始')
    print('工作中。。。')
    # 模拟io等待,有返回值，但是返回值没有意义
    res = await asyncio.sleep(2)
    print(res)
    print('工作结束')
    return '工作结果'


async def main():
    print('main工作开始')
    # 等待一个协程对象
    res = await work()
    print('mian工作中。。。')
    print('main工作结束')
    return 'main工作结果'


# 调用协程函数 会得到协程对象


# asyncio.run 做了3件事：
# 1。创建一个事件循环
# 2.将收到的协程对象，包装成一个任务task，交给事件循环
# 3.启动事件寻循环
# 注意：asyncio.run会阻塞当前线程，直至任务完成，并返回该任务的执行结果
result = asyncio.run(main())
print(result)
