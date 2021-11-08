"""
Section 1
Multithreading - Thread(4) - Lock, DeadLock
Keyword - Lock, DeadLock, Race Condition, Thread synchronization

"""

"""
1. Semaphore: 프로세스간 공유 된 자원에 접근 시 문제 발생 가능성
                -> 한 개의 프로세스만 접근 처리 고안(경쟁 상태 예방)

2. Mutex    : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것. -> 경쟁 상태 예방
3. Lock     : 상호 배제를 위한 잠금(Lock)처리 -> 데이터 경쟁
4. DeadLock : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)
                A는 자원1을 사용하고 있고, B는 자원2를 사용하고 있다.
                이 때 A는 자원2를 사용하기 위해 대기하고, B는 자원1을 사용하기 위해 대기한다.

            Race Condition(경쟁상태): 둘 이상의 입력이나 조작이 동시에 일어나 의도하지 않은 결과가 발생하는 경우
                                    -> 교착상태의 한 종류

5. Thread synchronization(스레드 동기화)를 통해서 안정적으로 동작하게 처리한다. (동기화 메소드, 동기화 블록)
6. Semaphire와 Mutex의 차이는?
            -> 둘 다 병렬 프로그래밍 환경에서 상호배제를 위해 사용
            -> 뮤텍스는 공유된 리소스에 하나의 스레드만 접근할 수 있게 제한
            -> 세마포어는 공유된 리소스에 대한 동시 엑세스를 일부 허용 (1개로 제한하면 뮤텍스가 됨)

"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    # 공유 변수(value)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # 변수 업데이트 함수
    def update(self, n):
        logging.info('Thread %s: Starting update', n)

        # 뮤텍스 & Lock 등 동기화(Thread synchronization 필요)

        # Lock 획득(방법1)

        # self._lock.acquire()
        # logging.info('Thread %s: has lock', n)

        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # logging.info('Thread %s: about to release lock', n)

        # Lock 반환
        # self._lock.release()

        # Lock 획득(방법2) 추천!
        
        with self._lock:
            logging.info('Thread %s: has lock', n)

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info('Thread %s: about to release lock', n)

        logging.info('Thread %s: Finishing update', n)


if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info('Main-Thread: before creating and running thread')

    # 클래스 인스턴스롸
    store = FakeDataStore()

    logging.info('Testing update. Starting value id %d', store.value)

    # With Context
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info('Testing update. Ending value id %d', store.value)