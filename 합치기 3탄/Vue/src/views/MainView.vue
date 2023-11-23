<script>
import NewsList from '@/components/News/NewsList.vue'
import Recommend from '@/components/Recommed/Recommend.vue';
import thumb1 from '@/assets/썸네일6.png'
import thumb2 from '@/assets/썸네일8.png'



export default {
    components: {
        Recommend, // 컴포넌트를 등록합니다.
        NewsList, // 컴포넌트를 등록합니다.
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
        <h3>메인페이지입니다</h3>
        <p>여기에는 대략적인 서비스 소개 넣는거 어떨까요</p>
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
        <Recommend/>
        <NewsList/>
    </div>
</template>

<style scoped>

.carousel-container {
    display: flex;
    justify-content: center;
}

.body {
  display: flex;
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

</style>
