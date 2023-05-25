# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    result = []
    score = {}
    for i, person in enumerate(name):
        score[person] = yearning[i]
    print(score)
    
    for x in photo:
        photoSum = 0
        for y in x:
            if y in name:
                photoSum += score[y]
        result.append(photoSum)
    
    return result