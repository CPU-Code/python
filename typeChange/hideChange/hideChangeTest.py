"""
 @dauthor : cpucode
 @date : 2022/2/28 13:50
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

num_int = 123
num_flo = 1.23

# 不同数据类型的变量 num_int 和 num_flo 相加，并存储在变量 num_new 中
num_enw = num_int + num_flo

# 查看三个变量的数据类型
print("type(num_int) : ", type(num_int))
print("type(num_flo) : ", type(num_flo))
print("type(num_new)  : ", type(num_enw))

# 将较小的数据类型转换为较大的数据类型，以避免数据丢失
print("num_new  : ", num_enw)

print("/**************************************/")

num_str = "456"
print("type(num_str) : ", type(num_str))

# 整型和字符串类型运算结果会报错，输出 TypeError
print("num_int + num_str : ", num_int + num_str)
