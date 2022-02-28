"""
 @dauthor : cpucode
 @date : 2022/2/28 10:53
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

sites = {'cpu', 'code', 'cpuCode', 'baobei'}


# 输出集合，重复的元素被自动去掉
print("sites = ", sites)

# 成员测试
if 'cpuCode' in sites:
    print('cpuCode 在集合中')
else:
    print('cpuCode 不在集合中')

# set可以进行集合运算
a = set('abc')
b = set('abb')
print("a = ", a)
print("b = ", b)

# a 和 b 的差集
print("a - b = ", a - b)

# a 和 b 的并集
print("a | b = ", a | b)

# a 和 b 的交集
print("a & b = ", a & b)

# a 和 b 中不同时存在的元素
print("a ^ b = ", a ^ b)
