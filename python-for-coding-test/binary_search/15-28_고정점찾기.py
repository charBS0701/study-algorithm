# 고정점이란 수열의 원소중에서 그 값이 인덱스와 동일한 원소
# n 개의 다른 원소가 오름차순으로 정렬되어있다.
# 고정점이 있다면 고정점을 출력하는 프로그램. 최대 1개만 존재한다.
# 시간복잡도 O(logN)으로 설계하지 않으면 시간초과 판정을 받는다.

n = int(input())
array = list(map(int,input().split()))

def find_value_equal_index(array, start, end):
    if start > end:
        return -1
    mid = (start+end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return find_value_equal_index(array, mid+1, end)
    else:
        return find_value_equal_index(array, start, mid-1)

length = len(array)
result = find_value_equal_index(array, 0, length-1)

print(result)
