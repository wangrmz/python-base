import copy

# 浅复制 VS 深复制
# 直接赋值 ：两个变量指向同一个对象，修改其中一个，会互相影响
# nums1 =[10,20,30,40,50]
# nums2 = nums1
# nums2[3]=99
# print(id(nums1),id(nums2))

#  浅拷贝：创建一个新的外层容器，但内部元素仍然引用原来的对象
# nums1 =[10,20,30,40,50]
# nums2 = copy.copy(nums1)
# nums2[3]=99 #
# print(id(nums1)) # 4301244544
# print(id(nums2)) # 4301404096
# print(nums1[3]) # 40
# print(nums2[3]) # 99

# 问题：嵌套数据仍然是共享的，修改嵌套数据会互相影响
# nums1 =[10,20,30,[40,50]]
# nums2 = copy.copy(nums1)
# print(id(nums1))
# print(id(nums2))
# nums2[3][0]=99
# print(nums1[3][0]) # 99
# print(nums2[3][0]) # 99

# 深拷贝：创建一个新的外层容器，并对其内部所有的【可变子对象】进行递归复制
# 深拷贝是比较消耗性能的，如果希望拷贝出来的数据和原来的没有一点关系就使用深拷贝
# nums1 =[10,20,30,[40,50]]
# nums2 = copy.deepcopy(nums1)
# nums2[3][0]=99
# print(nums1[3][0]) # 40
# print(nums2[3][0]) # 99


# 备注：
# 1. 深拷贝可以彻底消除数据之间的互相影响
# a=666
# b=copy.deepcopy(a)
# print(id(a))
# print(id(b))

# 2. 深拷贝遇到【不可变对象】不会复制，会直接引用
# 元组中的对象是不可变对象，深拷贝是没有用的
nums1 = (10, 20, 30, (40, 50))
nums2 = copy.deepcopy(nums1)

print(id(nums1))  # 4374436320
print(id(nums2))  # 4374436320

# 总结：区分可变对象，不可变其实没影响，重点是可变对象
