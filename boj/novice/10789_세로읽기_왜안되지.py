array = []
for i in range(5):
    array.append(list(input()))

for i in range(len(array[0])):
    for j in range(5):
        if len(array[j]) <= i:  
            continue
        print(array[j][i], end='')



