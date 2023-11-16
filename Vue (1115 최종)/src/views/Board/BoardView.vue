<template>
  <div>
    <h1>Board Page</h1>
    <RouterLink :to="{ name: 'FinanceBoardView' }">
      [금융 상품 리뷰]
    </RouterLink>
    <span> | </span>
    <RouterLink :to="{ name: 'ProductBoardView' }">
      [내가 가입한 상품 자랑]
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style>

</style>
