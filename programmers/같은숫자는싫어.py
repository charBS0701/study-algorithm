# 같은 숫자는 싫어
# https://campus.programmers.co.kr/courses/16066/lessons/148374
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            answer.append(arr[i])

    return answer

def solution2(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))