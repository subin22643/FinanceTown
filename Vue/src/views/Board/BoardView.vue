<template>
  <div>
    <h1>Board Page</h1>
    <RouterLink :to="{ name: 'ProductBoardView' }">
      [금융 상품 리뷰 게시판]
    </RouterLink>
    <span> | </span>
      
    <RouterLink :to="{ name: 'QnABoardView' }">
      [상담 게시판]
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style>

</style>
