<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="text-center mb-4">
          <h2 class="brand-title">수길이네 금융마을</h2>
        </div>
        <div class="confirmation-message">
          <p>진짜 회원탈퇴하시겠습니까?</p>
          <button class="btn btn-danger" @click="userDelete">네</button>
          <button class="btn btn-secondary" @click="goBack">아니요</button>
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
.brand-title {
  color: #375a7f;
  font-weight: 800;
  margin-bottom: 2rem;
}

.confirmation-message {
  background: #FAFAFA;
  border: 1px solid #B3B3B3;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.confirmation-message p {
  font-size: 18px;
  margin-bottom: 1rem;
}

.confirmation-message button {
  padding: 0.5rem 1rem;
  font-size: 18px;
  margin-right: 1rem;
}

.confirmation-message .btn-danger {
  background-color: #E74C3C;
  color: white;
  border: none;
}

.confirmation-message .btn-danger:hover {
  background-color: #C0392B;
}

.confirmation-message .btn-secondary {
  background-color: #B3B3B3;
  color: white;
  border: none;
}

.confirmation-message .btn-secondary:hover {
  background-color: #979797;
}
</style>
