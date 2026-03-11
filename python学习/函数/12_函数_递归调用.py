# 函数自己调用自己的一种操作
def welcome(n):
    print(f'Welcome to Python!，次数：{n}')
    if(n>1):
        welcome(n-1)
welcome(5)