# 纸张的厚度
# n = 0.1
# w = n
# for i in range(50):
#     w *= 2
#     print(w)
# print(w)

# 国王数麦粒
# 1:1 ,2:2,3:4,4:8
g = 1  # 当前格子里应该放的麦粒数
total = 0  # 麦粒总数
a = 0  # 棋盘格子数
while a < 100:
    total += g  # 麦粒总数
    print('在放满了%d个格子，总的麦粒数%d' % (a, total))
    g *= 2  # 当前格子应该放的麦粒数
    a += 1  # 走到下一个格子
print(total)

# 人生的复利。（1+0.01）

