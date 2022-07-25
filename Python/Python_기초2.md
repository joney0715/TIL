# Python 제어문

 

## 제어문

- 파이썬은 기본적으로 위에서 아래로 차례대로 명령을 수행
- 제어문은 순서도로 표현 가능



## 조건문

### 조건 표현식

- 조건 표현식을 일반적으로 조건에 따라 값을 정할때 활용
- 삼향 연산자로 부르기도함

```
true 인 경우 값 if 조건 else false인 경우 값
```

```python
value = num if num >= 0 else -num
```



## 반복문

### while문

- 조건식이 참인 경우 반복적으로 코드를 실행



### for문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체의 요소를 순회
- iterable
  - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
  - 순회형 함수(range, enumerate)



- 딕셔너리 순회

```python
grades = {'john':80, 'eric':90}
for student in grades:
    print(student, grades[student])
    
#john 80
#eric 90
```



- 딕셔너리의 메소드
  - key() : key로 구성된 결과
  - values() : value로 구성될 결과
  - items() : (key, value)의 튜플로 구성된 결과

```python
grades = {'john':80, 'eric':90}
for student, grade in grades.items():
    print(student, grades[student])
    
#john 80
#eric 90
```



- enumerate 순회

  - enumerate()
    - 인덱스와 객체를 쌍으로 담은 열거형 객체 반환

  ```python
  members = ['민수', '영희', '철수']
  
  for idx, number in enumerate(members):
      print(idx, number)
  
  #0 민수
  #1 영희
  #2 철수
  ```



- list comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

  ```python
  [code for 변수 in iterable]
  [code for 변수 in iterable if 조건식]
  ```



- dictionary comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

  ```python
  [key:value for 변수 in iterable]
  [key:value for 변수 in iterable if 조건식]
  ```

  

### 반복문 제어

- break
  - 반복문을 종료

- continue

  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

- for-else

  - 끝까지 반복문을 실행한 이후에 else 문 실행

    - break를 통해 중간에 종료된는 경우는 실행되지 않음

    ```python
    for char in 'apple':
        if char == 'b':
            print('b!')
            break
    else:
        print('b가 없습니다')
    
    # b가 없습니다
    ```

    

- pass

  - 아무것도 하지 않음



## 함수

### 함수의 종류

- 내장 함수
  - 파이썬에서 기본적으로 포함된 함수
- 외장함수
  - import 문을 통해 사용, 외부 라이브러리에서 제공
- 사용자 정의 함수
  - 직점 만들어서 사용하는 함수



### 함수의 기본 구조

- 선언과 호출
  - 함수의 선언은 def  키워드를 활용함
  - 파라미터를 넘겨줄 수 있음
  - 동작 후에는 return을 통해 결과값 전달
- 입력
- 문서화
- 범위
- 결과값



### 함수의 결과값

- 값에 따른 함수의 종류
  - Void function
    - 명시적인 return 값이 없는 경우, None을 반환하고 종료
  - value returning function
    - 함수 실행 후, return문을 통해 값 반환
    - return을 하게 되면, 값 반환 후 함수가 바로 종료
- print vs return
  - print를 사용하면 호출될 때마다 값이 출력됨
  - 데이터 처리를 위해서는 return 사용

- 두개 이상의 값 반환

```python
def test(x, y):
    return x - y, x * y

y = test(4, 5)
print(y) #(-1, 20)
print(type(y)) #<class 'tuple'>
```



### 함수의 입력

- Parameter : ㅎ마수를 정의할 때, 함수 내부에서 사용되는 변수
- Argument : 함수를 호출할 때, 넣어주는 값

```python
def function(ham): #Parameter : ham
    return ham

function('spam') #Argument : 'spam'
```



### Argument 

- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argument 는 소괄호 안에 할당
  - 필수와 선택 Argument 가 있음



### Keyword Argument

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Positional Argument를 활용할 수 없음

```python
add(x=2, y=5)
add(2, y=5)
add(x=2, 5) # -> Error 발생!
```



### Default Argument Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
  - 정의된 것 보다 더 적은 개수의 argumenr 들로 호출될 수 있음



