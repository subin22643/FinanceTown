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
    console.log(payload)
    // path('dj-rest-auth/', include('dj_rest_auth.urls')),
    // path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    const { username, password1, password2, nickname,
      email, gender, phone_number, age, money, salary } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname,
      email, age, money, salary
      }
    })
    .then((res) => {
      console.log(res)
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
        console.log(token.value)
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true })
