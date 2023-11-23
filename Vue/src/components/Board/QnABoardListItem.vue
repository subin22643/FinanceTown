<template>
  <div>
    <h3>제목 : {{ board.title }}</h3>
    <p> 내용 : {{ board.content }}</p>
    <p> 작성자 : {{ board.author.nickname }}</p>
    <p> 작성일 : {{ board.updated_at }}</p>
    <RouterLink :to="{ name: 'BoardDetail', params:{ id: board.id }, query:{ type:'QnA' } }">
      [DETAIL]
    </RouterLink>
    
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  board : Object,
})

</script>
