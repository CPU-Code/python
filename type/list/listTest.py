"""
 @dauthor : cpucode
 @date : 2022/2/28 10:02
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""


list = ['abc', 222, 3.3, 'cpuCode', 10.1]
tinylist = [111, 'cpu']

a = [1, 2, 3, 4, 5, 6]


# 输出完整列表
print("list : ", list)

# 输出列表第一个元素
print("list[0] : ", list[0])

# 从第二个开始输出到第三个元素
print("list[1:3] : ", list[1:3])

# 输出从第三个元素开始的所有元素
print("list[2:] : ", list[2:])

# 输出两次列表
print("tinylist * 2 : ", tinylist * 2)

# 连接列表
print("list + tinylist : ", list + tinylist)

print("/*************************************/")

print("a = ", a)

print("a[0] : ", a[0])
print("a[0] : ", a[2:5])

# 将对应的元素值设置为 []
a[2:5] = []
print("a = ", a)
