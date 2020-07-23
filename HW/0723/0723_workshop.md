# 0723_workshop



### 1. 숫자의 의미

```python
def get_secret_word(aski):
    name = ''
    for i in aski:
        name += chr(i)
    return name
```



### 2. 내 이름은 몇일까?

```python
def get_secret_number(aski):
    name = 0
    for i in aski:
        name += ord(i)
    return name
```



### 3. 강한 이름

```python
def get_strong_word(name1, name2):
    value1 = 0
    value2 = 0
    for i in name1:
        value1 += ord(i)
    for i in name2:
        value2 += ord(i)
    if value1 > value2:
        return name1
    else:
        return name2
```

