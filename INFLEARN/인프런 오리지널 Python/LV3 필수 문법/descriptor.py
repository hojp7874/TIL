"""
keyword - descriptor, set, get, del, property

1. 객체에서  서로 다른 객체를 속성값으로 가지는 것.
2. Read, Write, Delete 등을 미리 정의 가능
3. data descriptor(sef, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""
class Descriptor1(object):
    def __init__(self, name='Default'):
        self.name = name

    def __get__(self, obj, objtype):
        print('__get__')

        return self, obj, objtype, self.name

    def __set__(self, obj, name):
        print('__set__')
        print('obj', obj)
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string')
        
    def __delete__(self, obj):
        print('__del__')
        self.name = None
    
class Sample1(object):
    desc = Descriptor1()

s1 = Sample1()
s1.desc = 'Descriptor Test1'
print(s1.desc)
del s1.desc
print(s1.desc)

# class property(fget=None, fset=None, fdel=None, doc=None)

class Descriptor2(object):
    def __init__(self, value):
        self._name = value

    def getVal(self):
        print('__get__')
        return self, self._name
    
    def setVal(self, value):
        print('__set__')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should bs str')
        
    def delVal(self):
        print('__del__')
        self._name = None
    
    name = property(getVal, setVal, delVal, 'property method example')

s2 = Descriptor2('Descriptor test2')
print(s2.name)
del s2.name
print(s2.name)
print(Descriptor2.name.__doc__)

print('-'*200)

"""
keyword - descriptor vs property, low level(descriptor) vs high level(property)

1. 상황에 맞는 메서드 구현을 통한 객체기향 프로그래밍 구현
2. property와 달리 resue(재사용) 가능
3. ORM Framework 사용
"""

import os

class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        # print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))

class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname
    
s = DirectoryPath('./')
g = DirectoryPath('../')
print(s.size)
print(g.size)

print(dir(DirectoryPath))
print(DirectoryPath.__dict__)
print(dir(s.__dict__))

print('-'*200)

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value
    
    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', value)
        self.value = value


class Student:
    score = LoggedScoreAccess()

    def __init__(self, name):
        self.name = name

s1 = Student('Kim')
s2 = Student('Lee')

print(s1.score)
s1.score += 20
print(s1.score)

print(s2.score)
s2.score += 40
print(s2.score)

print(vars(s1))
print(vars(s2))
print(s1.__dict__)
print(s2.__dict__)