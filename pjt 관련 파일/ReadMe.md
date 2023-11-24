# 🏦Bank Snap

💰 본 프로젝트는 **삼성 청년 SW 아카데미** 1학기 관통 프로젝트 결과물입니다



# 🏡Team '수길이네 금융마을'

사용자들이 금융을 더 쉽고, 편안하며, 가까이 느낄 수 있도록 하는 마음을 담아 "수길이네 금융마을" 이라는 웹페이지를 기획하게 되었습니다. 거부감 없이 접근할 수 있도록 단순한 고전 게임의 컨셉으로 웹 페이지를 디자인 하였고, 간단한 금융 퀴즈/ 카드 뉴스/ 금융 꿀팁을 통해 누구나 즐겁게 금융에 대해 배울수 있는 웹 페이지를 구현했습니다.



# 🎯 목표 구현사항

- 금융상품 데이터 기반 예금 및 적금 금리 비교 서비스 구성
- 환율 정보 API를 활용한 환율 계산 서비스 구성
- 지도 API를 활용한 은행 검색 서비스 구성
- 커뮤니티(게시판) 서비스 구성
- 서비스 관리 및 유지보수 목표
- 금융 퀴즈 게임 구현
- 금융 관련 뉴스/Tips 메인페이지 게시



# ⏰ 개발 일정

- 2023년 11월 16일 ~ 2023년 11월 23일 (8일)👋

![개발 일정 간트차트](C:\Users\SSAFY\Desktop\개발 일정 간트차트.png)

# **🤝 팀 구성 및 업무 분담 내역**

| 이름   | 담당 영역                                                    | Github                           |
| ------ | ------------------------------------------------------------ | -------------------------------- |
| 정종길 | ● 백엔드(Django), 프론트엔드(Vue)<br/>- 로그인 및 회원가입 기능<br/>- 커뮤니티 게시판 기능<br/>- 카카오 맵 은행 검색 기능<br/>- 금융 꿀팁 크롤링 및 금융 퀴즈 기능 | https://github.com/JeongJonggil/ |
| 박수빈 | ● 백엔드(Django), 프론트엔드(Vue)<br/>- 예금/적금 금리 비교 서비스<br/>- 환율 계산기 서비스<br/>- 금융 뉴스 크롤링<br/>- 홈페이지 디자인<br/>- 발표 | https://github.com/subin22643/   |

# 🛠️ 기술 스택

- #### 언어

  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=white"/><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>

- #### **프론트엔드**

  <img src="https://img.shields.io/badge/Vuetify-1867C0?style=flat&logo=vuetify&logoColor=white"/><img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white"/><img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white"/><img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white"/><img src="https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white"/><img src="https://img.shields.io/badge/pinia-orange?style=flat&logo=pinia&logoColor=white"><img src="https://img.shields.io/badge/Axios-5A29E4?style=flat&logo=axios&logoColor=white"/><img src="https://img.shields.io/badge/MicrosoftPowerPoint-B7472A?style=flat&logo=microsoftpowerpoint&logoColor=white"/>

- #### 백엔드

  <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white"/><img src="https://img.shields.io/badge/JSON-000000?style=flat&logo=json&logoColor=white"/>

- #### DB, ORM

  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white"/> 

- #### 협업 툴

  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"/><img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white"/><img src="https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white"/><img src="https://img.shields.io/badge/ReadMe-018EF5?style=flat&logo=readme&logoColor=white"/><img src="https://img.shields.io/badge/Mattermost-0058CC?style=flat&logo=Mattermost&logoColor=white"/>

- #### 사용 api

  <img src="https://img.shields.io/badge/Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white"><img src="https://img.shields.io/badge/한국수출입은행-darkblue?style=flat"><img src="https://img.shields.io/badge/NAVER-lightgreen?style=flat&logo=naver"><img src="https://img.shields.io/badge/금융감독원-skyblue?style=flat">



