"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(1) - Synchronous
Keyword - I/O Bound, requests

"""

import requests
import time


# 실행함수1(다운로드)
def request_site(url, session):

    with session.get(url) as response:
        print(f"[Read Contents: {len(response.content)}, Status Code: {response.status_code}] from {url}")
        pass

# 실행함수2(요청)
def request_all_sites(urls):
    with requests.Session() as session:

        # 세션 확인
        # print(session)
        print(session.headers)

        for url in urls:
            request_site(url, session)

def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 10

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 실행 시간 측정
    duration = time.time() - start_time

    # 결과 출력
    print()
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == "__main__":
    main()