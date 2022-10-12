# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현

def fibo(x):
    if x == 2 or x == 1 :
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(40))

# O(2^n)의 시간복잡도