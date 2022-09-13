# n * m 미로
# 동빈위치 (1,1) 미로의 출구는 (n,m)에 위치
# 한번엔 한 칸씩 이동가능
# 괴물이 있는부분은 0, 없는 부분은 1
# 동빈이가 탈출하기위해 음직여야하는 최소 칸의 개수.

# 미로입력
n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int,input())))

# dfs 이용 ...
def dfs(maze, v, visit):
    return 0