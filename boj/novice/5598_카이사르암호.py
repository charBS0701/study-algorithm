data = input()

for x in data:
    if x <= 'C':
        print(chr(ord(x)+23), end='')
    elif x > 'C' and x <= 'Z':
        print(chr(ord(x)-3), end='')