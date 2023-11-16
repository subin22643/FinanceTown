<script setup>
import { ref } from 'vue'

defineProps({
    exchange: Object,
})

</script>

<template>
    <div>
        <!-- <p>조회결과: {{ exchange.result }}</p> -->
        <p>통화코드: {{ exchange.cur_unit }}</p>
        <p>국가/통화명: {{ exchange.cur_nm }}</p>
        <p>전신환(송금) 보내실 때: {{ exchange.tts }}</p> 
        <p>전신환(송금) 받으실 때: {{ exchange.ttb }}</p>
        <!-- <p>매매 기준율: {{ exchange.deal_bas_r }}</p>  -->
        <hr>
    </div>
</template>

<style scoped>

</style>
