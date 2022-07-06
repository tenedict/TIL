# Git

### git이란?

- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율

#### 즉 우리가 버전을 여러개를 만들어 관리가 가능함

##### Git은 파일을 modified, staged, committed로 관리

- **modified** : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
- **staged** : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)
- **committed** : 커밋이 된 상태



##  GIT의 기본 명령어 

**$git init**

- 로컬 저장소 생성

**$ git log**

- 저장소의 커밋 조회

**$git status**

- 파일의 상태를 확인하기 위하여 활용

**$git add**

- 파일이나 폴더를 스테이지로 올림

**$git commit -m'(커밋메세지)'**

- 버전 기록

####  사용자 정보는 커밋하기 위해 반드시 필요

- git config —global user.name “username”

- git config —global user.email “my@email.com”

- 설정 확인을 위해 git config 뒤 `  -l ,  —global -l, git config user.name '`으로 확인 가능

  







