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
    - 생성/소멸 cost가 높음(프로세스), 생성/소멸 빠름(스레드)
    - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드 작성 어려움/디버깅 어려움(스레드)

"""