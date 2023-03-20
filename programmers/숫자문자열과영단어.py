# 숫자 문자열과 영단어
# https://campus.programmers.co.kr/tryouts/72376/challenges?language=python3
# "one4seveneight"	1478
# "23four5six7"	234567
# "123"	123

import collections

def solution(s):
    answer = ""
    engTonum = collections.defaultdict(int)
    engTonum = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "zero" : "0"}
        
    word = ""
    
    for x in s:
        if word in engTonum.keys():
            answer += str(engTonum[word])
            word = ""
        if x in engTonum.values():
            answer += x
        else:
            word += x
    
    if word in engTonum.keys():
        answer += str(engTonum[word]) 
        
    answer = int(answer)
    
    return answer
    
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("123"))
