<template>
  <div>
    <h3>Board List</h3>
    <BoardListItem 
     v-for="board in store.boards"
     :key="board.id"
     :board="board"
    />
  </div>
</template>

<script setup>
import BoardListItem from '@/components/Board/BoardListItem.vue'
import { useBoardStore } from '@/stores/board';

const store = useBoardStore()

</script>
