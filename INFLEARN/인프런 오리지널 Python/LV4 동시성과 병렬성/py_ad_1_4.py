"""
Section 1
Multithreading - Thread(2) - Daemon, Join
Keyword - Threading DaemonThread, Join

"""

"""
DaemonThread(데몬스레드)
1. 백그라운드 실행
2. 메인스레드 종료시 즉시 종료
3. 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 ex) JVM의 가비지 컬렉션, 자동 저장
4. 일반 스레드는 작업 종료시 까지 실행
강사 생각: 스레드가 남아있으면 리소스를 계속 먹으니까 데몬을 해놓는게 좋을 듯!

"""

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)

    for i in d:
        print(i)
    logging.info("Sub-Thread %s: finishing", name)

# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', range(2000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(1000)), daemon=True)
    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # Daemon Thread 확인
    print(x.daemon)

    # daemon thread를 join하면 끝까지 실행이 된다. (매우 않좋은 코드)
    # x.join()
    # y.join()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")
