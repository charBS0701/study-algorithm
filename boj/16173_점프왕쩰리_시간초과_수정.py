from collections import deque

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

# print(board)
# 하, 우
dx = [1,0]
dy = [0,1]

# 방문체크
visit = [[0] * n for _ in range(n)]

# bfs
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        # 현재 위치에서 두 방향으로 확인
        for i in range(2):
            nx = x + dx[i] * board[x][y]
            ny = y + dy[i] * board[x][y]
            # 맵을 벗어난 경우
            if nx >= n or ny >= n:
                continue
            # 목적지인 경우
            elif board[nx][ny] == -1:
                print("HaruHaru")
                return
            # 이미 방문한 곳일 경우
            elif visit[nx][ny] == 1:
                continue
            else:
                queue.append((nx,ny))
    
    print("Hing")

    
bfs(0,0)