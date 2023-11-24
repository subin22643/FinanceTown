<template>
  <div>
    <QnABoardListItem 
     v-for="board in store.QnABoards"
     :key="board.id"
     :board="board"
    />
  </div>
</template>

<script setup>
import QnABoardListItem from '@/components/Board/QnABoardListItem.vue'
import { useBoardStore } from '@/stores/board';

const store = useBoardStore()

</script>
