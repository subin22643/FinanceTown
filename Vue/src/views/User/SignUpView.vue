<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="text-center mb-4">
            <h1 class="brand-title">수길이네 금융마을</h1>
          </div>
          <form @submit.prevent="signUp" class="signup-form">
            <!-- Username Field -->
            <div class="form-group">
              <input type="text" v-model.trim="username" class="form-control" placeholder="아이디">
              <div v-if="store.errorMessages.username" class="error-message">{{ store.errorMessages.username }}</div>
            </div>
            <!-- Nickname Field -->
            <div class="form-group">
              <input type="text" v-model.trim="nickname" class="form-control" placeholder="닉네임">
              <div v-if="store.errorMessages.nickname" class="error-message">{{ store.errorMessages.nickname }}</div>
            </div>
            <!-- Password Fields -->
            <div class="form-group">
              <input type="password" v-model.trim="password1" class="form-control" placeholder="비밀번호">
              <div v-if="store.errorMessages.password1" class="error-message">{{ store.errorMessages.password1 }}</div>
            </div>
            <div class="form-group">
              <input type="password" v-model.trim="password2" class="form-control" placeholder="비밀번호 재확인">
              <div v-if="store.errorMessages.password2" class="error-message">{{ store.errorMessages.password2 }}</div>
            </div>
            <!-- Age Field -->
            <div class="form-group">
              <input type="number" v-model.trim="age" class="form-control" placeholder="나이">
              <div v-if="store.errorMessages.age" class="error-message">{{ store.errorMessages.age }}</div>

            </div>
            <!-- Email Field -->
            <div class="form-group">
              <input type="email" v-model.trim="email" class="form-control" placeholder="이메일">
              <div v-if="store.errorMessages.email" class="error-message">{{ store.errorMessages.email }}</div>
            </div>
            <!-- Gender Field -->
            <div class="form-group">
              <select v-model="gender" class="form-control">
                <option value="">성별 선택</option>
                <option value="남성">남성</option>
                <option value="여성">여성</option>
              </select>
            </div>
            <!-- Phone Number Field -->
            <div class="form-group">
              <input type="text" v-model.trim="phone_number" class="form-control" placeholder="전화번호(ex.010-0000-000)">
              <div v-if="store.errorMessages.phone_number" class="error-message">{{ store.errorMessages.phone_number }}</div>
            </div>
            <!-- Money Field -->
            <div class="form-group">
              <input type="number" v-model.trim="money" class="form-control" placeholder="자산">
              <div v-if="store.errorMessages.money" class="error-message">{{ store.errorMessages.money }}</div>
            </div>
            <!-- Salary Field -->
            <div class="form-group">
              <input type="number" v-model.trim="salary" class="form-control" placeholder="연봉">
              <div v-if="store.errorMessages.salary" class="error-message">{{ store.errorMessages.salary }}</div>
            </div>
            <!-- Financial Products Field -->
            <!-- <div class="form-group">
                <input type="text" v-model.trim="financial_products" class="form-control" placeholder="금융 상품 (쉼표로 구분)">
                <div v-if="store.errorMessages.financial_products" class="error-message">{{ store.errorMessages.financial_products }}</div>
            </div> -->
            <!-- Submit Button -->
            <div class="form-group">
              <button type="submit" class="btn btn-submit">가입 하기</button>
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

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const gender = ref('')
const phone_number = ref('')
const email = ref('')
const age = ref('')
const money = ref('')
const salary = ref('')
const financial_products = ref('')

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    gender: gender.value,
    phone_number: phone_number.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    // financial_products: financial_products.value.split(',').map(fp => fp.trim())
  }
  store.signUp(payload)
}

//에러메시지 초기화 안하면 다시 회원가입페이지로 와도 계속 남아있음
onMounted(() => {
  store.clearErrorMessages()
})

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Gothic:wght@400;700;800&display=swap');


/* 전체 컨테이너 */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Nanum Gothic', sans-serif;
  height: auto; /* Same height as the login form for consistency */
  background: #fafafae3; /* Background color matching the login form */
}


/* 회원가입 폼 */
.signup-form {
  width: 100%;
  max-width: 1000px; /* Adjusted to match the login form */
  padding: 2rem;
  border: 3px solid #5d92aa; /* Border styling to match the login form */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}


/* 입력 필드 */
.form-control {
  width: 100%;
  padding: 0.5rem; /* Adjusted to match the login form */
  margin-bottom: 1rem;
  border: 2px solid #81d4fa; /* Border color to match the login form */
}

/* 버튼 */
.btn-submit {
  width: 100%;
  padding: 0.7rem 1rem; /* Adjusted to match the login form */
  background-color: #5d92aa; /* Button color to match the login form */
  color: white;
  border: none;
  border-radius: 0; /* Adjusted to match the login form */
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #01579b; /* Hover color to match the login form */
}

/* 에러 메시지 */
.error-message {
  color: #E74C3C;
  margin-top: 0.25rem;
  font-size: 0.875rem;
  font-family: 'Nanum Gothic', sans-serif; /* Error message font to match the login form */
}

/* 반응형 조정 */
@media (max-width: 768px) {
  .signup-form {
    max-width: 600px; /* Same as the login form for consistency */
    padding: 1.5rem;
  }
}

@media (max-width: 576px) {
  .container {
    margin-top: 0;
  }
  .signup-form {
    max-width: 100%; /* Same as the login form for consistency */
    padding: 1rem;
  }
}
</style>