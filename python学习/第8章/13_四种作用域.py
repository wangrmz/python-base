# 全局作用域
a = 100

# 嵌套定义的时候才会出现
def test(b):  # 外层函数作用域
    # global  a
    # a =999
    print('我是test函数')
    print(f'test中打印的a是{a}')
    print(f'test中打印的参数b:{b}')
    c = 200
    d = 300
    print('test中的c和d分别是', c, d)

    def inner():  # 局部作用域
        e = 400
        nonlocal  c # 表明是外层函数作用域的c,不是本地的
        c = 999
        print('inner中的e是', e)
        print('inner中打印的c是', c)

    inner()
    # print('*******',c) # 200
    print('*******',c) # 999 这里是声明了nonlocal的已经被改变了


print('全局打印的是', a)
test(66)

# 最大的作用域是内建作用域
# Python预先定义好的东西都会放在内建作用域中，虽有的.py文件都可以直接使用
# 局部作用域的优先级最高，首先被寻找
# Local->Enclosing->Gobal->Built-in
# 当访问一个变量的时候会按上述顺序进行查找
