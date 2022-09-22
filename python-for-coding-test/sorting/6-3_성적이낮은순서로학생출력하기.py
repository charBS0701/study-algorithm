n = int(input()) # 학생의 수 입력

def setting(data):
    return data[1]

students = []
for i in range(n): # 학생 정보 입력
    students.append(tuple(input().split()))

print(students)
students.sort(key=setting)

for x in students:
    print(x[0], end=' ')