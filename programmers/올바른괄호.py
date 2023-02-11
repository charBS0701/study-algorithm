# 올바른 괄호
# https://campus.programmers.co.kr/courses/16066/lessons/148375
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

import collections

# def solution(s):    # 효율성 테스트 시간초과
#     stack = collections.deque()
#     for i in s:
#         if i == ")":    # 닫는괄호일때
#             if stack.count("(") <= stack.count(")"):    # 스택에 닫는괄호가 여는괄호보다 많거나 같을때
#                 return False    
#             stack.append(i)
#         else:
#             stack.append(i)

#     if stack.count("(") != stack.count(")"):
#         return False
#     if stack.pop() == "(":  # 여는괄호로 끝나면 False
#         return False

#     return True

def solution2(s):
    stack = collections.deque()
    for i in s:
        if i == "(":
            stack.append(i)
        elif len(stack) and i == ")":   # 스택이 0이 아니고 )가 오는 경우
            stack.pop()
        else:   # )인데 스택이 0인 경우
            return False
    
    return False if len(stack) else True # ( 가 남아있는경우 False



print(solution2("()()"))
print(solution2("(())()"))
print(solution2(")()("))
print(solution2("(()("))