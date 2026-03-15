

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
    #  实例方法（给实例添加行为）
    def speak(self):
        print(f'我叫{self.name},年龄是:{self._age},身份证是:{self.__idcard}')


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
# 子类不能访问父类的私有属性
# s1 = Student('张三',18,'1111112334455')
# s1.hello() #'Student' object has no attribute '_Student__idcard'





















