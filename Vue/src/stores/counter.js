import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', () => {
  const deposits = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getDeposit = () => {
    axios({
      mehtod: 'get',
      url: `${API_URL}/search`
    })
      .then(res => {
        console.log(res.data.response) 
        deposits.value = res.data.response
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { deposits, API_URL, getDeposit }
}, { persist: true})



export const useSavingStore = defineStore('saving', () => {
  const savings = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getSaving = () => {
    axios({
      mehtod: 'get',
      url: `${API_URL}/search/saving-products`
    })
      .then(res => {
        // console.log(res.data.response)
        savings.value = res.data.response
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { savings, API_URL, getSaving }
}, { persist: true})
