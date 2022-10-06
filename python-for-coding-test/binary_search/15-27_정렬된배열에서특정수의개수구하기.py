# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# x가 등장하는 횟수를 계산하세요.
# 시간복잡도 O(logN)으로 설계하지 않으면 '시간초과'판정을 받습니다.

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_element(array, element):
    left = bisect_left(array, element)
    right = bisect_right(array, element)
    
    if right-left == 0:
        return -1
    else: 
        return right-left

print(count_element(array, x))
