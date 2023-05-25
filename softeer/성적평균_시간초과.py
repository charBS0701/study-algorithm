# https://softeer.ai/practice/info.do?idx=1&eid=389&sw_prbl_sbms_sn=204906
# 입력예제1
# 5 3
# 10 50 20 70 100
# 1 3
# 3 4
# 1 5
# 출력예제1
# 26.67
# 45.00
# 50.00

# N명의 학생들의 성적이 학번순서대로 주어짐
# 학번 구간 [A,B]가 주어졌을 때 이 학생들 성적의 평균을 구하는 프로그램

N, K = map(int, input().split()) # 학생수, 구간수

scores = list(map(int, input().split()))
scores.insert(0,-1)

for i in range(K):
    section = list(map(int,input().split()))
    scoresSum = sum(scores[section[0]:section[1]+1])
    print(f'{round(scoresSum/(section[1]-section[0]+1),2):.2f}')

