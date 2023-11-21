<script setup>
import { onMounted } from 'vue'
import { useNewsStore } from '@/stores/news'

const store = useNewsStore()

//조회 되면 onmounted로 바꾸기
const test = () =>{
    store.getTips()
}


const tipsList = store.tips  

</script>

<template>
    <div>
        <button @click="test">조회 test</button>
        <h3>오늘의 금융 꿀팁</h3>
        <p>{{ tipsList }} </p>
    </div>
</template>

<style scoped>

</style>