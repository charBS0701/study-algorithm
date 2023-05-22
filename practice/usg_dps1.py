# 연결 요소의 개수 구하기
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하세요
# (연결 요소는 에지로 연결된 노드의 집합을 의미)
# 입력: 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어집니다. (1 <= N <= 1,000, 0 <= M <= N*(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u, v가 주어집니다. (1 <= u, v <= N, u != v)
# 같은 간선은 한 번만 주어진다.
# 출력 : 첫째 줄에 연결 요소의 개수를 출력한다.

# 입력 예시
# 6 5 # 노드 개수, 에지 개수
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 출력 예시
# 2


v, e = map(int, input().split()) # 노드, 간선 수 입력
adjList = [[] for i in range(v+1)] # 인접리스트 초기화
visited = [0] * (v+1) # 노드 방문 여부
count = 0   # 연결요소 개수

for i in range(e): # 인접리스트 입력
    a, b = map(int, input().split()) 
    adjList[a].append(b)
    adjList[b].append(a)

def dfs(v): # 우선 dfs 를 실행하고 이 노드가 첫방문인지 검사
    if visited[v] == 0: # 방문하지 않은 노드라면
        visited[v] = 1  # 방문 처리
        for x in adjList[v]:
            dfs(x)

# for i in range(1,v+1): 
#     if visited[i] == 0:
#         count += 1 # 하나의 연결노드 탐색 시작
#         visited[i] = 1
#         for x in adjList[i]:
#             dfs(x)

################################################################
## 예시 답안
def dfs2(v):    # dfs2 가 실행됐다는 것은 이미 이 노드는 첫 방문인 것이다
    visited[v] = 1
    for i in adjList[v]:
        if not visited[i]:
            dfs2(i)

# for i in range(1, n+1):
#     if not visited[i]:
#         count +=1
#         dfs2(i)




################################################################
## 수정
def dfs3(v):
    visited[v] = 1
    for x in adjList[v]:
        if visited[x] == 0:
            dfs(x)

for i in range(1, v+1):
    if visited[i] == 0:
        count += 1
        dfs3(i)
            
print(count)

