# filter函数：对一组数据中，筛选出很符合条件的元素（过滤），并组成一组新数据。
# 语法格式：filter(过滤函数，可迭代对象)


# 筛选数值
# nums=[10,20,30,40,50]
# result=filter(lambda x:x>20,nums)
# print(list(result)) #[30, 40, 50]

# 筛选成年人
# persons = [
#     {'name':'zhangsan', 'age':14 ,'gender':'male'},
#     {'name':'lisi', 'age':15 ,'gender':'female'},
#     {'name':'wangwu', 'age':16 ,'gender':'male'},
#     {'name':'zhaoliu', 'age':21 ,'gender':'male'},
#     {'name':'lihua', 'age':22 ,'gender':'female'},
#     {'name':'sunqi', 'age':13 ,'gender':'male'},
# ]
#
# result=filter(lambda x:x['age']>=18 ,persons)
# print(list(result))

# 过滤一下非法字符串
names =['zhangsan','','lisi',None,'wangwu']
result=filter(lambda x:x,names)
print(list(result)) #['zhangsan', 'lisi', 'wangwu']

#注意点：
# 1.延迟执行：filter不会立刻计算，只有在‘需要结果’时候才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.fliter可能影响元素数量。

# filter函数的特殊用法：如果不传递过滤函数，那么会自动过滤掉“假值”
data =[0,1,'','hello',[],(),5]
result=filter(None,data)
print(list(result)) #[1, 'hello', 5]