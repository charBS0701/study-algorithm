# 두 개 뽑아서 더하기
# https://campus.programmers.co.kr/tryouts/72373/challenges?language=python3
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))