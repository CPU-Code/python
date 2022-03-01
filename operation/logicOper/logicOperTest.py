"""
 @dauthor : cpucode
 @date : 2022/3/1 8:59
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

a = 22
b = 11

if(a and b):
    print("a 和 b 都为 true")
else:
    print("a 和 b 有一个不为 true")

if(a or b):
    print("其中一个变量为 true")
else:
    print("a 和 b 都不为 true")

print("/***************************************************/")

# 修改变量 a 的值
a = 0

if(a and b):
    print("a 和 b 都为 true")
else:
    print("a 和 b 有一个不为 true")

if(a or b):
    print("其中一个变量为 true")
else:
    print("a 和 b 都不为 true")

if not(a and b):
    print("其中一个变量为 false")
else:
    print("a 和 b 都为 true")





