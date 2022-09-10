# 각 자리가 숫자(0-9)로만 이루어진 문자열 S가 주어졌을 때
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리 모든 연산은 왼쪽에서 순서대로 이루어진다 가정

data = input()
numbers = []

for i in range(len(data)): # 리스트에 숫자 하나씩 나누기
    numbers.append(data[i])
for i in range(len(numbers)): # 정수형으로 변환
    numbers[i] = int(numbers[i])

result = numbers[0]

for a in numbers[1:]:
    result = result + a if result + a >= result * a else result * a

print(result)