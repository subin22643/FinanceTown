<script setup>
import { onMounted } from 'vue'
import { useExchangeStore } from '../stores/exchange'
import ExchangeRateList from '@/components/ExchangeRateList.vue'


// const URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
// const API_KEY = 'Uy013h5RQvCr44y7rRuPpQxSqr2m7TlC'

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
