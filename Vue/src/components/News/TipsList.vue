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
        <h3>오늘의 금융 꿀팁</h3>
        <p v-for="tip in store.tips.data">
            <a :href="tip.originUrl.replace('www.', 'fine.')">{{ tip.subject }}</a>
        </p>
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

/* 카드 스타일 */
.card {
  background-color: #ffffff; /* 밝은 배경색 */
  border: 4px solid #29adff; /* 밝은 푸른색 테두리 */
  border-radius: 10px; /* 둥근 모서리 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 효과 */
  padding: 1em;
  margin: 1em auto;
  max-width: 95%;
  box-sizing: border-box;
}

/* 타이틀 스타일 */
.card h3 {
  background-color: #29adff; /* 푸른색 배경 */
  color: #ffffff; /* 흰색 텍스트 */
  padding: 0.5em;
  margin-top: -1em; /* 카드의 상단에 겹치도록 */
  text-align: center;
  border-radius: 5px 5px 0 0;
}

/* 링크 스타일 */
.card a {
  color: #29adff; /* 링크 색상 */
  text-decoration: none; /* 밑줄 제거 */
  display: block; /* 링크를 블록 요소로 만듦 */
  margin: 0.5em 0;
}

.card a:hover {
  color: #ffcc00; /* 호버 시 노란색으로 변경 */
  text-decoration: underline; /* 밑줄 표시 */
}

/* 구분선 스타일 */
.card hr {
  border: 0;
  height: 1px;
  background-image: linear-gradient(to right, #29adff, rgba(255, 255, 255, 0), #29adff);
  margin: 0.5em 0;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .card {
    width: 90%;
    margin: 1em;
  }
}
</style>