# 0723_practice1



### 1. abs() 직접 구현하기

```python
# 아래에 코드를 작성하시오.

def my_abs(x):
    if type(x) == float or type(x) == int:
        return (x ** 2) ** 0.5
    elif type(x) == complex:
        return (x.real**2 + x.imag**2)**0.5
```



### 2. all() 직접 구현하기

```python
# 아래에 코드를 작성하시오.

def my_abs(x):
    if type(x) == float or type(x) == int:
        return (x ** 2) ** 0.5
    elif type(x) == complex:
        return (x.real**2 + x.imag**2)**0.5
```



### 3. any() 직접 구현하기

```python
# 아래에 코드를 작성하시오.

def my_any(elements):
    count = 0
    for i in elements:
        if bool(i) == True:
            count += 1
    if count == 0:
        return False
    else:
        return True
```

