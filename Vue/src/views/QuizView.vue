<template>
  <div v-if="!quizCompleted" class="quiz-container">
    <h1>오늘의 금융 Quiz</h1>
    <div v-if="currentSlide < quizData.length" :key="currentSlide">
      <div class="question">{{ quizData[currentSlide].question }}</div>
      <div class="answers">
        <label v-for="(answer, letter) in quizData[currentSlide].answers" :key="letter">
          <input type="radio" :name="`question${currentSlide}`" :value="letter">{{ letter }}: {{ answer }}
        </label>
      </div>
      <button @click="showResults">결과확인</button>
    </div>
  </div>
  <div v-if="resultShown">{{ resultText }}</div>
  <div v-if="quizCompleted" class="completion-message">
    <h1>오늘의 금융 Quiz</h1>
    <h3>오늘 제공된 퀴즈를 완료하셨습니다.</h3>
    <p><strong>{{ quizData[0].question }}</strong></p>
      <ul>
        <li v-for="(answer, key) in quizData[0].answers" :key="key">
          {{ key.toUpperCase() }}: {{ answer }}
        </li>
      </ul>
      <p>정답: {{ quizData[0].correct }}</p>
      <p>설명: {{ quizData[0].explanations }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const quizData = ref('') // 서버에서 가져온 퀴즈 데이터
const currentSlide = ref(0)
const resultShown = ref(false)
const resultText = ref('')
const quizCompleted = ref(false)

const showResults = () => {
  const question = quizData.value[currentSlide.value] // 현재 퀴즈 문제
  const currentQuiz = quizData.value[currentSlide.value]
  const quizId = currentQuiz.id
  const selector = `input[name=question${currentSlide.value}]:checked` // 올바른 선택자 문자열
  const userAnswer = document.querySelector(selector)?.value

  if (userAnswer === question.correct) {
    alert('정답입니다!') // 결과를 alert으로 표시
  } else {
    alert('오답입니다.') // 결과를 alert으로 표시
  }
  
  quizCompleted.value = true // 퀴즈 완료 상태를 true로 설정합니다.
  resultShown.value = true // 결과 표시 상태를 true로 설정합니다.

  submitQuizAnswer(quizId)
}


// 서버에서 퀴즈 데이터를 가져오는 함수
const getQuiz = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/quiz/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    if (res.data.alreadyAnswered) {
      quizCompleted.value = true // 이미 퀴즈를 풀었으면 퀴즈 완료 상태로 설정
      quizData.value = [res.data.quizzes]
    } else {
      quizData.value = [res.data.quizzes] // 퀴즈 데이터를 로드합니다.
      console.log(quizData.value)
      console.log(quizCompleted.value)
    }
  })
  .catch((err) => {
    console.log(err)
  })
}

const submitQuizAnswer = (quizId) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/quiz/already/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      quiz_id: quizId,
    }
  })
  .then((res) => {
    console.log('퀴즈 답변이 기록되었습니다.');
  })
  .catch((err) => {
    console.log('퀴즈 답변 기록 중 오류가 발생했습니다.', err)
  })
}

onMounted(getQuiz); // 컴포넌트가 마운트될 때 fetchQuizData 함수를 호출합니다.

</script>

<style scoped>
.quiz-container {
  text-align: left; 
  padding: 20px;
  margin-top: 30px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  border: 1px solid #e0e0e0;
}

.completion-message {
  text-align: left !important;
  padding: 20px !important;
  margin-top: 30px !important;
  background-color: #f8f9fa !important;
  border-radius: 8px !important;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
  border: 1px solid #e0e0e0 !important;
}

h1 {
  margin-top: 0; 
  padding-top: 1rem; 
  text-align: center;
}

.main .carousel-container + .quiz-container {
  align-self: flex-start; 
}
.question {
  margin-bottom: 1rem;
  font-size: 1.25rem; 
  font-weight: bold; 
}

.answers {
  text-align: left; 
  padding: 20px;
  margin-top: 30px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  border: 1px solid #e0e0e0;
}


.answers label {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #fff; 
  border: 2px solid #ddd; 
  border-radius: 20px; 
  margin-bottom: 0.5rem; 
  cursor: pointer; 
  transition: background-color 0.3s, transform 0.3s; 
}

.answers label:hover {
  background-color: #efefef; 
  transform: scale(1.05); 
}

.answers input {
  margin-right: 1rem;
  accent-color: #4b9cd3;
}

button {
  padding: 0.75rem 1.5rem;
  border: none;
  background-color: #5cb85c; 
  color: white;
  border-radius: 20px; 
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s, transform 0.3s;
}

button:hover {
  background-color: #4cae4c; 
  transform: scale(1.05); 
}

button:disabled {
  background-color: #ccc; 
}

#result {
  padding: 1rem;
  margin-top: 1rem;
  background-color: #dff0d8;
  color: #3c763d;
  border-radius: 10px; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
  font-size: 1.25rem;
  font-weight: bold;
}


.completion-message h3 {
  margin-top: 0;
  color: blue; 
  padding-bottom: 10px; 
  border-bottom: 1px solid #e0e0e0;
  text-align: center;
}

.completion-message ul {
  list-style-type: none; 
  padding: 0;
  margin: 15px 0; 
}

.completion-message li {
  background-color: #fff; 
  padding: 10px;
  margin-bottom: 10px; 
  border-radius: 4px; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
}

.completion-message p {
  background-color: #e9ecef;
  padding: 10px;
  border-radius: 4px; 
}

</style>