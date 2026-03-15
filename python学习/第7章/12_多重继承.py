# 概念：多重继承是指一个类同时继承多个父类，从而拥有多个父类的属性和方法
# 举例子：就像孩子不仅继承爸爸的长相，也能继承妈妈的性格

# 定义一个Person类
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
    #  实例方法（给实例添加行为）
    def speak(self):
        print(f'我叫{self.name},年龄是:{self.age},性别是:{self.gender}')

class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

class Student(Person,Worker):
    def __init__(self, name, age, gender,company,stu_id,grade):
        # super只能拿到第一个类的初始化方法
        Person.__init__(self, name, age, gender)
        Worker.__init__(self,company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在努力学习，争取做{self.grade}年纪的第一名')


p1=Person('李华', 22, '男')
s2=Student('李华', 22, '男','微软中国','2025001','研一')
s2.study()
s2.do_work()

# 类的__mro__属性：用户记录属性和方法的查找顺序
# 通过实例去查找属性或者方法，会首先从实例本身去查找，没有则去__mro__
# 多重继承在实际开发中的使用并不是很多，了解即可
print(Student.__mro__) #(<class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Worker'>, <class 'object'>)
























