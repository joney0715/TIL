# 데이터 구조

## 데이터 구조 활용

- 데이터 구조를 활용하기 위해서 메서드를 활용
  - 메서드는 클래스 내부에 정의한 함수
  - 객체의 기능
  - 데이터구조.메서드() 의 형태로 활용



## 순서가 있는 데이터 구조

### 문자열

- 문자들의 나열
- 모든 문자는 str 타입
- 변경 불가능한 immutable
  - 변수안의 값을 바꾸게 되면 변수안의 주소를 바꿔서 값을 넣는 메커니즘, 주소의 값이 바뀌는게 아님



- s.find(x) : x의 첫 번째 위치를 반환. 없으면, -1을 반환 (오류가 나지 않음)
- s.index(x) : x의 첫 번째 위치를 반환, 없으면 오류 발생
- s.isalpha() : 알파벳 문자 여부 (단순 알파벳이 아닌 유니코드상 letter(한국어도 포함) )
- s.isupper() : 대문자
- s.islower() : 소문자



#### 문자열 검증 메서드

- isdecimal()
- isdigit()
- isnumeric()



#### 문자열 변경 메서드

- replace(old, new[, count]) : 문자열 교체, count를 지정하면 해당 개수만큼만 시행
- srip([chars]) : 공백이나 특정 문자 제거
- split(sep=None, maxsplit=-1) : 공백이나 특정 문자를 기준으로 분리
- join([iterable]) : 구분자로 iterable을 합침
- upper() : 모두 대문자로 변경
- lower() : 모두 소문자로 변경
- swapcase() : 대소문자 서로 바꿈



### 리스트

#### 리스트 메서드

- append(x) : 리스트 마지막에 항목 x 추가 
- insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입
- remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) 를 제거
- pop() : 리스트 가장 오른쪽에 있는 항목을 반환 후 제거
- pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
- clear() : 모든 항목 삭제
- extend(m) : 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능) (리스트끼리의 합)
- index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
- reverse() : 리스트 거꾸로 정렬
- sort() : 리스트 정렬 (매개변수 이용가능)
- count(x) : 리스트에서 항목 x의 갯수를 반환



### 셋

#### 셋 메서드

- copy() : 셋의 얕은 복사본을 반환
- add(x) : 항목 x가 셋에 없다면 추가
- pop() : 셋에서 랜덤하게 항목을 반환, 해당 항목 제거, set이 비어있으면 에러(keyError)
- remove(x) : 항목 x를 셋에서 삭제, 존재하지 않으면 에러(keyError)
- discard(x) : 항목 x가 셋에 있는 경우, 항목 x를 셋에서 삭제
- update(t) : 셋t에 있는 모든 항목 중 셋에 없는 항목을 추가
- clear() : 모든 항목 제거
- s.isdisjoint(t) : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환 (서로소)
- s.issubset(t) : 셋 s가 셋 t의 하위 셋인 경우, True 반환
- s.issuperset(t) : 셋 s가 셋 t의 상위 셋인 경우, True반환



### 딕셔너리

#### 딕셔너리 메서드

- clear() : 모든 항목 제거

- copy() : 딕셔너리의 얕은 복사본 반환

- keys() : 딕셔너리의 모든 키를 담은 뷰를 반환

- values() : 딕셔너리의 모든 값을 담은 뷰를 반환

- items() : 딕셔너리의 모든 키-값의 쌍을 담은 뷰를 반환

- get(k) : 키 k의 값을 반환, 없을 경우 None을 반환

- get(k, v) : 키 k의 값을 반환, 없을 경우 v를 반환

- pop(k) : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제, 없을 경우 에러 (keyError)

- pop(k, v) : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제, 없을 경우 v 반환

- update([other]) : 딕셔너리의 값을 매핑하여 업데이트

  ```python
  my_dict = {'apple':'사', 'banana':'바나나'}
  my_dict.update(apple='사과')
  print(my_dict) # {'apple':'사과', 'banana':'바나나'}
  ```

  

## 앝은 복사와 깊은 복사

### 복사 방법

- 할당 (Assignment)
- 앝은 복사 (Shallow copy)
- 깊은 복사 (Deep copy)



### 할당

- 대입 연산자 (=)

  - 리스트 복사 확인

  ```python
  original_list = [1, 2, 3]
  copy_list = original_list
  print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
  
  copy_list[0] = 'hello'
  print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]
  ```

  

### 얕은 복사

- 슬라이스 연산자를 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사

```python
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]
b[0] = 5
print(a, b) # [1, 2, 3] [5, 2 ,3]
```

- 얕은 복사의 주의사항

  - 복사하는 리스트의 원소가 주소를 참조하는 경우

  ```python
  a = [1, 2, ['a', 'b']]
  b = a[:]
  print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
  b[2][0] = 0
  print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
  ```

  

### 깊은 복사

- 리스트 복사 확인

  ```python
  import copy
  a = [1, 2, ['a', 'b']]
  b = copy.deepcopy(a)
  print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
  b[2][0] = 0
  print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
  ```

  