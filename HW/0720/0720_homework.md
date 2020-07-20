# 0720_homework

### 1. Python 예약어

```python
import keyword
print(keyword.kwlist)
> ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



### 2. 실수 비교

```python
num1 = 0.1 * 3
num2 = 0.3

import math
math.isclose(num1, num2)
>True
```



### 3. 이스케이프 시퀀스

```python
\n, \t, \\
```



### 4. String Interpolation

```python
name = '철수'
print(f'안녕, {name}야')
> 안녕, 철수야
```



### 5. 형 변환

```python
int('3.5')
```



### 6. 네모 출력

```python
n = 5
m = 9

print('''*****
*****
*****
*****
*****
*****
*****
*****
*****''')
```



### 7. 이스케이프 시퀀스 응용

```python
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
> "파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다."
> 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
```



### 8. 근의 공식

```python
sol1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
sol2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
```

