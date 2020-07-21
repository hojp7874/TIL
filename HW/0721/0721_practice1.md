# 0721_practice1



### 1. 갯수 구하기

```python
students = ['김철수', '이영희', '조민지']

# 아래에 코드를 작성하시오.
count = 0
for student in students:
    count +=1
print(count)
```



### 2. 득표수 구하기

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.
count = 0
for student in students:
    if student == '이영희':
        count +=1
print(count)
```



### 3. 최댓값 구하기

```python
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.
big = 0
for num in numbers:
    if big < num:
        big = num
print(big)
```



### 4. 최솟값 구하기

```python
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.
small = 99
for num in numbers:
    if small > num:
        small = num
print(small)
```



### 5. 최댓값과 등장 횟수 구하기

```python
numbers = [7, 10, 22, 7, 22, 22]

# 아래에 코드를 작성하시오.
big = 0
count = 1
for num in numbers:
    if big < num:
        big = num
        count = 1
    elif big == num:
        count +=1
print(big, count)
```



### 6. 5의 개수 구하기

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 아래에 코드를 작성하시오.

count = 0
for number in numbers:
    if number == 5:
        count +=1
print(count)
```



### 7. 'a'가 싫어

```python
word = input()

# 아래에 코드를 작성하시오.
result = ''
for char in word:
    if char != 'a':
        result += char
print(result)
```



### 8. 단어 뒤집기

```python
word = input()

# 아래에 코드를 작성하시오.

# 1.결과값 담을 변수 초기화
result = ''

# 2. 받은 문자열 순회
for char in word:
    result = char + result
print(result)
```

