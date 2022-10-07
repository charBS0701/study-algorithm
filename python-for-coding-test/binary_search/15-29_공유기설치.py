# from bisect import bisect_left, bisect_right

# n, c = map(int, input().split()) # 집의 수 n, 공유기의 수 c 입력
# homes = []

# # 집의 좌표입력
# for i in range(n):
#     homes.append(int(input()))

# homes.sort() # 정렬

# # 가장 인접한 두 공유기 사이의 최대 거리 출력

# # 시간제한 2초
# # 집의 수 200,000 O(nlogn)

# # 무조건 제일 작고 제일 큰 인덱스에는 설치해야함
# # 1 2 4 8 9
# # 1개를 9-1 =8, 8//2 = 4에 제일 가까운 곳에 설치해야함
# # 공유기가 4개면 ? 
# # 8//3 = 2 간격으로 설치해야함
# # (최대인덱스 - 최소인덱스) // c-1 한 곳에 제일 가까운 곳에 끼워 넣어야함
# # bisect 해서 끼워넣어야함

# # 간격 구하기 
# interval = (homes[-1] - homes[0]) // (c-1)

# # 공유기가 설치될 인덱스
# wifis = []
# wifis.append(bisect_left(homes,homes[0]+interval)) // 
# print(homes[wifis[0]])