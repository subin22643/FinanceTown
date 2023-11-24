<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/counter'
import SearchListItem from '@/components/Search/SearchListItem.vue';


const store = useFinanceStore()
store.getDeposit()

// 검색창에서 선택한 값
const selectedBank = ref('')
const selectedMonth = ref('')
const Infos = store.deposits

// 버튼 누르면 이 안에 조회된 데이터가 들어감
const searchProducts = ref([])
const searchMonth = ref([])
const searchBank_Month = ref([])

// 버튼 클릭하면 true 값으로 변경 (searchSavingListItem에 prop 보내는 데이터가 달라짐)
const searchList = ref(false)


const searchDeposit = () => {
    const bank = Infos.filter((info) => selectedBank.value === info.kor_co_nm)
    const month = Infos.map(info => {
        const month_options = info.deposit_options.filter(option => option.save_trm === parseInt(selectedMonth.value.replace(/[^0-9]/g, '')));
        if (month_options.length !== 0) {
            return {
            ...info,
            deposit_options: month_options
            };
        }
        return null;
        }).filter(Boolean);

    const bank_month = bank.map(info => {
        const month_options = info.deposit_options.filter(option => option.save_trm === parseInt(selectedMonth.value.replace(/[^0-9]/g, '')));
        if (month_options.length !== 0) {
            return {
            ...info,
            deposit_options: month_options
            };
        }
        return null;
        }).filter(Boolean);
    searchProducts.value = bank
    searchMonth.value = month
    searchBank_Month.value = bank_month
    searchList.value = true
    // console.log(searchBank_Month.value)
    // console.log(searchProducts.value)
    // console.log(searchMonth.value)
    // console.log(searchList.value)
}


</script>

<template>
    <div>
        <hr>
        <h3>예금 목록입니다</h3>
        <br>
        <strong>검색 조건을 입력하세요</strong>
        <br>
        <v-select v-model="selectedBank"
            label="은행"
            :items="['한국스탠다드차타드은행', '부산은행', '대구은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '국민은행', '신한은행', '농협은행주식회사', '하나은행', '주식회사 케이뱅크', '수협은행', '주식회사 카카오뱅크', '토스뱅크 주식회사']"
            variant="outlined"
            ></v-select>
        <v-select v-model="selectedMonth"
            label="예치기간"
            :items="['6개월', '12개월', '24개월', '36개월']"
            variant="outlined"
            ></v-select>
        <v-btn variant="outlined" @click="searchDeposit">
            조회
            </v-btn>  
        <br>
        <hr>
        <hr>
        <SearchListItem v-show="!searchList" :deposits="store.deposits" :ox="searchList"/>
        <SearchListItem v-show="searchList" :deposits="searchProducts" :month="searchMonth" :bankmonth="searchBank_Month" :ox="searchList"/>
    </div>
</template>

<style scoped>

</style>
