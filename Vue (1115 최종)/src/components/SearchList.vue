<script setup>
import { useFinanceStore } from '../stores/counter'
import SearchListItem from './SearchListItem.vue';

const store = useFinanceStore()
</script>

<template>
    <div>
        <h3>예금/적금 목록입니다</h3>
        <SearchListItem v-for="deposit in store.deposits" :key="deposit.id" :deposit="deposit"/>
    </div>
</template>

<style scoped>

</style>
