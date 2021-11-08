import timeit, time

def duration(func):
    def inner(*args):
        print(f"{func.__name__.upper()}...")
        start = timeit.default_timer()
        result = func(*args)
        print('Running Time:', timeit.default_timer() - start)
        return result
    return inner


@duration
def init_country(t):
    # print('function start!')
    time.sleep(t)
    # print('function end!')
    return

if __name__ == '__main__':
    init_country(1)
    init_country(2)