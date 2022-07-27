# 객체지향 프로그래밍

- 객체 지향 프로그래밍
  - 컴퓨터 프로그래밍의 패러다임
  - 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위(객체)들의 모임으로 파악
  - 각각의 객체는 메시지를 주고받고 데이터를 처리 가능
  - 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
  - 객체는 크게 **정보**와 **행동**으로 나누어 짐



- 객체지향 프로그래밍이 필요한 이유
  - 현실 세계를 프로그램 설계에 반영(추상화)



- 객체지향의 장점 / 단점
  - 장점
    - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - 필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움
  - 단점
    - 설계 시 많은 노력과 시간이 필요함
      - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    - 실행 속도가 상대적으로 느림
      - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름



# 객체

- 컴퓨터 과학에서 객체 또는 오브젝트라고도 불림
- 클래스에서 정의한 것을 토대로 메모리(실제 공간)에 할당된 것
- 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미
- 변수, 자료구조, 함수 또는 메서드가 될 수 있음
- **속성**과 **행동**으로 구성된 모든 것



### 객체와 인스턴스

- 클래스와 객체 관계
  - 클래스(설계도) - 가수  ==>  객체(실제 사례) - 이찬혁 
- 클래스로 만든 객체를 인스턴스 라고도 함
  - 객체와 인스턴스의 차이점
    - 이찬혁은 객체다 (O)
    - 이찬혁은 인스턴스다 (X)
    - 이찬혁은 가수의 인스턴스다 (O)

- 객체는 특정 타입의 인스턴스
  - 1, 2, 3 은 모두 int의 인스턴스
  - 'hello', 'bye'는 모두 string의 인스턴스
  - [1, 2, 3], []은 모두 list의 인스턴스



### 객체

- 객체(object)의 특징
  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가
  - 속성(attribute) : 어떤 상태(데이터)를 가지는가
  - 조작법(method) : 어떤 행위(함수)를 가지는가



# 객체와 클래스 문법

### 기본 문법

- 클래스 정의

```python 
# 클래스 정의
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()

# 메서드 호출
my_instance.my_method()

# 속성
my_instance.my_attribute
```



### 클래스와 인스턴스

- 객체의 설계도(클래스)를 가지고, 객체(인스턴스)를 생성
  - Person(클래스) ==> 가수(인스턴스), 감독(인스턴스), 팬(인스턴스)
- 클래스 : 객체들의 분류 / 설계도
- 인스턴스 : 하나하나의 실체



### 객체 비교하기

- ==
  - 동등한
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확이해 준 것은 아님
- is
  - 동일한(identical)
  - 두 변수가 동일한 객체를 가리키는 경우 True
- 객체 비교 예시

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True, False

a = [1, 2, 3]
b = a

print(a == b, a is b) # True Ture
```



# 속성

### 속성

- 특정 데이터 타입 / 클래스의 객체들이 가지게 될 상태 / 데이터를 의미
- 클래스 변수 / 인스턴스 변수가 존재

```python
class person:
    blood_color = 'red' # 클래스 변수
    population = 100 # 클래스 변수
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        
person1 = Person('john')
print(person1.name) # john      
```



### 인스턴스 변수

- 인스턴스 변수란?
  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수
- 생성자 메서드(___________init______)에서 **self.<name>**으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

```python
class Person:
    
    def __init__(self, name): # 인스턴스 변수 정의
        self.name = name 

john = Person('john') 
print(john.name) # john # 인스턴스 변수 접근 및 할당
john.name = 'John Kim'
print(john.name) # John Kim # 인스턴스 변수 접근 및 할당
```



### 클래스 변수

- 클래스 변수
  - 한 클래스의 모든 인스턴스가 공유하는 값을 의미
  - 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
  - 예시) 특정 사이트의 User 수 등의 클래스 변수를 사용해야 함
- 클래스 선언 내부에서 정의
- <classname>.<name>으로 접근 및 할당

```python
class Person:
    pi = 3.14 # 클래스 변수 정의
    
    def __init__(self, r): 
        self.r = r # 인스턴스 변수 정의
