<script setup>
// 고칠점
// 엔화랑 인도네시아 루피아 계산 별도로 해야함
// 환전 리스트에 한국 없애야함
// 바레인 디나르, 유로, 스위스 프랑 등 안되는 국가 수정


// 고민사항
// 출력 페이지에 통화 단위 추가하고싶음
// 문자로 입력시 '숫자로 입력하세요' 텍스트 추가하고 인풋값 초기화


import { useExchangeStore } from '@/stores/exchange'
import ExchangeRateListItem from '@/components/Exchange/ExchangeRateListItem.vue';
import { ref, watch } from 'vue';

const store = useExchangeStore()
const Infos = store.exchanges
const selectedOption = ref('')
const inputSend = ref('')
const inputReceive = ref('')

const result = ref([])

const exchangeMoney = () => {
    const currency = Infos.find((info) => selectedOption.value === info.cur_nm)
    console.log(inputReceive.value)
    if (currency) {
        if (inputReceive.value === 0 || inputReceive.value === '') {
            result.value = [
                currency.tts * inputSend.value,
                0
            ]
        }
        else {
        result.value = [
            inputSend.value / currency.tts ,
            currency.ttb / inputReceive.value
        ]}
    }
};


watch([inputSend, inputReceive, selectedOption], () => {
    exchangeMoney()
})

</script>

<template>
    <div>
        <strong>이건 내가 검색할거</strong>
        <form>
            <div class="dropbox">
                <select v-model="selectedOption">
                <option v-for="exch in store.exchanges" :key="exch.id">
                    {{ exch.cur_nm }}
                </option>
                </select>
            </div>
            <div class="input1">
                <label for="send">송금 보낼때 </label>
                <input type="number" id="send" v-model="inputSend">
            </div>
            <div class="input2">
                <label for="receive">송금 받을때 </label>
                <input type="number" id="receive" v-model=inputReceive>
            </div>
        </form>
        <p>* 엔화, 인도네시아 루피아는 100 단위, 나머지 모두 1단위</p>
        <hr>
        <div>
            <strong>환율 계산한 결과</strong>
            <p>통화: {{ selectedOption }}</p>
            <p>전신환(송금) 보내실 때: {{ inputSend }}원 -> {{ result[0] }}</p>
            <p>전신환(송금) 받으실 때: {{ inputReceive }} -> {{ result[1] }}원</p>
        </div>
        <br>
        <hr>
        <hr>
        <strong>환율표 환율표 환율표 환율표</strong>
        <ExchangeRateListItem
            v-for="exchange in store.exchanges" 
            :exchange="exchange" 
            />

 
    </div>


</template>

<style scoped>

</style>
