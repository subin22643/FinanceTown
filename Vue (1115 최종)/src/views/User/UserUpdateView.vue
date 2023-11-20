<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title d-inline-block mr-3">수길이네 금융마을</h2>
        </div>
        <form class="signup-form" @submit.prevent="update">
          <!-- Username Field -->
          <div class="form-group">
            <input type="text" v-model.trim="profileData.username" class="form-control" placeholder="아이디" readonly>
          </div>
           <!-- Nickname Field -->
           <div class="form-group">
            <input type="text" v-model.trim="profileData.nickname" class="form-control" placeholder="닉네임" >
            <div v-if="store.errorMessages.nickname" class="error-message">{{ store.errorMessages.nickname }}</div>
          </div>
          <!-- Password Fields -->
          <!-- <div class="form-group">
            <input type="password" v-model.trim="password1" class="form-control" placeholder="비밀번호">
          </div>
          <div class="form-group">
            <input type="password" v-model.trim="password2" class="form-control" placeholder="비밀번호 재확인">
          </div> -->
          <!-- Age Field -->
          <div class="form-group">
              <input type="number" v-model.trim="profileData.age" class="form-control" placeholder="나이" >
              <div v-if="store.errorMessages.age" class="error-message">{{ store.errorMessages.age }}</div>
          </div>
          <!-- Email Field -->
          <div class="form-group">
            <input type="email" v-model.trim="profileData.email" class="form-control" placeholder="이메일" >
            <div v-if="store.errorMessages.email" class="error-message">{{ store.errorMessages.email }}</div>
          </div>
          <!-- Gender Field -->
          <div class="form-group">
            <select v-model="profileData.gender" class="form-control">
              <option value="성별없음">성별 선택</option>
              <option value="남성">남성</option>
              <option value="여성">여성</option>
            </select>
          </div>
          <!-- Phone Number Field -->
          <div class="form-group">
            <input type="text" v-model.trim="profileData.phone_number" class="form-control" placeholder="전화번호" >
            <div v-if="store.errorMessages.phone_number" class="error-message">{{ store.errorMessages.phone_number }}</div>
          </div>
          <!-- Money Field -->
          <div class="form-group">
            <input type="number" v-model.trim="profileData.money" class="form-control" placeholder="자산" >
            <div v-if="store.errorMessages.money" class="error-message">{{ store.errorMessages.money }}</div>
          </div>
          <!-- Salary Field -->
          <div class="form-group">
            <input type="number" v-model.trim="profileData.salary" class="form-control" placeholder="연봉" >
            <div v-if="store.errorMessages.salary" class="error-message">{{ store.errorMessages.salary }}</div>
          </div>
          <!-- Financial Products Field -->
          <div class="form-group">
            <input type="text" v-model.trim="profileData.financial_products" class="form-control" placeholder="금융 상품 (쉼표로 구분)" >
            <div v-if="store.errorMessages.financial_products" class="error-message">{{ store.errorMessages.financial_products }}</div>
          </div>
          <!-- Submit Button -->
          <div class="form-group">
            <button type="submit" class="btn btn-submit">수정 하기</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const profileData = store.profileData

const update = () => {
  store.update()
}

onMounted(() => {
  store.clearErrorMessages()
})

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

.error-message {
    color: red;
    font-size: 0.8em;
    margin-top: 5px;
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
