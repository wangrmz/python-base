# 订单最大金额
timeout = 1000000


# 创建订单
def wechat_pay():
    print("我是微信支付")


def ali_pay():
    print("我是阿里支付")


def show_info():
    print("我是来自支付模块的show info")


# 测试代码，
if __name__ == '__main__':  # 当前运行作为主程序
    wechat_pay()
    ali_pay()



