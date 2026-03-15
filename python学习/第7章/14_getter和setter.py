

# 定义一个Person类
class Person:
    # 类属性
    max_age = 120
    planet = '地球'
    # 初始化（给实例添加属性）
    def __init__(self, name, age, idcard):
        # 给实例添加属性
        self.name = name # 公有属性：当前类、子类中、类外部，都可以访问
        self._age = age # 收保护的属性： 当前类、子类中可以访问
        self.__idcard = idcard # 私有属性：仅能在当前类中被访问
    #  注册age属性getter方法，当访问Person实例的age属性时，下面的age方法就会被自动调用
    @property
    def age(self):
        return self._age

    #  注册age属性setter方法，当修改Person实例的age属性时，下面的age方法就会被自动调用
    @age.setter
    def age(self, value):
        if value <= self.max_age:
            self._age = value
        else:
            print('年龄非法，修改失败')

    #  注册idcard属性getter方法，当访问Person实例的idcard属性时，下面的age方法就会被自动调用
    @property
    def idcard(self):
        return self.__idcard[:6]+'********'+self.__idcard[-4:]

    #  注册idcard属性setter方法，当修改Person实例的idcard属性时，下面的age方法就会被自动调用
    @idcard.setter
    def idcard(self, value):
        print('身份证号不允许修改，如有特殊需求，请联系管理员')

class Student(Person):
    def hello(self):
        print(f'我是学生{self.name}-{self._age}-{self.__idcard}')

p1=Person('张三',18,'1111112334455')
# p1.speak()

print(p1.name)
# 在类的外部，如果强制访问【受保护的属性】 也能访问到，但十分不推荐
print(p1._age)
# 在类的外部，如果强制访问私有属性，不能访问到，而且会报错
# print(p1.__idcard)
# python内部通过重命名的方式将私有属性隐藏了
print(p1.__dict__) #{'name': '张三', '_age': 18, '_Person__idcard': '1111112334455'}

print(p1.age)
p1.age=20
print(p1.age)

# 子类不能访问父类的私有属性
# s1 = Student('张三',18,'1111112334455')
# s1.hello() #'Student' object has no attribute '_Student__idcard'





















