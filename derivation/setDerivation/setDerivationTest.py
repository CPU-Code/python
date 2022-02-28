"""
 @dauthor : cpucode
 @date : 2022/2/28 14:18
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

setnew = {i**2 for i in (1, 2, 3)}

print(setnew)

a = {x for x in 'cpuCode' if x not in 'cpu'}

print(a)

print("type(a) : ", type(a))
