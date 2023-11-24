<script setup>
// 고민사항
// 문자로 입력시 '숫자로 입력하세요' 텍스트 추가하고 인풋값 초기화


import { useExchangeStore } from '@/stores/exchange'
import ExchangeRateListItem from './ExchangeRateListItem.vue';
import { ref, watch } from 'vue';

const store = useExchangeStore()
const Infos = store.exchanges
const selectedOption = ref('')
const inputSend = ref('')
const inputReceive = ref('')

const result = ref([])
const unit = ref('')


const exchangeMoney = () => {
    const currency = Infos.find((info) => selectedOption.value === info.cur_nm)
    if (currency) {
        // 환율값 안에 , 가 있으면 문자열로 인식해서 , 빼고 숫자로 반환
        if (typeof currency.tts === 'string' && currency.tts.includes(',')) {
            currency.tts = parseFloat(currency.tts.replace(/,/g, ''))
        }
        if (typeof currency.ttb === 'string' && currency.ttb.includes(',')) {
            currency.ttb = parseFloat(currency.ttb.replace(/,/g, ''))
        }
        // 국가별로 값 다르게 환산
        if (currency.cur_nm === '일본 옌') {
            if (inputReceive.value === 0 || inputReceive.value === '') {
                result.value = [
                    inputSend.value / currency.tts * 100,
                    0
                ];
            } else {
                result.value = [
                    inputSend.value / (currency.tts * 100),
                    currency.ttb / inputReceive.value * 100
                ];
            }
            unit.value = '옌'
        } else if (currency.cur_nm === '인도네시아 루피아') {
            if (inputReceive.value === 0 || inputReceive.value === '') {
                result.value = [
                    inputSend.value / currency.tts * 100,
                    0
                ];
            } else {
                result.value = [
                    inputSend.value / (currency.tts * 100),
                    currency.ttb / inputReceive.value * 100
                ];
            }
            unit.value = '루피아'
        } else if (currency.cur_nm === '한국 원') {
            result.value = [
                inputSend.value,
                inputReceive.value
            ]
            unit.value = '원'
        } else {
            if (inputReceive.value === 0 || inputReceive.value === '') {
                result.value = [
                    inputSend.value / currency.tts,
                    0
                ]
            }
            else {
                result.value = [
                    inputSend.value / currency.tts ,
                    currency.ttb / inputReceive.value
                ]
            }
            unit.value = currency.cur_nm.includes(' ') ? currency.cur_nm.split(' ')[1] : currency.cur_nm
        }
    }}

const cur_nm = store.exchanges.reduce((acc, ex) => {
    acc.push(ex.cur_nm)
    return acc
}, [])

watch([inputSend, inputReceive, selectedOption], () => {
    exchangeMoney()
})

</script>

<template>
    <div>
        <strong>통화 선택</strong>
        <form>
            <v-select v-model="selectedOption"
                label="통화"
                :items="cur_nm"
                variant="outlined"
                class="input-field"
                ></v-select>
            <v-form v-model="valid">
                <v-container>
                <v-row>
                    <v-col
                    cols="12"
                    md="4"
                    >
                    <v-text-field
                        type="number"
                        v-model="inputSend"
                        :rules="Number"
                        :counter="10"
                        label="송금 보낼 때"
                        required
                        hide-details
                        class="input-field"
                    ></v-text-field>
                    </v-col>

                    <v-col
                    cols="12"
                    md="4"
                    >
                    <v-text-field
                        type="number"
                        v-model="inputReceive"
                        :rules="Number"
                        :counter="10"
                        label="송금 받을 때"
                        hide-details
                        required
                        class="input-field"
                    ></v-text-field>
                    </v-col>
                </v-row>
                </v-container>
            </v-form>
        </form>
        <p>* 엔화, 인도네시아 루피아는 100 단위, 나머지 모두 1단위</p>
        <hr>
        <div>
            <strong>환율 계산한 결과</strong>
            <p v-if="selectedOption === ''">통화를 선택하세요
                <p>전신환(송금) 보내실 때: {{ inputSend }}원 -> {{ inputSend }}원</p>
                <p>전신환(송금) 받으실 때: {{ inputReceive }}원 -> {{ inputReceive }}원</p>
            </p>
            <p v-else>통화: {{ selectedOption }}
                <p v-if="inputSend === ''">전신환(송금) 보내실 때: 0원 -> 0{{ unit }}</p>
                <p v-else>전신환(송금) 보내실 때: {{ inputSend }}원 -> {{ result[0] }}{{ unit }}</p>
                <p v-if="inputReceive === ''">전신환(송금) 보내실 때: 0{{ unit }} -> 0원</p>
                <p v-else>전신환(송금) 받으실 때: {{ inputReceive }}{{ unit }} -> {{ result[1] }}원</p>
            </p>
        </div>
        <br>
        <hr>
        <hr>
        <strong>오늘의 환율</strong>
        <ExchangeRateListItem
            :exchange="store.exchanges" 
            />
    </div>


</template>

<style scoped>
.input-field {
  width: 80%;
}
</style>
