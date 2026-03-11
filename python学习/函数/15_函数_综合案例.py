# 健身挑战赛

def calc_total(*nums):
    print(nums)
    """
    计算运动总量
    
    """
    print(sum(nums))
    return sum(nums)

def calc_avg(total,days=7):
    """
    计算平均运动量
    """
    return total/days

def check_success(total,goal=120):
    if total > goal:
        return '恭喜，挑战成功'
    else:
        return '挑战失败'

# result=(check_success(calc_avg(calc_total(20,50,20,50,90,80,100),7),80))
# print(result)

def main(title,duration):
    """

    """
    print(f'【{title}】【{duration}】 天挑战赛（请输入每天的数量）')
    num1 =int(input('第1天：'))
    num2 =int(input('第2天：'))
    num3 =int(input('第3天：'))
    num4 =int(input('第4天：'))
    num5 =int(input('第5天：'))
    num6 =int(input('第6天：'))
    num7 =int(input('第7天：'))
    # 计算总数
    total=calc_total(num1,num2,num3,num4,num5,num6,num7)
    # 计算平均值
    avg=calc_avg(total)
    # 判断是否成功
    result=check_success(total)
    # 打印相关信息
    print(f'【{title}】【{duration}】 天健身总结')
    print('总数：%d,平均值：%.1f' % (total,avg))
    print(f'总数{total},平均值{avg:.1f}')
    print(result)

main('仰卧起坐',7)