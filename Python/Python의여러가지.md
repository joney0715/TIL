- 불린형들의 연산

```python
print(True + False) # 1
print(True * False) # 0
```



- enumerate

```py
for x, y in enumerate(range(4), 1):
    print(x, y)
    
'''
1 0
2 1
3 2
4 3
'''
# 인수 1을 넣어줬으므로 인덱스가 1부터 시작
```



- if문의 조건이 겹칠 때

```python
d = 90
if d > 30:
    print(1)
elif d > 80:
    print(2)
else:
    print(3)
    
# 1
# 제일 앞의 조건이 실행 됨
```



- 논리 연산자

```python
print(3.0 == 3)
# True
```



- 얕은 복사 깊은 복사

```python
import copy

copy.copy() # 얕은 복사
copy.deepcopy() # 깊은 복사
```

