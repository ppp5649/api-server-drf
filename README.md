## DRF로 구현한 REST API Server

### 개발 환경
+ Language : Python 3.10.9
+ Framework : Django 4.1.4 / djangorestframework 3.14.0
+ Database : MySQL 5.7.40
+ Test tool : Postman
+ Code Formatter : Black
-------------

### ERD
![user_erd](https://user-images.githubusercontent.com/59691376/210050578-c35ad427-bf75-48c6-b9dd-0b42a65e44b0.png)

-------------
### 기능

#### 유저
+ 회원가입 / 로그인 / 로그아웃
+ 유저 조회
+ 비밀번호 변경 및 초기화
+ 토큰 재발급

#### 가계부
+ 금액과 메모 생성, 조회, 수정, 삭제
+ 로그인되지 않은 사용자는 가계부 접근 제한
+ 작성자 본인만 가계부 수정, 삭제 가능 
-------------
### 주요 기능 API 테스트

+ 회원가입
  + Endpoint : /users/registration/ (POST)
  + HTTP Status Code : 201 (Created)
<img width="635" alt="회원가입" src="https://user-images.githubusercontent.com/59691376/210053093-ad1b2256-62c5-4293-a4c5-ceeeecb1f469.PNG">


+ 로그인
  + Endpoint : /users/login/ (POST)
  + HTTP Status Code : 200 (OK)
<img width="637" alt="로그인" src="https://user-images.githubusercontent.com/59691376/210053442-7a062a20-284b-4422-bc8b-d3fc89cbcaa0.PNG">


+ 가계부 생성
  + Endpoint : /post/ (POST)
  + HTTP Status Code : 401 (Created)
<img width="636" alt="가계부 생성" src="https://user-images.githubusercontent.com/59691376/210053626-ee1d548a-187a-44a7-a1c8-4929f752869e.PNG">


+ 가계부 조회 (로그인 하지 않은 사용자)
  + Endpoint : /post/6/ (GET)
  + HTTP Status Code : 401 (Unauthorized)
<img width="636" alt="로그인X 가계부 조회" src="https://user-images.githubusercontent.com/59691376/210053604-e4448f0e-39cf-4246-8be2-be73ea4b22f1.PNG">


+ 가계부 수정 (작성자 본인)
  + Endpoint : /post/6/ (PUT)
  + HTTP Status Code : 200 (OK)
<img width="635" alt="본인 가계부 수정" src="https://user-images.githubusercontent.com/59691376/210053644-af350639-cf72-4e75-b36f-609c68af9d0f.PNG">
  

+ 가계부 삭제 (작성자 본인 X)
  + Endpoint : /post/3/ (DELETE)
  + HTTP Status Code : 403 (Forbidden)
<img width="636" alt="타인 가계부 삭제" src="https://user-images.githubusercontent.com/59691376/210053660-5ae4189b-d32c-47a2-930c-4497cae3ae1d.PNG">
