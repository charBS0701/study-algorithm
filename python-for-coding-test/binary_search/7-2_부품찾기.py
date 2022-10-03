# 부품이 n개 있다
# 손님이 M개 종류를 대량 구매하겠다.
# 견적서 작성, 가게 안에 부품이 모두 있는지 확인

n = int(input()) # 부품 수 입력
stock = list(map(int,input().split())) # 재고 입력
m = int(input()) # 주문 수량 입력
order = list(map(int,input().split())) # 주문 입력

# 재고 정렬
stock.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for x in order:
    result = binary_search(stock, x, 0, n-1)
    print("yes" if result != None else "no", end=' ')
# 부품이 존재하면 yes 없으면 no