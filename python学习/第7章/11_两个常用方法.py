from datetime import datetime

# 定义一个Person类（
class Person:
    # 类属性
    max_age = 120
    planet = '地球'
    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.age = age
        self.gender = gender
# 定义一个Student类（派生类，子类），继承Person类（基类，父类，超类）
class Student(Person):
    def __init__(self,name,age,gender,dtu_id,grade):
        super().__init__(name,age,gender)
        self.dtu_id = dtu_id
        self.grade = grade


p1=Person('李华', 22, '男')
s2=Student('李华', 22, '男','2025001','初二')


# 验证方法
# 方法1:isinstance(instance,Class),作用：判断某个对象是否为指定累的或者其子类的实例
print(isinstance(p1,Person)) #True
print(isinstance(p1,Student)) #False
print(isinstance(s2,Person)) #True
print(isinstance(s2,Student)) #True




# 方法2:issubclass(Class1,Class2),作用：判断某个类是否为另外一个类的子类
print(issubclass(Student,Person))  # True
print(issubclass(Person,Student))  # False


















