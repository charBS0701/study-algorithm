# 2차원 리스트의 맵 정보 입력받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))