# 表达式：执行后能得到值的代码，就是表达式（表达式最终会形成一个值，可以写在任何需要值的地方）
a1 = 3 + 5
a2 = 'abc' * 3
a3 = 5 > 3
a4 = 'y' in 'python'
a5 = len('helllo')

# 条件表达式：根据条件的真假，在两个值中二选一的表达式（又称：三元表达式、三目运算符）。

age = 18
# text =''
# if age >= 18:
#     text ='成年'
# else:
#     text = '未成年'
# print(text)

# 条件表达式：值1 if 条件 else 值2
text = '成年' if age >= 18 else '未成年'
# java 的三目运算
# String res = age>=18 ?"成年":"未成年";
# 条件表达式的使用场景：简单的二选一场景

is_vip = True
discount = 0.8 if is_vip else 1.0
