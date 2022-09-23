n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1], input_data[2], input_data[3]))

array = sorted(array, key=lambda array: (-int(array[1]), int(array[2]), -int(array[3]), array[0]))


for x in array:
    print(x[0])
