<template>
  <hr>
  <h1>금융퀴즈 공간</h1>
  <div class="quiz-container">
    <div v-for="(question, index) in quizData" :key="index" v-show="currentSlide === index">
      <div class="question">{{ question.question }}</div>
      <div class="answers">
        <label v-for="(answer, letter) in question.answers" :key="letter">
          <input type="radio" :name="`question${index}`" :value="letter">{{ letter }}: {{ answer }}
        </label>
      </div>
    </div>
    <button v-if="currentSlide > 0" @click="showPreviousSlide">back</button>
    <button v-if="currentSlide < quizData.length - 1" @click="showNextSlide">next</button>
    <button v-if="currentSlide === quizData.length - 1" @click="showResults">결과확인</button>
    <div v-if="resultShown">{{ resultText }}</div>
  </div>
  <hr>
</template>

<script setup>
import { ref } from 'vue'

const quizData = ref([
  {
    question: '웹개발에 주로 사용되는 프론트언어는?',
    answers: {
      a: "일본어",
      b: "다랑어",
      c: "자바스크립트"
    },
    correct: 'c'
  },
  {
    question: '웹 디자인에 사용되는 언어는?',
    answers: {
      a: '미싱',
      b: 'css',
      c: '돈까s'
    },
    correct: 'b'
  },
  {
    question: '블로그 형태로 웹사이트를 쉽게 개발할 수 있는 방식을 무엇이라고 하는가?',
    answers: {
      a: 'CMS',
      b: 'WAX',
      c: 'KISWISS'
    },
    correct: 'a'
  }
])

const currentSlide = ref(0);
const resultShown = ref(false);
const resultText = ref('');

const showPreviousSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value -= 1;
  }
};

const showNextSlide = () => {
  if (currentSlide.value < quizData.value.length - 1) {
    currentSlide.value += 1;
  }
};

const showResults = () => {
  let numCorrect = 0;
  const answerContainers = document.querySelectorAll('.answers');
  quizData.value.forEach((question, index) => {
    const answerContainer = answerContainers[index];
    const selector = `input[name=question${index}]:checked`;
    const userAnswer = (answerContainer.querySelector(selector) || {}).value;

    if (userAnswer === question.correct) {
      numCorrect++;
    }
  });
  resultText.value = `${quizData.value.length}문제 중 ${numCorrect}개 정답입니다.`
  resultShown.value = true;
};
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
</style>