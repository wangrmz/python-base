score = 65
# if score > 90:
#     print('A')
# elif score >80:
#     print('B')
# elif score > 70:
#     print('C')
# else:
#     print('D')

# 依次判断
if score > 90:
    print('A')
if score > 80 and score < 90:
    print('B')
if score > 70 and score < 80:
    print('C')
if score > 60 and score < 70:
    print('D')

# bmi计算
# bmi =w/(h*h)
w = float(input('请输入你的体重'))
h = float(input('请输入你的身高'))
