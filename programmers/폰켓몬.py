# 폰켓몬
# https://campus.programmers.co.kr/tryouts/63115/challenges?language=python3
# [3,1,2,3]	2
# [3,3,3,2,2,4]	3
# [3,3,3,2,2,2]	2

def solution(nums):
    select = len(nums)//2
    kinds = len(set(nums))
    
    if kinds > select:
        return select
    else: 
        return kinds
    
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))