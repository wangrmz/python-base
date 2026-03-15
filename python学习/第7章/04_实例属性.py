# 定义一个Person类（
class Person:
    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        # 实例属性只能通过实例访问，不能通过类访问
        # 每个实例都有自己【独一份】的实例属性，不公有
        self.name = name
        self.age = age
        self.gender = gender



# 创建Person的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 只能通过实例访问
print(p1.name)
print(p1.age)
print(p1.gender)


