# 0722_workshop



### 1. List의 합 구하기

```python
def list_sum(a):
    sumall=0
    for i in a:
        sumall += i
    return sumall
```



### 2. Dictionry로 이루어진 List의 합 구하기

```python
def dict_list_sum(my_list):
    sumage = 0
    for i in my_list:
        sumage += i['age']
    return sumage
```



### 3. 2차원 List의 전체 합 구하기

```python
def all_list_sum(my_list):
    sum_all = 0
    for i in my_list:
        for j in i:
            sum_all += j
    return sum_all
```





