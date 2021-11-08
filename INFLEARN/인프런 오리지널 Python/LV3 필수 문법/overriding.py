"""
Method Overriding

1. 자식에서 부모클래스를 호출 후 사용
2. 메서드 재 정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능(구조적 접근)
4. 확장 가능, 다령성(다양한 방식으로 동작)
5. 가독성 증가, 오류가능성 감소, 메서드 이름 절약, 유지보수성 증가 등
"""


# Overriding 예제

class ParentEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):
    pass

c1 = ChildEx1()
p1 = ParentEx1()

print(c1.get_value())

print("dir 차이")
print(dir(p1))
print(dir(c1))

print("__dict__ 차이")
print(ParentEx1.__dict__)
print(ChildEx1.__dict__)


class ChildEx2(ParentEx1):
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()

print(c2.get_value())

import datetime

class Logger(object):
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now()} {msg}"
        # super().log(message)
        super(TimestampLogger, self).log(message)

class DateLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now().strftime('DY-%m-%d')} {msg}"
        # super().log(message)
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

l.log('Called logger.')
t.log('timestamp logger.')
d.log('date logger.')


"""
Method Overloading
Overriding과 비슷하나, 부모 클래스와는 상관 없음.
keyword: overloading, oop, multiple dispatch

1. 동일 메서드 재정의
2. 네이밍 기능 예측
3. 코드 절약, 가독성 향상
4. 메서드 파라미터 기반 호출 방식
"""


# 동적 타입 검사 -> 런타임에 실행(타입 에러가 실행시에 발견)

class SampleA():
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, z):
        return x + y + z


a = SampleA

# print(a.add(2, 3)) -> 에러발생
print(dir(a))

# 자료형에 따른 분기 처리

class SampleB():
    def add(self, datatype, *args):
        if datatype == 'int':
            return sum(args)
        
        if datatype == 'str':
            return ''.join([x for x in args])


b = SampleB()

print(b.add('int', 5, 6))

print(b.add('str', 'Hi', 'Python'))

print('-----------------------------------------------------------------------------')

from multipledispatch import dispatch

class SampleC():
    @dispatch(int, int)
    def product(x, y):
        return x * y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z

c = SampleC()

print(c.product(5, 6))
print(c.product(5, 6, 7))
print(c.product(5.0, 6.0, 7.0))

print(dir(c))