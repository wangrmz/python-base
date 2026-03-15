# Python中，所有的类都继承了object类，即：object类是所有类的顶层父类
# 因为 object 是所有类的父类，所以Python所有对象，都间接是 object 类的实例
# 定义一个Person类
class Person:
    # 初始化（给实例添加属性）
    def __init__(self, name, age, idcard):
        # 给实例添加属性
        self.name = name  # 公有属性：当前类、子类中、类外部，都可以访问
        self._age = age  # 收保护的属性： 当前类、子类中可以访问
        self.__idcard = idcard  # 私有属性：仅能在当前类中被访问

# 验证一下：所有类继承了object类
# print(issubclass(Person, object))
# print(issubclass(int, object))
# print(issubclass(str, object))


p1 = Person('张三',18,'2122222')
print(isinstance(p1, Person))
print(isinstance(p1, object))


# 所有对象都继承了object类所提供的：各种属性和方法，从而保证了每个对象都具备统一的基本能力
for key  in object.__dict__.keys():
    print(key)

print(p1.__dict__) # 对象身上自己的东西
print(dir(p1)) # 对象可以访问到的东西（自己的，继承的）

print(p1.__str__())
print(p1)
