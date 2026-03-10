# input()的使用:捕获键盘的输入，认为输入都是字符串
# a = input("请输入你的名字：")
# print(a)

# 任务1
name = input("请输入你的名字：")
print(name)

# 任务2
age = input("请输入你的年龄：")
# print(type(age))
year = 2024
# print(type(year))
birth = year - int(age)
print("出生年份是 %d 年" % (birth))
