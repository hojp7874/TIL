# 0721_homework



### 1. Mutable & Immutable 

```python
Mutable = list, set, dictionary

Immutable = string, range, tuple
```



### 2. 홀수만 담기

```python
odd = list(range(51)[1:51:2])
print(odd)
```



### 3. Dictionary 만들기

```python
dict(홍진표=26, 강석민=26, 강채원=25, 김효진=26, 박주동=26, 이동희=26, 이준희=29, 김대중=26, 임지성=26, 박철완=26, 허태윤=27, 고영지=27)
```



### 4. 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*', end='')
    print()
```



### 5. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```



### 6. 평균 구하기

```python
scores = [80, 89, 99, 83]

print(sum(scores)/len(scores))
```

