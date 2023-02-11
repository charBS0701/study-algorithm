# 위장
# https://campus.programmers.co.kr/tryouts/63117/challenges?language=python3
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5

from collections import Counter
from functools import reduce


def solution(clothes):      # hash 사용
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1 # type의 key인 밸류가 없으면 0으로 하겠다

    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer-1

def solution2(clothes):         # Counter 사용
    # 1. 의상 종류별 Counter를 만든다
    counter = Counter([type for clothe, type in clothes])

    # 2. 모든 종류의 count + 1 을 누적하여 곱해준다
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) -1
    # reduce(집계함수(인자2개,누적값,순회값), 순회가능데이터, [초기값]) : 누적집계를 위한 내장함수
    # acc : 누적자, cur : 루프값
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

## 풀이 참고
# https://coding-grandpa.tistory.com/88