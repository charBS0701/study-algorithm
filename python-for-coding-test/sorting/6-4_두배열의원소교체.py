n, k = map(int, input().split()) # 배열의 크기와 교체횟수 입력

# 배열 입력
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

for i in range(k):
    if a[i] >= b[-i]:
        break
    a[i], b[-i] = b[-i], a[i]

print(sum(a))

