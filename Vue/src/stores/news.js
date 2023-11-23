import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useNewsStore = defineStore('news', () => {
  const news = ref([])
  const tips = ref([])
  const URL = 'http://127.0.0.1:8000'
  const getNews = function() {
    axios({
      method: 'GET',
      url: `${URL}/news/`
    })
      .then(res => {
        console.log(res.data)
        news.value = res.data
      })
      .catch(err => console.log(err))
  }


  const getTips = function() {
    axios({
      method: 'GET',
      url: `${URL}/news/tips/`
    })
      .then(res => {
        console.log(res.data)
        tips.value = res.data
      })
      .catch(err => console.log(err))
  }
  
  return { news, URL, tips, getNews, getTips }
}, { persist: true })