# Data Structure 1

> Difination of 'Data Structure' is the easy way for access and change data



## string

> immutable, ordered, iterable

### 조회/탐색

> - __.find(x)__ : x의 첫 번째 위치를 반환. 없으면, -1 반환
>
> ```python
> 'apple'.find('p')
> >>> 1
> 
> 'apple'.find('f')
> >>> -1
> ```
>
> - __.index(x)__ : x의 첫 번째 위치를 반환. 없으면, 오류 발생.
>
> ```python
> 'apple'.index('p')
> >>> 1
> ```
>
> 

### 값 변경

> - __.replace(old, new[, count])__ : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환. count를 지정하면 해당 갯수만큼만 시행.
>
> ```python
> 
> ```
>
> - __.strip([chars])__ :
>
> ```python
> 
> ```
>
> - __.split()__ :
>
> ```ㅔㅛ쇄ㅜ
> 
> ```
>
> - __'separator'.join(interable)__ : separator를 interable 사이에 넣어서 문자열로 출력
>
> ```python
> word = '배고파'
> words = ['안녕', 'hello']
> '!'.join(word)
> >>> '배!고!파'
> ```
>
> 
>
> 
>
> 
>
> 
>
> 

### 문자 변형

> 





## List

> mutable, ordered, iterable

### 값 추가 및 삭제

> - __append(x)__ : 리스트에 값을 추가
>
> ```python
> cafe = ['starbucks', 'tomntoms', 'hollys']
> print(cafe)
> >>> ['starbucks', 'tomntoms', 'hollys']
> 
> cafe.append('banapresso')
> print(cafe)
> >>> ['starbucks', 'tomntoms', 'hollys', 'banapresso']
> 
> new_cafe = cafe.append('banapresso')
> print(new_cafe)
> >>> None
> ```
>
> - __.extend(iterable)__ :
>
> ```python
> cafe.extend(['wcafe', '빽다방'])
> print(cafe)
> >>> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방']
> 
> cafe += ['mc_cafe', 'droptop']
> print(cafe)
> >>> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop']
> ```
>
> 
>
> ```python
> cafe.append(['coffeenie'])
> print(cafe)
> print('-----')
> 
> cafe.extend(['twosome_place'])
> print(cafe)
> 
> >>> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie']]
> -----
> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie'], 'twosome_place']
> ```
>
> ```python
> print(cafe)
> cafe.extend('ediya')
> print(cafe)
> 
> >>> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie'], 'twosome_place']
> ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie'], 'twosome_place', 'e', 'd', 'i', 'y', 'a']
> ```
>
> - __.insert(i, x)__ : 
>
> ```python
> 
> ```
>
> - __`.remove(x)`__
>
> ```python
> 
> ```
>
> 
>
> 

### 리스트 복사 방법

> 
>
> 
>
> 
>
> 
>
> 
>
> 

### List Comprehension

> 







## Built-in Function

