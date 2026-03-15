from datetime import datetime


# 定义一个Person类
class Person:

    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.age = age
        self.gender = gender

    # 静态方法
    # 使用@staticmethod修饰的方法就叫做静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self,cls参数，它收到的都是自定义参数
    # 静态方法通常用于定义：与类相关的工具方法

    @staticmethod
    def is_adult(year):
        # 获取当年的年份
        current_year = datetime.today().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True,False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        # print(idcard)
        # 遮盖身份证
        return idcard[:6]+'******'+idcard[-4:]

# 验证一下：静态方法是保存在类身上的
# print(Person.__dict__)

# 静态方法需要通过类去调用
result=Person.is_adult(2004)
print(result)

idcard = Person.mask_idcard('320323199611222643')
print(idcard)

# 类方法需要类调用
# Person.test1(11) #我是test1 <class '__main__.Person'> 11
# Person.change_planet('火星')
# print(Person.planet)
# print(Person.__dict__)


# 创建Person的实例对象
# p1 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')

