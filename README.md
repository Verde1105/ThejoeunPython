# ThejoeunPython

# Python 과정 정보

- dhsdad@naver.com

- 설문
1. 본인 이름, 핸드폰 번호
2. 본인 중장기 목표 및 계획
3. 대학 및 전공
4. 경력(분야,년수)
5. mbti
6. 요청사항

- 강사 정보
    - 손형진
    - 010-2895-5017

---
# Github Commit 순서
1. 깃 초기화
```
git init
```
2. 깃 `연동`, `등록`
```
git remote add origin <주소>
```
- 2.1 아래 메시지가 뜬 경우
```
fatal: detected dubious ownership in repository at 'E:/Workspace/Thejoeun'
'E:/Workspace/Thejoeun' is on a file system that does not record ownership
To add an exception for this directory, call:

        git config --global --add safe.directory E:/Workspace/Thejoeun
```
- 그냥 복사해서 실행하면 됨
```
git config --global --add safe.directory E:/Workspace/Thejoeun
```
3. 깃 `연동` 확인
```
git remote -v
```
- 3.1 쳣는데 아무것도 안뜨면 `연동` 다시 해야됨
- 3.2 등록된 결과
```
origin  https://github.com/Verde1105/ThejoeunPython.git (fetch)
origin  https://github.com/Verde1105/ThejoeunPython.git (push)
```

---
---
4. add 전 해야할 사항!
- pull 명령어를 통해 레포지토리의 파일을 받아준다.
```
git pull origin master
```

4. 커밋할 파일 추가, . = 모든것
```
git add .
``` 
5. 커밋 메시지 추가
```
git commit -m "추가할 메세지 입력"
```
- 5.1 아래와 같은 결과가 출력된 경우
```
E:\Workspace\Thejoeun>git commit -m "파이썬첫날"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'verde@DESKTOP-UT4BDSN.(none)')
```
- 5.2 내가 누구인지 `명시`가 안된것이므로 `명시`를 한다.
- 5.3 아래에 있는 명령어를 실행시켜주면 해결된다.
```
git config --global user.email "lunaflo@naver.com"
git config --global user.name "Verde1105"
```

6. 깃허브에 푸쉬
```
git push origin master
```

- 6.1 아래와 같은 에러가 발생한 경우
```
error: src refspec master does not match any
```
- 6.2 똑같은 이름의 브랜치를 생성 후 switch를 한다.
```
git checkout -b 'master'
```
- 6.3 다시 push 명령어 진행