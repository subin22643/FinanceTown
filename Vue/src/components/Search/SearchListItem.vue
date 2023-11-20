<script setup>
import { useFinanceStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'



const props = defineProps({
    deposits: Object,
    month: Object,
    bankmonth: Object,
    ox: Boolean
})

const store = useFinanceStore()
store.getDeposit()


</script>

<template>
    <div v-if="month?.length === 0 && deposits?.length != 0 && ox === true">
        <p v-for="deposit in deposits" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ deposit.dcls_month }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ deposit.etc_note }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ deposit.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ deposit.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ deposit.join_member }}</p>
                <p>가입 방법 : {{ deposit.join_way }}</p> -->
                <p>금융회사 명 : {{ deposit.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ deposit.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ deposit.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in deposit.deposit_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="bankmonth?.length != 0 && ox === true">
        <p v-for="deposit in bankmonth">
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ deposit.dcls_month }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ deposit.etc_note }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ deposit.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ deposit.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ deposit.join_member }}</p>
                <p>가입 방법 : {{ deposit.join_way }}</p> -->
                <p>금융회사 명 : {{ deposit.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ deposit.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ deposit.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in deposit.deposit_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="month?.length != 0 && deposits?.length === 0 && ox === true">
        <p v-for="deposit in month" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ deposit.dcls_month }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ deposit.etc_note }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ deposit.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ deposit.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ deposit.join_member }}</p>
                <p>가입 방법 : {{ deposit.join_way }}</p> -->
                <p>금융회사 명 : {{ deposit.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ deposit.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ deposit.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in deposit.deposit_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="bankmonth?.length === 0 && month?.length != 0 && deposits?.length != 0 && ox === true">
        <p>조건에 맞는 상품이 없습니다</p>
    </div>

    <div v-if="ox === false">
        <p v-for="deposit in deposits" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ deposit.dcls_month }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ deposit.etc_note }}</p>
                <p>금융회사 코드 : {{ deposit.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ deposit.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ deposit.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ deposit.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ deposit.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ deposit.join_member }}</p>
                <p>가입 방법 : {{ deposit.join_way }}</p> -->
                <p>금융회사 명 : {{ deposit.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ deposit.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ deposit.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ deposit.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in deposit.deposit_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: deposit.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
 
</template>

<style scoped>

</style>
