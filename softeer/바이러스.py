# https://softeer.ai/practice/info.do?idx=1&eid=407
# 입력예제1
# 2 3 2
# 출력예제1
# 18

virus, rate, n = map(int, input().split())

for i in range(n):
    virus = virus * rate
    virus = virus % 1000000007


print(virus%1000000007)