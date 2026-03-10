# 创建字符串
s='hello,world'

print(s[0])
print(s[4])
print(s[-1])
# 切片：[起始索引：结束索引+1:步长]从索引开始到索引+1，[start,end+1)
print(s[0:4])
print(s[0:9:1])
# step
# 起始索引默认0，结束索引默认-1，步长默认1
print(s[0:9])
s2='123456789'
print(s2[0:9:2])
print(s2[1:9:2])
# 字符串的反转
print(s2[-1:-10:-1])
print(s2[::-1])