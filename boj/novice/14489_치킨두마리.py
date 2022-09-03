a, b = map(int,input().split())
price = int(input())

print(a+b if a+b<price*2 else a+b-price*2)