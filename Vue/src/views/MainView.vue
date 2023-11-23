<script>
import NewsList from '@/components/News/NewsList.vue'
import TipsList from '@/components/News/TipsList.vue'
import Recommend from '@/components/Recommed/Recommend.vue';
import thumb1 from '@/assets/썸네일6.png'
import thumb2 from '@/assets/썸네일8.png'
import QuizView from '@/views/QuizView.vue'


export default {
    components: {
        Recommend, // 컴포넌트를 등록합니다.
        NewsList, // 컴포넌트를 등록합니다.
        QuizView,
        TipsList,
    },
    data() {
        return {
            items: [
            {src: thumb1},
            {src: thumb2},
            ]
        }
    }
  }

</script>

<template>
    <div class="main">
        <div class="carousel-container">
            <v-carousel hide-delimiters :style="{ width: '85%' }">
                <v-carousel-item
                    v-for="(item,i) in items"
                    :key="i">
                    <v-img :src="item.src" class="custom-img"></v-img>
                </v-carousel-item>
            </v-carousel>
        </div>
    </div>
    <div class="body">
    <div class="row">
      <QuizView class="item"/>
      <Recommend class="item"/>
    </div>
    <div class="row">
      <NewsList class="item"/>
      <TipsList class="item"/>
    </div>
  </div>
</template>

<style scoped>

.carousel-container {
    display: flex;
    justify-content: center;
}

.body {
  display: flex;
  flex-direction: column; 
  justify-content: space-between; /* Center content horizontally */
  align-items: stretch;
  text-align: center;
  width: 90%; /* Utilize the full width of the viewport */
  margin: 0 auto;
  padding: 20px;
}

.body > * {
  flex: 1; /* 각 아이템이 사용할 수 있는 공간을 동등하게 나눔 */
  margin: 0 30px; /* 좌우 마진을 주어서 사이의 간격을 조절 */
}

/* 첫 번째 컴포넌트의 경우 오른쪽 마진을 추가 */
.body > :first-child {
  margin-right: 30px;
}

/* 두 번째 컴포넌트의 경우 왼쪽 마진을 추가 */
.body > :last-child {
  margin-left: 30px;
}

.custom-img {
  width: 100%; /* 이미지 너비를 100%로 설정하여 가로로 꽉 차게 합니다. */
  height: auto; /* 높이를 auto로 설정하여 비율을 유지합니다. */
}

.row {
  display: flex; /* Flexbox 사용 */
  justify-content: space-between; /* 가로로 요소들을 공간을 균등하게 나누어 배치 */
  margin-bottom: 30px; /* 각 행의 하단 여백 */
}

.item {
  flex: 1; /* 각 아이템이 사용할 수 있는 공간을 동등하게 나눔 */
  margin: 0 15px; /* 좌우 마진을 주어서 사이의 간격을 조절 */
}

/* 첫 번째 행의 마지막 아이템과 두 번째 행의 첫 번째 아이템의 마진 조정 */
.row:first-child > .item:last-child, .row:last-child > .item:first-child {
  margin-right: 30px;
  margin-left: 0;
}

/* 마지막 행의 마지막 아이템의 하단 여백 제거 */
.row:last-child {
  margin-bottom: 0;
}

/* 반응형을 고려한 스타일 조정 */
@media (max-width: 768px) {
  .row {
    flex-direction: column; /* 모바일에서는 요소들을 세로로 쌓음 */
  }
  
  .item {
    margin: 10px 0; /* 모바일에서는 상하 여백만 조정 */
  }
}

</style>
