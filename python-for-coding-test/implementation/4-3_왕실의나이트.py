# 8 x 8 의 좌표평면의 왕실 정원 특정한 한 칸에 나이트가 서 있다.
# 이동 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오

data = input()
row = int(data[1])
column = ord(data[0])

moves = [(-2,-1),(-1,-2),(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2)]

count = 0
for i in moves:
    n_row = row + i[0]
    n_column = column + i[1]
    if n_row < 1 or n_row > 8 or chr(n_column) < 'a' or chr(n_column) > 'h':
        continue
    count += 1

print(count)