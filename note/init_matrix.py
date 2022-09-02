# 2차원 배열 0으로 초기화
n, m = map(int, input().split()) # 행, 열의 수 입력

matrix = [[0] * m for _ in range(n)] # 결과 리스트

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()