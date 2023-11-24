<template>
  <div class="create-board-page">
    <h1 class="create-board-title">게시글 작성</h1>
    <form @submit.prevent="createBoard" class="create-board-form">
      <div>
        <label for="title" class="create-board-label">제목</label>
        <input type="text" v-model.trim="title" id="title" class="create-board-input">
        <div v-if="store.errorMessages.title" class="error-message">{{ store.errorMessages.title }}</div>
      </div>
      <div>
        <label for="content" class="create-board-label">내용</label>
        <textarea v-model.trim="content" id="content" class="create-board-textarea"></textarea>
        <div v-if="store.errorMessages.content" class="error-message">{{ store.errorMessages.content }}</div>
      </div>
      <div>
        <label for="category" class="create-board-label">분류</label>
        <select v-model="Category" id="category" class="create-board-select">
          <option value="product">금융 상품 리뷰 게시판</option>
          <option value="QnA">상담 게시판</option>
        </select>
      </div>
      <input type="submit" class="create-board-submit">
    </form>
  </div>
</template>


<script setup>
import { ref,onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'

const store = useBoardStore()
const title = ref('')
const content = ref('')
const Category = ref('')

const createBoard = () => {
  const boardData = ref({title:title.value ,content:content.value})
  if(Category.value == "product"){
    store.createProductBoards(boardData.value)
  }
  else if(Category.value == "QnA"){
    store.createQnABoards(boardData.value)
  }
  else {
    alert('분류를 선택해 주세요')
  }
}

onMounted(() => {
  store.clearErrorMessages()
})

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

.create-board-page {
  text-align: center;
  padding: 40px; /* 여백을 늘립니다. */
  background-color: #FAFAFA;
  margin: 50px auto;
  width: 80%;
  max-width: 700px;
  border: 1px solid #B3B3B3;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Black Han Sans', sans-serif;
}

.create-board-title {
  color: #375a7f;
  margin-bottom: 2rem;
  font-size: 4em;
}

.create-board-form {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* 입력란을 왼쪽 정렬로 맞춥니다. */
  width: 100%;
  max-width: 500px; /* 폼의 최대 너비를 설정합니다. */
  margin: auto; /* 폼을 중앙 정렬합니다. */
}

.create-board-label {
  font-weight: bold;
  text-align: left;
  display: block;
  margin-bottom: 0.5rem; /* 라벨과 입력란 간의 간격을 조정합니다. */
  font-size: 3em; /* 라벨의 폰트 크기를 조정합니다. */
}

.create-board-input,
.create-board-select, .create-board-textarea  {
  width: 500px; /* 부모 요소의 전체 너비를 사용합니다. */
  padding: 1rem; /* 입력란의 패딩을 늘립니다. */
  margin-bottom: 1rem; /* 입력란 간의 간격을 조정합니다. */
  font-size: 1em; /* 입력란의 폰트 크기를 조정합니다. */
  border: solid gray 3px;
  font-family: 'Noto Sans KR', sans-serif;
}


.create-board-submit {
  width: auto; /* 제출 버튼의 너비를 내용에 맞게 조정합니다. */
  padding: 1rem 2rem; /* 제출 버튼의 패딩을 늘립니다. */
  font-size: 2em; /* 제출 버튼의 폰트 크기를 조정합니다. */
  margin-top: 1rem; /* 제출 버튼 위의 간격을 조정합니다. */
  align-self: center; /* 버튼을 폼의 중앙에 위치시킵니다. */
}

.error-message {
  color: red;
  font-size: 0.8rem;
  margin-top: 5px;
  align-self: center; /* 에러 메시지를 중앙에 위치시킵니다. */
}
</style>
