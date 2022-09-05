# 프로그래밍에서는 xy좌표가 기존 수학의 xy좌표와 반대인 점이 아직 헷갈린다


h, w = map(int, input().split()) # 격자판의 세로 가로 입력
arr = [[0 for y in range(w+1)] for x in range(h+1)] # 격자판 세팅

n = int(input()) # 놓을 수 있는 막대의 개수

# 막대의 길이(l), 방향(d), 좌표(x,y) 입력
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        arr[x][y] = 1
        if d==0: # 가로방향일 때
            y+=1
        elif d==1: # 세로방향일 때
            x+=1

for i in range(h):
    for j in range(w):
        print(arr[i+1][j+1], end=' ')
    print()
            
            
            
