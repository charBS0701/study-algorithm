# 길이가 n인 정수 배열 a와 b가 있다.
# 다음과 같이 함수 S를 정의하자
# S = A[0] x B[0] + ... + A[N-1] x B[N-1]

# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단 B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오

n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

s = 0
for i in range(n):
    a = min(a_list)
    b = max(b_list)
    s += a*b
    a_list.pop(a_list.index(a))
    b_list.pop(b_list.index(b))

print(s)
