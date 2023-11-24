<template>
  <div class="board-item">
    <h3 class="board-title">제목 : {{ board.title }}</h3>
    <p class="board-content">내용 : {{ board.content }}</p>
    <p class="board-author">작성자 : {{ board.author.nickname }}</p>
    <p class="board-date">작성일 : {{ board.updated_at }}</p>
    <RouterLink
      class="board-detail-link"
      :to="{ name: 'BoardDetail', params: { id: board.id }, query: { type: 'QnA' } }"
    >
      [DETAIL]
    </RouterLink>

    <hr class="board-divider">
  </div>
</template>


<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  board: Object,
});
</script>

<style scoped>
.board-item {
  background-color: #fff;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.board-title {
  font-size: 3rem;
  color: #333;
  margin: 0;
}

.board-content {
  font-size: 2rem;
  color: #666;
  margin: 10px 0;
  font-weight: bold;
}

.board-author {
  font-size: 1.5rem;
  color: #888;
  margin: 0;
}

.board-date {
  font-size: 1.5rem;
  color: #888;
  margin: 0;
}

.board-detail-link {
  text-decoration: none;
  color: #375a7f;
  font-weight: bold;
  margin-top: 10px;
  display: inline-block;
  font-size: 2rem;
}

.board-divider {
  border: 0.5px solid #e0e0e0;
  margin-top: 10px;
}
</style>