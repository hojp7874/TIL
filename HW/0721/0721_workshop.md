# Python 02. 데이터 & 제어문



### 1. 간단한 N의 약수 (SWEA #1933)

```python
number = int(input())

for i in range(1, number+1):
    if number % i == 0:
        print(i, end=' ')
```



### 2. 중간값 찾기 (SWEA #2063 변형) 

```python
numbers = [...]

my_sum = 0
count = 0
for number in numbers:
    my_sum += number
    count += 1
print(my_sum/count)
```



### 3. 계단 만들기 

```python
number = int(nput())

for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
```



### 4. 구구단을 외자, 구구단을 외자 2 X 1 ?! 

```python
for i in range(2, 10):
    print(f'------- [{i}단] -------')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')
```

