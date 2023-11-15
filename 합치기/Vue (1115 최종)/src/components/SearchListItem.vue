<script setup>
defineProps({
    deposit:Object
})
</script>

<template>
    <div>
        <!-- <p>공시 제출월 [YYYYMM] : {{ deposit.dcls_month }}</p>
        <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
        <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
        <p>기타 유의사항 : {{ deposit.etc_note }}</p>
        <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
        <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ deposit.fin_co_subm_day }}</p>
        <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p> -->
        <p>금융 상품명 : {{ deposit.fin_prdt_nm }}</p>
        <!-- <p>가입 제한 : {{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
        <p>가입 대상 : {{ deposit.join_member }}</p>
        <p>가입 방법 : {{ deposit.join_way }}</p> -->
        <p>금융회사 명 : {{ deposit.kor_co_nm }}</p>
        <!-- <p>최고 한도 : {{ deposit.max_limit }}</p> -->
        <!-- <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p> -->
        <!-- <p>우대 조건 : {{ deposit.spcl_cnd }}</p> -->
        <hr>
    </div>
</template>

<style scoped>

</style>