```



### 클래스 변수 활용

- 사용자가 몇 명인지 확인하고 싶다면?
  - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정하면 됨

```python
class Person:
    count = 0
    # 인스턴스 변수 설정
    def __init__(self, name):
        self.name = name
        Person.count += 1
        
person1 = Person('a')
person2 = Person('b')

print(Person.count) # 2
```



### 클래스 변수와 인스턴스 변수

- 클래스 변수를 변경할 때는 항상 **클래스.클래스변수** 형식으로 변경



# 메서드

### 메서드

- 특정 데이터 타입 / 클래스의 객체어 공통적으로 적용 가능한 행위 (함수)
- 클래스 안에 있는 함수



### 메서드의 종류

- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드



### 인스턴스 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

```python
class MyClass:
    
    def instance_method(self, arg1, ...)
    
my_instance = MyClass()
my_instance.instance_method(....)
```



### self

- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
  - 매개변수 이름을 self를 첫 번째 인자로 정의
  - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 룰



### 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
  - 인스턴스 생성
  - `_init_` 메서드 자동 호출



### 매직 메서드

- Double underscre가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
- 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에 자동으로 불리는 메서드



### 매직 메서드의 예시

- 객체의 특수 조작 행위를 지정(함수, 연산자 등)
- `__str__` : 해당 객체의 출력 형태를 지정
  - 프린트 함수를 호출할 때 자동으로 호출
  - 어떤 인스턴스를 출력하면 `__str__`의 return값이 출력

![image-20220727110635831](C:\Users\joney\AppData\Roaming\Typora\typora-user-images\image-20220727110635831.png)



### 클래스 메서드

- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스가 전달 됨



### 데코레이터

- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용 되기 때문에 작성 순서가 중요
- 데코레이터를 활용하면 쉽게 여러 함수를 원하는데로 변경 가능

데코레이터가 없는 경우

```python
def hello():
    print('hello')
    
#데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받음
    def wrapper(): #함수 내에서 새로운 함수 선언
    	print('함수 시작') # original 함수 꾸밈
        original()
        print('함수 끝') # original 함수 꾸밈
     return wrapper

add_print(hello)()
#'함수 시작'
#'hello'
#'함수 끝'
print_hello = add_print(hello)
print_hello()
#'함수 시작'
#'hello'
#'함수 끝'
```

데코레이터 사용

- 쉽게 여러 함수를 원하는대로 변경 가능

```python
#데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받음
    def wrapper(): #함수 내에서 새로운 함수 선언
    	print('함수 시작') # original 함수 꾸밈
        original()
        print('함수 끝') # original 함수 꾸밈
     return wrapper

@add_print
def print_hello():
    print('hello')
    
print_hello()
#'함수 시작'
#'hello'
#'함수 끝'
```





### 클래스 메서드와 인스턴스 메서드

- 클래스 메서드 => 클래스 변수 사용
- 인스턴스 메서드 => 인스턴스 변수 사용
- 인스턴스 변수, 클래스 변수 모두 사용하고 싶다면?
  - 클래스는 인스턴스 변수 없이 사용 불가능
  - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘가 사용이 가능



### 스태틱 메서드

- 스태틱 메서드
  - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
- 언제 사용?
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용

- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
  - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속
  - 주로 해당 클래스로 한정하는 용도로 사용

```python
class Person:
    count = 0 # 클래스 변수
    def __init__(self, name): # 인스턴스 변수 설정
        seld.name = name
        Person.count += 1
        
    @staticmethod
    def check_rich(money): # 스태틱은 cls, self 사용 x
        return money > 10000
    
