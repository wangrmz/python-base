# 列表的创建
# 空列表
test =[]
print(type(test))

test=[1,2,3,45,True,False,'hello']
print(type(test))
print(test)

# 添加元素
test.append(4)
for i in test:
    print(i)

print('*'*10)
# for i in test:
#     if i%2==0: print(test[i])
print('*'*10)

list3=list() #类型转换：把参数转为列表
list4=list('1234567') #类型转换：把参数转为列表（str-list is ok）
print(list3)
print(list4)

# 列表的索引
print(list4[3])


# 列表的切片：包头不包尾
# ['1', '2', '3', '4', '5', '6', '7']
# 在Python中，可以使用列表的切片来获取列表的一部分。
# 列表切片的语法是通过使用冒号（:）来指定切片的起始位置、结束位置和步长。切片操作返回一个新的列表
print(list4[2:6:2]) # 取出list4[2]与list[6] 且左闭右开，间隔为2，所以最终取出list4[2],list[5]

# 列表的加法和乘法
print(test +list4) #两个列表合并
print(list4 * 3) #这里是重复3次的意思

# 列表的成员运算
print('1' not in list4)
print('1'  in ['1',2,3,4])
# 这里只比较了第一个元素，第一个元素小即为true，没啥意义
print([1,2,3]  < [2,3,4])

# 内置函数
print(len(list4)) #列表长度
print(min(list4)) #元素最小
print(max(list4)) #元素最大

# del list4 #删除变量
# print(list4)

#列表的遍历
print('*' * 10)
for i in test:
    print(i)

print('*' * 10)

# 带有下标进行打印
for i,j in enumerate(test): #枚举
    print(i,j)
print('*' * 10)
for i in range(len(test)):
    print(i,test[i])


# 列表的常用方法 变量.方法名()
print('*' * 10)
#添加元素
list4.append('666')
print(list4)
#添加列表
list4.extend([1,2,4])
print(list4)
# 插入元素
list4.insert(2,'hello')
print(list4)
# 根据索引来删除元素
list4.pop(3)
print(list4)
# 根据元素来删除，删除的是元素值，从头开始找，只删除第一个
list4.remove(2)
# 反转列表
list4.reverse()
# 清空列表
list4.clear()

# 计算若干人的平均年龄

age =[10,20,30,40,23,45]
total =0
for i in age:
    total += i
print(total /len(age))
print(sum(age) /len(age))