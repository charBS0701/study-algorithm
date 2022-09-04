s = input()

for x in range(ord('a'), ord('z')+1):
    if chr(x) in s:
        print(s.index(chr(x)), end= ' ')
    else:
        print(-1, end=' ')