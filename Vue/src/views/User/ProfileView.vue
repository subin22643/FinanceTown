<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h1 class="brand-title d-inline-block mr-3">수길이네 금융마을</h1>
          <div class="text-center mt-3">
            <button class="btn btn-edit fs-4 text-body-secondary" @click="goToUpdatePage">회원정보수정</button>
            <button class="btn btn-edit fs-4 text-body-secondary" @click="goToPasswordChangePage">비밀번호변경</button>
            <button class="btn btn-edit fs-4 text-body-secondary" @click="goToDeletePage">회원탈퇴</button>
          </div>
        </div>
        <form class="signup-form">
          <!-- Username Field -->
          <div class="form-group">
            <label for="nickname">아이디</label>
            <input type="text" v-model.trim="profileData.username" class="form-control" placeholder="아이디" readonly>
          </div>
          <!-- Nickname Field -->
          <div class="form-group">
            <label for="nickname">닉네임</label>
            <input id="nickname" type="text" v-model.trim="profileData.nickname" class="form-control" readonly>
          </div>
          <!-- Password Fields
          <div class="form-group">
            <label for="password1">비밀번호</label>
            <input id="password1" type="password" v-model.trim="profileData.password1" class="form-control">
          </div>
          <div class="form-group">
            <label for="password2">비밀번호 재확인</label>
            <input id="password2" type="password" v-model.trim="profileData.password2" class="form-control">
          </div> -->

          <!-- Age Field -->
          <div class="form-group">
            <label for="age">나이</label>
            <input id="age" type="number" v-model.trim="profileData.age" class="form-control" readonly>
          </div>

          <!-- Email Field -->
          <div class="form-group">
            <label for="email">이메일</label>
            <input id="email" type="email" v-model.trim="profileData.email" class="form-control" readonly>
          </div>

          <!-- Gender Field -->
          <div class="form-group">
            <label for="gender">성별</label>
            <input id="gender" type="text" v-model.trim="profileData.gender" class="form-control" readonly>
          </div>

          <!-- Phone Number Field -->
          <div class="form-group">
            <label for="phone_number">전화번호</label>
            <input id="phone_number" type="text" v-model.trim="profileData.phone_number" class="form-control" readonly>
          </div>

          <!-- Money Field -->
          <div class="form-group">
            <label for="money">자산</label>
            <input id="money" type="number" v-model.trim="profileData.money" class="form-control" readonly>
          </div>

          <!-- Salary Field -->
          <div class="form-group">
            <label for="salary">연봉</label>
            <input id="salary" type="number" v-model.trim="profileData.salary" class="form-control" readonly>
          </div>


          <!-- Financial Products Field -->
          <div class="form-group">
            <label for="financial_products">금융 상품</label>
            <input id="financial_products" type="text" v-model.trim="profileData.financial_products" class="form-control" readonly>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useUserStore()
const profileData =  ref('')

onMounted(() => {
  store.setProfileData();
  profileData.value = store.profileData;
});


const goToUpdatePage = () => {
  router.push({ name: 'UserUpdate'});
}

const goToPasswordChangePage = () => {
  router.push({ name: 'PasswordChange'});
}

const goToDeletePage = () => {
  router.push({ name: 'UserDelete'});
}


</script>


<style scoped>
.container {
  padding-top: 50px;
  text-align: center;
}

.brand-title {
  color: #375a7f; /* 진한 색상으로 변경 */
  font-family: 'Nanum Gothic', sans-serif;
  font-weight: 800; /* 폰트 굵기 증가 */
  margin-bottom: 1rem;
}

.signup-form {
  background: #FAFAFA; /* 연한 배경색으로 조정 */
  border: 1px solid #B3B3B3; /* 테두리 색상 변경 */
  padding: 2rem; /* 패딩 증가 */
  border-radius: 0.5rem; /* 모서리 둥글게 */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과를 부드럽게 */
  width: 100%;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1rem; /* 입력 필드 간 여백 조정 */
  display: flex;
  flex-direction: column; /* 세로로 요소 배치 */
}

.form-control {
  border: 1px solid #B3B3B3; /* 테두리 색상 변경 */
  padding: 0.5rem; /* 내부 패딩 증가 */
  font-size: 20px; /* 원하는 크기로 조정 */
}

/* 추가한 스타일 */
.form-group label {
  font-weight: 700; /* 레이블 텍스트 굵기 증가 */
  text-align: left; /* 레이블 텍스트를 왼쪽 정렬 */
}

/* readonly 필드 스타일 */
.form-control:read-only {
  background-color: #dcdcdc; /* 배경색 변경 (예: 밝은 회색) */
  color: #6c757d; /* 텍스트 색상 변경 */
  cursor: not-allowed; /* 커서를 비활성화 모양으로 변경 */
}

/* 반응형 조정 */
@media (max-width: 576px) {
  .container {
    padding-top: 30px;
  }

  .brand-title {
    font-size: 1.5em; /* 모바일 화면에 맞게 폰트 크기 조정 */
  }

  .signup-form {
    padding: 1rem; /* 모바일 화면에 맞게 패딩 조정 */
  }
}
</style>