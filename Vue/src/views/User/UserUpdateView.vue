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
            <label for="username">아이디</label>
            <input type="text" v-model.trim="profileData.username" class="form-control" id="username" placeholder="아이디" readonly>
          </div>
          <!-- Nickname Field -->
          <div class="form-group">
            <label for="nickname">닉네임</label>
            <input type="text" v-model.trim="profileData.nickname" class="form-control" id="nickname" placeholder="닉네임" >
            <div v-if="store.errorMessages.nickname" class="error-message">{{ store.errorMessages.nickname }}</div>
          </div>
          <!-- Age Field -->
          <div class="form-group">
            <label for="age">나이</label>
            <input type="number" v-model.trim="profileData.age" class="form-control" id="age" placeholder="나이" >
            <div v-if="store.errorMessages.age" class="error-message">{{ store.errorMessages.age }}</div>
          </div>
          <!-- Email Field -->
          <div class="form-group">
            <label for="email">이메일</label>
            <input type="email" v-model.trim="profileData.email" class="form-control" id="email" placeholder="이메일" >
            <div v-if="store.errorMessages.email" class="error-message">{{ store.errorMessages.email }}</div>
          </div>
          <!-- Gender Field -->
          <div class="form-group">
            <label for="gender">성별</label>
            <select v-model="profileData.gender" class="form-control" id="gender">
              <option value="성별없음">성별 선택</option>
              <option value="남성">남성</option>
              <option value="여성">여성</option>
            </select>
          </div>
          <!-- Phone Number Field -->
          <div class="form-group">
            <label for="phone_number">전화번호</label>
            <input type="text" v-model.trim="profileData.phone_number" class="form-control" id="phone_number" placeholder="전화번호" >
            <div v-if="store.errorMessages.phone_number" class="error-message">{{ store.errorMessages.phone_number }}</div>
          </div>
          <!-- Money Field -->
          <div class="form-group">
            <label for="money">자산</label>
            <input type="number" v-model.trim="profileData.money" class="form-control" id="money" placeholder="자산" >
            <div v-if="store.errorMessages.money" class="error-message">{{ store.errorMessages.money }}</div>
          </div>
          <!-- Salary Field -->
          <div class="form-group">
            <label for="salary">연봉</label>
            <input type="number" v-model.trim="profileData.salary" class="form-control" id="salary" placeholder="연봉" >
            <div v-if="store.errorMessages.salary" class="error-message">{{ store.errorMessages.salary }}</div>
          </div>
          <!-- Financial Products Field -->
          <!-- <div class="form-group">
            <label for="financial_products">금융 상품</label>
            <input type="text" v-model.trim="profileData.financial_products" class="form-control" id="financial_products" placeholder="금융 상품 (쉼표로 구분)" >
            <div v-if="store.errorMessages.financial_products" class="error-message">{{ store.errorMessages.financial_products }}</div>
          </div> -->
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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
.container {
  padding-top: 50px;
  font-family: 'Black Han Sans', sans-serif;
}

.brand-title {
  color: #375a7f;
  font-weight: 800;
  margin-bottom: 1rem;
  font-size: 2em;
}

.signup-form {
  background: #FAFAFA;
  border: 1px solid #B3B3B3;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-control {
  border: 1px solid #B3B3B3;
  padding: 0.5rem;
  font-size: 0.9rem; /* 수정된 글자 크기 */
}

.form-group label {
  font-weight: 700;
}

/* 수정된 버튼 컨테이너 스타일 */
.text-center.mt-3 {
  display: flex;
  justify-content: space-between; /* 버튼들 사이에 공간을 고르게 분배 */
  padding: 0; /* 추가된 패딩 제거 */
}

/* 수정된 버튼 스타일 */
.btn-edit {
  flex: none; /* flex-grow 제거 */
  margin: 0 10px; /* 버튼 사이의 간격을 늘림 */
  padding: 0.4rem 0.6rem; /* 패딩 조정 */
  font-size: 0.8rem; /* 글자 크기 조정 */
}

.form-control[readonly] {
  background-color: #e9ecef; /* 배경색 */
  color: #495057; /* 글자색 */
  cursor: not-allowed; /* 커서 변경 */
  border: 1px solid #ced4da; /* 실선 테두리로 변경 */
}
.btn-submit {
  width: 100%;
  padding: 10px;
  background-color: #375a7f;
  border: none;
  border-radius: 5px;
  color: white;
  margin-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.error-message {
  color: red;
  font-size: 0.8em;
  margin-top: 5px;
}

/* 반응형 조정 */
@media (max-width: 576px) {
  .container {
    padding-top: 30px;
  }

  .brand-title {
    font-size: 1.5em;
  }

  .signup-form {
    padding: 1rem;
  }
}
</style>