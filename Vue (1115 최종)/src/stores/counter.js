import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', () => {
  const deposits = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getDeposit = () => {
    axios({
      mehtod: 'GET',
      url: `${API_URL}/search/deposit-products`
    })
      .then(res => {
        // console.log(res.data)
        // console.log(res.data.response.result.baseList)
        deposits.value = res.data.response.result.baseList
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { deposits, API_URL, getDeposit }
}, { persist: true})
