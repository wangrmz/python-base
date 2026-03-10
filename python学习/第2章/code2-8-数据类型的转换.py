# 转换成整数int
# 字符串str->整数int
# 纯数字的字符串
s = '2024'
print(s)
n = int(s)
print(type(s), type(n), sep=",")

# 浮点数float-->整数int
s1 = 2.23
print(int(s1))

# 布尔boolean->int
s2, s3 = True, False
print(int(s2), int(s3))

print("#" * 20)
# 转为浮点数float
# str->float
s = '324.6'
print(float(s))

# int->float
n = 2024
print(float(n))
# boolean ->float
print(float(s2), float(s3))

print("#" * 20)
# 运行结果，只要不是空串就为True,否则就是false

# True
# False
# str->bool
s = 'sdw323'
print(bool(s))

s1 = ''
print(bool(s1))

# 转成字符串
print("#" * 20)
# int->str
n = 5
print(str(n))
print(type(str(n)))

# float->str
f = 5.3
print(str(f))
print(type(str(f)))

# bool->str
a = True
print(type(a))
print(type(str(a)))

# 进制的转换
print("#" * 20)
s = '1a'
print(int(s, 16))
ss = '10'
print(int(ss, 2))
