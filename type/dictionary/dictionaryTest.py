"""
 @dauthor : cpucode
 @date : 2022/2/28 11:09
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

dictnum = {}
dictnum['one'] = '1 - cpu'
dictnum[2] = '2 - code'

tinydict = {'name': 'cpuCode', 'code': 1, 'site': 'https://blog.csdn.net/qq_44226094'}


# 输出键为 'one' 的值
print("dict['one'] : ", dictnum['one'])

# 输出键为 2 的值
print("dict[2] : ", dictnum[2])

# 输出完整的字典
print("tinydict : ", tinydict)

# 输出所有键
print("tinydict.keys() : ", tinydict.keys())

# 输出所有值
print("tinydict.values() : ", tinydict.values())

print("/*****************************************************************/")

dictValue = dict([('cpuCode', 1), ('cpu', 2), ('code', 3)])

print("dictValue : ", dictValue)

dictValue1 = {x: x**2 for x in (2, 4, 6)}

print("dictValue1 : ", dictValue1)

dictValue2 = dict(cpuCode=1, cpu=2, code=3)

print("dictValue2 : ", dictValue2)
