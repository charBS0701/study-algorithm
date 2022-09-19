import time
start = time.time()

# 기능을 구현 코드 (문제 해결 코드)
n = 10

result = 0
for i in range(1,n+1):
    result += i

print("result : ", result)

end = time.time()
print("exe time: ", end - start)