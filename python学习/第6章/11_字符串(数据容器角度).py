# 字符串的下标

# msg ='welcome to python'
# print(msg)
# print(msg[3])
# print(msg[-1])

# 字符串中的字符，不可修改
# TypeError: 'str' object does not support item assignment
# msg ='welcome to python'
# print(msg)
# msg[1]='a'


# 字符串不能嵌套
# msg ='welcome to'hello' python'
# msg ='welcome to"hello'"python'
# msg ='welcome to\'hello\'python'
# print(msg)

# 常用方法
# index,
# split：将字符串按照指定自负进行分隔，并返回一个列表
# msg ='welcome to @python'
# result=msg.index('t')
# print(result)

# result2=msg.split('@')
# print(result2)

# msg ='welcome to @python'
# result3=msg.replace('n','N')

# print(result3)

# count方法：统计指定字符在字符串中出现的次数
# print(msg.count('t'))

# strip方法：从某个字符串中删除指定字符串中的任意字符
# 从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
# msg2 ='666 尚python北6京666'
# result4=msg2.strip('6')
# print(result4)

# 这个指定的字符串是不挑顺序，只有存在就是干掉
# msg3 ='1234尚python北34京4321'
# result5=msg3.strip('1324')
# print(result5)
#
#
# msg4='34215尚python北34京4132' #'15尚python北34京41'
# result6=msg4.strip('5432')
# print(result6)


# 开发中常用去除空格
# msg5=' 北京你好  '
# result7=msg5.strip()
# print(result7)

# len函数：统计字符串中字符的个数，字符串的长度


# 字符串的循环遍历
msg ='welcome to @python'
# while 循环
index =0
while index < len(msg):
    print(msg[index])
    index+=1

print('*'*10)
# for 循环
for item in msg:
    print(item)

print('*' * 10)


for i in range(1,len(msg)):
    print(msg[i])
    i+=1







