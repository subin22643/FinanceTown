<script setup>
import { onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchange'
import ExchangeRateList from '@/components/Exchange/ExchangeRateList.vue'

const store = useExchangeStore()

onMounted(() => {
    store.getExchanges()
})

</script>

<template>
    <div>
        <h3>환율 계산기</h3>
        <ExchangeRateList />
    </div>
</template>

<style scoped>

</style>
