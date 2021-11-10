"""
Section 2
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPollExecutor
Keyword - ProcessPollExecutor, as_completed, futures, timeout, dict

"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS = [
    'http://www.daum.net/',
    'http://www.cnn.com/',
    'http://www.naver.com/',
    'http://www.ruliweb.com/',
    'http://www.some-made-up-domain.com/',
]

# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=10) as conn:
        # print(conn.read())
        return conn.read()

def main():
    # 프로세스풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드(실행X)
        future_to_url = {executor.submit(load_url, url, 0-3): url for url in URLS}

        # 중간확인
        # print(future_to_url)

        # 실행
        for future in as_completed(future_to_url):
            # Key값이 Future 객체
            url = future_to_url[future]

            try:
                # 결과
                data = future.result()
            except Exception as exc:
                # 예외 처리
                print('%r generated an exception: %s' % (url, exc))
            else:
                # 결과 확인
                print('%r page is %d bytes' % (url, len(data)))


# 메인 시작
if __name__ == "__main__":
    main()