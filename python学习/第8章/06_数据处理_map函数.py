# map函数：对一组数据中的每一个元素，统一执行某种操作（加工），并生成一组新的数据
# 语法格式：map（操作函数，可迭代对象）

# 统一数据处理
# nums = [10, 20, 30, 40]
# # def double(x):
# #     return x * 2
# # map函数的返回值是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
# result = map(lambda x:x * 2, nums)
# print(list(result))
# print(nums)

# 字符串转换
# names =('python','java','js')
# result = map(lambda x: x.upper(), names)
# print(tuple(result)) #('PYTHON', 'JAVA', 'JS')
#
# # 类型转换
# str_number={'1','2','3','4','5','6','7','8','9'}
# result = map(int, str_number)
# print(list(result)) #[1, 9, 2, 3, 8, 5, 4, 6, 7]

#注意点：
# 1.延迟执行：map不会立刻计算，只有在‘需要结果’时候才执行计算
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”
# 3.map不会影响元素数量

nums=[10,20,30,40]
result = map(lambda x:x * 2, nums)
# 需要的话可以进行保存
nums2=list(result)
# print(list(result)) # 在这里才去计算，遍历转换的时候
# print(list(result)) # []这一行就是空列表了，因为被耗尽了
print(nums2)



