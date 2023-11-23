<template>
  <hr>
  <h1>금융퀴즈 공간</h1>
  <div v-if="!quizCompleted" class="quiz-container">
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
  <hr>
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
    } else {
      quizData.value = [res.data.quizzes] // 퀴즈 데이터를 로드합니다.
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
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f4f4f4; /* 배경색 */
  padding: 2rem;
  border-radius: 10px; /* 모서리 둥글게 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  max-width: 500px; /* 최대 너비 */
  margin: auto; /* 가운데 정렬 */
}

.question {
  margin-bottom: 1rem;
  font-size: 1.25rem; /* 글자 크기 */
  font-weight: bold; /* 글자 두께 */
}

.answers {
  margin-bottom: 1rem;
}

.answers label {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #fff; /* 배경색 */
  border: 2px solid #ddd; /* 테두리 */
  border-radius: 20px; /* 모서리 둥글게 */
  margin-bottom: 0.5rem; /* 여백 */
  cursor: pointer; /* 커서 모양 */
  transition: background-color 0.3s, transform 0.3s; /* 애니메이션 효과 */
}

.answers label:hover {
  background-color: #efefef; /* 호버 시 배경색 */
  transform: scale(1.05); /* 호버 시 크기 증가 */
}

.answers input {
  margin-right: 1rem;
  accent-color: #4b9cd3; /* 체크박스 색상 */
}

button {
  padding: 0.75rem 1.5rem;
  border: none;
  background-color: #5cb85c; /* 버튼 배경색 */
  color: white; /* 글자색 */
  border-radius: 20px; /* 모서리 둥글게 */
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s, transform 0.3s;
}

button:hover {
  background-color: #4cae4c; /* 호버 시 배경색 */
  transform: scale(1.05); /* 호버 시 크기 증가 */
}

button:disabled {
  background-color: #ccc; /* 비활성화 시 배경색 */
}

#result {
  padding: 1rem;
  margin-top: 1rem;
  background-color: #dff0d8; /* 결과 배경색 */
  color: #3c763d; /* 결과 글자색 */
  border-radius: 10px; /* 모서리 둥글게 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  font-size: 1.25rem; /* 글자 크기 */
  font-weight: bold; /* 글자 두께 */
}

.completion-message {
  text-align: left; /* 텍스트 왼쪽 정렬 */
  padding: 20px; /* 안쪽 여백 */
  margin-top: 30px; /* 위쪽 여백 */
  background-color: #f8f9fa; /* 연한 회색 배경색 */
  border-radius: 8px; /* 모서리 둥글게 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 박스 그림자 효과 */
  border: 1px solid #e0e0e0; /* 테두리 */
}

.completion-message h3 {
  margin-top: 0;
  color: blue; /* 질문 텍스트 색상 */
  padding-bottom: 10px; /* 질문 아래 패딩 */
  border-bottom: 1px solid #e0e0e0; /* 질문 아래 테두리 */
}

.completion-message ul {
  list-style-type: none; /* 목록 스타일 제거 */
  padding: 0;
  margin: 15px 0; /* 위아래 여백 */
}

.completion-message li {
  background-color: #fff; /* 배경색 */
  padding: 10px; /* 안쪽 여백 */
  margin-bottom: 10px; /* 아래쪽 여백 */
  border-radius: 4px; /* 모서리 둥글게 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 박스 그림자 효과 */
}

.completion-message p {
  background-color: #e9ecef; /* 배경색 */
  padding: 10px; /* 안쪽 여백 */
  border-radius: 4px; /* 모서리 둥글게 */
}

</style>