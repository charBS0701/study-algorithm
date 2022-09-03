a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0
t = 0

s = sum(a)
t = sum(b)

print(s if s>= t else t)