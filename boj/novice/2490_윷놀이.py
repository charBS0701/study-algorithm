for i in range(3):
    count = 0
    data = map(int,input().split())
    for x in data:
        if x == 0:
            count += 1
    
    if count == 0:
        print('E')
    elif count == 1:
        print('A')
    elif count == 2:
        print('B')
    elif count == 3:
        print('C')
    else:
        print('D')


## answer
# cnt = list(map(int, line.split())).count(0)