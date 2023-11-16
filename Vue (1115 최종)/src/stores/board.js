import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBoardStore = defineStore('counter', () => {
  const boards = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  // const token = ref(null)

  const getFinanceBoards = function () {
    
    //금융 상품 리뷰 게시판 데이터 요청
    axios({
      method: 'get',
      url : `${API_URL}/boards/finance/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        boards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }

  const getProductBoards = function () {

    //상품 자랑 게시판 데이터 요청
    axios({
      method: 'get',
      url : `${API_URL}/boards/product/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        boards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createFinanceBoards = function () {
      //금융 상품 리뷰 게시판 데이터 요청
      axios({
        method: 'post',
        url : `${API_URL}/boards/finance/`,
        // headers: {
        //   Authorization: `Token ${token.value}`
        // }
      })
        .then((res) =>{
          boards.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }

  const createProductBoards = function () {
    //금융 상품 리뷰 게시판 데이터 요청
    axios({
      method: 'post',
      url : `${API_URL}/boards/finance/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        boards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }

    return { 
      boards, API_URL,
      getFinanceBoards,
      getProductBoards,
      createFinanceBoards,
      createProductBoards
    }
    }
    , { persist: true }
    )
