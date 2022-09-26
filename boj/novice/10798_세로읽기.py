array = [[-1] * 15 for _ in range(5)]

for i in range(5):
    word = input()
    for j in range(len(word)):
        array[i][j] = word[j]
    
for i in range(15):
    for j in range(5):
        if array[j][i] != -1:
            print(array[j][i], end='')