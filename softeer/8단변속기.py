# https://softeer.ai/practice/info.do?idx=1&eid=408
# 1단에서 8단으로 연속적으로 변속 : ascending
# 8단 -> 1단 : descending
# else : mixed

# 변속 순서가 주어졌을 때 위 셋 중 판별

gear = list(map(int,input().split()))
ascending = list(range(1,9))
descending = list(range(8,0,-1))

if gear == ascending:
    print("ascending")
elif gear == descending:
    print("descending")
else:
    print("mixed")