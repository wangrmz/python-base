# 定义一个Person类（
class Person:
    # max_age、planet都是类属性，类属性是在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age = 120
    planet = '地球'

    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        # self.age = age
        self.gender = gender
        if age <= Person.max_age:
            self.max_age = age
        elif age > Person.max_age:
            self.max_age = Person.max_age


# 创建Person的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 实例属性只能通过实例访问
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# 验证一下：类属性是保存在类身上的
# {'__module__': '__main__', '__firstlineno__': 2, 'max_age': 18, 'planet': '地球', '__init__': <function Person.__init__ at 0x102ac76a0>, '__static_attributes__': ('age', 'gender', 'name'), '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# print(Person.__dict__)

# 验证一下：实例身上是没有类属性的
# {'name': '张三', 'age': 18, 'gender': '男'}
# {'name': '李四', 'age': 22, 'gender': '女'}
# print(p1.__dict__)
# print(p2.__dict__)

# 验证一下：类属性可以通过类访问，也可以通过实例访问
# print(Person.max_age)
# print(p1.max_age)  # 查找max_age的过程：1.实例自身(p1)->2.实例的缔造者
# print(p1.planet)

# 测试年龄超出范围
p3 = Person('张三', 170, '男')
print(p3.__dict__) #{'name': '张三', 'age': 170, 'gender': '男', 'max_age': 120}




