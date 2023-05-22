# https://softeer.ai/practice/info.do?idx=1&eid=394
# 입력예제2
# 5 3
# 7 5 7 7 1
# 1 2
# 2 3
# 3 4
# 출력예제2
# 2

n, relation = map(int, input().split())

canLift = list(map(int,input().split()))
canLift.insert(0,0) # 회원번호와 인덱스번호를 맞추기 위함함

imBest = [0] + [1] * (n) # 인덱스0은 0설정, 나머지는 자신이 최고라고 설정정

for i in range(relation):
    a, b = map(int, input().split())
    if not (canLift[a] > canLift[b]):   # a가 b보다 크지 않으면
        imBest[a] = 0
    if not (canLift[b] > canLift[a]):   #b가 a보다 크지 않으면
        imBest[b] = 0

print(imBest.count(1))