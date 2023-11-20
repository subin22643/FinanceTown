<template>
  <div>
    <h1>  금융 상품 리뷰 게시판 </h1>
    <RouterLink :to="{ name: 'BoardCreate'}">
      [CREATE]
    </RouterLink>
    <BoardList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/Board/BoardList.vue'

const store = useBoardStore()

onMounted(() => {
  store.getProductBoards()
})

</script>

<style>

</style>
