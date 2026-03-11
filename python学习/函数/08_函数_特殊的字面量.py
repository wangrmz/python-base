'''
特殊的字面量-None
NoneType类型：None
None是一个特殊的字面量，表示：空值/无值/无意义
意义更中立，更开放，None是不按时类型的
如果确定是字符串类型可以写''
None转为布尔值是False
None不能参与数据运算，也不能与字符串拼接
不给函数返回值，函数也会默认返回None
'''


msg = None
# None的类型是NoneType
print(type(msg))

bool(msg)
if msg:
    print('你好')

