# 챗봇 만들기 
------
## 카카오 오픈 빌더 연동
### 1. 구름 IDE Flask 도커 만들기
### 2. 카카오 오픈빌더  
 1) 봇생성
 2) 스킬생성 : Flask 서버의 JSON형태로 데이터를 주고 받을 주소지정
 3) 시나리오 > 블록추가 > 봇응답 > 스킬데이터 

------
## KoNLPy(코엔엘파이)
### 설치 
* 참고 사이트 : https://hogni.tistory.com/39
0) JDK 설치 후 경로 설정 
1) pip upgrade : pip install --upgrade pip 
2) JPype1 설치
* Python 에서 JVM 을 띄운 뒤, 서로 통신을 하는 라이브러리
* JPype 설치 : pip install JPype1-1.2.0-cp38-cp38-win_amd64.whl
  + JPype 다운로드 사이트 : https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
  + 오류시 참고 사이트 : http://blog.naver.com/PostView.nhn?blogId=kdj0876&logNo=222259132909&parentCategoryNo=&categoryNo=90&viewDate=&isShowPopularPosts=true&from=search
3) KoNLPy 패키지 설치 : pip install konlpy
 
------
## Vscode 가상환경 생성
1. 터미널 모드 실행 : python -m venv chatenv
* 참고 사이트 : https://mr-spock.tistory.com/19
2. 가상환경 선택 : [ Ctrl + Shift + P ] 키를 눌러 ">select Interpreter"를 검색 후 가상 환경을 선택
3. 기존에 열려있던 터미널 창을 닫고, 다시 터미널 창을 열어 줌
* 가상환경이 열리지 않는 경우는 powershell을 관리자 권한으로 권한 변경해야 함(변경후 터미널 재실행)
  + Set-ExecutionPolicy RemoteSigned 명령실행 후 A로 권한 변경후 Get-ExecutionPolicy 확인 
  + 참고 사이트 : https://jy-tblog.tistory.com/8

## VScode Git 
0.로컬 저장소에서 git config
  * git config --global user.email "user@email.com"
  * git config --global user.name "username"
1. 원격 저장소와 로컬 저장소 연결 : ctrl+shift+p git clone 원격저장소 주소
* 참고 사이트 : https://technote.kr/352
2. add(staging) -> commit -> push 
* 참고 사이트 : https://dev-youngjun.tistory.com/7
