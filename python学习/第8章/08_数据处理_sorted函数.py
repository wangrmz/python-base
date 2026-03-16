# sorted函数：对一组数据进行排序，并返回一组新数据。
# 语法格式：sorted(可迭代对象,key=xxx,reverse=xxx)

# 数字排序
# nums=[16,2,60,4,50]
# result = sorted(nums)
# # result = sorted(nums,reverse=True)# 从大到小
# print(result) #[2, 4, 16, 50, 60]


# 按照字符串的长度进行排序
# names=['python','java','sql']
# # result=sorted(names) #['java', 'python', 'sql'] 这是默认是按照字符串的Unicode进行排序的
#
# # 自己定义
# result=sorted(names,key=lambda n:len(n)) #['sql', 'java', 'python']
# result2=sorted(names,key=len,reverse=True) #['python', 'java', 'sql']
# print(result)
# print(result2)


# 根据字典的某个字段进行排序
persons = [
    {'name':'zhangsan', 'age':14 ,'gender':'male'},
    {'name':'lisi', 'age':15 ,'gender':'female'},
    {'name':'wangwu', 'age':16 ,'gender':'male'},
    {'name':'zhaoliu', 'age':21 ,'gender':'male'},
    {'name':'lihua', 'age':22 ,'gender':'female'},
    {'name':'sunqi', 'age':13 ,'gender':'male'},
]

result = sorted(persons, key=lambda x: x['age'], reverse=True)

print(list(result))

# max函数，min函数，也是可以传递key参数，用于设置筛选数据
nums =[10,20,30,40,50]
result1 = max(nums)
result2 = min(nums)
result22 = max(persons, key=lambda x: x['age'])
print(result22) #{'name': 'lihua', 'age': 22, 'gender': 'female'}





