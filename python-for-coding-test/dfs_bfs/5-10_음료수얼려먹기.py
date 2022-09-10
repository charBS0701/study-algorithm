# N x M 크기의 얼음 틀이 있다.
# 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려 있는 부분기리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라

n, m = map(int ,input().split())
frame = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 데이터 입력받기
for i in range(n): 
    ice = input()
    for j in range(m):
        frame[i+1][j+1] = ice[j]

# 그래프 생성
graph = []
for _ in range(n*m):
    graph.append([])


