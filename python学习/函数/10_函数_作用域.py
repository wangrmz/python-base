'''
全局作用域 vs 局部作用域
全局：在当前文件的任意位置都能使用
局部：只能在当前函数中使用，在函数调用时创建，在函数执行结束后销毁
'''

a = 100
b = 200

def test():
    c='hello'
    d='你好啊'
    # 如果想要修改全局变量需要声明，否则还是在定义局部变量
    global  a
    a =300
    print(a)
    print(b)
    print(c)
    print(d)

test()

print('*'*10)
n =100
def test3():
    global n
    n +=1
    print(n)
test3()
test3()
print(n)