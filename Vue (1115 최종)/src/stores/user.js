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
      email, age, money, salary, financial_products  } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname,
      email, age, money, salary, financial_products
      }
    })
    .then((res) => {
      const password = password1
      logIn({ username, password })
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/login/`,
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
      url: `${API_URL}/dj-rest-auth/logout/`,
    })
      .then((res) => {
        token.value = null
        console.log(token.value)
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true })
