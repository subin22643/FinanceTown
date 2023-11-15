<script setup>
import { onMounted } from 'vue'
import { useFinanceStore } from '../stores/counter';
import axios from 'axios'
import SearchList from '../components/SearchList.vue'

const store = useFinanceStore()

onMounted(() => {
    store.getDeposit()
})

</script>

<template>
    <div>
        <h2>조회 페이지(예적금 목록 출력)</h2>
        <SearchList/>
    </div>
</template>

<style scoped>

</style>
