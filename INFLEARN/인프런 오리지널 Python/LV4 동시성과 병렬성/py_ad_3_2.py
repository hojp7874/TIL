"""
Section 3
Concurrency, CPU Bound vs I/O Bound - Blocking vs Non-Blocking IO
Keyword - Blocking IO, Non-Blocking IO, Sync, Async

"""

"""
IO작업: Input과 Output을 통해 외부와 통신하는 기법
        블루투스, 오디오 등 완전히 개별된 장치와의 통신

Blocking IO vs Non-Blocking IO

    Blocking IO
    - 시스템 콜 요청 시 -> 커널 IO 작업 완료 시 까지 응답 대기 (순차적 처리)
    - 제어권이 IO작업에게 있음 -> 커널 소유 -> 응답(Response) 전 까지 대기(Block) -> 다른 작업 수행 불가능
        일을 시켜놓고 그 일이 완료될 때 까지 대기

    Non-Blocking IO
    - 시스템 콜 요청 시 -> 커널 IO 작업 완료 여부 상관없이 즉시 응답
    - 제어권(IO작업) -> 유저프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인
        일을 시켜놓고 다른일을 함

    Sync vs Async

    - Sync: IO작업 완료 여부에 대한 Noty는      유저 프로세스 -> 커널   (호출하는 함수 -> 호출되는 함수)
        주기적으로 작업 완료 여부를 확인해야 함.

    - Async: IO작업 완료 여부에 대한 Noty는     커널 -> 유저 프로세스   (호출되는 함수 -> 호출하는 함수)
        작업이 완료되면 커널에서 신호를 보내줌.

Async non_blocking IO (AsyncIO. 가장 중요)

    일을 시켜놓고 그 시간동안 작업완료여부 상관없이 다른 일에 집중할 수 있음.
    
"""