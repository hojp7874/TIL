# 0720_workshop



### 1. 세로로 출력하기

```python
number = int(input())

for num in range(number):
    print(num+1)
```



### 2. 가로로 출력하기

```python
number = int(input())

for num in range(number):
    print(num+1, end=' ')
```



### 3. 거꾸로 세로로 출력하기

```python
number = int(input())

for num in range(number):
    print(number - num)
```



### 4. 거꾸로 출력해 보아요 (SWEA #1545)

```python
number = int(input())

for num in range(number):
    print(number - num, end=' ')
```



### 5. N줄 덧셈 (SWEA #2025)

```python
number = int(input())

sum = 0
for num in range(number):
    sum += num+1
print(sum)
```

