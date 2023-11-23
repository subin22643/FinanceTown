import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore('exchange', () => {
  const exchanges = ref([])
  const URL = 'http://127.0.0.1:8000'
  const getExchanges = function() {
    axios({
      method: 'GET',
      url: `${URL}/exchanges`
    })
      .then(res => {
        console.log(res.data)
        exchanges.value = res.data.response
      })
      .catch(err => console.log(err))
  }
  return { exchanges, URL, getExchanges }
}, { persist: true })
