<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { routerKey, useRoute } from 'vue-router'
import { useFinanceStore } from '../stores/counter';

const props = defineProps({
    deposits: Object,
})


const store = useFinanceStore()
const route = useRoute()
const product = ref('')
const options = ref('')

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/search/deposit-product/${route.params.fin_prdt_cd}`
    })
        .then((res) => {

            // console.log(res.data)
            product.value = res.data
            options.value = res.data.deposit_options
        })
        .catch((err) => {
            console.log(err)
        })
}) 

const cartButtons = ref({})


const cartOption = (product, option) => {
    const cart = JSON.parse(localStorage.getItem('cart')) || []
    const isDuplicate = cart.length > 0 && cart.find((item) => item[1].id === option.id)
    
    if (!isDuplicate) {
        cart.push([product, option])
        cartButtons.value[option.id] = '담은 옵션 삭제'        
    } else {
        cart.pop(option)
        cartButtons.value[option.id] = '옵션 담기'
    }
    localStorage.setItem('cart', JSON.stringify(cart))
}


const existingOption = JSON.parse(localStorage.getItem('save')) || []
if (existingOption.length > 0 && existingOption.find((item) => item.id === videoId)) {
    saveButton.value = '저장 취소'
}



</script>

<template>
    <div>
        <h2>해당 상품 옵션 보기</h2>
        <br>
        <h3>상품 정보</h3>
            <p>공시 제출월 [YYYYMM]: {{ product.dcls_month }}</p>
            <p>금융회사 코드: {{ product.fin_co_no }}</p>
            <p>금융상품 코드: {{ product.fin_prdt_cd }}</p>
            <p>기타 유의사항: {{ product.etc_note }}</p>
            <p>금융회사 제출일 [YYYYMMDDHH24MI]: {{ product.fin_co_subm_day }}</p>
            <p>금융 상품 코드: {{ product.fin_prdt_cd }}</p>
            <p>금융 상품명: {{ product.fin_prdt_nm }}</p>
            <p>가입 제한: {{ product.join_deny }}</p>
            <p>가입 대상: {{ product.join_member }}</p>
            <p>가입 방법: {{ product.join_way }}</p>
            <p>금융회사 명: {{ product.max_limit }}</p>
            <p>최고 한도: {{ product.mtrt_int }}</p>
            <p>우대 조건: {{ product.spcl_cnd }}</p>
        <br>
        <br>
        <hr>
        <h3>옵션 정보</h3>
        <div v-if="options" v-for="option in options" :key="option.id">
            <p>금융 상품 코드: {{ option.fin_prdt_cd }}</p>
            <p>저축 금리 유형: {{ option.intr_rate_type }}</p>
            <p>저축 금리 유형명: {{ option.intr_rate_type_nm }}</p>
            <p>저축 금리: {{ option.intr_rate }}</p>
            <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
            <p>저축기간: {{ option.save_trm }}</p>
            <button @click="cartOption(product, option)">{{ cartButtons[option.id] || '옵션 담기' }}</button>
            <hr/>
        </div>
    </div>
</template>

<style scoped>

</style>
