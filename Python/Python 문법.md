# Python 문법

## 기초 문법

### 주석

> `#`을 앞에 붙여서 사용한다.

```python
# 이것이 주석입니다.
```

### 코드 라인

> 파이썬 코드는 1줄 1문장이 원칙
>
> 파이썬에서는 `;`을 작성하지 않음
>
> 다만 한줄로 표기할 때 `;`를 사용할 수 있음

```python
print('안녕')
print('안녕')print('안녕') <- 잘못된 표기
print('안녕');print('안녕') <- 실행은 되는데 이렇게는 잘 안씀
```



### 변수

#### `type`

> 변수의 타입을 확인하는 명령어

```python
type(20)
> int
(정수의 경우 int(integer)로 표기된다.)

type('사람')
> str
(글자의 경우 str(string)로 표기된다.)

type(0.02)
> float
(실수의 경우 float(floating point number)로 표기된다.)

type(3+2j)
> complex
(복소수의 경우 complex(complex number)로 표기된다.)
```

##### 실수 연산의 주의점

```python
print(3.5 - 3.2)
> 0.2999999999999998
```

> 위와같이 실수연산 시 오차가 존재한다.
>
> 따라서 적절한 보정을 해주어야 한다.

```python
round(3.5 - 3.2, 2) == 0.3
> True
```

> 또는 아래와 같이 sys모듈을 통해 처리할 수 있다.

```python
import sys
print(sys.float_info.epsilon)
> 2.220446049250313e-16
> True
```

> 또는 math 모듈을 통해 처리할 수 있다. (가장 편함)

```python
import math
math.isclose(a, b)
> True
```

##### 복소수 연산의 주의점

> 문자열을 변환할 때, +나 - 주위에 공백을 포함하면 안됨

```python
c = complex('3+4j') 	O
c = complex('3 + 4j') 	X
```



#### `id`

> 해당 값의 메모리 주소를 확인하는 명령어

```python
id(3)
> 10914560
```

#### 변수 입력

> 같은 값을 서로다른 변수에 할당할 수 있음
>
> 여러 변수 할당을 동시에 할 수도 있음

```python
a = 20
b = 20
print(a, b)
> 20 20
```

```python
a, b = 10, 20
print(a, b)
> 10 20

a, b = b, a
print(a, b)
> 20 10
```

#### 식별자(Identifiers)

식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

##### 식별자의 조건

> 기존에 존재하는 예약어는 사용이 불가하다.
>
> 그 종류는 아래의 명령어로 확인할 수 있다.

```python
import keyword
print(keyword.kwlist)
> ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

>  내장함수나 모듈 등의 이름은 입력은 되지만 사용하면 안된다.

```python
print = 'ssafy'
print('print')
> 오류
```

> 위의 코드를 입력하면 print명령어에 ssafy가 입력되어서 기존의 print역할을 잊게된다.
>
> 이렇게 잘못 입력하면 생성한 print를 삭제해야 한다.

```python
del print
```



### 문자타입(str)의 문장 쓰는 법

>  기본적으로 `"` = `'` 이지만 문장 내 따옴표와 같은 종류를 쓰면 문제가 생김

```python
print("나는 "진표" 입니다")
> 오류

print('나는 "진표" 입니다')
> 나는 "진표" 입니다
```

> 큰 따옴표로 여러 줄 문장을 작성할 수 있다.

```python
print('''나는
    진표
    입니다.''')
> 나는
> 진표
> 입니다.
```

> 연산자를 사용할 수도 있다.

```python
'hello' + 'hello'
> 'hellohello'

'hello' * 3
> 'hellohellohello'

'hello' '진표'
> 'hello진표' <- #(썩 좋지 못한 형태)
```

> 변수화도 가능

```python
name = '진표'
'my name is' + name
> my name is진표
```

#### 이스케이프 시퀀스

> \를 활용하여 특수한 문자를 조작할 수 있음



























#### 참/거짓(Boolean) 타입

#### 형변환(연산하는 타입을 직접 일치시키는 것이 좋은 습관임.)

- 암시적 형변환

  - bool
  - Nembers(int, float, complex)

  ```python
  # boolean과 integer는 더할 수 있다. (Python이 자동으로 형변환을 시켜준다.)
  True + 3
  > 4
  
  False + 3
  > 3
  
  int(True)
  > 1
  
  # None 타입은 더할 수 없다.(None은 값이 존재하지 않기 때문)
  None + 3
  > 오류
  ```

  ```python
  # int, float, complex는 더할 수 있을까
  int_num = 2020
  float_num = 3.14
  complex_num = 2+3j
  
  int_number + float_num
  > 2023.14 #float형
  
  int_num + complex_num
  > (2022+3j) #complex형
  ```

  

- 명시적 형변환

  - ㅇ

  ```python
  # integer와 string 사이는 명시적 형변환 필요
  str(1) + '등'
  > '1등'
  
  float('3.5')
  > 3.5
  
  # 정수가 아닌 string은 int로 변환할 수 없음
  int('3.5')
  > 오류
  
  int(3.5)
  > 3
  
  int(float('3.5'))
  > 3
  ```



### 연산자(Operator)

- 산술연산자
- 비교 연산자
- 논리 연산자
- 복합 연산자
- 기타 연산자

#### 산술 연산자

> 

| 연산자 | 내용     |
| ------ | -------- |
| +      | 덧셈     |
| -      | 뺄셈     |
| *      | 곱셈     |
| /      | 나눗셈   |
| //     | 몫       |
| %      | 나머지   |
| **     | 거듭제곱 |

```python
a = 5 // 2
b = 2 % 2

print(a)
print(b)


```



```python
num = 2020
print(-num)
> -2020
```



#### 비교 연산자

| `<`      | 미만                   |
| -------- | ---------------------- |
| `<=`     | 이하                   |
| `>`      | 초과                   |
| `>=`     | 이상                   |
| `==`     | 같음                   |
| `!=`     | 같지않음               |
| `is`     | 객체 아이덴티티        |
| `is not` | 부정된 객체 아이덴티티 |

```python
3 == 3.0
> True

'hello' == 'HELLO'
> False
```



#### 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

| A    | B    | and  | or   |
| ---- | ---- | ---- | ---- |
| T    | T    | T    | T    |
| T    | F    | F    | T    |
| F    | T    | F    | T    |
| F    | F    | F    | F    |

```python
print(True and False)
> False

print(True or False)
> True
```

##### 단축 평가

```python
'a' and 'b'
> 'b' # 'a'와 'b' 모두 평가 하고 뱉어냄

'a' or 'b'
> 'a' # 'a'만 평가하고 뱉터냄(단축 평가)
```



#### 복합 연산자

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |



#### 기타 주요 연산자

```python
[1, 2, 3] = [4, 5, 6]
> [1, 2, 3, 4, 5, 6]

'a' in 'hello'
> False

23 in range(3, 45, 5)
> True
```

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
> True

print(a is b)
> False
```

```python
# Indexing/Slicing
[1, 2, 3, 4, 5]{1:3}
```



#### 연산자 우선순위

0. ()
1. Slicing
2. Indexing



