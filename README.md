## DRF로 구현한 REST API Server
![MySQL 장고 이미지](https://user-images.githubusercontent.com/59691376/210086551-9b4516d9-2e14-41ea-ae6f-0608e064b576.png)

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
### 구현 과정
#### User Model 설계  
유저에게 필요한 Field들을 판단한 후 추가해주었고 코드의 재사용성을 높이기 위해 AbstractBaseUser를   
상속받아 커스텀 유저 모델을 구현함

#### MySQL 연동 및 마이그레이션  
mysqlclient를 이용하여 MySQL을 연동하였고 마이그레이션을 통해 설계 해놓은 User Model을 MySQL Table로 생성함

#### 회원가입 / 로그인 / 로그아웃 구현 (JWT Token 인증)  
JWT Token을 이용한 유저 인증을 간단하게 구현하기 위해 dj-rest-auth와 simplejwt를 사용하였음  
(기본적으로 제공하는 기능이 많기 때문에 빠르게 개발할 수 있다고 판단함)

#### Post Model 설계  
요구 조건에 맞게 가계부를 작성하는데 필요한 Field들을 판단한 후 추가해주었음
 
#### PostViewSet 클래스 구현 (가계부 views.py)  
CRUD가 한꺼번에 지원되는 ModelViewSet을 활용하여 PostViewSet 클래스를 구현함

#### PostViewSet에 권한 및 인증 추가  
GET Method(조회)인 경우를 제외하고 가계부 작성자 본인이 아니라면 접근 권한을 갖지 못하도록 설정함 (permissions.py)
또한, 기존에 로그인에 사용됐던 JWT Token 인증을 활용하여 로그인되지 않은 사용자는 가계부에 접근하지 못하도록 설정함

---------

### 주요 기능 API 테스트

+ 회원가입
  + Endpoint : /users/registration/
  + HTTP Method : POST
  + HTTP Status Code : 201 (Created)
<img width="635" alt="회원가입" src="https://user-images.githubusercontent.com/59691376/210053093-ad1b2256-62c5-4293-a4c5-ceeeecb1f469.PNG">


+ 로그인
  + Endpoint : /users/login/
  + HTTP Method : POST
  + HTTP Status Code : 200 (OK)
<img width="637" alt="로그인" src="https://user-images.githubusercontent.com/59691376/210053442-7a062a20-284b-4422-bc8b-d3fc89cbcaa0.PNG">


+ 가계부 생성
  + Endpoint : /post/
  + HTTP Method : POST
  + HTTP Status Code : 201 (Created)
<img width="636" alt="가계부 생성" src="https://user-images.githubusercontent.com/59691376/210053626-ee1d548a-187a-44a7-a1c8-4929f752869e.PNG">


+ 가계부 조회 (로그인 하지 않은 사용자)
  + Endpoint : /post/6/
  + HTTP Method : GET
  + HTTP Status Code : 401 (Unauthorized)
<img width="636" alt="로그인X 가계부 조회" src="https://user-images.githubusercontent.com/59691376/210053604-e4448f0e-39cf-4246-8be2-be73ea4b22f1.PNG">


+ 가계부 수정 (작성자 본인)
  + Endpoint : /post/6/
  + HTTP Method : PUT
  + HTTP Status Code : 200 (OK)
<img width="635" alt="본인 가계부 수정" src="https://user-images.githubusercontent.com/59691376/210053644-af350639-cf72-4e75-b36f-609c68af9d0f.PNG">
  

+ 가계부 삭제 (작성자 본인 X)
  + Endpoint : /post/3/
  + HTTP Method : DELETE
  + HTTP Status Code : 403 (Forbidden)
<img width="636" alt="타인 가계부 삭제" src="https://user-images.githubusercontent.com/59691376/210053660-5ae4189b-d32c-47a2-930c-4497cae3ae1d.PNG">

-------------
