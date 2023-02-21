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

def solution4(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
    
    return participant[len(participant)-1]

def solution5(participant, completion):     # hash 사용
    hashDict = {}
    sumHash = 0

    # 1. Hash : Participant의 dic 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다

    return hashDict[sumHash]

# import collections
def solution6(participant, completion):     # Counter 사용
    # 1. participant의 Counter를 구한다
    # 2. completion의 Counter를 구한다
    # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
    answer = collections.Counter(participant) - collections.Counter(completion)

    # 4. counter의 key값을 반환한다
    return list(answer.keys())[0]



print(solution5(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution4(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution6(["marina", "josipa", "nikola", "vinko", "filipa", "el"],["josipa", "filipa", "marina","vinko", "nikola"]))

## 풀이 참고
# https://coding-grandpa.tistory.com/85