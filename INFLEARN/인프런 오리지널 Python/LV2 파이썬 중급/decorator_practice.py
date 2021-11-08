# def decorator1(func):
#     print('decorator에 들어왔다.')
#     print(func)
#     def inner(*args):
#         print('inner에 들어왔다.')
#         print(func)
#         print(*args)
#         result = func(*args)
#         print('inner에서 나간다.')
#         return result
#     print('decorator에서 나간다.')
#     return inner

# @decorator1
# def add(a, b):
#     return a + b

# print(add(1, 3))
# print(add(2, 4))
# print(add(3, 5))

# print('-'*200)

def decorator2(*args1):
    print('decorator에 들어왔다.')
    print(args1)
    def wrapper(func):
        print('wrapper에 들어왔다.')
        print(args1, func)
        def inner(*args2):
            print('inner에 들어왔다.')
            print(args1, func, args2)
            result = func(args1, args2)
            print('inner에서 나간다.')
            return result
        print('wrapper에서 나간다.')
        return inner
    print('decorator에서 나간다.')
    return wrapper

@decorator2(1, 2, 3, 4)
@decorator2('a', 'b', 'c')
def print_test(*args):
    print(args)
    assert args == 1
    return args

print('result: ', print_test(5, 6, 7))
print('result: ', print_test(8, 9, 0))