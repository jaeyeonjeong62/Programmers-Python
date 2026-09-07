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

