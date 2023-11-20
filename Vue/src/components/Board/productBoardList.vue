<template>
  <div>
    <productBoardListItem 
     v-for="board in store.productBoards"
     :key="board.id"
     :board="board"
    />
  </div>
</template>

<script setup>
import productBoardListItem from '@/components/Board/productBoardListItem.vue'
import { useBoardStore } from '@/stores/board';

const store = useBoardStore()

</script>
