# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 5 ≤ players의 길이 ≤ 50,000
# 2 ≤ callings의 길이 ≤ 1,000,000
# players	callings	result
# ["mumu", "soe", "poe", "kai", "mine"]	["kai", "kai", "mine", "mine"]	["mumu", "kai", "mine", "soe", "poe"]

# 1. 풀이
# 일부 테스트케이스 시간초과
def solutionFailed(players, callings):
    for x in callings:
        rank = players.index(x)
        players[rank], players[rank-1] = players[rank-1], players[rank]
    return players

# 2. 풀이
def solution(players, callings):
    playerDic = { player : rank for rank, player in enumerate(players) }

    for calling in callings:
        pre, index = playerDic[calling] - 1 , playerDic[calling]  # 앞사람 인덱스, 불린사람 인덱스
        players[pre], players[index] = players[index], players[pre]  # 배열 순서 바꾸기
        playerDic[players[pre]] -= 1   # 딕셔너리 값 변경  # 배열 바뀐것 주의
        playerDic[players[index]] += 1
    
    return players