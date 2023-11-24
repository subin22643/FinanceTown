import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {

  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const loginUserNickname = ref('')
  const loginUsername = ref('')

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
    old_password:'',  //dj-rest-auth 라이브러리 사용시 비밀번호 변경 에러 메시지 필드명
    new_password2:'', //dj-rest-auth 라이브러리 사용시 비밀번호 변경 에러 메시지 필드명
    non_field_errors: '' //dj-rest-auth 라이브러리 사용시 로그인 데이터 불일치 에러 메시지 필드명
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
      alert("회원가입 성공")
      router.push({name: 'LogIn'})

      // 회원가입 후 자동 로그인
      // const password = password1
      // logIn({ username, password })
    })
    .catch(err => {
      console.log(err)
      setErrorMessages(err)
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
    loginUserNickname.value = res.data.nickname
    loginUsername.value = res.data.username
    token.value = res.data.key
    setProfileData() // 로그인 할 때 프로필 정보 받아오기
    router.push({ name: 'main' })
    // console.log(profileData.value)
  })
  .catch((err) => {
    setErrorMessages(err)
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
        router.push({ name: 'LogIn' })
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


// 프로필 수정 요청
  const update = () =>{
  // console.log(profileData)
    axios({
    method: 'put',
    url: `${API_URL}/accounts/profile/`,
    data : profileData.value ,
    headers: {
      'Authorization': `Token ${token.value}`
    }
    })
    .then((res) => {
      console.log(res.data)
      alert('프로필이 수정되었습니다.')
      router.push({ name: 'Profile' })
    })
    .catch((err) => {
      setErrorMessages(err)
    })
  }


//비밀번호 변경
const passwordChangeData = ref({
  old_password: '',
  new_password1: '',
  new_password2: ''
})


const changePassword = () => {
  console.log(passwordChangeData.value)
    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: passwordChangeData.value,
      headers: {
        'Authorization': `Token ${token.value}`
      }
    })
    .then((res) => {
        alert('비밀번호가 변경되었습니다.')
        passwordChangeData.value = {
          old_password: '',
          new_password1: '',
          new_password2: ''
        }
        logOut()
      })
    .catch((err) =>{
        console.error(err)
        setErrorMessages(err)
        passwordChangeData.value = {
          old_password: '',
          new_password1: '',
          new_password2: ''
        }
  })
}


//회원탈퇴
  const userDelete = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/profile/`,
      headers: {
      'Authorization': `Token ${token.value}`
    }
    })
      .then((res) => {
        alert('회원탈퇴가 처리되었습니다.')
        logOut()
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, token, isLogin, loginUserNickname, loginUsername, profileData, errorMessages, passwordChangeData,
    signUp, logIn, logOut, setProfileData, update, changePassword, userDelete, clearErrorMessages }
}, { persist: true })