<script>
import TipsList from '@/components/News/TipsList.vue'
import QuizView from '@/views/QuizView.vue'
import NewsList from '@/components/News/NewsList.vue'
import Recommend from '@/components/Recommed/Recommend.vue';
import thumb1 from '@/assets/썸네일6.png'
import thumb2 from '@/assets/썸네일8.png'



export default {
    components: {
        Recommend,
        NewsList,
        QuizView,
        TipsList
    },
    data() {
        return {
            items: [
            {src: thumb1},
            {src: thumb2},
            ]
        }
    },
  }


</script>

<template>
    <div class="main">
        <div class="carousel-container">
            <v-carousel hide-delimiters :style="{ width: '60%', height: 'auto' }">
                <v-carousel-item v-for="(item,i) in items" :key="i">
                  <div class="image-wrapper">
                    <img :src="item.src" alt="" class="custom-img" ref="carouselImage">
                  </div>
                  
                </v-carousel-item>
            </v-carousel>
        </div>
    </div>
    <div class="body">
      <div class="row">
        <QuizView/>
        <Recommend/>
      </div>
      <div class="row">
        <NewsList/>
        <TipsList/>
      </div>
    </div>
</template>

<style>
.carousel-container {
    margin: 20px;
    display: flex;
    justify-content: center;
}


.body {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center items horizontally */
  padding: 0 30px; /* Adjust padding as needed */
  max-width: 1200px; /* Increase the maximum width as needed */
  margin: 0 auto
}

.row {
  display: flex; 
  justify-content: center; /* 가운데 정렬 */
  flex-wrap: wrap; /* 항목들이 너비를 초과할 경우 다음 줄로 넘어갈 수 있도록 함 */
  margin-bottom: 30px;
}


.row > * {
  width: 100%;
  flex: 1;
  margin: 0 15px;
  min-width: 0; /* Prevent flex items from not shrinking */
  box-sizing: border-box; /* Include padding and borders in width and height */
}


.row > :first-child {
  margin-left: 0;
}

.row > :last-child {
  margin-right: 0;
}


/* Set a minimum width for the items to prevent them from becoming too narrow */
.item {
  flex: 1 1 200px; /* flex-grow, flex-shrink, flex-basis */
  margin: 0 15px;
}

.image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* Ensure the image takes full height within the carousel item */
}

.custom-img {
  max-width: 100%; /* Ensure the image doesn't exceed the carousel width */
  max-height: 100%; /* Ensure the image doesn't exceed the carousel height */
  width: auto; /* Let the width adjust to maintain aspect ratio */
  height: auto; /* Let the height adjust to maintain aspect ratio */
}

</style>

