# 높이가 H보다 긴 떡은 H위의 부분이 잘리고 낮은 떡은 안잘린다
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

n, m = map(int,input().split()) # 떡의개수, 요청한 떡의 길이
ddeoks = list(int,input().split()) # 개별 떡의 높이

ddeoks.sort() # 떡 오름차순 정렬

to_customer = 0 # 손님에게 줄 떡
result = max(ddeoks)-1 # 절단기 길이를 제일 긴떡 -1 로 설정

# 절단기를 큰수로 시작해서 절단기보다 큰 떡들만으로 수행하여야 한다
# target = 절단기
# 절단기보다 


# def binary_search(array, target, start, end):
#     if target

# while True:



#     if to_customer >= m: #요청한 떡길이를 충족시키면 탈출
#         break
