# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

n = int(input())
hour = 0
min = 0
sec = 0

count = 0

while True:
    if hour > n:
        break
    if (str(hour).find('3') != -1) or (str(min).find('3') != -1) or (str(sec).find('3') != -1):
        count += 1
        
    sec += 1

    if sec == 60:
        min += 1
        sec = 0
    if min == 60:
        hour += 1
        min = 0

print(count)