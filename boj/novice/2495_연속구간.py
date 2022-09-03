a = []
for i in range(3):
    data = input()
    results = []
    result = 1
    for j in range(1,len(data)):
        if data[j-1] == data[j]:
            result += 1
        else:
            results.append(result)
            result = 1
    a.append(max(results))

for x in a:
    print(x)

# 맞는데 왜안되냐 ㄹㅇ