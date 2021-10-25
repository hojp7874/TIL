# ERROR

[TOC]

### SSL 인증서

err code:

```
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] ...
```

파이썬에서 https로 된 사이트에 요청을 보낼 때 이러한 에러가 발생한다.



원인:

`PEP 467`이 개정되면서 모든 https 통신은 필요한 인증서와 호스트명을 기본으로 체크해야한다.

기존의 라이브러리 `urllib`, `urllib2`, `http`, `httplib` 는 이러한 처리가 안되어있어서 에러가 발생한다.



해결방법:

import ssl

`ssl._ create_unverified_context()`를 `urllib.request.urlopen`의 파라미터로 넘겨주면 된다.

```
context = ssl._create_unverified_context()
response = urllib.request.urlopen(requests, data=data.encode('utf-8'), context=context)
```

