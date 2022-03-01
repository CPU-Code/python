"""
 @dauthor : cpucode
 @date : 2022/3/1 9:19
 @github : https://github.com/CPU-Code
 @csdn : https://blog.csdn.net/qq_44226094
"""

a = 22
b = 11
c = 10
d = 5
e = 0

e = (a + b) * c / d
print("(a + b) * c / d = ", e)

e = ((a + b) * c) / d
print("((a + b) * c) / d = ", e)

e = (a + b) * (c / d)
print("(a + b) * (c / d) = ", e)

e = a + (b * c) / d
print("a + (b * c) / d = ", e)

x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")







