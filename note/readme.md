# 파이썬 표준 라이브러리
<a href="https://docs.python.org/ko/3/library/index.html"> Document </a>
<br>

<a href="#내장함수">1. 내장함수</a>
> 기본 내장 라이브러리

<a href="#itertools">2. itertools</a>
> 반복되는 형태의 데이터를 처리하는 기능을 제공, 순열과 조합 라이브러리 제공.

<a href="#heapq">3. heapq</a>
> 힙(Heap) 기능 제공, 우선순위 큐 기능을 구현하기 위해 사용됨.

<a href="#bisect">4. bisect</a>
> 이진 탐색(Binary Search) 기능을 제공하는 라이브러리

<a href="#collections">5. collections</a>
> 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

<a href="#math">6. math</a>
> 필수적인 수학적 기능을 제공. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, PI같은 상수 포함.
---
<br>

## <a name="내장함수">내장함수</a>
import 명령어 없이 바로 사용할 수 있는 내장 함수
- input()
- print()
- sum() : iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
- min(), max() : 파라미터가 2개 이상 들어왔을 때 가장 작은/큰 값을 반환한다.
- eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
    ```
    result = eval("(3+5)*7")
    ```
- sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.
  - key 속성으로 정렬 기준을 명시할 수 있으며 reverse 속성으로 뒤집을지 여부 설정.
  ```
  result = sorted([('홍길동',35), ('이순신',75), ('아무개',50)], key = lambda x: x[1], reverse=True)
  ```
  - 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있다.
---
<br>

## <a name="itertools">itertools</a>
반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
- permutations
> iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
> permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
>```
>from itertools import permutations
>data = ['A', 'B', 'C'] # 데이터 준비
>result = list(permutations(data, 3)) # 모든 순열 구하기
>print(result)
>```
- combinations 
> iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
> ```
> from itertools import combinations
> data = ['A', 'B', 'C'] # 데이터 준비
> result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
> print(result)
> ```
- product
> 중복순열
> ```
> from itertools import product
> data = ['A', 'B', 'C'] # 데이터 준비
> result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
> print(result)
> ```
- combinations_with_replacement
> 중복조합
> ```
> > from itertools import combinations_with_replacement
> data = ['A', 'B', 'C'] # 데이터 준비
> result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기
> print(result)
> ```
---
<br>

## <a name="heapq">heapq</a>
heap기능을 위해 heapq 라이브러리 제공
다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 **우선순위 큐** 기능을 구현하고자 사용됨.
파이썬의 힙은 최소 힙(min heap)으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은'원소이기 때문이다.
- heapq.heappush() : 힙에 원소 삽입
- heapq.heappop() : 힙에서 원소를 꺼냄
- 힙 정렬(heap sort)를 heapq로 구현

```
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result
  
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```

> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<br>
또한 파이썬에서는 최대 힙(max heap)을 제공하지 않는다. 따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.
힙에 원소를 삽입하기 전에 잠시 부호를 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.
이러한 방식으로 최대 힙을 구현하여 내림차순 힙 정렬을 구현하는 예시는 다음과 같다.

```
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in ragne(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```
---
<br>

## <a name="bisect">bisect</a>
파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공.
'정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. **bisect_left()와 bisect_right()의 시간복잡도는 O(logN)**에 동작한다.
- bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a,x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
```
from bisect import bisect_left, bisect_right

a = [1.2.4.4.8]
x = 4

print(bisect_left(a,x)) ## 삽입되는 인덱스 리턴
print(bisect_left(a,x))
```
또한 두 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용될 수 있다.
아래의 count_by_range(a, left_value, right_value) 함수를 확인해보자. 이는 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환한다.
다시 말해 원소의 값을 x라고 할 때, left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산할 수 있다.
```
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index
  
# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))
```
---
<br>

## <a name="collections">collections</a>
파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리다.
코딩테스트에서 유용하게 사용되는 클래스는 **deque**와 **Counter**이다.
- deque
> 보통 파이썬에서는 deque를 사용해 큐를 구현한다. 별도로 제공되는 Queue 라이브러리가 있는데 일반적인 큐 자료구조를 구현하는 라이브러리가 아니다.
> 리스트에서는 앞쪽에 있는 원소를 삭제하거나 앞쪽에 새 원소를 삽입할 때의 시간 복잡도는 O(N)이다.
> 반면에 deque는 O(1)이다.
> deque에서는 리스트 자료형과는 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다.
> 스택이나 큐의 기능을 모두 포함한다고도 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대응으로 사용될 수 있다.
> - popleft() : 첫 번쨰 원소를 제거
> - pop() : 마지막 원소를 제거
> - appendleft(x) : 첫 번째 인덱스에 원소 x를 삽입
> - append(x) : 마지막 인덱스에 원소를 삽입

```
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 반환
```
> deque([1,2,3,4,5])
> [1,2,3,4,5]
<br>

- Counter
> iterable 객체가 주어 졌을 때, 해당 객제 내부의 원소의 등장 횟수를 세는 기능 제공.

```
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 반환
```
> 3
> 1
> {'red': 2, 'blue':3, 'green':1}

---
<br>

## <a name='math'>math</a>
자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리

```
import math

print(math.factorial(5)) # 5 팩토리얼을 출력
print(math.sqrt(7)) # 7의 제곱근을 출력
print(math.gcd(21,14)) # 21과 14의 최대 공약수 출력
print(math.pi) # 파이(pi)를 출력
print(math.e) # 자연상수 e 출력
```


