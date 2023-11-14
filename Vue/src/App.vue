<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <div class ="ms-4 mt-3">
      <h1>메인 페이지</h1>
      <RouterLink :to="{ name: 'search' }">조회</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'map' }">지도</RouterLink>
      <RouterView/>
    </div>
</template>

<style scoped>

</style>