### 가변 인자 (*args)

- 가변인자란?

  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용

- 가변인자는 언제 사용하는가?

  - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

  ```python
  def add(*args):
      for arg in args:
          print(arg)
          
  add(2)
  add(2, 3, 4, 5)
  ```



### 패킹 / 언패킹

- 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해햐야 함

- 패킹

  - 여러개의 데이터를 묶어서 변수에 할당하는것

  ```python
  number = (1, 2, 3, 4, 5) #패킹
  print(number) #((1, 2, 3, 4, 5))
  ```

  

- 언패킹

  - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는것

  ```python
  number = (1, 2, 3, 4, 5)
  a, b, c, d, e = number # 언패킹
  print(a, b, c, d, e) #1 2 3 4 5
  ```

  - 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
  - 언패킹시 왼쪽의 변수에 asterick(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

  ```python
  number = (1, 2, 3, 4, 5) #패킹
  
  a, b *rest = number
  print(a, b, rest) # 1 2 [3, 4, 5]
  
  a, *rest, e = number
  print(rest) # [2, 3, 4]
  ```



### Asterick(*) 와 가변 인자

- *는 시퀀스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자

  - 주로 튜플이나 리스트를 언패킹하는데 사용
  - *를 활용하여 가변 인자를 만들 수 있음

  ```python
  def func(*args):
      print(args)
      print(type(args))
      
  func(1, 2, 3, 'a', 'b')
  '''
  (1, 2, 3, 'a', 'b')
  <class 'tupple'
  '''
  ```

  

### 가변 키워드 인자 (**kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- **kwargs 는 딕셔너리로 묶여 처리되며, parameter에 \*\*를 붙여 표현

```python
def family(**kwargs):
	for key, value in kwargs.items():
        print(key, ':', value)
        
family(father = '아부지', mother = '어무니', baby = '아기')
'''
father : 아부지
mother : 어무니
baby : 아기
'''
```



### 가변인자와 가변키워드 인자 동시 사용 예시

```python
def print_family_name(*parents, **pets):
    print('아부지 :', parents[0])
    print('어무니 :', parents[1])
    if pets:
        print('반려동물들..')
        for title, name in pets,items():
            print('{} : {}'.format(title, name))
        
print_family_name('아부지', '어무니', dog='멍멍이', cat='냥냥이')
```





## Python의 Scope

### Scope

- 함수는 코드 내부에 local space를 생성하며, 그 외의 공간인 global scope로 구분
- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scop: 함수가 만든 scope, 함수 내부에서만 참조 가능
- vaiable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



### 변수 수명 주기

- 변수는 각자의 수명주기가 존재

  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

  ```python
  def func():
      a = 20
      print('local', a) #local a
      
  func()
  print('global', a) #NameError: name 'a' is not defined
  ```



### 이름 검색 규칙

- 파이썬에서 사용되는 이름(식별자) 들은 이름 공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB rule이라 부름
  - Local scope : 지역 범위(현재 작업 중인 범위)
  - Enclosed scope : 지역 범위 한 단계 위 범위
  - Global scope : 최상단에 위치한 범위
  - Built-in scope : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)
    - ex) print()
- 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

```python
a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c) # 10 1 300 
    local(300)
    print(a, b, c) #10 1 3
enclosed()
print(a, b) #0 1
```



### Global 문

- 현재 코드 블록 전체에 적용되며 , 나열된 식별자가 global variable임을 나타냄

  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
  - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

  ```python
  #함수 내부에서 글로벌 변수 변결하기
  a = 10
  def func1():
      global a
      a = 3
  
  print(a) # 10
  func1()
  print(a) # 3
  ```

  ```python
  #주의 사항 1
  a = 10
  def func1():
      print(a) # global a 선언 전에 사용
      global a
      a = 3
  
  print(a) 
  func1()
  print(a) 
  
  #SyntaxError: name 'a' is used prior to global declaration
  ```

  ```python
  #주의 사항 2
  a = 10
  def func1(a):
      global a # parameter에 global 사용 불가
      a = 3
  
  print(a) 
  func1(3)
  print(a) 
  
  #SyntaxError: name 'a' is parameter and global
  ```



