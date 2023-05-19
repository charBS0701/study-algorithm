# https://softeer.ai/practice/info.do?idx=1&eid=413&sw_prbl_sbms_sn=202424
# 입력예제1
# 1
# 출력예제1
# 9

n = int(input())

dot = 2
for i in range(n):
    dot = dot + (dot-1)

print(pow(dot,2))