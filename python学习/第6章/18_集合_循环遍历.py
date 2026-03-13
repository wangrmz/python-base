s1={1,2,3,4,5,6,7,8,9}

# 集合不能使用while循环遍历
# index=0
# while index<len(s1):
#     print(index)
#     index+=1

for index,value in enumerate(s1):
    print(index,value)

for item  in s1:
    print(item)