"""
 @dauthor : cpucode
 @date : 2022/2/28 14:18
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""


listdemo = ['cpu', 'code', 'cpuCode']

# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

# 以三个数字为键，三个数字的平方为值
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

print("type(dic) : ", type(dic))
