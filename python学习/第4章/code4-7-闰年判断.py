# 普通闰年是4的倍数，且不是100的倍数
# 世纪闰年逼必须是400的倍数
year = int(input('请输入年份'))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('是闰年')
# else:
#     print('不是闰年')

# 简化
if (not year % 4 and year % 100) or year % 400:
    print('是闰年')
else:
    print('不是闰年')
