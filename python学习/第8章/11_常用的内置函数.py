# 一、输入与输出
# print() ===> 输出指定内容
# 完整参数：print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数详解：
#    1. objects: 要输出的内容
#    2. sep: 分隔符 关键字参数
#    3. end: 结束符 关键字参数
#    4. file: 输出位置 关键字参数
#    5. flush: 是否立即刷新
from time import sleep

# print(10,20,30,40,sep='-',end='!')
# # 写入文件
# 'w'：write写入的意思
# f = open('a.txt','w',encoding='utf-8')
# print(10,20,30,40,sep='-',end='!',file=f)

# print('加载中',end='')
# print('.',end='',flush=True) #表明不进行缓存，立即刷新
# sleep(1)
# print('.',end='',flush=True)
# sleep(1)
# print('.',end='',flush=True)
# sleep(1)
# print('.',end='',flush=True)
# sleep(1)
# print('.',end='',flush=True)
# sleep(1)
# print('.',end='',flush=True)
# print('完成！',end='')

# print('加载中', end='')
# # 第一种进度条
# for i in range(5):
#     print('.', end='', flush=True)  # 表明不进行缓存，立即刷新
#     sleep(1)
# print('完成！', end='')

# print('加载中', end='')
# # 第二种进度条
# for index in range(1,101):
#     print(f'\r已加载{index}%', end='', flush=True)
#     sleep(0.1)
# print('完成！', end='')

# input() ===> 获取用户输入 ，都是字符串

# 二、类型转换
# int() ====> 转为整数
# float() ====> 转为浮点数
# str() ====> 转为字符串
# bool() ====> 转为布尔值
# list() ====> 转为列表
# tuple() ====> 转为元组
# set() ====> 转为集合
# dict() ====> 转为字典

# 三、数学相关
# abs()========>取绝对值
# print(abs(-22))

# round()========>四舍五入
# 注意：round的四舍五入，是银行家舍入法：小于5就舍，大于5就入，等于5看奇偶（奇入偶舍）
print(round(3.4))
print(round(4.4))
print(round(4.6))
print(round(6.5))
print(round(7.543,2))


# pow()========>次方
print(pow(2,3))
print(pow(2,-1))
print(pow(2,0.2))
print(pow(2,3,5)) # 2 的三次方对5进行取模

# divmod()========>商和余数
print(divmod(10,3)) # (3, 1)

# max()========>最大值（支持key函数）
# min()========>最小值（支持key函数）
# sum()========>求和
# map()========>加工一组数据
# filter()========>过滤数据（支持key函数）
# reduce()========>合并计算
# sorted()========>排序（支持key函数）


# # 四、数据容器相关
# len() ===> 获取容器中元素的个数
# range() ===> 生成一个数字序列（可用于循环）
# for index in range(0, 10, 2):
#     print(index)

# sorted() ===> 对序列进行排序，返回新列表
# enumerate() ===> 给序列添加索引
# zip() ===> 将多个序列一一配对
# names=('张三','李四','王五')
# scores=[50,60,70]
# result=zip(names,scores)
# print(list(result)) #[('张三', 50), ('李四', 60), ('王五', 70)]

# # 五、类型判断与对象相关
# type() ===> 查看类型
# isinstance() ===> 判断类型
# issubclass() ===> 判断两个类的继承关系
# id() ===> 查看对象的内存地址

# # 六、逻辑判断相关
# all() ===> 全为真返回True
l1=[10,'北京',{1,2,3},0]
print(all(l1)) #False
# any() ===> 有一个为真即可
print(any(l1)) #True
# 七、字符串相关
# ord()===>获取字符的Unicode编码值

# chr()===>将Unicode编码值转为字符
