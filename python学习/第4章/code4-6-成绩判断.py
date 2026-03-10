# py_score = int(input('请输入你的python课程成绩'))
# c_score = int(input('请输入你的c课程成绩'))
#
# if py_score >= 60 or c_score >= 60:
#     print('合格')
# else:
#     print('重修')

# 上面可以优化需要判断输入是否为阿拉伯数字
py_score = input('请输入你的python课程成绩')
c_score = input('请输入你的c课程成绩')
if py_score.isdigit() and c_score.isdigit():
    if int(py_score) >= 60 or int(c_score) >= 60:
        print('合格')
    else:
        print('重修')
else:
    if not py_score.isdigit():
        print('py的成绩请输入阿拉伯数字')
    if not c_score.isdigit():
        print('c的成绩请输入阿拉伯数字')
