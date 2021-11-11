"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, asyncio

I/O Bound Asyncio 예제

"""

import asyncio
import aiohttp
import time

# threading 보다 높은 코드 복잡도 -> async, await 적절하게 코딩

# 실행함수1(다운로드)
async def request_site(session, url):

    # 세션 확인
    print(session)
    # print(session.headers)

    async with session.get(url) as response:
        print(f"Read Contents {response.content_length}, from {url}")


# 실행함수2(요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        
        # 태스크 확인
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True) # 크롤러 403에러 벤 먹일 수 있으니 예외처리

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
    # asyncio.run(request_all_sites(urls))
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls))

    # 실행 시간 측정
    duration = time.time() - start_time

    # 결과 출력
    print()
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == "__main__":
    main()