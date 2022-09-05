# 0과 1로 이루어진 문자열 S
# 이 문자열 S의 모든 숫자를 전부 같게 만들려고 함
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는것
# 행동의 최소 횟수를 구하여라

data = input()

# 약분
new_data = data[0]

for i in range(1,len(data)):
    if new_data[-1] != data[i]:
        new_data += data[i]
    
count0 = 0
count1 = 0
for a in new_data:
    if a == '0':
        count0 += 1
    elif a == '1':
        count1 += 1

print(min(count0, count1))