"""
 @dauthor : cpucode
 @date : 2022/2/25 14:35
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

# 使用反斜杠(\)+n转义特殊字符
print('hello\ncpuCode')

# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(r'hello\ncpuCode')