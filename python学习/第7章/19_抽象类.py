# 抽象类：是一种不能直接实例化的类，通常被称为规范，让子类去继承，并实现其中定义的抽象方法

from abc import ABC, abstractmethod
# 一旦继承了ABC类，那么就是抽象类
class MustRun(ABC):
    @abstractmethod
    def run(self):
        # print('我在努力的奔跑')
        pass

class Person(MustRun):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def run(self):
        print(f'我叫{self.name},我在努力的奔跑')


p1 = Person('张三',18,'男')
p1.run()

