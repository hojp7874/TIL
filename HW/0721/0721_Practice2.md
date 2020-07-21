# 0721_Practice2



### 1. 더블더블 (SWEA #2019 변형)

```python
number = int(input())

# 아래에 코드를 작성하시오.

result = 1
for num in range(1, number):
    if num % 2 == 0:
        result = result * 3
    else:
        result = result * 2
print(result)
```



### 2. 간단한 소수 판별 1

```python
number = int(input())

# 아래에 코드를 작성하시오.

for num in range(2, number):
    if number % num == 0:
        print('N')
        break
else:
    print('Y')
```



### 3. 간단한 소수 판별 2

```python
numbers = [26, 39, 51, 53, 57, 79, 85]

# 아래에 코드를 작성하시오.

for number in numbers:
    for num in range(2, number):
        if number % num == 0:
            print(f'{number}은(는) 소수가 아닙니다. {num}은(는) {number}의 인수입니다.')
            break
    else:
        print(f'{number}은(는) 소수입니다.')
```

