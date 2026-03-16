# 变量类型注解：给变量加上类型说明，增强代码的可读性，让IDE的提示更友好
num: int = 100
price: float = 12.5
message: str = '你好啊'
is_vip: bool = True
result: None = None  # 语法上没有问题，但是没有意义

# 注意：可以先写变量的类型注解，以后在赋值
school: str
print('****')
school = '苏州'

# hobby是列表，并且列表中的所有元素都是str
hobby: list[str] = ['打球', '听音乐', '看电影']

# hobby是列表，并且列表中的所有元素可以是str 或者 int 类型 python3.10以及以上版本才可以使用管道符 “｜”
hobby: list[str | int] = ['打球', '听音乐', '看电影']
# 上面的这行代码的旧写法如下：
from typing import Union

hobby: list[Union[str, int]] = ['打球', '听音乐', '看电影']

# cities是集合，并且集合中的所有元素都是str
cities: set[str] = {'北京', '深圳', '上海'}
cities.add('苏州')

# cities是集合，并且集合中的所有元素可以是str、float、bool类型
cities: set[str | float | bool] = {'北京', '深圳', '上海'}
cities.add('苏州')
cities.add(True)

# 字典类型
# persons 是字典，键是str 类型，值是int类型
persons: dict[str, int] = {'张三': 18, '李四': 19, '王五': 20}

# persons 是字典，键是str 类型或者int类型，值是int类型
persons: dict[str | int, int] = {'张三': 18, '李四': 19, '王五': 20}
persons[222] = 24
print(persons)  # {'张三': 18, '李四': 19, '王五': 20, 222: 24}

# 元组类型的声明比较特殊,元组是不可变的
#  scores是元组，并且元组中只能包含1个int类型的元素
scores: tuple[int] = (60,)
#  scores是元组，并且元组中包含3个int类型的元素
scores: tuple[int, int, int] = (60, 70, 80)

#  scores是元组，并且元组中包含任意个int类型的元素
scores: tuple[int, ...] = (60, 70, 80,100,2111)


#  scores是元组，并且元组中包含任意个元素，但是每个元素的类型可以是int或者str
scores: tuple[int | str, ...] = (60, 70, 80,100,2111,'你好')

# Python 会根据初始赋值推导变量的类型：
# 1. 对于普通变量：后续如果改变类型，不会警告。
# 2. 对于容器变量：要求内部元素类型必须与推导出来的一致，否则就会警告。
x=100
x='你好'

y =[10,20,30]
y.append(40)
