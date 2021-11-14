"""
Section 2
Parallelism with Multiprocessing - Process vs Thread, Parallelism
Keyword - Process, Thread, 병렬성

"""

"""
1. Parrallelism
    - 완전히 동일한 타이밍에 태스크 실행
    - 다양한 파트로 나눠서 실행
    - 멀티프로세싱에서 CPU가 1Core인 경우 만족하지 않음.
    - 딥러닝, 비트코인 채굴 등

2. Process vs Thread
    - 독립된 메모리(프로세스), 공유 메모리(스레드)
    - 많은 메모리 필요(프로세스), 적은 메모리 필요(스레드)
    - 좀비(데드)프로세서는 생성될 가능성 있는데, 좀비(데드)스레드는 생성될 가능성 낮음
    - 오버헤드 큼(프로세스), 오버헤드 작음(스레드)
    - 생성/소멸 cost가 높음(프로세스), 생성/소멸 비교적 빠름(스레드)
    - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드 작성 어려움/디버깅 어려움(스레드)

3. CPU == Processor >= Core && Program >= Process
    - Processor는 CPU라고 보면 됨
    - Processor에는 제어장치(CU, Control Unit)와 연산장치(ALU, Arithmetic Logic Unit), 레지스터 메모리가 있음
    - Processor는 여러 Core로 나눌 수 있으며, 각 Core는 CU, ALU, 레지스터를 가지고 있음(레지스터는 Core당 여러개도 가능)
    - Processor는 HW 적인 개념이라면, Process는 SW 적인 개념이다.
    - Program이 실행되면, 새로운 Process가 생성되고, 이 Process의 주소공간으로 실행파일을 RAM에 올린다.
        -> CPU는 기본적으로 HDD는 접근할 수 없기 때문에 RAM에 올려서 실행가능하게 만든 것.
        -> 따라서 Program당 하나의 Process가 할당된다. (multiprocess의 경우 여럿의 Process)
"""