### nonlocal

- global을 제외하고 가장 가까운 (둘러싸고 있는) scope의 변수를 연결하도록 함
  - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
  - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global과는 달리 이미 존재하느 이름과의 연결만 가능
- nonlocal은 이름공간상에 존재하는 변수만 가능

```python
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x) # 2
   
func1()
print(x) # 0
```



### 함수의 범위 주의

- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
- 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색
  - 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
  - 값을 할당하는 경우 해당 scope의 이름공간에 새롭게 생성되기 때문
  - 단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것
- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
  - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생
  - 가급적 사용하지 않는 것을 권장
  - 함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천



## 함수 응용

### map

- map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고 그 결과를 map object로 반환



### filter

- filter(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고 그 결과를 True인 것들을 Filter object로 반환

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result)) # <filter object at 0x000001FB4B217F40> <cladd 'filter'>
print(list(result)) # [1, 3]
```



### zip

- zip(*iterables)
- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane','ashley']
boys = ['justin','eric']
pair = zip(girls, boys)
print(list(pair)) # [('jane','ashley'), ('justin','eric')]
```



### lambda 함수

- lambda[parameter] : 표현식

- 표현식을 계산한 결과값을 반환하는 함수

- 이름이 없는 함수여서 익명함수라고도 불림

- return문을 가질 수 없음

- 간편 조건문 외 조건문이나 반복문을 가질 수 없음

- 장점

  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def 를 사용할 수 없는 곳에서도 사용가능

  ```python
  # 삼각형의 넓이를 구하는 공식 - def
  def triangle_area(b, h):
      return 0.5 * b * h
  print(triangle_area(5, 6)) # 15.0
  
  # 삼각형의 넓이를 구하는 공식 - lambda
  triangle_area = lambda b, h : 0.5 * b * h
  print(triangle_area(5, 6)) # 15.0
  ```



### 재귀 함수

- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음 (점화식)
  - 변수의 사용이 줄어들며, 코드 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

```python
#팩토리얼
def factorial(n):
	if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
   
print(factorial(4)) # 24
```

```python
#for 사용
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
```



- 재귀 함수 주의 사항
  - 재귀 함수는 base case에 도달할 때까지 함수를 호출함
  - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
  - 파이썬에서는 최대 재귀 깊이가 1000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

-  반복문과 재귀 함수 비교
  - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용
  - 재귀 호출은 변수 사용을 줄여줄 수 있음
  - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림



## 모듈

- 합, 평균, 표준편차 등 자주 쓰는 기능들
- 다양한 기능을 하나의 파일로 (모듈)
- 다양한 파일을 하나의 폴더로 (패키지)
- 다양한 패키지를 하나의 묶음으로 (라이브러리)
- 이러한 것들을 관리하는 관리자 (pip)
- 패키지의 활용 공간 (가상환경)



### 모듈과 패키지

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 거
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 않에는 또 다른 서브 패키지를 포함

```python
import module
from module import var, function, Class
from module import *

form package import module
form package.module import var, function, Class
```



### 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수 (예 : random.py)

- 파이썬 패키지 관리자 (pip)

  - PyPI(Python Package Index) 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
  - 패키지 설치는 pip 명령어 사용

  ```
  # 설치
  pip install SomePackage
  pip install SomePackage==1.0.5
  pip install SomePackage>=1.0.4
  
  # 삭제
  pip uninstall SomePackage
  
  #패키지 목록
  pip list
  pip show Somapackage
  ```

  

## 사용자 모듈과 패키지

- 패키지
  - 패키지는 여러 모듈 / 하위 패키지로 구조화
  - 모든 폴더에는 _____init_____.py 를 만들어 패키지로 인식



## 가상 환경

### 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
  - 모두 pip를 통해 설치
- 복수의 프로젝트를 하는 경우 버전이 상이할 가능성 있음
  - 과거 프로젝트 - 버전 2.x
  - 현재 프로젝트 - 버전 3.x
- 이러한 경우 가상 환경을 만들어 프로젝트별로 독립적인 패키지를 관리 가능

