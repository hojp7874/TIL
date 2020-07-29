# error_exception

## Error

### Syntax Error

> - `else` 옆에 `:`가 없음
>
> ```python
> if True:
>     print('참')
> else
>     print('거짓')
> 
> >>> SyntaxError: invalid syntax
> ```
>
> - `''`가 닫히지 않았음
>
> ```python
> print('hi)
>       
> >>> SyntaxError: EOL while scanning string literal
> ```



### Exception Error

> 실행 도중 예상치 못한 상황을 맞으면 나타나는 에러
>
> 문법적으로는 옳지만, 실행시 발생하는 에러
>
> - 0으로 나눗셈을 시도
>
> ```python
> 10 * (1/0)
> 
> >>> ZeroDivisionError: division byzero
> ```
>
> - 정의되지 않은 변수 사용
>
> ```python
> print(abc)
> 
> >>> NameError: name 'abc' is not defined
> ```
>
> - 자료형에 대한 타입 자체가 잘못됨
>
> ```python
> 1 + '1'
> 
> >>> TypeError: unsupported operand type(s) for +: 'int' and 'str'
> ```
>
> 
>
> 
>
> 



## Exception Handling

### try & except

> try구문을 실행하고 예외 상황이 발생했을 때 except구문을 실행한다.
>
> ```python
> try:
>     <에러가 날 것 같은 구문>
> except:
>     <에러가 났을 경우 실행>
> ```
>
> - 예시
>
> ```python
> num = input('값을 입력하시오 : ')
> try:
>     print(int(num))
> except:
>     print('error: 숫자를 입력하세요')
> ```
>
> - __에러 메시지 처리__
>
> as 키워드를 활용하여 에러 메시지를 보여줄 수도 있다.
>
> ```python
> try:
>     empty_list = []
>     print(empty_list[-1])
> except IndexError as error:
>     print(error)
> ```
>
> 



### 복수의 예외 처리

> ```python
> try:
>     num = input('100으로 나눌 값을 입력하시오: ')
> 	print(100/int(num))
> except (ValueError, ZeroDivisionError):
>     print('무언가 잘 못 되었습니다.')
> 
> try:
>     num = input('100으로 나눌 값을 입력하시오: ')
> 	print(100/int(num))
> except ValueError:
>     print('error: int가 아닌 값이 입력되었습니다.')
> except ZeroDivisionError:
>     print('0으로는 나눌 수 없습니다.')
> ```
>
> 