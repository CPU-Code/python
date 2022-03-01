"""
 @dauthor : cpucode
 @date : 2022/3/1 9:12
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

a = 22
b = 22

if(a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if(id(a) == id(b)):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

print("/***************************************/")

# 修改变量 b 的值
b = 33

if(a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

if(a is not b):
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")





