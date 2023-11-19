<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title">수길이네 금융마을</h2>
        </div>
        <div>
          <p>진짜 회원탈퇴 ?</p>
          <button @click="userDelete">yes</button>
          <button @click="goBack">no</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'; 
import { useUserStore } from '@/stores/user';

const router = useRouter()
const store = useUserStore()

const userDelete = () => {
  store.userDelete()
}

// 이전 페이지로 이동하는 함수
const goBack = () => {
  router.go(-1)
}
</script>


<style scoped>

</style>