
# 1. 우선 순위 큐

선입선출인 일반적인 큐와는 다르게 큐에 넣는 순서와 상관없이 값이 작은 요소가 먼저 처리되거나, 요소에 우선 순위를 부여해서 우선 순위가 높은 요소를 먼저 처리 가능한 큐.




# 2. 클래스 임포트

queue 내장 모듈에서 제공되기 때문에 별다른 설치 없이 임포트 가능
```python
from queue import PriorityQueue  
```



# 3. 사용 방법

## 3.1 큐 생성

PriorityQueue( ) 를 사용하여 비어있는 우선 순위 큐를 초기화.

큐의 크기는 디폴트가 무한대이므로 크기를 제한하고 싶은 경우는 maxsize 지정
```python
que = PriorityQueue()
que = PriorityQueue(maxsize=8)
```



## 3.2 요소 추가

PriorityQueue 클래스의 put() 메소드를 사용하여 큐에 요소 추가.
```python
que.put(5)
que.put(1)
que.put(6)
que.put(2)
```



## 3.3 요소 삭제

PriorityQueue 클래스의 get() 메소드를 사용하여 큐에 있는 요소 삭제.

get()은 꺼낸 요소를 반환.

추가 순서에 상관없이 작은 값이 반환.

```python
print(que.get()) 
#1
print(que.get()) 
#2
```



## 3.4 우선 순위 부여

오름 차순이 아닌 다른 기준으로 원소를 정렬하고 싶다면 우선 순위를 튜플 자료형으로 부여.

```python
que.put((3, 'A'))
que.put((1, 'B'))
que.put((2, 'C'))

print(que.get()[1])  
# B
print(que.get()[1])  
# C
```
