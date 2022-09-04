n = int(input())
data = input()
list = []
for x in data:
    list.append(int(x))

print(sum(list))

## answer
# print(sum(list(map(int, list(input())))))