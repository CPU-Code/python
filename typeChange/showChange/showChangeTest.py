"""
 @dauthor : cpucode
 @date : 2022/2/28 13:54
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""


# int() 强制转换为整型

# x 输出结果为 1
x = int(1)
# y 输出结果为 2
y = int(2.8)
# z 输出结果为 3
z = int("3")

print(x)
print(y)
print(z)
print("/**********************************************/")

# float() 强制转换为浮点型

# x 输出结果为 1.0
a = float(1)
# y 输出结果为 2.8
b = float(2.8)
# z 输出结果为 3.0
c = float("3")
# w 输出结果为 4.2
d = float("4.2")

print(a)
print(b)
print(c)
print(d)
print("/**********************************************/")

# str() 强制转换为字符串类型

# e 输出结果为 's1'
e = str("s1")
# g 输出结果为 '2'g
f = str(2)
# g 输出结果为 '3.0'
g = str(3.0)

print(e)
print(f)
print(g)
print("/**********************************************/")

# 整型和字符串类型进行运算，用强制类型转换

num_int = 123
num_str = "456"

print("num_int : ", num_int)
print("num_str : ", num_str)
print("type(num_int) : ", type(num_int))
print("type(num_str) : ", type(num_str))

# 强制转换为整型
num_str = int(num_str)
print("类型转换后，num_str : ", num_str)
print("类型转换后，type(num_str) : ", type(num_str))

num_sum = num_int + num_str

print("num_sum : ", num_sum)
print("type(num_sum) : ", type(num_sum))




