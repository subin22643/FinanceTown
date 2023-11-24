<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="text-center mb-4">
          <h1 class="brand-title">수길이네 금융마을</h1>
        </div>
        <form @submit.prevent="logIn" class="signup-form">
          <div class="form-group">
            <label for="username" class="form-label">ID</label>
            <input id="username" type="text" v-model.trim="username" class="form-control">
            <div v-if="store.errorMessages.username" class="error-message">{{ store.errorMessages.username }}</div>
            <div v-if="store.errorMessages.non_field_errors" class="error-message">{{ store.errorMessages.non_field_errors}}</div>
          </div>
          <div class="form-group">
            <label for="password1" class="form-label">비밀번호</label>
            <input id="password1" type="password" v-model.trim="password" class="form-control">
            <div v-if="store.errorMessages.password" class="error-message">{{ store.errorMessages.password }}</div>
            <div v-if="store.errorMessages.non_field_errors" class="error-message">{{ store.errorMessages.non_field_errors}}</div>
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-submit">로그인</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

onMounted(() => {
  store.clearErrorMessages()
})

</script>

<style setup>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

/* 전체 페이지 컨테이너 스타일 */
.row {
  width: 1000px;
  height: auto;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  /* min-height: 87vh; */
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
  height: auto;
}

/* 로그인 폼 컨테이너 스타일 */
.signup-form {
  width: 100%;
  max-width: 1000px;
  padding: 2rem;
  background: #fafafae3;
  border: 3px solid #5d92aa;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
}

/* 브랜드 타이틀 스타일 */
.brand-title {
  color: #437fa1;
  font-family: 'Black Han Sans', sans-serif; /* Black Han Sans 폰트 적용 */
  text-align: center;
  margin-bottom: 1rem;
}

/* 폼 그룹 스타일 */
.form-group {
  margin-bottom: 1rem;
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
}

/* 폼 레이블 스타일 */
.form-label {
  display: block;
  color: #0277bd;
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
  margin-bottom: 0.5rem;
}

/* 입력 필드 스타일 */
.form-control {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 2px solid #81d4fa;
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
}

/* 로그인 버튼 스타일 */
.btn-submit {
  width: 100%;
  padding: 0.7rem 1rem;
  background-color: #5d92aa;
  color: white;
  border: none;
  border-radius: 0;
  font-family: 'Black Han Sans', sans-serif; /* Black Han Sans 폰트 적용 */
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #01579b;
}

/* 에러 메시지 스타일 */
.error-message {
  color: #E74C3C;
  margin-top: 0.25rem;
  font-size: 0.875rem;
  font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
}

/* 반응형 조정 */
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
