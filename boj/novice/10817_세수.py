a, b, c = map(int,input().split())
data = []
data.append(a)
data.append(b)
data.append(c)

data.sort()
print(data[1])

## answer
# print(sorted(map(int,input().split()))[1])