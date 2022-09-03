x = []
y = []
for i in range(3):
    data = list(map(int,input().split()))
    x.append(data[0])
    y.append(data[1])

if x[0] == x[1]:
    new_x = x[2]
elif x[1] == x[2]:
    new_x = x[0]
else:
    new_x = x[1]

if y[0] == y[1]:
    new_y = y[2]
elif y[1] == y[2]:
    new_y = y[0]
else:
    new_y = y[1]
    
print(new_x, new_y)

## answer
# x.sort()
# y.sort()
# print(x[0] if x[0] != x[1] else x[2], y[0] if y[0] != y[1] else y[2])