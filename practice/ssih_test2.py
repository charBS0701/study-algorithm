# 연속된 글자수 카운트 정렬. 맨끝문자와 처음문자가 이어짐.
# 결과 오름차순 정렬

data1 = ['a','a','a','b','b','a','a','a']
data2 = ['w','o','w','w','o','w']

def count_seq(data):
    result = []
    count = 1
    circulating = False # 맨 앞문자와 맨 뒤문자가 같은 리스트인가?
    if data[0] == data[-1]: # 순환하는 데이터면 뒤에 연결
        circulating = True
        for i in range(len(data)):
            if data[-1] == data[i]: # 맨뒤 데이터와 앞의 데이터가 다를때까지 뒤에 추가
                data.append(data[i])
            else:
                break
    data.append(-1) # 현재원소와 다음원소를 비교하는데 out of index를 피하기 위함

    for i in range(len(data)-1): # -1이 맨뒤에 있으니까 그 전까지만 반복
        if data[i] == data[i+1]: # 현재원소와 다음원소가 같으면
            count += 1
        else: # 연속되는 문자가 끝나면 
            result.append(count)
            count = 1
        
    if circulating: # 순환하는 리스트면 결과리스트의 맨 앞 원소를 제거해야함
        result.pop(0)
    
    result.sort()
    return result

print(count_seq(data1))
print(count_seq(data2))


