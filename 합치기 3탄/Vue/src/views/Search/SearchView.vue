<script setup>
import { RouterLink, RouterView } from 'vue-router'



</script>

<template>
    <div>
        <h2>조회 페이지</h2>
        <RouterLink :to="{ name: 'searchlist' }">예금 조회</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'searchsavinglist'}">적금 조회</RouterLink>
        <RouterView />
    </div>
</template>

<style scoped>

</style>
