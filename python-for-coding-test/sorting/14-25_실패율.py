# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담긴배열 return
def solution(N, stages):
    answer = []
    failRate = [ 0 for i in range(N+1)] # N+1개의 배열
    for x in stages:
        if x > n : continue
        failRate[x] += 1

    for i in range(1,N+1):
        failRate[i] = failRate[i] / (len(stages) - failRate[i-1])
        # 몽;린옴ㅇ닝ㅁㄴㅇ왼ㅇㅇ뫼ㅏㅓㅣ넝;리 모르겠음 
    
    for i in range(1,N+1):
        answer.append(failRate.index(max(failRate)))
        failRate[failRate.index(max(failRate))] = -1

    return answer


n = int(input()) # 스테이지의 개수 입력

# 사용자가 현재 멈춰있는 스테이지 번호
stages = map(int, input().split())

print(solution(n,stages))