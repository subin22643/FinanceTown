<script setup>
import { useUserStore } from '@/stores/user';
const store = useUserStore()
</script>

<template>
    <div class="card">
        <h1>👍 {{ store.loginUserNickname }}님을 위한 상품 추천 👍</h1>
        <br>
        <br>
        <br>
        <div>
            <h3><strong>상품 정보</strong></h3>
            <p>WON플러스예금</p>
            <p>우리은행</p>
            <br>
            <h3><strong>옵션 정보</strong></h3>
            <p>최고 우대 금리: 4.02</p>
            <p>저축기간: 6</p>
        </div>
    </div>
</template>

<style scoped>

.card {
    width: 680px;
    padding: 20px;
    border: 5px gray solid;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    align-items: flex;
    height: 520px;
    margin-top: 30px;
}

h1 {
  margin-top: 0; 
  padding-top: 1rem; 
  text-align: center;
}



h3 {
    text-align: center;
}

p {
    text-align: center;
    font-size: 20px;
}
</style>
