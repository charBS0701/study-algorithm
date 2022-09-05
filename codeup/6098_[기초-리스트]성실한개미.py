# 먹이를 못찾고 오른쪽 구석까지 갔을때의 case를 처리 못해서 무한루프가 나왔었음
# 미로입력을 int로 바꿔주지 않아서 오류가 났었음

size = 10
maze = [[0 for i in range(size+1)] for j in range(size+1)]

# 미로입력
for i in range(size):
    arr = input().split()
    for j in range(len(arr)):
        maze[i+1][j+1] = int(arr[j])

ant = [2,2] # 개미 위치

while True:
    if maze[ant[0]][ant[1]] == 2: # 먹이 찾음
        maze[ant[0]][ant[1]] = 9 # 지나온 길 표시
        break
    maze[ant[0]][ant[1]] = 9 # 지나온 길 표시
    if maze[ant[0]][ant[1]+1] != 1: # 오른쪽이 비어있으면 이동
        ant[1] += 1
    elif maze[ant[0]+1][ant[1]] != 1: # 아래쪽이 비어있으며 이동
        ant[0] += 1
    else:
        break;

# 미로출력
for i in range(1,size+1):
    for j in range(1, size+1):
        print(maze[i][j], end=' ')
    print()
        
    
            
