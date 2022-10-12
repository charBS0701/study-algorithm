x, y = map(int,input().split()) # 게임횟수, 이긴게임 입력

# x와 y가 주어졌을 때, 최소 몇 번 더 해야 z가 변하는지 구하는 프로그램


def binary_search(array, start, end):
    while(start <= end):
        mid = (start+end) // 2
        win_rate = (100*(y+mid)) // (x+mid) # 승률
        if win_rate > (100*y // x): # 승률이 올랐을 떄
            end = mid - 1
        elif win_rate == (100*y // x): #승률이 그대로일 때
            start = mid + 1
        if start <= end:
            return mid
# 10전 8승
# 11전 9승
result = binary_search( [i for i in range(x+1)] , 1, x ) # 1번부터 x번 
print(result) # (0~10, 1, 10)