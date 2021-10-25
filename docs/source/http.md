# HTTP

> HyperText Transfer Protocol. W3 상에서 정보를 주고받을 수 있는 프로토콜.

[TOC]

## Request

요청 규약

### start line

요청의 메타데이터를 담고있습니다.

__HTTP Method__

request가 의도한 action을 정의합니다.

__Request target__

request가 전송되는 타겟 uri를 의미합니다.

__HTTP Version__

사용되는 HTTP의 버전을 의미합니다.

기존에 버전 개념이 없던 HTTP가 개선되면서 이전과 차별화하기 위해 버전 개념이 생겼습니다.

- HTTP/0.9

  버전이 생기기 이전의 HTTP를 0.9로 정의합니다.

  버전 개념이 없었을 때의 통신규약이므로, 버전 정보가 따로 전송되지 않습니다.

  이 버전에서는 `GET` 메소드만 가능합니다.

  ```
  GET /mypage.html
  ```

  ```
  <HTML>
  A very simple HTML page
  </HTML>
  ```

  

- HTTP/1.0

  - 요청에 HTTP version이 추가되었습니다.

  - 응답에 상태코드가 추가되었습니다.
  - HTTP 헤더 개념이 추가되었습니다.
  - 헤더의 도움으로 HTML 파일 외 다른 문서를 전송할 수 있게 됩니다.

  ```
  GET /mypage.html HTTP/1.0
  User-Agent: NCSA_Mosaic/2.0 (Windows 3.1)
  ```

  ```
  200 OK
  Date: Tue, 15 Nov 1994 08:12:31 GMT
  Server: CERN/3.0 libwww/2.17
  Content-Type: text/html
  <HTML>
  A page with an image
    <IMG SRC="/myimage.gif">
  </HTML>
  
  ```

  

- HTTP/1.1

  `뭔소린지 모르겠음...`

  [HTTP의 진화 - HTTP | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP)

- HTTP/2



### headers

해당 request에 대한 추가정보를 담고있습니다.

`key: value` 형식입니다.

headers도 3부분으로 구분된다. (general headers, request headers, entity headers)

```
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Content-Length: 257
Host: google.com
User-Agent: HTTPie/0.9.3
```

__이하 요청을 보내는 쪽은 client, 받는쪽은 server로 정의합니다.__

- Host

  server의 host url 입니다.

- User-Agent

  client의 정보를 담고있습니다. (ex. 웹브라우저 정보: Mozilla/5.0)

- Accept

  client가 이해 가능한 컨텐츠 타입으로, 해당 타입의 response를 받기 원한다는 뜻입니다.

- Connection

  해당 요청이 끝난 후 client와 server가 계속해서 네트워크 커넥션을 유지할지를 선택합니다.

- Content-Type

  body의 타입입니다. (ex. JSON: application/json)

- Content-Length

  body의 길이입니다.

### body

request가 전달하려는 메시지가 담긴 부분입니다. (GET처럼 body가 없는 요청도 있습니다.)

## Response

응답 규약

### status line

response의 상태 정보를 담고있습니다.

__HTTP version__

HTTP 버전 정보

__Status code__

200: 성공

400: client error

500: server error

...

__Status text__

status code의 설명

404: Not Found



### headers

기본적으로 request의 header와 동일하지만, response에서만 사용되는 값들이 있다.

ex. User-Agent 대신 Server 헤더가 들어갑니다.

### body

기본적으로 request의 body와 동일합니다.

