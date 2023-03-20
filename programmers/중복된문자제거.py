# 중복된 문자 제거
# https://campus.programmers.co.kr/tryouts/72374/challenges?language=python3
# "people"	"peol"

def solution(my_string):
    answer = ''
    for x in my_string:
        if x not in answer:
            answer += x
    return answer

def solution2(my_string):
    answer = ''
    result = set(my_string)
    for x in my_string:
        if x in result:
            answer += x
            result.remove(x)
    return answer

print(solution("people"))
print(solution2("people"))