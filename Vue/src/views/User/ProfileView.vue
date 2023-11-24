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
          <!-- <div class="form-group">
            <label for="financial_products">금융 상품</label>
            <input id="financial_products" type="text" v-model.trim="profileData.financial_products" class="form-control" readonly>
          </div> -->
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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
/* 전체 컨테이너 */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Nanum Gothic', sans-serif;
  background: #fafafae3; /* 배경색 일치 */
  /* 기타 필요한 스타일 */
}

/* 회원정보 수정, 비밀번호 변경, 회원탈퇴 버튼 스타일 */
/* 버튼 스타일 */

.text-center.mt-3 {
  display: flex;
  justify-content: space-evenly; /* 버튼들 사이에 공간을 고르게 분배 */
  margin-bottom: 1rem; /* 아래쪽 여백 추가 */
  white-space: nowrap;
  font-family: 'Black Han Sans', sans-serif;
}

/* 버튼 스타일 */
.btn-edit {
  flex-grow: 1; /* 버튼들이 가용 공간을 모두 차지하도록 함 */
  margin: 0 5px; /* 버튼 사이의 간격을 줌 */
  padding: 0.4rem 0.6rem; /* 패딩 조정 */
  font-size: 0.9rem; /* 글자 크기 조정 */
}

.btn-edit:hover {
  background-color: #e6e6e6; /* 호버 상태의 배경색 */
}
/* 폼 스타일 */
.signup-form {
  width: 100%;
  max-width: 1000px;
  padding: 2rem;
  border: 3px solid #5d92aa; /* 테두리 스타일 일치 */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* 입력 필드 스타일 */
.form-control {
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #81d4fa; /* 테두리 색상 일치 */
  font-family: 'Nanum Gothic', sans-serif; /* 폰트 적용 */
  /* 기타 필요한 스타일 */
}


.form-control[readonly] {
  background-color: #e9ecef; /* 배경색 */
  color: #495057; /* 글자색 */
  cursor: not-allowed; /* 커서 변경 */
  border: 1px solid #ced4da; /* 실선 테두리로 변경 */
}


/* 입력 필드 레이블 스타일 */
.form-group label {
  font-family: 'Black Han Sans', sans-serif;
  font-weight: 700;
  /* 기타 필요한 스타일 */
}

/* 반응형 디자인 조정 */
@media (max-width: 768px) {
  .signup-form {
    max-width: 600px;
    padding: 1.5rem;
  }
}

@media (max-width: 576px) {
  .container {
    margin-top: 0;
  }
  .signup-form {
    max-width: 100%;
    padding: 1rem;
  }
}
</style>