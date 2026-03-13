# keys方法：用于获取字典中所有的键,返回值是dict_keys
d1 = {'张三':72,'李四':66,'王五':85}
# result=d1.keys()
# print(result,type(result)) #dict_keys(['张三', '李四', '王五']) <class 'dict_keys'>
# print(d1.values()) # dict_values([72, 66, 85])
# print(d1.items()) # dict_items([('张三', 72), ('李四', 66), ('王五', 85)])

# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
# for item in result:
#     print(item)

# 借助内置的list函数，可以进行类型转换dict_keys->list
# list1=list(result)
# print(list1,type(list1)) #['张三', '李四', '王五'] <class 'list'>

# dict_values和dict_keys类似，可以转换成list
# result= d1.values()
# print(result,type(result)) # dict_values([72, 66, 85]) <class 'dict_values'>

# items方法“获取字典中所有键值对（每组键值对以元组的形式呈现）
result= d1.items()
print(result,type(result)) #dict_items([('张三', 72), ('李四', 66), ('王五', 85)]) <class 'dict_items'>
