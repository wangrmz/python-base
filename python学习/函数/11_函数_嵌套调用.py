# 函数的嵌套调用测试1
# def speak(msg):
#     print('-----')
#     print(msg)
#     print('-----')
#
# def greet(name,msg):
#     print(f'我叫做{name},我想说的话在下面：')
#     speak(msg)
#     print('我想说的话结束了')
#
# greet('张三','你好')

def greet(name,msg):
    print(f'我叫做{name},我想说的话在下面：')
    speak(msg)
    print('我想说的话结束了')
def speak(msg):
    print('-----')
    print(msg)
    print('-----')

greet('张三','你好')

# 函数的调用，栈结构，先进后出