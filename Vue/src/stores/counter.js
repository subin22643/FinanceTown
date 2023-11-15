import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore('exchange', () => {
  const exchanges = ref([])
  const params = {
    authkey: 'Uy013h5RQvCr44y7rRuPpQxSqr2m7TlC',
    searchdate: '20231014',
    data: 'AP01'
  }
  // const URL = 'http://127.0.0.1:8000'
  const URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
  const getExchanges = function() {
    axios({
      method: 'GET',
      url: 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON',
      params: params.value
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => console.log(err))
  }
  return { exchanges, URL, getExchanges }
}, { persist: true })