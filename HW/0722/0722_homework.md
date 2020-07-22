# 0722_homework



### 1. Built-in 함수

```python
len
max
min
print
sum
```



### 2. 정중앙 문자

```python
def get_middle_char(string):
    if len(string) % 2 == 1:
        return string[int((len(string)-1)/2)] # len을 이용한 중간글자 찾기
    else:
        return string[int(len(string)/2-1):int(len(string)/2+1)] # slice이용
```



### 3. 위치 인자와 키워드 인자

```python
4번
```



### 4. 나의 반환값은

```python
None
```



### 5. 가변 인자 리스트

```python
def my_avg(a, b, c, d, e):
    my_list = (a, b, c, d, e)
    sum_all = 0
    count = 0
    for i in my_list:
        sum_all += i
        count += 1
    return sum_all/count
```









