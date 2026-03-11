# 函数的基本使用




# 定义函数
def welcome():
    print('欢迎来到尚硅谷课堂！')
    print('尚硅谷，让天下没有难学的技术')

#调用函数必须在定义之后
welcome()

print("*"*20)
# 参数的使用
# 行参的使用范围
def order(num,dish):
    print(f'您点的是：{num}份{dish}')

order(1,'辣椒炒肉')
order(2,'辣子鸡')