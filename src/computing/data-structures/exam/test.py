a = {1: "Ketchup", 2: "Mustard", 3: "Relish"}
b = a
a[4] = "BBQ"
b[5] = "Ranch"
a[5] = "Ranch"
b[7] = "Mayo"
print(a)
print(b)
print(b[6])
