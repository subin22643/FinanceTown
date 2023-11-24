<script setup>
import { onMounted,ref } from 'vue'
import { useNewsStore } from '@/stores/news'

const store = useNewsStore()

onMounted( () => {
    store.getTips()
})

</script>

<template>
    <div class="card">
        <h3>🍯 오늘의 금융 꿀팁 🍯</h3>
        <p v-for="tip in store.tips.data">
            <a :href="tip.originUrl.replace('www.', 'fine.')" v-html="tip.subject"></a>
        </p>
    </div>
</template>

<style scoped>

/* 카드 스타일 */
.card {
  background-color: #ffffff; /* 밝은 배경색 */
  border: 5px solid #401d00; /* 붉은색 테두리 */
  border-radius: 10px; /* 둥근 모서리 */
  box-shadow: 0 0 10px rgba(231, 76, 60, 0.1); /* 부드러운 붉은색 그림자 효과 */
  margin: 1em auto;
  max-width: 95%;
  box-sizing: border-box;
  width: 700px;
  padding: 20px;
  align-items: flex;
}

/* 타이틀 스타일 */
.card h3 {
  background-color:#401d00; /* 붉은색 배경 */
  color: #ffffff; /* 흰색 텍스트 */
  padding: 0.5em;
  text-align: center;
  border-radius: 5px 5px 0 0;
}

/* 링크 스타일 */
.card a {
  color: gray; /* 밝은 파란색 링크 색상 */
  text-decoration: none; /* 밑줄 제거 */
  display: block; /* 링크를 블록 요소로 만듦 */
  margin: 5px 0;
  font-size: 20px;
}

.card a:hover {
  color: #f39c12; /* 호버 시 오렌지색으로 변경 */
  text-decoration: underline; /* 밑줄 표시 */
}
</style>