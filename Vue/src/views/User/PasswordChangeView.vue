<template>
  <div class="password-change-container">
    <h2>비밀번호 변경</h2>
    <form @submit.prevent="changePassword">
      <div>
        <label for="oldPassword">현재 비밀번호</label>
        <input type="password" id="oldPassword" v-model="store.passwordChangeData.old_password" required>
        <div v-if="store.errorMessages.old_password" class="error-message">{{ store.errorMessages.old_password }}</div>
      </div>
      <div>
        <label for="newPassword">새 비밀번호</label>
        <input type="password" id="newPassword" v-model="store.passwordChangeData.new_password1" required>
      </div>
      <div>
        <label for="confirmPassword">새 비밀번호 확인</label>
        <input type="password" id="confirmPassword" v-model="store.passwordChangeData.new_password2" required>
        <div v-if="store.errorMessages.new_password2" class="error-message">{{ store.errorMessages.new_password2 }}</div>
      </div>

      <button type="submit">비밀번호 변경</button>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const changePassword = ()=> {
  store.changePassword()
}

</script>

<style scoped>
.password-change-container {
  text-align: center;
  margin-top: 50px;
  padding: 20px;
  background-color: #FAFAFA;
  border: 1px solid #B3B3B3;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 700px;
  margin: 0 auto;
}

.password-change-container h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #375a7f;
}

.password-change-container form div {
  margin-bottom: 15px;
}

.password-change-container label {
  font-weight: 700;
  display: block;
  text-align: left;
  margin-bottom: 5px;
  color: #495057;
}

.password-change-container input[type="password"] {
  border: 1px solid #B3B3B3;
  padding: 10px;
  font-size: 16px;
  width: 100%; /* 가로로 늘리기 위해 유지 */
}

.password-change-container button {
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
}

.password-change-container button:hover {
  background-color: #2c446b;
}

.error-message {
  color: #E74C3C;
  font-size: 14px;
  margin-top: 5px;
}
</style>
