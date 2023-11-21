<script setup>
import { onMounted } from 'vue'
import { useNewsStore } from '@/stores/news'

const store = useNewsStore()

onMounted(() => {
    store.getTips()
})

const tipsList = store.tips  

</script>

<template>
    <div>
        <h3>오늘의 금융 꿀팁</h3>
        <p>{{ tipsList }} </p>
            <!-- <p v-for="tip in tipsList">

            </p> -->
    </div>
</template>

<style scoped>

</style>