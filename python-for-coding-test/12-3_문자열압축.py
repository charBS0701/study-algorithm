def solution(s):
    for i in range(len(s)//2):
        for j in range(s):
            
            n_s = s[j:j+i]

data = input() # 문자열 입력

print(solution(data))

# 모르겠다 ~~