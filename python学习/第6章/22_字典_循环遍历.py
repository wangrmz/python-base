# 字典不能使用while循环遍历，但可以使用for循环遍历

d1 = {'张三':72,'李四':66,'王五':85}

# 遍历字典
for key in d1:
    print(f'{key}的成绩是: {d1[key]}')

# 遍历字典的key
for key in d1.keys():
    print(f'{key}的成绩是: {d1[key]}')