# 컴포넌트 구조

![수길이네 컴포넌트 구조](C:\Users\정종길\Desktop\진짜 pjt\pjt 관련 파일\수길이네 컴포넌트 구조.PNG)

# ERD

- 유저 - 게시판 - 댓글
- 유저 - Quiz model (하루에 퀴즈를 한 번만 풀 수 있도록 퀴즈를 푼 기록 저장)

![수길이네 ERD-1](C:\Users\SSAFY\Desktop\GitHUb\finalpjt\pjt 관련 파일\수길이네 ERD-1.PNG)

![수길이네 ERD-2](C:\Users\SSAFY\Desktop\GitHUb\finalpjt\pjt 관련 파일\수길이네 ERD-2.PNG)

### 🧾개발일지

|            | 정종길                                                       | 박수빈                                                       |
| :--------: | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 2023-11-16 | 프로젝트 컨셉 아이디어 회의 <br />- 프로젝트 구상, 컴포넌트 기획 및 제작 <br/> - 게시판/댓글 CRUD 기능 백엔드 코드 작성 | - 프로젝트 컨셉 아이디어 회의 <br />- 프로젝트 구상, 컴포넌트 기획 및 제작 <br />-  Auth(로그인 및 회원가입 등) 기능 백엔드 영역 코드 작성 |
| 2023-11-17 | - Auth 관련 기능 디버깅 및  프론트-백엔드 연결<br/>- 카카오 맵 키워드 검색 기능 구현 | - 카카오 맵, 금융상품 정보, 환율 API 테스트<br/>- 예/적금 상품 dB 저장, 전체 및 상세조회 기능 구현<br/> - 금융 상품 검색 기능 구현 |
| 2023-11-18 | - 게시판/댓글 CRUD 기능 디버깅 <br/>- 게시판/댓글 기능 프론트 - 백엔드 연결 | - 예/적금 금리 비교 페이지 디버깅 및 프론트-백엔드 연결<br/>- 환율 계산기 페이지 기능 구현 |
| 2023-11-19 | - 코드 병합(GitHub merge 작업)<br/>- Auth 관련 에러 메세지 출력 기능 추가 | - 코드 병합(GitHub merge 작업)<br/>- 메인 페이지 제작 및 금융 뉴스 기능 구현 |
| 2023-11-20 | - 중간 점검 및 계획 수정                                     | - 중간 점검 및 계획 수정                                     |
| 2023-11-21 | - 게시판 좋아요 기능 구현<br />- 카카오 맵 키워드 검색 결과 목록 화면 추가 | - MainView, 예적금, 환율 계산기 CSS 적용 <br/>- MainView 캐러셀 제작 |
| 2023-11-22 | - 금융 퀴즈 기능 구현<br/>- 홈페이지 디버깅 및 CSS 보완      | - 홈페이지 디버깅 및 CSS 보완                                |
| 2023-11-23 | - 코드 병합(GitHub merge 작업)<br />- Readme 작성 및 발표 ppt 작성<br />- 홈페이지 디버깅 및 CSS 보완 | - 코드 병합(GitHub merge 작업)<br />- Readme 작성 및 발표 ppt 작성<br />- 홈페이지 디버깅 및 CSS 보완 |
| 2023-11-24 | - 최종 점검 및 발표                                          | - 최종 점검 및 발표                                          |

### 🔥이슈 관리

