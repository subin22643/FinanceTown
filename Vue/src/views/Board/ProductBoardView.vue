<template>
  <div>
    <h1> 금융 상품 리뷰 게시판 </h1>
    <RouterLink :to="{ name: 'BoardCreate' }">
      [게시글 작성]
      <hr>
    </RouterLink>
    <productBoardList />
  </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { RouterLink } from 'vue-router'
import productBoardList from '@/components/Board/productBoardList.vue'

const store = useBoardStore()

onMounted(() => {
  store.getProductBoards()
})

</script>

<style scoped>

</style>
