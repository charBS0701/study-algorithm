# 기능개발
# https://campus.programmers.co.kr/courses/16066/lessons/148376
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

from collections import deque


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while(progresses):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while(progresses and progresses[0] >= 100):
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        if count:
            answer.append(count)
            count = 0
    return answer

#deque을 사용한 버전입니다.
def solution2(progresses, speeds):
    ProgressesQue = deque(progresses)
    SpeedsQue = deque(speeds)
    count = 0
    answer = []
    while ProgressesQue:
        if ProgressesQue[0] + SpeedsQue[0] >= 100:
            ProgressesQue.popleft()
            SpeedsQue.popleft()
            count += 1
        else:
            if count:
                answer.append(count)
                count = 0
            for i in range(len(ProgressesQue)):
                ProgressesQue[i] += SpeedsQue[i]
    answer.append(count)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

## 풀이 참고
# https://velog.io/@jin00/%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C-Python