def parse(str):
    correct = True
    left = 0
    right = 0   
    mystack = []
    
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            mystack.append('(')
        else:
            right += 1
            if len(mystack) == 0:
                correct = False
            else:
                mystack.pop()
                
        if left == right:
            return i + 1, correct 
        
    return 0, False


def solution(p):
    if len(p) == 0:
        return p
    
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]
    
    if correct:
        return u + solution(v)
    
    answer = '(' + solution(v) + ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
            
    return answer

# w를 두 "균형괄호" u, v로 분리
# u는 더이상 분리될 수 없어야한다.
# u가 올바른 괄호문자열이라면 v로부터 다시 두 "균형괄호" 2개로 분리한다.
    # 수행한 결과 문자열을 u에 이어 붙이고 반환
# u가 올바른 괄호문자열이 아니라면 다음
    # 빈 문자열에 첫번째 문자로 '('를 붙인다.
    # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
    # ')'를 다시 붙인다.
    # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    # 생성된 무나졍ㄹ 반환