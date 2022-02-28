"""
 @dauthor : cpucode
 @date : 2022/2/28 14:18
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

a = (x for x in range(1, 10))

# 返回的是生成器对象
print(a)

# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print("tuple(a) : ", tuple(a))


