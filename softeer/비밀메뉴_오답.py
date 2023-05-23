# 비밀메뉴
# https://softeer.ai/practice/info.do?idx=1&eid=623

##### 실패 테스트 케이스 존재 #####

# k개 버튼, 1부터 k까지 번호
# 비밀메뉴 : m개의 버튼 조작
# 사용자의 n개의 버튼 조작이 있을 때 비밀메뉴 받을 수 있는지

m, n, k = map(int, input().split())
secret = list(map(int,input().split()))
command = list(map(int,input().split()))


def isSecret(command, secret):
    if n<m: # 입력키가 비밀키보다 짧으면
        print("normal")
        return
    count = 0
    for i in range(n):            
        for j in range(m):
            if j+count >= m:
                print("normal")
                return
            if command[i] == secret[j+count]:
                count += 1
                break
            else:
                count = 0
                break

        if count == m:  # 비밀키를 입력받으면
            print("secret")
            return
    
    print("normal")


isSecret(command,secret)