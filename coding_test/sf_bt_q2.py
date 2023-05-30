# 2번
# 자동차 계약을 하면 주문 큐에 넣고 순서대로 출고
# 이전까지 계약한 모델의 빈도수가 가장 높은 수부터 먼저 반환 하는 규칙이 있는 큐
# 이런 규칙대로 자동차 모델을 알파뱃 문자 하나로 관리하는 큐를 FQ라고 부른다
# 인큐(X) 
    # 알파뱃 하나 입력받아 FQ에 저장
# 디큐()
    # FQ에서 빈도수가 가장 높은 문자중 가장 먼저 인큐된 문자를 반환, 제거
    # 빈도수가 같다면 가장먼저 인큐된거
    # FQ비어있으면 * 반환

# 첫번째 줄 : 명령행 개수 N
## 1<=N<=100
# 두번째부터 N개 줄 : 인큐 또는 디큐
## 인큐(알바뱃)
## 디큐

# 디큐가 반환하는 문자를 공백으로 구분해 순서대로 출력
# 디큐: 같은 모델 모두 제거가 아니라 맨앞의 하나만 반환

N = int(input())
FQ = {}
result = []
for i in range(N):
    command = input().split()
    if command[0] == 'enqueue':
        if command[1] in FQ:
            FQ[command[1]] += 1 # 이미 있는 모델일 때
        else:
            FQ[command[1]] = 1 # 처음 받는 모델일 때
    if command[0] == 'dequeue':
        if not FQ: # 큐가 비어있으면
            result.append("*")
        else:
            model = list(FQ.keys())[0]
            result.append(model)
            if FQ[model] == 1:  # 해당 모델의 값이 1일경우 지움
                FQ.pop(model)
            else:
                FQ[model] -= 1
    FQ = dict(sorted(FQ.items(), key=lambda x: (-x[1],x[0]))) # 정렬

for model in result:
    print(model, end=" ")