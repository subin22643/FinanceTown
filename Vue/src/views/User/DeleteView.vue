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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');

.container {
  font-family: 'Black Han Sans', sans-serif;
}

.brand-title {
  color: #375a7f;
  font-weight: 800;
  margin-bottom: 2rem;
  font-size: 2em; /* 일관된 제목 크기 */
}

.confirmation-message {
  background: #FAFAFA;
  border: 1px solid #B3B3B3;
  padding: 2rem;
  border-radius: 8px; /* 일관된 테두리 둥글기 */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 700px; /* 컨테이너 최대 너비 */
  margin: 0 auto; /* 가운데 정렬 */
}

.confirmation-message p {
  font-size: 1.5rem; /* 텍스트 크기 조정 */
  color: #495057; /* 텍스트 색상 조정 */
  margin-bottom: 1rem;
}

.confirmation-message button {
  padding: 0.8rem 1.6rem; /* 버튼 패딩 조정 */
  font-size: 1rem; /* 버튼 폰트 크기 조정 */
  margin: 0 10px; /* 버튼 사이 간격 조정 */
  border-radius: 5px; /* 버튼 테두리 둥글기 */
  border: none; /* 테두리 제거 */
  cursor: pointer; /* 클릭 가능한 커서 스타일 */
  transition: background-color 0.3s; /* 부드러운 색상 전환 */
}

.confirmation-message .btn-danger {
  background-color: #375a7f; /* 통일된 버튼 색상 */
}

.confirmation-message .btn-danger:hover {
  background-color: #2c446b; /* 호버 시 색상 */
}

.confirmation-message .btn-secondary {
  background-color: #B3B3B3; /* 보조 버튼 색상 */
}

.confirmation-message .btn-secondary:hover {
  background-color: #979797; /* 호버 시 보조 버튼 색상 */
}

</style>
