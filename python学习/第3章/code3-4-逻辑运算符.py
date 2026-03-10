# 与，而且：and
print(True and False)
print(True and True)
print(True and True and False)
print(1 == 1 and 2 > 1)

# 短路运算
print('hello' and 'hi')
print('' and 'hi')
print(0 and 1)
print(1 and 1)

# 或者：or
print('#' * 20)
print(True or False)
print(False or True)
print(False or False)

print(1 or 0)
print(2024 or 2025 or 0)
print(0 or '' or 888)

print('#' * 20)
# 非：not,一元运算符
print(not True)
print(not False)
print(not 1)
print(not '')
print(not '222')

# 比较运算符的优先级
# 一元运算符优先级最高not>and>or

print(True and False and not False)
print(True or False and True and not False)
print(True or False and (True and (not False)))
