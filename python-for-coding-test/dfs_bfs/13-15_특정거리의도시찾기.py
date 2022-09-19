from collections import deque

n, m, k, x = map(int,input().split())

# 그래프 입력
graph = [[] for i in range(n+1)]
print(graph)
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

print(graph)
distances = [ 0 for _ in range(n+1) ]
distance = 0

def bfs(start):
    queue = deque(start)

    while queue:
        for time in len(queue):
            v = queue.appendleft() 
            distance += 1
            for i in graph[v]:
                queue.append(i)
                distances[i] = distance



    

