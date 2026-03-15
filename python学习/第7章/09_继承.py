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
        # self.name = name
        # self.age = age
        # self.gender = gender
        # 方式1 推荐
        super().__init__(name,age,gender)
        # 方式2
        # Person.__init__(self,name,age,gender)
        self.dtu_id = dtu_id
        self.grade = grade

    def study(self,msg):
        print('子类的独有方法')



# 创建Student的实例对象
# 查找、speak方法的过程：1实例自身self->2.Student类->3.Person类
# s1=Student('张三', 18, '男')
s2=Student('李华', 22, '男','2025001',89)
print(s2.__dict__) # {'name': '李华', 'age': 22, 'gender': '男', 'dtu_id': '2025001', 'grade': 89}

# def speak(msg):
#     print('我是s1自身的speak方法',msg)
# s1.speak = speak
# s1.speak('你好')
#
# # {'name': '张三', 'age': 18, 'gender': '男'}
# # <class '__main__.Student'>
# print(s1.__dict__)
# print(type(s1))