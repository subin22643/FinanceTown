<<<<<<< HEAD
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from './user'
import { useRouter } from 'vue-router';
import axios from 'axios'

export const useBoardStore = defineStore('counter', () => {
=======
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';
import axios from 'axios'

export const useBoardStore = defineStore('board', () => {
>>>>>>> jonggil
  const productBoards = ref([])
  const QnABoards = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const useStore = useUserStore()
  const router = useRouter()

<<<<<<< HEAD
  const getProductBoards = function () {
    
    //금융 상품 리뷰 게시판 조회 요청
=======
  //금융 상품 리뷰 게시판 조회 요청
  const getProductBoards = function () {
>>>>>>> jonggil
    axios({
      method: 'get',
      url : `${API_URL}/boards/product/`,
      headers: {
          Authorization: `Token ${useStore.token}`
        }
      })
      .then((res) =>{
        productBoards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
<<<<<<< HEAD
    
    const getQnABoards = function () {
      //QnA 게시판 요청 조회 요청
      axios({
        method: 'get',
        url : `${API_URL}/boards/QnA/`,
        headers: {
          Authorization: `Token ${useStore.token}`
        }
      })
        .then((res) =>{
          QnABoards.value = res.data
        })
        .catch((err) => {
          console.log(err)
          setErrorMessages(err)
        })
      }
    
  const createProductBoards = function (boardData) {
    //상품 리뷰 게시판 생성
=======


  //QnA 게시판 요청 조회 요청
  const getQnABoards = function () {
    axios({
      method: 'get',
      url : `${API_URL}/boards/QnA/`,
      headers: {
        Authorization: `Token ${useStore.token}`
      }
    })
      .then((res) =>{
        QnABoards.value = res.data
      })
      .catch((err) => {
        console.log(err)
        setErrorMessages(err)
      })
    }


  //상품 리뷰 게시판 생성
  const createProductBoards = function (boardData) {
>>>>>>> jonggil
    axios({
      method: 'post',
      url : `${API_URL}/boards/product/`,
      data: boardData,
      headers: {
        Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) =>{
      console.log(res.data)
      alert("게시판이 등록 되었습니다.")
<<<<<<< HEAD
      router.push({ name: 'BoardView' })
=======
      router.push({ name: 'ProductBoardView' })
>>>>>>> jonggil
    })
    .catch((err) => {
      console.log(err)
      setErrorMessages(err)
    })
  }
  
<<<<<<< HEAD
  const createQnABoards = function (boardData) {
      //QnA게시판 생성
=======

  //QnA게시판 생성
  const createQnABoards = function (boardData) {
>>>>>>> jonggil
      console.log(boardData)
      axios({
        method: 'post',
        url : `${API_URL}/boards/QnA/`,
        data : boardData,
        headers: {
          Authorization: `Token ${useStore.token}`
        }
      })
      .then((res) =>{
        console.log(res.data)
        alert("게시판이 등록 되었습니다.")
<<<<<<< HEAD
        router.push({ name: 'BoardView' })
=======
        router.push({ name: 'QnABoardView' })
>>>>>>> jonggil
      })
      .catch((err) => {
        console.log(err)
        setErrorMessages(err)
      })
    }
<<<<<<< HEAD
  
=======
>>>>>>> jonggil

  //에러메시지 처리하는 로직
  const errorMessages = ref({
    title: '',
    content: '',
  })


  //에러메시지 담기
  const setErrorMessages = (err) => {
    if (err.response && err.response.data) {
      const errors = err.response.data;
      for (const key in errorMessages.value) {
        if (errors.hasOwnProperty(key)) {
          errorMessages.value[key] = errors[key].join(', ')
        } else {
          errorMessages.value[key] = '' // 에러가 없는 경우 빈 문자열로 초기화
        }
      }
    }
  }

<<<<<<< HEAD
=======

>>>>>>> jonggil
  //에러메시지 초기화
  const clearErrorMessages = () => {
    for (const key in errorMessages.value) {
      errorMessages.value[key] = '';
    }
  };

<<<<<<< HEAD
=======

>>>>>>> jonggil
  return { 
      API_URL,  
      productBoards, 
      QnABoards, 
      errorMessages,
      getProductBoards,
      getQnABoards,
      createProductBoards,
      createQnABoards,
      setErrorMessages,
      clearErrorMessages
  }
    }
    , { persist: true }
    )