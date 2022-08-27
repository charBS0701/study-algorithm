# N x M 직사각형의 장소. 각각의 칸은 바다 혹은 육지이다. 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A,B)로 나타낼 수 있고 바다로 되어 있는 공간에는 갈 수 없다.

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향을 회전한 다음 왼쪽으로 한 칸을 전진한다.
#  왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#  이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# 캐릭터가 방문한 칸의 수를 출력하는 프로그램

# 첫째 줄에 맵의 세로크기 N 과 가로크기 M을 공백으로 구분하여 입력한다.
# 둘쨰 줄에 게임 캐릭터가 있는 칸의 좌표를 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# 0북 1동 2남 3서
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. 맵의 외각은 항상 바다, 0육지 1바다

n, m = map(int, input().split())
a, b, d = map(int, input().split())

map = [[0 for i in range(m+1)] for j in range(n+1)]
map_visit_check = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(m):
    row = input().split()
    for j in range(len(row)):
        map[i+1][j+1] = int(row[j])
    

visit_count = 1 # 현재 있는곳은 방문 했으니
map_visit_check[a][b] = 1 # 현재 있는곳은 방문 했으니

while True:
    if (map[a-1][b-1] == 1 or map_visit_check[a-1][b-1] == 1) and (map[a+1][b-1] == 1 or map_visit_check[a+1][b-1] == 1) and (map[a-1][b+1] == 1 or map_visit_check[a-1][b+1] == 1) and (map[a+1][b+1] == 1 or map_visit_check[a+1][b+1] == 1):
        break

    if d == 0:  # 북쪽을 볼 때
        d = 3
        if map[a][b-1] != 1 and map_visit_check[a][b-1] != 1: # 왼쪽이 바다가 아니고 방문한곳이 아니면
            b -= 1 # 한칸 이동
            map_visit_check[a][b] = 1 # 방문체크
            visit_count += 1
    elif d == 3:  # 서쪽을 볼 때
        d = 2
        if map[a+1][b] != 1 and map_visit_check[a+1][b] != 1:
            a += 1
            map_visit_check[a][b] = 1
            visit_count += 1
    elif d == 2: #  남쪽을 볼 때
        d = 1
        if map[a][b+1] != 1 and map_visit_check[a][b+1] != 1:
            b += 1
            map_visit_check[a][b] = 1
            visit_count += 1
    elif d == 1: # 동쪽을 볼 때
        d = 0
        if map[a-1][b] != 1 and map_visit_check[a-1][b] != 1:
            a += 1
            map_visit_check[a][b] = 1
            visit_count += 1

    
print(visit_count)