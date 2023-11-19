import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const pageNickname = ref('')

  //에러메시지 출력
  const errorMessages = ref({
    username: '',
    password: '',
    password1: '',
    password2: '',
    nickname: '',
    email: '',
    gender: '',
    phone_number: '',
    age: '',
    money: '',
    salary: '',
    non_field_errors: '' //dj-rest-auth 라이브러리 사용시 에러 메시지 필드명
    // financial_products: ''
  })
  
  //에러메시지 초기화
  const clearErrorMessages = () => {
    for (const key in errorMessages.value) {
      errorMessages.value[key] = '';
    }
  };

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


  // 로그인 여부
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  //회원가입
  const signUp = function (payload) {
    const { username, password1, password2, nickname,
      email, gender, phone_number, age, money, salary } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, nickname,
      email, gender, phone_number, age, money, salary
      }
    })
    .then((res) => {
      console.log("회원가입 성공")
      router.push({name: 'Complete'})

      // 회원가입 후 자동 로그인
      // const password = password1
      // logIn({ username, password })
    })
    .catch(err => {
      setErrorMessages(err)
      //   if (err.response && err.response.data) {
      //   const errors = err.response.data;
      //   for (const key in errorMessages.value) {
      //     if (errors.hasOwnProperty(key)) {
      //       errorMessages.value[key] = errors[key].join(', ')
      //     } else {
      //       errorMessages.value[key] = '' // 에러가 없는 경우 빈 문자열로 초기화
      //     }
      //   }
      // }
      })
  }

  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload
    
    return axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        pageNickname.value = res.data.nickname
        token.value = res.data.key
        setProfileData() //로그인 할 때 프로필 정보 받아오기
        router.push({ name: 'main' })
        // console.log(profileData.value)
      })
      .catch((err) => {
        setErrorMessages(err)
        // console.log(err)
      //   if (err.response && err.response.data) {
      //   const errors = err.response.data;
      //   for (const key in errorMessages.value) {
      //     if (errors.hasOwnProperty(key)) {
      //       errorMessages.value[key] = errors[key].join(', ')
      //     } else {
      //       errorMessages.value[key] = ''
      //     }
      //   }
      // }
      })
  }

  //로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        profileData.value = ''
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  //프로필 정보 가져오기
  const profileData = ref('')
  const setProfileData = () =>{
    axios({
    method: 'get',
    url: `${API_URL}/accounts/profile/`,
    headers: {
      'Authorization': `Token ${token.value}`
    }
  })
  .then((res) => {
    profileData.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
  }

  // profile update 요청
  const update = () =>{
  // console.log(profileData)
    axios({
    method: 'put',
    url: `${API_URL}/accounts/profile/`,
    data : profileData.value
      // username: profileData.username,
      // nickname: profileData.nickname,
      // password1: profileData.password1,
      // password2: profileData.password2,
      // age: profileData.age,
      // email: profileData.email,
      // gender: profileData.gender,
      // phone_number: profileData.phone_number,
      // money: profileData.money,
      // salary: profileData.salary,
      // financial_products: profileData.financial_products,
    ,
    headers: {
      'Authorization': `Token ${token.value}`
    }
    })
    .then((res) => {
      console.log(res.data)
      router.push({ name: 'Profile' })
    })
    .catch((err) => {
      setErrorMessages(err)
    })
  }
  return { API_URL, token, isLogin, pageNickname, profileData, errorMessages, 
    signUp, logIn, logOut, setProfileData, update, clearErrorMessages }
}, { persist: true })
