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

    #  实例方法（给实例添加行为）
    def run(self, distance):
        print(f'我叫{self.name},疯狂跑了:{distance}米')

    # 使用@classmethod 装饰过的方法就叫做类方法，保存在类身上
    # 类方法收到的参数是：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls,value):
        cls.planet=value
        # print('我是test1',cls,value)

    @classmethod
    def create(cls,info_str):
        print(info_str)
        # 从info_str 中取出来有效信息
        name,year,gender = info_str.split('-')
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year-int(year)
        # 创建并返回一个Person类的实例对象
        return cls(name,age,gender)



# 验证一下：类方法是保存在类身上的
# print(Person.__dict__)

# 类方法需要类调用
# Person.test1(11) #我是test1 <class '__main__.Person'> 11
# Person.change_planet('火星')
# print(Person.planet)
# print(Person.__dict__)


# 创建Person的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')

#
# print(p1.__dict__)
# print(p2.__dict__)
# 验证一下类方法已经修改了
# print(p1.planet)


p3=Person.create('李华-2003-女')
print(p3.__dict__) #{'name': '李华', 'age': 23, 'gender': '女'}

# 注意点：类方法，也能通过实例调用到，但是非常不推荐
p4=p3.create('李华-2003-女')
print(p4.__dict__)



