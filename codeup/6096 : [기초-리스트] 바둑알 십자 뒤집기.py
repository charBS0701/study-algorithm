# 막힌 부분은
# 1. 바둑판의 좌표를 어떻게 0부터가 아닌 1부터로 받을 것인가
# -> 문제의 바둑판은 좌표가 19x19 인데 20x20의 리스트를 미리 생성하여서
# 19x19의 초기 설정 좌표를 받을 때 range(1,19+1) 로 입력하였다

# 2. x좌표와 y좌표의 혼동
# 프로그래밍에서의 (2,3) 은 x=2, y=3 이 아니라 세로로 2칸, 가로로 3칸 인 것을 인지하지 못하였었다.
# 즉. arr[2][3] 이다.

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
    
