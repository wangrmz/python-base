# 鸭子多态：如果一个东西看起来像鸭子，叫起来也像鸭子，那么它就是鸭子
# 鸭子类型是一个编程风格，它不检查对象的类型，只关心对象能否做某件事（是否有对应的方法）
# 鸭子多态
# class Animal:
#     def speak(self):
#         print('动物正在发出声音！')

class Dog:
    def speak(self):
        print('汪汪汪！')

class Cat:
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')
class Fish:
    def speak(self):
        print('咕噜噜！')

def make_sound(animal): # 没有类型限制
    # 多态的体现
    animal.speak()

# 创建实例对象
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

# 汪汪汪！
# 喵喵喵！
# 哼哼哼！
# 咕噜噜！
make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)