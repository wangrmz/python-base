# 订单最大金额
max_order_amount=1000000

# 创建订单
def create_order():
    print("create order")

def cancel_order():
    print("cancel order")

def show_info():
    print("我是来自d订单模块的show info")


# 控制可引入的范围
__all__ = ('create_order', 'show_info')