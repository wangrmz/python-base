# 前置知识一：
# 1. 每次调用函数时，Python 都会为函数创建一个新的局部作用域
# 2. 函数执行完毕后，这个局部作用域会被销毁，其中的局部变量也会随之被释放
# def outer():
#     num =10
#     num+=1
#     print(num)
# outer()
# outer()

# # 前置知识二：
# 1. 在 Python 中，【内层函数】可以访问其【外层函数】作用域中的变量
# 2. 访问外层函数变量无需使用 nonlocal；但修改外层变量时要使用 nonlocal

# def outer():
#     num =10
#     def inner():
#         nonlocal num
#         num =99
#         print('inner中的的num:',num)
#     inner()
#     print('num:',num)
#
# outer()

# 什么是闭包？：--- 闭包= 内层函数+被内层函数所引用到的外层变量
# 闭包产生的条件：
# 1.要有函数嵌套
# 2.在【内层函数】中，要访问【外层函数】的变量
# 3.并且在【外层函数】中腰返回【内层函数】。--只有返回了【内层函数】闭包才能活下来
# def outer():
#     num = 10
#     num1 = 100
#     msg='来苏州玩'
#     print(hex(id(num))) #0x103d42ad8
#
#     def inner():
#         nonlocal num, num1
#         num += 1
#         print('inner中的的num:', num)
#
#     # print(id(inner))
#     return inner
#
#
# f = outer()
# f() # 11
# f() # 12
# f() # 13

# print(id(f))
# 结论：
# 1. outer函数中，被inner所使用到的那些变量会被封存到【闭包单元(ce11)】中。
# 如果没有被内层用到，是不会被封存到闭包的
# 2. 这些 ce11 会组成一个 __closure__ 元组，最终放在了 inner 函数身上。

# 打印__closure__元组
# (<cell at 0x104403580: int object at 0x1058a2ad8>, <cell at 0x1044035b0: int object at 0x1058a2ad8>)
# print(f.__closure__)
# print(f.__closure__[0]) #打印元组中的某一项
# print(f.__closure__[0].cell_contents) #打印元组中的某一项的具体值
# print(f.__closure__[1].cell_contents) #打印元组中的某一项的具体值


# 注意点：
# 1.调用n次外层函数，就会得到n个不同的闭包，并且这些闭包之间互不影响
# def outer():
#     num = 10
#     num1 = 100
#     msg = '来苏州玩'
#
#     def inner():
#         nonlocal num, num1
#         num += 1
#         print('inner中的的num:', num)
#
#     return inner
#
#
# f1 = outer()
# f2 = outer()
# f1() #11
# f1() #12
# print('*' * 20)
# f2() #11
# f2() #12

# 2.内层函数中的用到的外层变量是可变对象，多个闭包之间互不影响
# def outer():
#     nums=[]
#     def inner(value):
#         # nonlocal nums
#         nums.append(value)
#         print(nums)
#     return inner
#
# f1=outer()
# f1(10)
# f1(20)
# f1(30)
# print('*'*20)
# f2=outer()
# f2(66)

# 闭包的优点：
# 1. 可以“记住”状态：不用全局变量，也不用写类，就能在多次调用之间保存数据。
# 2. 可以做“配置过的函数”：先传一部分参数，把环境固定住，得到一个定制版函数。
# 3. 可以实现简单的“数据隐藏”：外层变量对外不可见，只能通过内层函数访问。
# 4. 是装饰器（decorator）等高级用法的基础。
# def beauty(char, n):
#     def show_msg(msg):
#         print(char * n + msg + char * n)
#
#     return show_msg
#
#
# f = beauty('&', 5)
# f('你好')

# 闭包的缺点：
# 1. 理解成本较高：对初学者不太友好，滥用会让代码难读。
# 2. 如果闭包里引用了很大的对象，又长期不释放，可能会增加内存占用。
# 3. 很多场景下，其实用【类 + 实例属性】会更清晰，闭包不一定是最优解。
class Beauty:
    def __init__(self,char,num):
        self.char = char
        self.num = num

    def show_msg(self,msg):
        print(self.char * self.num + msg + self.char * self.num)

b1=Beauty('*',5)
b1.show_msg('你好') # *****你好*****