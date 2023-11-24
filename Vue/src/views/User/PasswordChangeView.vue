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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

.password-change-container {
  text-align: center;
  margin-top: 50px;
  padding: 20px;
  background-color: #FAFAFA;
  border: 1px solid #B3B3B3;
  border-radius: 8px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 700px;
  margin: 50px auto;
  font-family: 'Black Han Sans', sans-serif;
}

.password-change-container h2 {
  color: #375a7f;
  font-weight: 800;
  font-size: 2em;
  margin-bottom: 20px;
}

.password-change-container form div {
  margin-bottom: 15px;
}

.password-change-container label {
  font-weight: 700;
  text-align: left;
  display: block;
  margin-bottom: 5px;
  color: #495057;
}

.password-change-container input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #81d4fa;
  font-size: 1rem;
  margin-bottom: 10px;
}

.password-change-container button {
  width: 100%;
  padding: 10px;
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  margin-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  cursor: pointer;
}

.password-change-container button:hover {
  background-color: #2c446b;
}

.error-message {
  color: red;
  font-size: 0.8rem;
  margin-top: 5px;
}

@media (max-width: 576px) {
  .password-change-container {
    padding: 1rem;
  }

  .password-change-container h2 {
    font-size: 1.5em;
  }
}
</style>
