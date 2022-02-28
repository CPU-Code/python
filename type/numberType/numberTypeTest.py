"""
 @dauthor : cpucode
 @date : 2022/2/25 16:45
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""


class A:
    pass


class B(A):
    pass


a, b, c, d = 20, 5.5, True, 4+3j
d = 111

print(type(a), type(b))
print(type(c), type(d))


print(isinstance(d, int))


print("/****************************************/")


print("isinstance(A(), A) : ", isinstance(A(), A))

print("type(A()) == A : ", type(A()) == A)

print("isinstance(B(), A) : ", isinstance(B(), A))

print("type(B()) == A : ", type(B()) == A)




