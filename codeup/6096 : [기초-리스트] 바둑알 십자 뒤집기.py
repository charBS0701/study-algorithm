size = 19 # 바둑판의 크기
arr = [[0 for i in range(size+1)] for j in range(size+1)] # 바둑판 생성

# 바둑판 배열 입력
for y in range(1,size+1):
    d = input().split()
    for x in range(1,size+1):
        d[x-1] = int(d[x-1]) # 정수로 바꾸기
        arr[y][x] = 0 if d[x-1]==0 else 1 # 입력받은 값으로 바둑판 세팅
    

# 뒤집기 횟수 입력
n = int(input())

# 뒤집기 좌표 입력
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1,size+1):
        arr[x][j] = 1 if arr[x][j] == 0 else 0
        arr[j][y] = 1 if arr[j][y] == 0 else 0

# 출력
for i in range(1, size+1):
    for j in range(1, size+1):
        print(arr[i][j], end=' ')
    print()
    
