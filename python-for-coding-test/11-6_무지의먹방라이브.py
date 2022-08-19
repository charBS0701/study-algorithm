# 회전판에 먹어야 할 N개의 음식이 있다.
# 각 음식에는 1부터 N까지 번호가 붙어있다
# 각 음식을 섭취하는데 일정 시간이 소요된다

# 무지는 다음과같은 방법으로 음식을 섭취합니다
# 1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
# 2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
# 3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
#  다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말합니다.
# 4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정합니다.

# 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었습니다.
# 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 합니다.
# 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times, 
# 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때,
# 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하시오


def solution(food_times, k):
    result = 0
    for i in range(k):
        if food_times[result%len(food_times)] != 0:
            food_times[result%len(food_times)] -= 1
            result += 1
            result %= result%len(food_times)
        else: # 해당 음식이 남아 있지 않으면
            result += 1
            result %= result%len(food_times)
            i -= 1
            continue

# 몰라잉

    # 몇 번 음식부터 먹어야하는지 리턴, 없으면 -1
    return (result+1)%len(food_times)


food_times = list(map(int,input().split()))
k = int(input())

print(solution(food_times,k))


