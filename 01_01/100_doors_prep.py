doors = 101 * [False]   # 101 is used just so that we can access the Door1 with doors[1]
# print (doors)


for i in range(1,101):
    for j in range(i,101,i):
        doors[j] = not doors[j]

for i,j in enumerate(doors):
    if (j==True):
        print(str(i), end=", ")
