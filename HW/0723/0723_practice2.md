# 0723_practice2



### 1. 불쌍한 달팽이

```python
def snail(height, day, night):
    i = 0
    move = 0
    while move < 100:
        move = day + (day - night) * i
        i += 1
    return i
```



### 2. 자릿수 더하기

```python
def sum_of_digit(number):
    size = len(str(number))
    value = list(range(size))
    for i in range(1, size + 1):
        value[i-1] = 0
        while number >= (10 ** (size - i)):
            number -= (10 ** (size - i))
            value[i-1] += 1
    return sum(value)
```

