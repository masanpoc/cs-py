a = 5
a **= 2
b = a % 5
a *= b
b += 5
a -= b
c = a == b
d = a**2 == b**2
e = c or d
print(a, b, c, d, e)
