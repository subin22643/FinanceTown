<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title">수길이네 금융마을</h2>
        </div>
        <form @submit.prevent="signUp" class="signup-form">
          <!-- Username Field -->
          <div class="form-group">
            <input type="text" v-model.trim="username" class="form-control" placeholder="아이디">
          </div>
           <!-- Nickname Field -->
           <div class="form-group">
            <input type="text" v-model.trim="nickname" class="form-control" placeholder="닉네임">
          </div>
          <!-- Password Fields -->
          <div class="form-group">
            <input type="password" v-model.trim="password1" class="form-control" placeholder="비밀번호">
          </div>
          <div class="form-group">
            <input type="password" v-model.trim="password2" class="form-control" placeholder="비밀번호 재확인">
          </div>
          <!-- Age Field -->
          <div class="form-group">
              <input type="number" v-model.trim="age" class="form-control" placeholder="나이">
          </div>
          <!-- Email Field -->
          <div class="form-group">
            <input type="email" v-model.trim="email" class="form-control" placeholder="이메일">
          </div>
          <!-- Gender Field -->
          <div class="form-group">
            <select v-model="gender" class="form-control">
              <option value="">성별 선택</option>
              <option value="male">남성</option>
              <option value="female">여성</option>
            </select>
          </div>
          <!-- Phone Number Field -->
          <div class="form-group">
            <input type="text" v-model.trim="phone_number" class="form-control" placeholder="전화번호">
          </div>
          <!-- Money Field -->
          <div class="form-group">
              <input type="number" v-model.trim="money" class="form-control" placeholder="자산">
          </div>
          <!-- Salary Field -->
          <div class="form-group">
              <input type="number" v-model.trim="salary" class="form-control" placeholder="연봉">
          </div>
          <!-- Financial Products Field -->
          <div class="form-group">
              <input type="text" v-model.trim="financial_products" class="form-control" placeholder="금융 상품 (쉼표로 구분)">
          </div>
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
import { ref } from 'vue'
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
</script>

<style scoped>
.container {
  padding-top: 50px;
}

.brand-title {
  color: #00a2ff; /* Sky-blue color for the brand title */
  font-size: 2em;
  margin-bottom: 30px;
}

.signup-form {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  color: #6c757d; /* Gray text for the labels */
}

.form-control {
  border-radius: 5px;
  border: 1px solid #ced4da;
  height: 40px; /* Reduced height for a more compact look */
}

.btn-submit {
  width: 100%;
  padding: 10px;
  background-color: #00a2ff; /* Sky-blue background for the button */
  border: none;
  border-radius: 5px;
  color: white;
  margin-top: 20px; /* Space above the button */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.btn-submit:hover {
  background-color: #008bdc; /* Slightly darker on hover */
}

/* Responsive adjustments */
@media (max-width: 576px) {
  .container {
    padding-top: 30px;
  }

  .brand-title {
    font-size: 1.5em;
  }

  .signup-form {
    padding: 15px;
  }
}
</style>
