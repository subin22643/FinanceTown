

<body>
<img src="header_photo.png" alt="배너 그림" />
</body>



[TOC]






# Bank Snap🏦

💰 본 프로젝트는 **삼성 청년 SW 아카데미** 1학기 관통 프로젝트 결과물입니다

​	<br>	<br>



## **개요🌱**

- 금융상품정보 웹 애플리케이션
- 예적금상품조회, 금융상품추천, 환율계산, 은행 검색, 커뮤니티 기능을 제공
- 

​	<br>	<br>

## Team 😀

​	<br>	<br>



## 프로젝트 기간💞️

- 2023년 11월 14일 ~ 2023년 11월 24일 (11일)👋


  ### 일정

  | 일시      | 진행내용                                                     | 특이사항                                                     | 비고                                                         |
  | :-------- | ------------------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | 11/14(화) | 1. 카카오맵 api를 이용한 은행 위치 검색 기능 구현<br />2. 수출입은행 api를 통해 환율계산기능 구현<br />3. vue 컴포넌트 구성 <br />4. 프로젝트 레포 생성 | 1-1. XX+은행으로 검색하는 알고리즘(초기값 명지) <br />2-1. 환율계산기의 양방향 숫자 기입 기능의 문제<br />3-1 . 컴포넌트와 뷰의 기능의 차이에 대한 고찰<br />4-1. git desktop 이용 | 1-1-1. 필요시 변경예정<br />**1-1-2. 브라우저의 네비게이션 기능을 이용하라는 조언**<br />2-1-1. 한쪽에는 숫자를 기입, 다른쪽은 숫자 출력으로 기능 변경<br />3-1-1. (자료를 참고하자) |
  | 11/15(수) | 1. 프로젝트 명, 프로젝트 로고 선정<br />2. 커뮤니티 페이지 구현(CRUD)<br />3. 회원가입, 로그인 기능 구현<br />4. 상단 바 네비게이션 구성 | <br />2-1. 커뮤니티의 게시글 수정 문제<br />3-1. 로그인기능구현 - 토큰을 통해 권한을 주는 동작이 정상작동을 하지 않았다<br /> | <br /><br />3-1-1. 코드에 오타가 있었다.                     |
  | 11/16(목) | 1. readme 초기안 작성<br />2. DB구조 설계<br />3. 금감원api를 통해 은행 상품 정보 불러오기<br />4. 메인페이지 내용 설정<br />5. 전역범위 css 수정 | <br />2-1. 회원정보와 은행정보를 얼마나 나눠야할지 고민<br />2-2. 예적금 상품을 연결한 키 설정<br />3-1. 상품정보란 하위에 예금, 적금을 넣을 지 고민<br />4-1. 메인페이지에 경제관련 뉴스<br />5-1. 네비게이션바 상단 고정, 페이지 화면 범위 수정 | <br />2-1-1. 회원정보<br />2-2-1. 상품키와 예치기간을 기준으로 연결<br /><br />4-1-1. 네이버검색 API 이용 |
  | 11/17(금) | 1. 메인페이지 naver api 통해 경제뉴스<br />~~2. user테이블 구조 수정~~<br />3. 은행상품데이터 출력<br />4. 환율계산기, 금리비교, 메인페이지 디자인 수정<br />5. 은행찾기 지역별 검색으로 수정<br /> | 1-1. api 요청에서 오류가 있었다.<br />1-2. 메인페이지 내용추가가 필요<br /><br />3-1. DB내용 재설정<br />3-2. 18시 이후 API서버 점검예정<br />4-1. 조금씩 나아지는 중 | 1-1-1. 코드리뷰 3시간만에 찾아낸 오류 : 두가지 코드 중 하나에 키 값이 누락되었다....<br /><br />1-2-1. 사진자료 등을 추가<br /><br />3-1-1. 은행상품 데이터에서 은행명은 외래키로 받아오는 것으로 변경<br />3-2-1. json파일로 데이터 저장하여 사용 |
  | 11/18(토) | 1. 로그인 인증권한 수정 <br />2. 마이페이지 공부하기 <br />3. 금융상품 상세페이지 <br />4. bootstrap 템플릿 적용하기<br />5. 계산 파일 수정 | <br />2-1.  6주차 프로젝트 자료 참고<br />2-2. 작성게시글 및 댓글 불러왔다 참좋았다.<br />4-1.  UI 구현하는 작업<br />5-1. 시간을 금요일 날짜로 고정 시켜둠 | <br /><br /><br />4-1-1. 기능이 구현된 코드위에 디자인을 입히는 작업이 어려웠다.<br />5-1-1. 주말에는 환율자료를 받아오지못해서 조정이 필요했다. |
  | 11/19(일) | 1. 관심상품 등록 기능 추가<br />2. 마이페이지 기능 구현      | 1-1. 버튼 누를 시에 마이페이지에 상품 추가<br /> 2-1. 마이페이지로 인해 메인페이지 로딩이 안됐어요 ㅠㅜㅠㅠㅠ<br /> | 1-1-1.<br />2-1-1. 기존에 등록된 사용자 (가져올 데이터가 없거나) or 등록되지 않은 사용자<br /> |
  | 11/20(월) |                                                              |                                                              |                                                              |
  | 11/21(화) |                                                              |                                                              |                                                              |
  | 11/22(수) |                                                              |                                                              |                                                              |
  | 11/23(목) | 발표자료 구성                                                |                                                              |                                                              |
  | 11/24(금) | 발표!!!!                                                     |                                                              |                                                              |

  <br><br>


## 개발 환경 👀

<p align="center">
  <img src="https://img.shields.io/badge/API-Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white"> 
  <img src="https://img.shields.io/badge/API-한국수출입은행-darkblue?style=flat">
  <img src="https://img.shields.io/badge/API-금융감독원-skyblue?style=flat">
  <img src="https://img.shields.io/badge/API-NAVER-lightgreen?style=flat&logo=naver">
  <img src="https://img.shields.io/badge/Language-Python-007396?style=flat&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/Language-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=white"> 
  <img src="https://img.shields.io/badge/Database-Sqlite-green?style=flat&logo=sqlite&logoColor=white"> 
  <img src="https://img.shields.io/badge/Framework-django-darkgreen?style=flat&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/Framework-Vue-D22128?style=flat&logo=vue.js&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Bootstrap-purple?style=flat&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/Library-pinia-orange?style=flat&logo=pinia&logoColor=white">
</p>


```markdown
python: 3.9.13

JavaScript: es6++??

Sqlite: <- 플러그인으로 쓰는데??

Django: 4.2.7

djangorestframework: 3.14.0

Vite: 4.4.11 <-툴인데??

Vue: 4.4.0

bootstrap: 5.3.1

pinia: 2.1.7 

기술스택을 작성하는 법을 보고 수정을 하자
```



​	<br>	<br>	


## 협업 툴 👊

- Notion

- Mattermost

- github

  <br><br>



## ERD

![DB구조](doc\구조\DB.png)

  <br> <br>


## 주요기능



## ~~아키텍쳐 👨‍💻 수정이 필요합니다ㅠㅠ!~~ 

[![TechArchitecture](https://user-images.githubusercontent.com/53832553/154430527-09bd19d6-993f-4dc0-ae4f-5a5e77220055.png)](https://user-images.githubusercontent.com/53832553/154430527-09bd19d6-993f-4dc0-ae4f-5a5e77220055.png)

​	<br>	<br>
