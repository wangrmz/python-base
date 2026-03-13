# tuple的创建
'''
元组中的元素是不可修改的，只能查

'''
# 定义元组
tuple1 =(1,2,3,True,'hello')
print(tuple1)
print(type(tuple1))
list1 =[1]
print(list1)
# python解释器只有一个元素会误会是int类型，可以添加一个,
tuple2=(1,)
print(type(tuple2))

print('*'*10)
# 元组的下标
# 元组中的元素不可修改
t1=(28,44,66,89,11)
print(t1[3])
# t1[0]=100
# 元组中的元素不可修改,但是元组中如果存放了可变类型（列表），那么可变类型中的内容仍可修改
t2=(28,44,66,89,11,[100,200,300,('你好','世界')])
print(t2)
# t2[5]=400
t2[5][2]=400
print(t2)


print('*'*10)

tuple3=() # 类型转换
print(type(tuple3))

tuple5=tuple('hello') # str->tuple
print(type(tuple5))
print(tuple5)

tuple6= tuple([1,2,3,4,5,6]) # list->tuple
list1=list(tuple6)
print(list1)

print('*'* 10)
str1=str(tuple5) #带着格式直接转换的
print(str1)
print(str1[2])
print(type(str1))

# 内置函数，max,min,len,sum,sorted(排序函数是特殊的，因为不修改原元组，返回一个新的列表)


