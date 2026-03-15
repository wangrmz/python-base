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

    #  实例方法（给实例添加行为）
    def speak(self, msg):
        print(f'我叫{self.name},年龄是:{self.age},性别是:{self.gender},我想说:{msg}')


# 定义一个Student类（派生类，子类），继承Person类（基类，父类，超类）
class Student(Person):
    def __init__(self,name,age,gender,dtu_id,grade):
        super().__init__(name,age,gender)
        self.dtu_id = dtu_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会覆盖夫类中的方法
    def speak(self,msg):
        super().speak(msg)
        print(f'我是学生{self.name},学号:{self.dtu_id},正在读:{self.grade},我想说:{msg}')


s2=Student('李华', 22, '男','2025001','初二')
s2.speak('你好')

