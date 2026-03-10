# tuple的创建
tuple1 =(1,2,3,True,'hello')
print(tuple1)
print(type(tuple1))
list1 =[1]
print(list1)
# python解释器只有一个元素会误会是int类型，可以添加一个,
tuple2=(1,)
print(type(tuple2))

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

