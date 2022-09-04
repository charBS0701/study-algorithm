t = int(input())
results = []
for i in range(t):
    v, e = map(int,input().split())
    result = 2 - v + e
    results.append(result)

for x in results:
    print(x)
