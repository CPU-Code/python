"""
 @dauthor : cpucode
 @date : 2022/2/28 14:14
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

names = ['cpu', 'code', 'cpuCode']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(10) if i % 3 == 0]
print(multiples)
