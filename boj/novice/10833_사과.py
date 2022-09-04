n = int(input())

leftover = 0

for school in range(n):
    students, apples = map(int,input().split())
    for i in range(1,101):
        if i * students > apples:
            leftover += apples - (i-1) * students
            break

print(leftover)


## answer
# sum += b % a