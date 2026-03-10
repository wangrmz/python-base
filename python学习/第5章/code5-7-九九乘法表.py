# 九九乘法表
'''
1x1=1
1X2=2 2X2=4
1X3=3 2X3=6 3X3=9
...
...
...

'''

for i in range(9):
    for j in range(i+1):
     # print('%dx%d=%d' % (i+1,j+1,(i+1)*(j+1)),end=' ')
     print('%dx%d=%d' % (j+1,i+1,(i+1)*(j+1)),end=' ')
    print()


