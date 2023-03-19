# [Hashing] 실습 문제 풀기
# https://campus.programmers.co.kr/tryouts/72365/challenges
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]

import collections 
def solution(id_list, report, k):
    answer = [] # 유저별로 처리 결과 메일을 받은 횟수
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)
    
    for x in report:
        data = x.split()
        if data[1] in reportHash[data[0]] : continue # 중복처리
        reportHash[data[0]].add(data[1])
        stoped[data[1]] += 1
        
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user] >= k:
                mail += 1
        answer.append(mail)
        
    return answer
        
 
def solution2(id_list, report, k):
    answer = [] # 유저별로 처리 결과 메일을 받은 횟수
    report = list(set(report)) # 중복신고제거, 다시 리스트로
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)
    
    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stoped[b] += 1
        
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user] >= k:
                mail += 1
        answer.append(mail)
    
    return answer
        
            
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print(solution2(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
