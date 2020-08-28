# 01_django_model

### CharField(max_length=None)

- 길이에 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수인자
- 필드의 최대길이, 데이터베이스와 django의 유효성 검사에서 사용

### TextField()

- 글자의 수가 많을 때 사용

### DateTimeField()

- 최초 생성 일자: auto_now_add = True
  - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
  - 테이블에 어떤 데이터를 최초로 넣을 때
- 최종 수정 일자: `auto_now=True`
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

---

## Migrations

### makemogrations

- 모델을 변결한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
- 모델을 활성화 하기 전에 DB 설계도를 작성
- 생성된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라고 생각



### migrate

- 작성된 마이그레이션 파일들을 기반으로 실제 DB에 반영
- db.sqlite3 라는 데이터베이스 파일에 테이블을 생성
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸



### sqlmigrate

- 해당 마이그레이션 파일이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인하기 위한 명령어



### showmigrations

- 마이그레이션 파일들의 migrate 여부를 확인하기 위한 명령어



### Model의 중요 3단계

1. models.py: 변경사항 (작성, 수정, 삭제 등) 발생
2. makemigrations: 설계도 만들기
3. migrate: DB에 적용