| Name   | Content                                                      | **해결 여부**(Y/N) | **해결 과정**                                                |
| ------ | ------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| 정종길 | 커스텀한 User 모델에 dj-rest-auth 라이브러리 사용하여 회원 가입 시 dB에 저장이 안됨. | Y                  | serializers.py에  CustomRegisterSerializer, 및 adapter.py 코드 작성해서 dj-rest-auth 라이브러리 회원가입 로직 오버라이드 함 |
|        | 프로필 페이지 onMounted시 로그인 유저정보를 받아옴. 그런데 해당 유저 정보를 사용하려 하니 undefined로 출력됨. | Y                  | axios가 비동기 함수라 해당 작업이 완료되기 전에 const profileData = store.profileData 부분이 먼저 할당되어서 문제가 발생 하는거 같음. 그냥 다른 함수 로직으로 axios 요청하여 해결함 |
|        | 환경 변수 사용 시 settings.py 까지는 인식이 되는데 views.py에서 인식을 못함. | Y                  | settings.py에서 사용하는 환경 변수명을 대문자로 하니 해결됨  |
| 박수빈 | GitHub로 서로가 진행한 프로젝트를 merge하려 했으나 Conflict 발생. (파일이 사라지는 등 원본 파일이 보존 되지 않음) | Y                  | 서로의 프로젝트의 코드를 비교하며 로컬 환경에서 코드를 합침.<br />이후 merge과정 중 conflict 발생 시 원본파일을 보존하기 위해 개별 branch 추가 생성하여 별도 파일 관리. |
|        | 카카오맵 API 가이드에서 샘플 코드가 Vue3 문법이 아니라 적용이 잘 되지 않음. | Y                  | Vue3 공식문서를 통해 문법을 참고하여 샘플 코드의 문법을 바꿔서 사용함 |
|        | 프론트(vue)에서 axios를 통해 api에 응답 요청 시 corf 에러 발생. | Y                  | 일반적으로 백엔드 서버에서 api 요청하면 corf제약이 없음 → 백엔드 서버(django)에서 api요청을 통해 데이터를 받아온 후 프론트로 내려주어 해결함<br/>※ 프론트에서 요청 시 corf가 발생하는 곳도 있고 아닌 곳도 있음(youtube api는 프론트에서 처리 가능함). api 서버마다 다름 |

### 🪢서비스 구현

| No   | 구분              | 기능                                              | 구현 정도(⭐⭐⭐⭐⭐) |
| ---- | ----------------- | ------------------------------------------------- | ---------------- |
| 1    | 메인 페이지       | 메인페이지 레이아웃 및 디자인 CSS                 | ⭐⭐⭐⭐⭐            |
| 2    |                   | 오늘의 금융 퀴즈/뉴스/꿀팁                        | ⭐⭐⭐⭐⭐            |
| 4    | 회원 커스터마이징 | 회원가입 및 로그인/로그아웃                       | ⭐⭐⭐⭐             |
| 5    |                   | 로그인 상태에 따른 페이지 접근 및 권한 관리       | ⭐⭐⭐⭐⭐            |
| 6    |                   | 회원가입/로그인 정보 입력 오류시 에러 메시지 출력 | ⭐⭐⭐⭐             |
| 7    | 예/적금 금리 비교 | API를 활용한 금융 상품 정보 DB 저장               | ⭐⭐⭐⭐⭐            |
| 8    |                   | 예/적금 상품 조회<br />(카테고리별 검색)          | ⭐⭐⭐⭐⭐            |
| 9    |                   | 상품 상세 정보 페이지 출력                        | ⭐⭐⭐⭐⭐            |
| 10   |                   | 예/적금 관심상품 등록 기능                        | ⭐⭐⭐              |
| 12   | 환율 계산기       | API를 활용한 환율 정보 출력                       | ⭐⭐⭐⭐             |
| 13   |                   | 환율 계산기 기능 구현                             | ⭐⭐⭐⭐             |
| 14   | 근처 은행 검색    | API를 활용한 Kakao 맵 화면 구현                   | ⭐⭐⭐⭐⭐            |
| 15   |                   | 은행 위치 검색(카테고리별 검색)                   | ⭐⭐⭐⭐⭐            |
| 16   |                   | 검색 결과에 따른 장소 목록 표시                   | ⭐⭐⭐⭐⭐            |
| 17   | 커뮤니티(게시판)  | 게시글 및 댓글 CRUD                               | ⭐⭐⭐⭐⭐            |
| 18   |                   | 게시글 좋아요                                     | ⭐⭐⭐⭐⭐            |
| 19   |                   | 사용자 로그인 정보에 기반한 기능 제어             | ⭐⭐⭐⭐             |
| 20   | 프로필            | 회원 프로필 수정 (기본 정보 수정)                 | ⭐⭐⭐⭐⭐            |
| 21   |                   | 비밀번호 변경 및 회원 탈퇴                        | ⭐⭐⭐⭐⭐            |
| 22   |                   | 개인별 상품 추천 알고리즘                         | 미구현           |

