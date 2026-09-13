# 1. 자료형
## 리스트 자료형
### 리스트 만들기

```
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)
```

### 리스트 컴프리헨션
```
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20 if i%2 == 1)]
print(array)
```
```
# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
```

### 리스트 관련 기타 메서드
|메서드명|사용법|설명|시간<br>복잡도|
|---|---|---|---|
|append()|변수명.append()|리스트에 원소를 하나 삽입할 때 사용한다.|O(1)|
sort()|변수명.sort()|기본 정렬 기능으로 오름차순으로 정렬한다.|O(NlogN)
||변수명.sort(reverse = True)|내림차순으로 정렬한다.||
|reverse()|변수명.reverse()|리스트의 원소의 순서를 모두 뒤집어 놓는다.|O(N)|
|insert()|insert(삽입할 위치 인덱스, 삽입할 값)|특정한 인덱스 위치에 원소를 삽입할 때 사용한다.|O(N)|
|count()|변수명.count(특정 값)|리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.|O(N)|
|remove()|변수명.remove(특정 값)|특정한 값을 갖는 원소를 제거하는데,<br>값을 가진 원소가 여러 개면 하나만 제거한다.|O(N)|

```
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않은 값만을 저장
result [i for i in a if not in remove_set]
print(result)
```

*파이썬에서 리스트, 문자열, 튜플 등 순차적인 정보를 담는 자료형을 iterable 자료형이라고 한다. in 문법은 이러한 iterable 자료형에 모두 사용이 가능하다.*

## 집합 자료형
### 집합 자료형의 연산
```
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b)
print(a & b)
print(a - b)
```

### 집합 자료형 관련 함수
```
# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러 개 추가
data.update([5,6])

# 특정한 값을 갖는 원소 삭제
data.remove(3)
```

---
# 2. 조건문

```
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다')

print('프로그램을 종료합니다.')
```
```
score = 85

if score >= 80: result = 'Success'
else: result = 'Fail'
```
```
score = 85
result = "Success" if score >= 80 else "Fail"
```

---

# 3. 반복문

---

# 4. 함수

```
def add(a,b):
    print(a+b)

add(b = 3, a = 7)
```
```
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)
```

```
def add(a,b):
    return a+b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3,7))
```

---

# 5. 입출력

**입력을 위한 전형적인 소스코드**
```
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)
```
**공백을 기준으로 구분하여 적은 수의 데이터 입력**
```
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int,input().split())
```

```
import sys
sys.stdin.readline().rstrip()
```

```
answer = 7
print(f"정답은 {answer}입니다.")
```

---

# 6. 주요 라이브러리의 문법과 유의점

## 내장 함수
print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리

- ```sum()```
- ```min()```
- ```max()```
- ```eval()```
```
result = eval("(3 + 5) * 7")
# 56
```
- ```sorted()```
```
result = sorted([9,1,8,5,4])
result = sorted([9,1,8,5,4], reverse = True)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
data = [9,1,8,5,4]
data.sort()
```

## itertools
파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공

```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data,3)) #모든 순열 구하기
```

```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data,2)) #2개를 뽑는 모든 조합 구하기
```
```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)
```

```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기(중복 허용)
```


## heapq
힙(Heap) 기능을 제공하는 라이브러리.
우선순위 큐 기능을 구현하기 위해 사용

```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대롤 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

    result = heapsort([1,3,5,7,9,2,4,6,8,0])
```

```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대롤 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

    result = heapsort([1,3,5,7,9,2,4,6,8,0])
```


## bisect
이진 탐색(Binary Search) 기능을 제공하는 라이브러리

- `bisect_left(a,x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- `bisect_right(a,x)`: 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

```python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))
```

```python
from bisect_import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
```


## collections
덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

### `deque`

```python
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) #리스트 자료형으로 변환
```

### `Counter`

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter('blue')) #'blue'가 등장한 횟수 출력
print(dict(counter)) #사전 자료형으로 변환
```


## math
필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함

```python
import math

print(math.factorial(5)) #5 팩토리얼을 출력
```

```python
import math

print(math.sqrt(7)) #7의 제곱근을 출력
```

```python
import math

print(math.gcd(21,14))
```

```python
import math

print(math.pi) #파이(pi) 출력
print(math.e) #자연상수 e 출력
```

