# Git

> Git은 분산 버전 관이 시스템(DVCS)이다.
>
> 소스코드의 버전 및 이력을 관리할 수 있다.



## 준비사항

윈도우에서 `git`을 활용하기 위해서는 `git bash`가 필요하다.

git을 활용할 때 GUI기반 퉁들도 존재한다.(ex-`seurcetree`)

설치를 완료한 뒤엔 `author`정보를 입력한다.

```bash
$ git config --global user.name "User Name"
$ git config --global user.email "User Email"

$ git config --global --list
user.name=Jinpyo Hong
user.email=hojp7874@gmail.com
```



## 로컬 저장소(Local Repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init

Initialized existing Git repository in C:/Users/hojp7/Desktop/ssafy/TIL/.git/
```

- 저장소를 초기화하면, `.git`이라는 폴더가 생성된다. 여기에 git과 관련된 모든 정보가 들어간다.
- git bash에 `(master)`라고 표기되는데, 이는 현재 `master` 브랜치에 있다는 것을 의미한다.



### 2. `add`

작업공간(work directory)에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`라는 공간으로 이동시켜야 한다.

```bash
$ git add . # 현재 디랜토리의 모든 파일
$ git add a.txt # 특정 파일
$ git add assets/ # 특정 폴더
```



`add`하기 전 상태

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        startcamp/git_basic.md

nothing added to commit but untracked files present (use "git add" to track)
```



`add`후 상태

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   startcamp/git_basic.md
```



### 3. Commit

commit은 이력을 확정짓는 명령어다. 해당 시점에서 스냅샷을 찍는다.

commit을 할 땐은 반드시 메시지를 입력해야 한다. 메시지는 변경사항에 대한 정확한 내용을 파악할 수 있게끔 작성한다.

```bash
$ git commit -m "git_basic.txt 파일 주가"
[master a1124b2] git_basic.txt ?뚯씪 二쇨?
 1 file changed, 158 insertions(+)
 create mode 100644 startcamp/git_basic.md
```



지금까지 작성한 이력들을 확인하기 위해 `git log` 명령어를 사용할 수 있다.

```bash
$ git log
commit a1124b2576a00ee884def9a2f03e4919038ef93c (HEAD -> master)
Author: User Name <User Email>
Date:   Fri Jul 17 15:24:32 2020 +0900

    git_basic.txt 파일 주가
```



## 원격 저장소(Remote Repository)활용하기

원격 저장소를 제공하는 서비스는 여러 종류가 있지만, 대표적인 Github를 기준으로 작성한다.



### 준비사항

- Github에 저장소 생성



### 원격 저장소 등록

```bash
$ git remote add origin 저장소URL
```

- 원격 저장소 `remote`로 `origin`이라는 이름으로 `저장소URL`을 추가`add`한다.

- 등록된 원격 저장소 현황을 확인하기 위해서 `git remote-v`명령어를 실행한다.



### 원격 저장소에 업로드 (`push`)

```bash 
$ git push origin master
```

- origin이라는 이름으로 설정된 저장소 UTL로 `master`브랜치를 업로드(`push`)한다.
- 이후 수정사항이 발생할 때마다 `add`, `commit`, `push`작업을 수행한다.



**항상 모든 명령어 입력할때마다 관련 상태를 확인하는 습관을 기르자!**

`git status`, `git remote -v`, `git log`

