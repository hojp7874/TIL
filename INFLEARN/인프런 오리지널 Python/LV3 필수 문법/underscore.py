"""
property
접근지정자

다양한 underscore의 활용
파이썬 접근지정자 설명
"""

# 값을 무시할 때 사용
x, _, y = (1, 2, 3)

a, *_, b = (1, 2, 3, 4, 5)

print(x, y, a, b)


# 접근지정자
# name: public
# _name: protected
# __ private
# 이것들의 '강제성은 없지만' 사용자들이 사용하는 `국룰`이다.
# 타 클래스의 __는 접근하지 않는 것이 국룰이다.
# name managling 이라고 치면 자세히 나옴

class SampleA:
    def __init__(self):
        self.x = 'x'
        self._y = '_y'
        self.__z = '__z' #==> '_SampleA__z' 로 바뀜

a = SampleA()
print(a.x)
print(a._y)
# print(a.__z)
print(a._SampleA__z)
print(dir(a))


# Getter, Setter 메서드 활용

class SampleB:
    def __init__(self):
        self.x = 'x'
        self.__y = '__y'

    def get_y(self):
        return self.__y
    
    def set_y(self, value):
        self.__y = value


b = SampleB()
b.x = 1
b.set_y(2)
print(b.x)
print(b.get_y())
print(dir(b))


"""
Getter, Setter
keyword: @Property

Property의 장점:
1. 파이써닉한 코드
2. 변수 제약 설정
3. Getter, Setter효과 동등(코드 일관성)
    - 캡슐화-유효성 검사 기능 추가 용이
    - 대체 표현(속성 노출, 내부의 표현 숨기기 가능)
    - 속성의 수명 및 메모리 관리 용이
    - 디버깅 용이
    - Getter, Setter 작동에 대해 설계된 여러 라이브러리 상호 운용성 증가
"""

class SampleA:
    def __init__(self):
        self.x = 'x'
        self.__y = '__y'

    @property
    def y(self):
        print('Called get method')
        return self.__y
    
    @y.setter
    def y(self, value):
        print('Called set method')
        self.__y = value
    
    @y.deleter
    def y(self):
        print('Called delete method')
        del self.__y


class SampleB:
    def __init__(self):
        self.x = 'x'
        self.__y = '__y'

    def get_y(self):
        return self.__y
    
    def set_y(self, value):
        self.__y = value
    
    def del_y(self):
        del self.__y

a = SampleA()
b = SampleB()
print(a.x)
print(a.y)
print(b.x)
print(b.get_y())
print('-'*200)
print(a._SampleA__y)
print(a)
print(dir(SampleA))
a.y = 3
del a.y
print(dir(SampleB))
print(SampleA.__dict__)

print('-'*200)

class Test:
    def __init__(self):
        self.__a = 'a'
       
    @property
    def aa(self):
        print("getter")
        return self.__a
       
    @aa.setter
    def aa(self, value):
        print("setter")
        self.__a = value
       
    @aa.deleter
    def aa(self):
        print("deleter")
        del self.__a

a = Test()
a.aa = 1
a.aa
del a.aa