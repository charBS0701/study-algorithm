import collections
# 완주하지 못한 선수
# https://campus.programmers.co.kr/tryouts/63116/challenges
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"

# def solution(participant, completion):    # 효율성 테스트 실패
#     # participant.sort()
#     # completion.sort()

#     for com in completion:
#         participant.remove(com)

#     return participant[0]

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):   # zip : 내장함수, 같은 인덱스끼리 짝 지어줌
        if p != c:
            return p
    return participant[-1]


print(solution3(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution3(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))