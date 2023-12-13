count = 0
for x in range(3):
    for x in range(3):
        count = count + x
        # print(x)

list1 = ["Alison", "Mina", "Leticia", "Elaine", "Sonny", "Benito"]
list2 = ["Yuri", "Andrew", "Mina", "Elaine", "Charles", "Alison"]
for name1 in list1:
    for name2 in list2:
        if name1 == name2:
            print(name1)
