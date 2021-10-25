# Django

## Mixin

> class에 부가적인 기능이나 정보를 추가해주기 위한 모듈로, 다중 상속과 유사한 개념입니다.



```python
class FirstMixin:
    pass

class SecondMixin:
    pass

class Parent:
    pass

class Child(FirstMixin, SecondMixin, Parent):
    pass
```

* child class가 Parant로부터 상속받고있고, FirstMixin, SecondMixin의 기능을 추가로 확장하고 있습니다.





## Generic View

> Django에서 미리 만들어놓은 범용적인 view의 형태.
>
> 이를 활용하여 더욱 빠르게 개발할 수 있습니다.

### Generic View의 종류

1. Base View
   - View: 최상위에 있는 부모 제네릭 뷰 클래스
   - TemplateView: 











(주)서큘러스

임베디드 개발자(Python)

https://github.com/themakerrobot/openpibo-python

교육용 로봇 'PIBO'의 라이브러리 및 툴 개발 업무를 수행했습니다.
PIBO는 Raspberry Pi와 atmega328p를 베이스로 로봇을 제어합니다.



교육용 로봇 라이브러리 사용 가이드 공식문서 제작

교육자 및 피교육자(중학생 이상)를 대상으로 서비스 공식 가이드 작성하였습니다.
- link: https://themakerrobot.github.io/openpibo-python/build/html/index.html
- 기술: shpinx, github pages



교육용 로봇 라이브러리 툴 개발

로봇 사용에 도움이 되는 각종 편의 툴을 개발했습니다. (모션 제작기, 프로세스 검사기 등)
- link: https://github.com/themakerrobot/openpibo-tools
- 기술: python, flask, jquery



교육용 로봇 라이브러리 패키지화

디렉토리 재구성 및 라이브러리 패키지화 등을 통해 서비스 사용성을 개선했습니다.
- link(패키지화 전): https://github.com/themakerrobot/openpibo
- link(패키지화 후): https://github.com/themakerrobot/openpibo-python