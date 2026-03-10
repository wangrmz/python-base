x = 10

# match语句
match x:
    case 1:
        print('x is 1')
    case 2:
        print('x is 2')
    case _:  # 匹配所有其他值
        print('x is not 1 or 2')

# 匹配字符串
s = 'hello'
match s:
    case 'hello':
        print('正确')
    case 'hell':
        print('不正确')
