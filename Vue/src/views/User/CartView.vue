<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const cartItem = ref(null)
cartItem.value = JSON.parse(localStorage.getItem('cart'))




</script>

<template>
    <div>
        <h2>담은 상품 보기</h2>
        <hr>
        <hr>
        <div v-if="cartItem">
            <div v-for="item in cartItem">
                <strong>상품 정보</strong>
                    <!-- <p>공시 제출월 [YYYYMM] : {{ item[0].dcls_month }}</p>
                    <p>금융회사 코드 : {{ item[0].fin_co_no }}</p>
                    <p>금융상품 코드 : {{ item[0].fin_prdt_cd }}</p>
                    <p>기타 유의사항 : {{ item[0].etc_note }}</p>
                    <p>금융회사 코드 : {{ item[0].fin_co_no }}</p>
                    <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ item[0].fin_co_subm_day }}</p>
                    <p>가입 제한 : {{ item[0].join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                    <p>가입 대상 : {{ item[0].join_member }}</p>
                    <p>가입 방법 : {{ item[0].join_way }}</p>
                    <p>최고 한도 : {{ item[0].max_limit }}</p>
                    <p>우대 조건 : {{ item[0].spcl_cnd }}</p>
                    <p>최고 우대 금리: {{ item[1].intr_rate2 }} -->
                    <p>금융상품 코드 : {{ item[0].fin_prdt_cd }}</p>
                    <p>금융 상품명 : {{ item[0].fin_prdt_nm }}</p>
                    <p>금융회사 명 : {{ item[0].kor_co_nm }}</p>
                    <p>만기 후 이자율 : {{ item[0].mtrt_int }}</p>
                <strong>옵션 정보</strong>
                    <p>금융 상품 코드: {{ item[1].fin_prdt_cd }}</p>
                    <p>저축 금리 유형: {{ item[1].intr_rate_type }}</p>
                    <p>저축 금리 유형명: {{ item[1].intr_rate_type_nm }}</p>
                    <p>저축 금리: {{ item[1].intr_rate }}</p>
                    <p>최고 우대 금리: {{ item[1].intr_rate2 }}</p>
                    <p>저축기간: {{ item[1].save_trm }}</p>
                <hr>
            </div>
        </div>
        <div v-else>담은 옵션이 없습니다</div>
    </div>
</template>

<style scoped>

</style>
