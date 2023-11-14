<script setup>

import axios from 'axios'


const URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1'

const params = {
    'auth': 'c8753044e7de2142207743a6737640ce',
    'topFinGrpNo': '020000',
    'pageNo': '1',
}

</script>

<template>
    <div>
        <h2>조회 페이지(예적금 목록 출력)</h2>
    </div>
</template>

<style scoped>

</style>
