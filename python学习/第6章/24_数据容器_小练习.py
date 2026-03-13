# 练习一：水果清单
fruits = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.88,
    '哈密瓜': 8.8
}

# 需求1：打印所有的水果
for key in fruits:
    # print(key)
    print(f'{key},价格是：{fruits[key]}')
    # print(fruits[key])
# 需求2：找到最贵水果

price = 0.0
fruit = ''
for key in fruits:
    money = fruits[key]
    # print(money) # 打印水果的价格
    if (money > price):
        price = money
        fruit = key
print(f'最贵的水果是:{fruit},它的价格是:{price}')

# 获取最贵的水果
# 开发中常用，比较的是value ,返回的是对应的key
key = max(fruits, key=fruits.get)
# print(key)
print(f'最贵的水果是:{key},它的价格是:{fruits[key]}')

# 练习二：学生成绩表
students = [
    {'name': '张三',
     'scores': {'语文': 88, '数学': 92, '英语': 95}
     },
    {'name': '李四',
     'scores': {'语文': 88, '数学': 92, '英语': 95}
     },
    {'name': '王五',
     'scores': {'语文': 88, '数学': 92, '英语': 95}
     }
]

# 需求1：计算每位学生的平均分
# for stu in students:
#     print(stu)
#     score_list = stu['scores'].values()
#     # 计算平均值
#     avg = sum(score_list) / len(score_list)
#     print(f'{stu['name']}的平均成绩是:{avg:.1f}')


# 需求2：找到总分最高的学生
def find_best():
    # 记录分数最高的学生
    best_students = []
    # 记录最高分数
    best_score = 0
    for stu in students:
        score_list = stu['scores'].values()
        total = sum(score_list)
        if total > best_score:
            # 最高分
            best_students= [stu['name']] #放进列表
            best_score = total
        elif total == best_score:
            best_students.append(stu['name'])
    print(f'最高分为{best_score},取得最高分的学生是:{best_students}')

find_best() # 调用



# 练习三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1:统计“好喝”的次数
res=comment.count('好喝')
print(res)

# 需求2:将字符串中的“贵”替换为“略高”
result=comment.replace('贵','略高')
print(result)

# 需求3:是否包含“推荐”两个字
print('推荐' in comment)

# 数据容器总结
'''
有序与无序：

有序：列表（list）、元组（tuple）、字符串（str）——元素有顺序，可通过下标访问元素。

无序：集合（set）、字典（dict）——元素没有固定位置，不能用下标访问。

可修改：

可变：列表（list）、集合（set）、字典（dict）——可以对内容进行增、删、改操作。

不可变：元组（tuple）、字符串（str）——内容固定，创建后无法修改。

可重复：

允许重复：列表（list）、元组（tuple）、字符串（str）

不允许重复：集合（set）、字典（dict）
备注：字典的 key 是唯一的，但 value 可重复



'''
