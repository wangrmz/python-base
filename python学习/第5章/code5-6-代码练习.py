# 打印m行n列 *
# 方式1
# m = 4
# n = 5
# for i in range(m):
#     print('*' * n)

# 方式2
# m = 4
# n = 5
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()


# *                 1: 1 = n*2-1
# ***               2: 3
# *****             3: 5
# *******           4: 7
# *********         5: 9
# ***********
# *************
#  打印n行的等腰三角形
# n = 7
# a = 1
# b= n-1
# for i in range(n):
#     print(' '* b + '*' * a)
#     a += 2
#     b -= 1

# 简化 找到数量关系
n = 10
for i in range(n):
    print(' '* (n-1-i) + '*' * (i *2 +1))


# 穷举
peach =1
while True:
    d1= peach //2 -1
    d2= d1 //2 -1
    d3= d2 //2 -1

    if   d3==1:
        print(peach)
        break
    peach += 1
