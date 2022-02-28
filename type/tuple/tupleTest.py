"""
 @dauthor : cpucode
 @date : 2022/2/28 10:27
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""


tuple = ('abcd', 8848, 2.21, 'cpuCode', 48.2)
tinytuple = (123, 'cpu')


# 输出完整元组
print(tuple)

# 输出元组的第一个元素
print(tuple[0])

# 输出从第二个元素开始到第三个元素
print(tuple[1:3])

# 输出从第三个元素开始的所有元素
print(tuple[2:])

# 输出两次元组
print(tinytuple * 2)

# 连接元组
print(tuple + tinytuple)

# 修改元组元素的操作是非法的
tuple[1] = 11
