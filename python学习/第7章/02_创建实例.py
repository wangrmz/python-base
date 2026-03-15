# 定义一个Person类（
class Person:
    # 初始化
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.age = age
        self.gender = gender


# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 如果直接打印一个实例的话，我们是看不到实例身上的属性的
# print(p1)
# print(p1)

# 通过点语法可以访问或者修改实例身上的属性
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print('-' * 20)
# print(p2.name)
# print(p2.age)
# print(p2.gender)

# 通过实例.__dict__可以查看实例身上的所有属性,很简洁打包成字典
# {'name': '张三', 'age': 18, 'gender': '男'}
# {'name': '李四', 'age': 22, 'gender': '女'}
# print(p1.__dict__)
# print(p2.__dict__)


# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p1.address ='苏州'
print(p1.__dict__) #{'name': '张三', 'age': 18, 'gender': '男', 'address': '苏州'}
# <class '__main__.Person'>
# <class '__main__.Person'>
print(type(p1))
print(type(p2))