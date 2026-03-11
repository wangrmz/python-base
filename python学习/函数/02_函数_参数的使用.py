
# 行参的使用范围在函数范围之内
def order(num,dish):
    print(f'您点的是：{num}份{dish}')
    print(f'{dish}可是很好吃的')
    print(f'您只点了{num}份，够吃吗？')

order(1,'辣椒炒肉')
