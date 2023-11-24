<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { routerKey, useRoute } from 'vue-router'
import { useFinanceStore } from '@/stores/counter';

const props = defineProps({
    deposits: Object,
})


const store = useFinanceStore()
const route = useRoute()
const product = ref('')
const options = ref('')
const existingOptions = JSON.parse(localStorage.getItem('cart')) || []
const optionsId = ref('')


onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/search/deposit-product/${route.params.fin_prdt_cd}`
    })
        .then((res) => {
            // console.log(res.data.deposit_options)
            product.value = res.data
            options.value = res.data.deposit_options
            optionsId.value = options.value.map((option) => option.id)
            const existingOptionsId = existingOptions.map(([_, option]) => option.id)
            for (const existingOptionId of existingOptionsId) {
                cartButtons.value[existingOptionId] = '담은 옵션 삭제'  
            }}
        )
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
        cart.splice(cart.findIndex(item => item[1].id === option.id), 1)
        cartButtons.value[option.id] = '옵션 담기'
    }
    localStorage.setItem('cart', JSON.stringify(cart))
}

</script>

<template>
    <div>
        <h2>해당 상품 옵션 보기</h2>
        <br>
        <h3>상품 정보</h3>
            <!-- <p>공시 제출월 [YYYYMM]: {{ product.dcls_month }}</p>
            <p>금융회사 코드: {{ product.fin_co_no }}</p>
            <p>금융상품 코드: {{ product.fin_prdt_cd }}</p>
            <p>금융회사 제출일 [YYYYMMDDHH24MI]: {{ product.fin_co_subm_day }}</p>
            <p>금융 상품 코드: {{ product.fin_prdt_cd }}</p>
            <p>가입 제한: {{ product.join_deny }}</p> -->
            <p>금융회사 명: {{ product.kor_co_nm }}</p>
            <p>금융 상품명: {{ product.fin_prdt_nm }}</p>
            <p>최고 한도: {{ product.max_limit }}</p>
            <p>가입 대상: {{ product.join_member }}</p>
            <p>가입 방법: {{ product.join_way }}</p>
            <p>우대 조건: {{ product.spcl_cnd }}</p>
            <p>기타 유의사항: {{ product.etc_note }}</p>
        <br>
        <br>
        <hr>
        <h3>옵션 정보</h3>
        <div v-if="options" v-for="option in options" :key="option.id">
            <!-- <p>금융 상품 코드: {{ option.fin_prdt_cd }}</p>
            <p>저축 금리 유형: {{ option.intr_rate_type }}</p> -->
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

button {
    background-color: #4CAF50; /* Green background */
    border: none; /* No borders */
    color: white; /* White text */
    padding: 15px 32px; /* Padding */
    text-align: center; /* Centered text */
    text-decoration: none; /* No underline */
    display: inline-block; /* Inline-block */
    font-size: 14px; /* Font size */
    margin: 4px 2px; /* Margin */
    cursor: pointer; /* Pointer cursor on hover */
    border-radius: 8px; /* Rounded corners */
}


button:hover {
    background-color: #45a049; /* Darker shade of green */
}

</style>
