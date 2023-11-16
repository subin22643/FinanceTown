import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('counter', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    console.log(payload.nickname, payload.birth_date, payload.gender, payload.phone_number)

    const { username, password1, password2, nickname,
      birth_date, gender, email, phone_number  } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname,
      birth_date, gender, email, phone_number
      }
    })
    .then((res) => {
      console.log(nickname, birth_date, gender, phone_number)

      const password = password1
      logIn({ username, password })
    })
    // .catch((err) => {
    //   console.log(err)
    // })
    .catch((err) => {
      if (err.response) {
        // 요청이 이루어졌으며 서버가 상태 코드로 응답했지만
        // 요청이 처리되지 않았습니다.
        console.log(err.response.data);
        console.log(err.response.status);
        console.log(err.response.headers);
      } else if (err.request) {
        // 요청이 이루어 졌으나 응답을 받지 못했습니다.
        console.log(err.request);
      } else {
        // 오류를 발생시킨 요청을 설정하는 중에 문제가 발생했습니다.
        console.log('Error', err.message);
      }
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true })
