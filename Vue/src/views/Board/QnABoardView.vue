<template>
  <div>
    <h1> 상담 게시판 </h1>
    <RouterLink :to="{ name: 'BoardCreate'}">
      [게시글 작성]
      <hr>
    </RouterLink>
    <BoardList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/Board/QnABoardList.vue'

const store = useBoardStore()

onMounted(() => {
  store.getQnABoards()
})

</script>

<style>

</style>
