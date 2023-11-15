<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <div>
      <h1>메인 페이지</h1>
      <RouterLink :to="{ name: 'search' }">조회</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'map' }">지도</RouterLink>
      <RouterView/>
    </div>
</template>

<style scoped>

</style>
