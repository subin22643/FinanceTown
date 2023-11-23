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
.error-message {
    color: red;
    font-size: 0.8em;
    margin-top: 5px;
}
</style>
