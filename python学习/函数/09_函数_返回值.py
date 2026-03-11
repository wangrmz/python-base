'''
函数的返回值
函数执行完毕后，会把执行结果交给调用者，这个执行结果就是返回值
'''

def add(n1,n2):
    print('n1:',n1)
    print('n2:',n2)
    return n1+n2

result = add(1,2)
print(result)

#print函数没有返回值None