while True:
    data = input()
    if data == '#':
        break
    count = 0
    for x in data:
        if x in ['a','e','i','o','u','A','E','I','O','U']:
            count += 1

    print(count)