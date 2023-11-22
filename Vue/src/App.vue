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
        <ul class="navbar-nav mx-auto">
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
                <p class="nav-item nav-link">{{ store.pageNickname }}님 환영합니다.</p> 
                <RouterLink :to="{ name:'Profile' }" class="nav-item nav-link">프로필 보기</RouterLink>
                <RouterLink :to="{ name:'Cart' }" class="nav-item nav-link">담은 상품</RouterLink>

                <a class="nav-item nav-link" href="#" @click="logOut">로그아웃</a>
              </div>
            </template>
        </div>
      </div>
    </nav>
    <div>
      <RouterView/>
    </div>
  </div>
  <footer class="footer">
    <p class="text">👨🏻‍💻 JeongJonggil & ParkSubin 👩🏻‍💻</p>
    <img :src="bottom" alt="바닥" class="full-width-image">
  </footer>
</template>


<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { useUserStore } from '@/stores/user';
  import logoImage from '@/assets/로고 그림만.png'
  import logoText from '@/assets/로고 글자집.png'
  import bottom from '@/assets/바닥2.png'
  import sky from '@/assets/하늘5.png'
  
  const store = useUserStore()
  const logOut = function () {
    store.logOut()
  }
</script>


<style>

@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Gothic:wght@400;700;800&display=swap');

.navbar {
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
  text-align: right;
}


.main-container {
  min-height: 90.6vh;
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

</style>