### 🍀 배운점 및 느낀점

- 정종길

프로젝트를 진행하기 전 열정과 근거 없는 자신감으로 가득 찼었습니다. 그러나 프로젝트 시작과 동시에 django 가상환경 활성화 명령어가 기억나지 않는 것을 시작으로 쉽지않은 나날을 보낸 것 같습니다. 프로젝트 기간동안 에러와 가장 많은 시간을 함께하며, 때로는 밉기도하고 가끔은 고맙기도 하고 정이 많이 들었습니다. 덕분에 에러 발생 시 추측보다는 에러 메시지를 꼼꼼히 확인하는 습관이 생겼고 디버깅에 대한 감각도 많이 늘은 것 같습니다. 또한, Chatgpt를 사용하면서 코드를 하나씩 작성하고 문법에 집중하기 보다 앞으로는 코드의 흐름을 이해하고 작성된 코드를 바탕으로 커스텀하는 능력을 길러야겠다는 생각이 들었습니다. 프로젝트 중간 어지럽혀져 있는 파일과 코드 조각들을 보며 설계 단계의 중요성을 느끼게 되었고, 이번 프로젝트 경험을 바탕으로 부족한 점들을 보완하여 다음 프로젝트에서는 진행방향과 완성도 높은 결과물을 만들 수 있을거라 믿어 의심치 않습니다 . 끝으로, 프로젝트 기간동안 짜증도 많이내고 한숨도 많이 쉬었지만, 옆에서 힘든 내색 없이 끝까지 열심히 해준 페어 박수빈양에게 고맙고 정말 수고했다는 얘기를 전하고 싶습니다. 

- 박수빈

첫 프로젝트라 계획도 없이 막무가내로 기능 구현부터 시작했습니다. 초기 기획이 부족하니 구조가 이상해서 다 갈아엎기도 하고, 열심히 구현해놨던 기능이 필요 없어져서 삭제하기도 했습니다. 기획과 설계의 중요성을 깨닳았습니다. 또 에러를 많이 보다 보니 코드 작성도 중요하지만 디버깅에 더욱 집중하게 되었습니다. 공식문서를 많이 참고하는 습관이 생겼고 에러 메세지를 더 잘 파악할 수 있게 되었습니다. 개인 학습에서는 코드 구현에 집중했다면, 이번 프로젝트를 통해서 기획, 디자인, 서비스 등 사용자 입장에서 더욱 넓은 시야로 볼 수 있게 되었습니다. 처음으로 제 손으로 결과물을 만들어보니 뿌듯하기도 했고, 하고싶었던 것들을 더 구현해내지 못해서 아쉽기도 했습니다. 이번 프로젝트에서 배우고 느낀점들을 토대로 다음에는 더 만족스러운 결과물을 내고 싶습니다. 처음하는 프로젝트라 많이 힘들어했는데 옆에서 이해해주고 많이 응원해준 팀원에게 고맙다는 얘기를 전하고 싶습니다. 덕분에 프로젝트 기간 동안 즐겁게 개발할 수 있었습니다. 

​	- 복습 열심히 (코드 작성보다는 개념 이해 위주로)

​	- 초기 기획부터 (방향, 기능, 화면 구성에 대한 고민 / 사용자 중심으로)

​	- 앱 이름, 변수명 적절히
