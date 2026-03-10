# while True:
#     print(111)
#     name = input('请输入你的名字')
#     if name == 'wangrm':
#         print('欢迎回家')
#         break
#     elif name == 'wangrumeng':
#         print('恭喜发财')
#         break

# for i in range(10):
#     if i > 0 and i % 3 == 0:
#         print('当前 %d 能被3整除' % (i))
#         break

# 判断一个整数n是否是质数
# 质数（素数） 是指在大于1的自然数中，除了1和它本身以外，不能被其他自然数整除的数。
# 换句话说，质数只有两个正因数：1和它本身。
# 从2开始到它本身-1 是否能整除

# n = 15
# a = 2
# flag = 0
# while a < n:
#     if n % a == 0:
#         flag = 1
#         print('不是质数')
#         break
#     a += 1
# print(flag)
# if flag == 0:
#     print(n,'是质数')
# else:
#     print(n,'不是质数')


# while + else 搭配
# n = 7
# a = 2
# while a < n:
#     if n % a == 0:
#         print(n, '不是质数')
#         break
#     a += 1
# else:
#     print(n, '是质数')


# for循环判断
# range(a,b),其中这个范围是左闭右开
n = 8
for a in range(2, n):
    if n % a == 0:
        print(n, '不是质数')
        break
else:
    print(n, '是质数')
