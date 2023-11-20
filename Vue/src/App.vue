<template>
  <nav class="navbar navbar-expand navbar-light bg-light">
    <RouterLink class="navbar-brand" :to="{ name: 'main' }">수길이네 금융마을</RouterLink>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav mr-auto">
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
          <RouterLink class="nav-link" :to="{ name: 'BoardView' }">커뮤니티 게시판</RouterLink>
        </li>
      </ul>
      <template v-if="!store.isLogin">
        <div class="navbar-nav">
          <RouterLink :to="{ name:'LogIn' }" class="nav-item nav-link">로그인</RouterLink>
          <RouterLink :to="{ name:'SignUp' }" class="nav-item nav-link">회원가입</RouterLink>          
        </div>
      </template>
      <template v-else>
        <div class="navbar-nav">
          <p class="nav-item nav-link">{{ store.loginUserNickname }}님 환영합니다.</p> 
          <RouterLink :to="{ name:'Profile' }" class="nav-item nav-link">프로필 보기</RouterLink>          
          <!-- <RouterLink :to="{ name:'UserUpdate' }" class="nav-item nav-link">회원정보수정</RouterLink>           -->
          <a class="nav-item nav-link" href="#" @click="logOut">로그아웃</a>
        </div>
      </template>
    </div>
  </nav>
  <div class="router-view-container">
  <button class="nav-item nav-link back" @click="goBack"> ← 뒤로 가기</button>
    <RouterView/>
  </div>
</template>


<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { useUserStore } from '@/stores/user';
  import { useRouter } from 'vue-router';
  
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

.nav-link {
  color: #495057; /* 네비게이션 링크 컬러 */
}

.nav-link:hover {
  color: #007bff; /* 호버 효과를 위한 메인 브랜드 컬러 */
}

.back {
    margin-left: 10px; /* 버튼 간격 조정 */
    color: blueviolet;
    font-weight: bolder;
    border: 2px solid gray;
    padding: 5px;
    margin-bottom: 20px;
  }

.router-view-container {
  padding: 20px;
  margin-top: 20px;
  background-color: #f8f9fa; /* 연한 배경색 */
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
}
</style>
