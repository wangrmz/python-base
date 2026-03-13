#列表的遍历

test=[1,2,3,45,True,False,'hello']
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