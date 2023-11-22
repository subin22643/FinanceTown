<script setup>
import { onMounted,ref } from 'vue'
import { useNewsStore } from '@/stores/news'

const store = useNewsStore()

onMounted( () => {
    store.getTips()
})

</script>

<template>
    <div>
        <h3>오늘의 금융 꿀팁</h3>
        <p v-for="tip in store.tips.data">
            <a :href="tip.originUrl.replace('www.', 'fine.')">{{ tip.subject }}</a>
            <hr>
        </p>
    </div>
</template>

<style scoped>

</style>