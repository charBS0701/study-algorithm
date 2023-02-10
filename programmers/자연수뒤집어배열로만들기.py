# 자연수 뒤집어 배열로 만들기
# https://campus.programmers.co.kr/courses/16066/lessons/148368?language=python3
# 12345	[5,4,3,2,1]
def solution(n):
    answer = []
    arr = str(n)
    for i in range(len(arr)):
        answer.append(n%10)
        n //= 10
    return answer

def solution2(n):
    n = str(n)
    answer = []

    for i in range(1, len(n)+1):
        a = int(n[-i])
        answer.append(a)

    return answer

print(solution2(12345))