# 2등 보너스 번호 당첨을 따로 flag를 둬야함

lotto = input().split()    # 로또당첨번호 입력
for i in range(len(lotto)):    # 정수로 변경
    lotto[i] = int(lotto[i])

my_number = input().split()    # 내 번호 입력
for i in range(len(my_number)):    # 정수로 변경
    my_number[i] = int(my_number[i])

count = 0    
second = False    # 2등보너스 당첨유무

for i in range(len(lotto)-1):    # 맞춘개수 카운팅
    for j in range(len(my_number)):
        if lotto[i] == my_number[j]:
            count+=1

if count==6:
    print('1')
elif count==5:
    for i in range(len(my_number)):    # 2등 보너스 번호 당첨 유무
        if my_number[i] == lotto[len(lotto)-1]:
            second = True
            break
    if second == True:
        print('2')
    else: print('3')
elif count==4:
    print('4')
elif count == 3:
    print('5')
else:
    print('0')

    
    
