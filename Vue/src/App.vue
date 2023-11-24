<template>
  <div class="full-width">
    <img :src="sky" alt="하늘" :style="{ height: '50px', width: '100%'}">
  </div>
  <div class="main-container">
    <nav class="navbar navbar-expand navbar-light bg-light">
      <RouterLink class="navbar-brand" :to="{ name: 'main' }">
        <img class="logo-image" :src="logoImage" alt="로고">
        <img class="logo-text" :src="logoText" alt="로고">
      </RouterLink>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav text-center w-100">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'search' }">조회</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'exchange' }">환율 계산기</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'map' }">지도</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'BoardView' }">게시판</RouterLink>
          </li>
        </ul>
          <div class="user ml-auto">
            <template v-if="!store.isLogin">
              <div class="navbar-nav">
                </div>
                <RouterLink :to="{ name:'LogIn' }" class="nav-item nav-link">로그인</RouterLink>
                <RouterLink :to="{ name:'SignUp' }" class="nav-item nav-link">회원가입</RouterLink>          
            </template>
            <template v-else>
              <div class="navbar-nav">
                <div class="user-container"><p class="nav-item nav-link">{{ store.loginUserNickname }}님 환영합니다!</p>
                    <div class="nav-icons">
                      <RouterLink :to="{ name:'Profile' }" class="nav-item nav-link"><img :src="profile" alt="profile" class="nav-img"></RouterLink>
                      <RouterLink :to="{ name:'Cart' }" class="nav-item nav-link"><img :src="cart" alt="cart" class="nav-img"></RouterLink>
                      <a class="nav-item nav-link" href="#" @click="logOut"><img :src="logout" alt="logout" class="nav-img"></a>
                    </div>
                </div>
              </div>
            </template>
        </div>
      </div>
    </nav>
    <div class="router-view-container">
      <button class="nav-item nav-link back" @click="goBack"> ← 뒤로 가기</button>
      <RouterView/>
    </div>
  </div>
  <footer class="footer">
    <p class="text"><a href="https://github.com/JeongJonggil"><img :src="jonggil" alt="종길" :style="{ height: '30px', width: '30px'}"> JeongJonggil</a>
       & 
       <a href="https://github.com/subin22643">ParkSubin <img :src="subin" alt="수빈" :style="{ height: '30px', width: '30px', margintop:'10px'}"></a></p>
       <img :src="bottom" alt="바닥" class="full-width-image">
  </footer>
</template>


<script setup>
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  import { useUserStore } from '@/stores/user';
  import logoImage from '@/assets/로고 그림만.png'
  import logoText from '@/assets/로고 글자집.png'
  import bottom from '@/assets/바닥2.png'
  import sky from '@/assets/하늘5.png'
  import profile from '@/assets/person.png'
  import cart from '@/assets/cart4.png'
  import logout from '@/assets/logout.png'
  import jonggil from '@/assets/종길로고.png'
  import subin from '@/assets/수빈보정로고.png'
  
  const store = useUserStore()
  const router = useRouter()
  const logOut = function () {
    store.logOut()
  }

  const goBack = function () {
    router.back()
  }

</script>


<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Gothic:wght@400;700;800&display=swap');



.navbar {
  position: sticky; /* 네비게이션 바를 스크롤에 따라 상단에 고정 */
  top: 0; /* 상단에 고정되는 지점 설정 */
  z-index: 1020; /* 부트스트랩 z-index 범위 안에서 상위에 위치 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
  font-weight: bold;
  color: #007bff; /* 메인 브랜드 컬러 */
}

.navbar-brand:hover {
  color: #0056b3; /* 호버 효과를 위한 약간 어두운 색상 */
}

.navbar-nav .nav-link {
    margin-right: 20px; /* 원하는 여백 크기로 조정 */
}

.nav-link {
  color: #495057; /* 네비게이션 링크 컬러 */
  font-family: 'Black Han Sans', sans-serif;
  font-size: 40px;
}

.nav-link:hover {
  color: brown; /* 호버 효과를 위한 메인 브랜드 컬러 */
}

.nav-item {
  color: black;
  font-family: 'Nanum Gothic', sans-serif;
  font-size: 20px;
  margin-right: 10px;
}


.router-view-container {
  padding: 20px;
  margin-top: 20px;
  background-color: #f8f9fa; /* 연한 배경색 */
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
}


.user-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 0px;
  margin-top: -10px;
  white-space: nowrap;
}


.nav-icons {
  display: flex;
  justify-content: space-around; /* 아이콘들을 가운데 정렬합니다. */
  margin-top: -30px;
}

.nav-icons .nav-item {
  margin: 0px; /* 좌우 마진을 10px로 조정합니다. */
}

.text {
  color: #000;
  text-align: center;
  font-feature-settings: 'clig' off, 'liga' off;
  font-family: Inter;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  line-height: 130%; /* 20.8px */
}

.footer {
  background-color: #f5f5f5;
  text-align: center;
  width: 100%;
  height: 5%;
  bottom: 0px;
}

.footer a {
  color: black;       /* 링크 색상을 검정색으로 설정 */
  text-decoration: none; /* 밑줄 없애기 */
}

.logo-image {
  margin-left: 20px;
  width: 60px;
  height: 60px;

}

.logo-text {
  margin-left: 10px;
  width: 160px;
  height: 96px;
  margin-top: -10px;
}


footer > img {
  height: 50px;
  width: 100%;
}


.user {
  display: flex;
  flex-direction: row;
  align-items: center; 
  justify-content: flex-end;
  margin-right: 1rem; 
  white-space: nowrap;
}


.main-container {
  min-height: 90.7vh;
  max-width: 85%;
  margin: 0 auto;
}

* {
  font-family: 'Noto Sans KR', sans-serif;
}


.full-width-image {
  width: 100%;
}

.full-width-image {
  width: 100%;
  height: auto; /* 비율을 유지하기 위해 자동으로 설정합니다. */
}

.nav-img {
  width: 40px;
  height: 40px;
}

.back {
  font-size: 0.8em;
  color: #004aad;
  background-color: #ffffff;
  border: 4px solid #004aad;
  border-radius: 0;
  padding: 5px 10px;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
  transition: filter 0.3s;
  box-shadow: 0 0 0;
  margin-top: -20px; /* 뒤로가기 버튼을 위로 이동 */
  margin-bottom: 30px;
}

.back:hover {
  filter: brightness(0.9);
}
</style>