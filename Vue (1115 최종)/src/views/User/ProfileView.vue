<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title d-inline-block mr-3">수길이네 금융마을</h2>
          <button class="btn btn-edit" @click="goToUpdatePage">수정하기</button>
          <button class="btn btn-edit" @click="goToPasswordChangePage">비밀번호변경</button>
          <button class="btn btn-edit" @click="goToDeletePage">회원탈퇴</button>
        </div>
        <form class="signup-form">
          <!-- Username Field -->
          <div class="form-group">
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

</style>