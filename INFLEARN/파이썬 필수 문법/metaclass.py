"""
Meta Class
Keyword - Type(name, base, dct), Dynamic metaclass

1. 메타클래스 동적 생성
2. 동적 생성한 메타클래스
3. 의도하는 방향으로 직접 클래스 생성에 관여
"""

# type 동적생성 예제
# 인자: name(이름), bases(상속), dct(속성, 메서드)
s1 = type('Sample1', (), {})

print(s1)
print(type(s1))
print(s1.__base__)
print(s1.__dict__)

print('-'*200)

class Parent1:
    pass

s2 = type(
    'Sample2',
    (Parent1,),
    dict(attr1=100, attr2='hi')
    )

# == 이것과 같음.
# class Sample2(Parent1):
#     attr1 = 100
#     attr2 = 'hi'

print(s2)
print(type(s2))
print(s2.__base__)
print(s2.__dict__)
print(s2.attr1, s2.attr2)

print('-' * 200)

class SampleEx:
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n
    
    def mul(self, m, n):
        return m * n

ex = SampleEx()

print(ex.attr1)
print(ex.attr2)
print(ex.add(100, 200))
print(ex.mul(100, 20))

print('-'*200)

s3 = type(
    'Sample3',
    (object, ),
    dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y: x * y)
    # {'attr1':30, 'attr2':100, 'add':lambda x, y: x + y, 'mul':lambda x, y: x * y}
    )

print(s3.attr1)
print(s3.attr2)
print(s3.add(100, 200))
print(s3.mul(100, 20))


"""
keyword - type ingeritance, custom metaclass

1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기(intercept)
    - 클래스 수정하기(modify)
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환

메타클래스는 99% 사용자에게는 필요없는 문법.
이걸 꼭 해야 할 필요는 없음. 그렇질 안길 권장함.
그러나 꼭 필요한 사람이 있음.
"""

# 커스텀 메타클래스 생성 예제(type상속x)

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


CustomList1 = type(
    'CustomList1',
    (list,),
    {
        'desc': '커스텀 리스트1',
        'cus_mul':cus_mul,
        'cus_replace': cus_replace
    }
)

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])
c1.cus_mul(1000)

print(c1)
print(c1.desc)
print(dir(c1))

print('-'*200)

# 좀 더 깊게 들가보자.
# new -> init -> call 순서
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__', self, object_or_name, bases, dict)
    # 인스턴스 실행

    def __call__(self, *args, **kwargs):
        print('__call__', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)    # 클래스 인스턴스 생성(메모리 초기화)

    def __new__(metacls, name, bases, namespace):
        print('__new__', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespace)

CustomList2 = CustomListMeta(
    'CustomList2',
    (list,),
    {}
)

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print(c2)
print(c2.desc)