person1 = Person('아이유')
print(Person.check_rich(10000)) # True 스태틱은 클래스로 접근 가능
print(person1.check_rich(10000)) # True 스태틱은 인스턴스로 접근 가능
```



### 인스턴스와 클래스 간의 이름 공간

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 순으로 탐색



# 메서드 정리

### 메서드 정리

- 인스턴스 메서드
  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작
- 클래스 메서드
  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메서드
  - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
    - 객체 상태나 클래스 상태를 수정할수 없음

예시

```python
class MyClass:
    
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'
```



- 클래스 자체에서 인스턴스 메서드는 호출할 수 없음

```python
MyClass.method() # self가 정의되어 있지 않아서 오류
```



- 인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근 가능



# 객체 지향의 핵심 개념

### 객체 지향의 핵심 4가지

- 추상화
- 상속
- 다형성
- 캡슐화



### 추상화

- 현실 세계를 프로그램 설계에 반영
  - 복잡한 것은 숨기고, 필요한 것만 들어내기



### 상속

- 상속이란
  - 두 클래스 사이 부모 - 자식 관계를 정립하는 것
- 클래스는 상속이 가능함
  - 모든 파이썬 클래스는 object를 상속 받음

```python
class ChildClass(ParentCalss):
    pass
```



- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재상용성이 높아짐



### 상속 관련 함수와 메서드

- super()
  - 자식 클래스에서 부모 클래스를 사용하고 싶은경우

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super.__init__(name, age)
        self.student_id = student_id
```



### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색



### 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):
    gene = 'XX'
    
class Dad(Person):
    gene = 'XY'
    
class FirstChiled(Dad, Mom):
    def cry(self):
        return 'cry'

baby1 = FirstChiled('baby'):
print(baby1.gene) # XY
# FirstChiled에서 Dad가 먼저 들어가 있어서 XY가 출력 됨
# Mom이 먼저 들어가면 XX가 출력됨
```



### 다형성

- 다형성이란
  - 여러 모양을 뜻하는 그리스어
  - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
  - 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답 가능**



### 메서드 오버라이딩

- 상속받은 메서드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
  - 상속 받은 클래스에서 같은 이름의 메서드로 덮어 씀
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 super 활용



### 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
  - 예시 : 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로 존재하지 않음



### 접근 제어자 종류

- Public Access Modifier
- Protect Access Modifier
- Private Access Modifier



### Publid Member

- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출이 가능, 하위 클래스 overriding 허용
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지



### Protected Member

- 언더바 1개로 시작하는 메서드나 속성
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스 override 허용



### Private Member

- 언더바 2개로 시작하는 메서드나 속성
- 본 클래스 내부에서만 사용이 가능
- 하위클래스 상속 및 호출 불가능(오류)
- 외부 호출 불가능(오류)



### getter 메서드와 setter 메서드

- 변수에 접근할 수 있는 메서드를 별도로 생성
  - getter 메서드 : 변수의 값을 읽는 메서드
    - @property 데코레이터 사용
  - setter 메서드 : 변수의 값을 설정하는 성격의 메서드
    - @변수.setter 사용



# 에러와 예외 처리

### 문법 에러

- SyntaxError가 발생하면, 프로그램이 실행되지 않음
- 문제가 발생한 위치를 ^을 사용하여 표현
- Invaild syntax : 문법 오류

```python
while
	break
```



- assign to literal : 잘못된 할당

```python
5 = 3
```



- EOL(End of Line)

```python
print('hello'
```



- EOF(End of File)

```python
print(
```



### 예외

- 실행 도중 예상치 못한 상황이 맞이한 경우, 실행을 멈춤
  - 문법, 표현이 올바르더라도 발생하는 에러
  - 실행 중에 감지되는 에러
- 사용자 정의 예외를 만들어 관리 가능

- 예외의 예시

  - ZeroDivisionError : 어떤 값을 0으로 나눈 경우 발생

  - NameError : namespace에 이름이 없는 경우 발생

  - TypeError : 타입이 불일치하는 경우, argument가 누락 혹은 초과, Type불일치된 경우 발생 
  - ValueError : 값이 적절하지 않거나 없는 경우 (`int('1.3')`)

  - IndexError : Index가 없거나 범위를 초과한 경우 발생

  - KeyError : 존재하지 않는 키값을 호출한 경우 발생

  - ModuleNotFoundError : 사용하려는 모듈을 찾을 수 없는 경우 발생

  - ImportError : 모듈은 있으나 존재하지 않는 클래스나 함수를 가져오는 경우
  - IndentationError : 탭이 올바르지 않은 경우
