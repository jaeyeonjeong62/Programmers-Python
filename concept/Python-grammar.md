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
|remove()|변수명.remove(특정 값)|특정한 값을 갖는 원소를 제거하는데, 값은 가진 원소가 여러 개면 하나만 제거한다.|O(N)|

```
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않은 값만을 저장
result [i for i in a if not in remove_set]
print(result)
```
