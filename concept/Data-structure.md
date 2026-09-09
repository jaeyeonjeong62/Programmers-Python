## 스택(Stack)

## 큐(Queue)

## 우선순위 큐(Priority Queue)

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 데이터를 우선순위에 따라 처리하고 싶을 때 사용
    - 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

|자료구조|추출되는 데이터|
|---|---|
|스택(Stack)|가장 **나중에** 삽입된 데이터|
|큐(Queue)|가장 **먼저** 삽입된 데이터|
|우선순위 큐(Priority Queue)|**가장 우선순위가 높은** 데이터|

- 우선순위 큐를 구현하는 방법
    1. 단순히 리스트를 이용하여 구현
    2. 힙(heap)을 이용하여 구현
- 데이터의 개수가 N개 일 때, 구현 방식에 따른 시간 복잡도

|우선순위 큐 구현 방식|삽입 시간|삭제 시간|
|---|---|---|
|리스트|$\mathcal{O}(1)$|$\mathcal{O}(N)$|
|힙(Heap)|$\mathcal{O}(logN)$|$\mathcal{O}(logN)$|

- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일 **(힙 정렬)**
    - 이 경우 시간 복잡도는 $\mathcal{O}(NlogN)$

```python
import heapq

numbers = [4, 1, 3, 2]
heap = []

# 모든 데이터 넣기
for number in numbers:
    heapq.heappush(heap, number)

# 모두 꺼내서 정렬된 리스트 만들기
result = []

while heap:
    result.append(heapq.heappop(heap))

print(result)
# [1, 2, 3, 4]
```




## 힙(Heap)