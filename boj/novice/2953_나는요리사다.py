data = []
for i in range(5):
    data.append(sum(map(int,input().split())))

print(data.index(max(data))+1, max(data))