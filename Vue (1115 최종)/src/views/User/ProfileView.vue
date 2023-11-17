<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title d-inline-block mr-3">수길이네 금융마을</h2>
          <button class="btn btn-edit" @click="goToEditPage">수정하기</button>
        </div>
        <form class="signup-form">
          <!-- Username Field -->
          <div class="form-group">
            <input type="text" v-model.trim="username" class="form-control" placeholder="아이디" readonly>
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
            <input id="financial_products" type="text" v-model.trim="financial_products" class="form-control" readonly>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';

const router = useRouter();

const store = useUserStore()


const goToEditPage = () => {
  router.push({ name: 'UserUpdate', params: { profileData: profileData.value } }); // 여기에 실제 수정 페이지의 라우트 경로를 넣어야 합니다.
};
const profileData = ref({
  username: '',
  nickname: '',
  password1: '',
  password2: '',
  age: '',
  email: '',
  gender: '',
  phone_number: '',
  money: '',
  salary: '',
  // financial_products: ''
});

// 처음 1회 profile 요청
axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/`,
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
  .then((res) => {
    Object.assign(profileData.value, res.data);
  })
  .catch((err) => {
    console.log(err)
  })
</script>


<style scoped>

</style>