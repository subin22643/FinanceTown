<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createBoard">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
        <div v-if="store.errorMessages.title" class="error-message">{{ store.errorMessages.title }}</div>
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
        <div v-if="store.errorMessages.content" class="error-message">{{ store.errorMessages.content }}</div>
      </div>
      <div>
        <label for="category">분류:</label>
        <select v-model="Category" id="category">
          <option value="product">금융 상품 리뷰 게시판</option>
          <option value="QnA">상담 게시판</option>
        </select>
      </div>>
      <input type="submit">
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

<style>
.error-message {
    color: red;
    font-size: 0.8em;
    margin-top: 5px;
}
</style>
