from re import M


def lotate(key):
    global m
     
    # new key 생성
    new_key = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        arr = input().split()
        for j in range(len(arr)):
            key[i][j] = int(arr[j])

    for j in range(m,-1,-1):
        for i in range(m):
            new_key[i][j] = key[i][m-i]
    return new_key

def move(key):
    global m

    for i in range(m):
        for j in range(m):
            new_key[i][j] = key
# 키 생성
key = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    arr = input().split()
    for j in range(len(arr)):
        key[i][j] = int(arr[j])


for i in range(len(key)):
    for j in range(len(key[0])):
        print(key[i][j], end=' ')
    print()


print()
print()

key = lotate(key)

for i in range(len(key)):
    for j in range(len(key[0])):
        print(key[i][j], end=' ')
    print()


