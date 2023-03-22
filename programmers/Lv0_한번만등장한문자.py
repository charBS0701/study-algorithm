# 한 번만 등장한 문자
# https://campus.programmers.co.kr/tryouts/72375/challenges?language=python3
# "abcabcadc"	"d"
# "abdc"	"abcd"
# "hello"	"eho"

def solution(s):
    answer = []
    for x in s:
        if s.count(x) == 1:
            answer.append(x)
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer

def solution2(s):
    return ''.join(sorted(i for i in s if s.count(i) == 1))

print(solution("abcabcadc"))
print(solution("abdc"))
print(solution2("hello"))
