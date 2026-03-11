
# 行参的使用范围在函数范围之内
def greet(name,gender,age,height):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')

# 位置参数，必须和函数定义的顺序一致
greet('wangrm','女',30,165)
# 关键字参数可以不考虑顺序，支持乱序
greet(name='wangrm',gender='女',age=30,height=165)
# 混用：使用关键嘴参数时，位置参数必须在关键字参数之前
greet('wangrm',gender='女',height=165,age=30)

#错误例子
# greet(height=165,age=30,'wangrm',gender='女')

# greet('wangrm',30,165)
