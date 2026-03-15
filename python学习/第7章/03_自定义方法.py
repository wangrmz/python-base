# 定义一个Person类（
class Person:
    # 初始化（给实例添加属性）
    def __init__(self, name, age, gender):
        # 给实例添加属性
        self.name = name
        self.age = age
        self.gender = gender

    # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其他参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self,msg):
        print(f'我叫{self.name},年龄是:{self.age},性别是:{self.gender},我想说:{msg}')


# 验证一下：speak是存在Person类身上的
# print(Person.__dict__)

# 创建Person的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# 验证一下：Person的实例对象身上是没有speak方法
# print(p1.__dict__)
# print(p2.__dict__)

# 所有Person类的实例对象，都可以调用到speak方法
# 当执行p1.speak()的时候，查询speak方法的过程：1.实例对象自身（p1）->2.实例的缔造者身上

# 验证一下上述的查找

def speak():
    print('hello')

p1.speak = speak
print(Person.speak) # <function Person.speak at 0x100bab740>
print(p1.__dict__) # {'name': '张三', 'age': 18, 'gender': '男', 'speak': <function speak at 0x100b3b2e0>}
print(p2.__dict__) # {'name': '李四', 'age': 22, 'gender': '女'}
p1.speak() #hello