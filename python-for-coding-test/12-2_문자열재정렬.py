# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

str = input()

# 입력받은 문자를 오름차순으로 정렬
str = sorted(str)

sum = 0

# 문자를 하나씩 확인
for i in str:
    if ord(i) >= ord('0') and ord(i) <= ord('9'): # 문자가 숫자이면
        sum += int(i) # 합계에 더하기
    else: # 그렇지 않으면 출력
        print(i, end='')
    
print(sum) # 합계 출력
