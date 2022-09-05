# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없다.

n, m, k = map(int, input().split()) # 배열의크기, 더해지는 횟수, k
numbers = input().split()

for i in range(n): # 배열의 원소를 정수로 변환
    numbers[i] = int(numbers[i])

numbers.sort() # 입력받은 수들 정렬하기

sum = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # m이 0이면 반복문 탈출
            break   
        sum += numbers[-1] 
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이면 반복문 탈출
        break
    sum += numbers[-2] # 두 번쨰로 큰 수 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(sum) # 최종 답안 출력
