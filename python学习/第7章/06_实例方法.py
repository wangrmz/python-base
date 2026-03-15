# 定义一个Person类（
class Person:
    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.age = age
        self.gender = gender

    #  实例方法（给实例添加行为）
    def speak(self, msg):
        print(f'我叫{self.name},年龄是:{self.age},性别是:{self.gender},我想说:{msg}')

    #  实例方法（给实例添加行为）
    def run(self, distance):
        print(f'我叫{self.name},疯狂跑了:{distance}米')

# 创建Person的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')


print(Person.__dict__)
print(p1.__dict__)

print(p2.__dict__)
p1.speak('hello')
p1.run(distance=10)



