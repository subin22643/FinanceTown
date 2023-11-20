<template>
  <div>
    <p>{{ board.title }}</p>
    <p>{{ board.content }}</p>
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
