# 병행성
# 이터레이터, 제너레이터
"""제너레이터 == 이터레이터를 만들어내는 것"""

# 파이썬에서 반복 가능한 타입
# collections, text file, list, dict, set, tuple, unpacking, *args: iterable

# 반복 가능한 이유? -> 내부적으로 iter(x) 함수가 호출이 됨.
t = 'abcdefghijklmnopqrstuvwxyz'

w =  iter(t)
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()



# 반복형 확인

from collections import abc


print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))


class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WprdSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tommorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print()
print()

# generator
# 1. 지능형 list, dict, 집함 ->< 데이터 양 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word

        return
    def __repr__(self):
        return 'WordSpliFenerator (%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)
print(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))


print()
print()
print()
def generator_ex1():
    print("start")
    yield 'A Point'
    print('continue')
    yield 'B Point'
    print('end')

temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    # print(v)
    pass

temp2 = [x for x in generator_ex1()]
temp3 = (x for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

# for i in temp3:
    # print(i)