"""
Section 1
Multithreading - Python's GIL
Kwyword - CPython, 메모리관리, GIL 사용 이유

"""

"""
GIL(Global Interpreter Lock)
1. CPython -> Python(bytecode) 실행 시 여서 thread를 사용 할 경우
    단일 스레드만이 Python object에 접근하게 제한하는 mutex(mutex: thread간 통신방법 중 하나)
2. CPython 메모리관리가 취약(즉, Thread-safe)
3. 단일 스레드로 충분히 빠르다.
4. 프로세스 사용 가능(Numpy/Scipy) 등 GIL 외부 영역에서 효율적인 코딩 가능
5. 병렬 처리는 Multiprocessing, acyncio 등 선택지 다양
6. Thread 동시성 완벽 처리를 위해 -> Jython, IromPython, Stackless Python 등이 존재

"""