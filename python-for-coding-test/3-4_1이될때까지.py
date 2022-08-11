# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

# N과 K가 주어질 때 N이 1이 될 때가지 1번 혹은 2번의 과정의 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

n, k = map(int,input().split())
result = 0

while n>1:
    if n % k == 0:
        n /= k
        result +=1
    else:
        n -= 1
        result +=1

print(result)


# # 예시답안... 왜 저렇게 풀지 ? 시간복잡도 ?
# n, k = map(int,input().split())
# result = 0

# # N이 K 이상이라면 K로 계속 나누기
# while n >= k:
#     # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     # K로 나누기
#     n //= k
#     result += 1

# # 마지막으로 남은 수에 대하여 1씩 빼기
# while n > 1:
#     n -= 1
#     result += 1

# print(result)
