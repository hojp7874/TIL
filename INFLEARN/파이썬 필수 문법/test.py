class Bicycle:
    wheel = 2
    sit = 1
    handle = 2
    ...
   
class ThreeBicycle(Bicycle):
    wheel = 3

b = Bicycle()
t = ThreeBicycle()
print(b.wheel)
print(t.wheel)