# lambda, reduce, map, filter
from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(lambda x, y: x+y, a))

from copy import copy, deepcopy

a = [1, 2, 3, [4, 5, 6], [7, 8, 9]]

b = copy(a)
c = deepcopy(a)

print(id(a))
print(id(b))
print(id(c))
print(id(a[3]))
print(id(b[3]))
print(id(c[3]))

"""
context manager
keyward: contextlib, __enter__, __exit__, exception

context manager는 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할을 함.
with 구문을 이해해야 함.
"""

file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1')
finally:
    file.close()


with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2')


class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWrite started: __init__')
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        print('MyFileWriter started: __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back):
        print('MyFilterWriter started: __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()


with MyFileWriter('./testfile3.txt', 'w') as f:
    print("#")
    f.write('Contetx Manager Test3\nContextlib Test3')
    print("#")


"""
contextlinb : measure execution(타이머) 제작
"""

import time
class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
    
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
        return True


with ExcuteTimer('Start! job') as v:
    print('Received start monotonic1: {}'.format(v))
    for i in range(100000000):
        pass
    raise Exception('Raise! Exception!!')