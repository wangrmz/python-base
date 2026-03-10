# print('hello python')

# for i in range(5):
#     print('hello python')
#     print(i)
#
# print(list(range(10)))
# 高斯求和
# result =0
# for i in range(101):
#     result +=i
#
# print(result)


# 阶乘 1！+2！+3！...+n!
# 内外变量不要重复
# 1！=1*1
# 2!=2*1
# 3!=3*2*1
# 4!=4*3*2*1
# 嵌套for循环
# result2 = 0
# for n in range(5):
#     if n > 0:
#         result = 1
#         for i in range(n + 1):
#             if i > 0:
#                 result *= i
#         print(result)
#         result2 += result
#
# print(result2)

# while循环 嵌套
n = 1
result2 = 0
while n < 5:
    result = 1
    m = 1
    while m <= n:
        result *= m
        m += 1
        print(result)
    result2 += result
    n += 1
print(result2)
