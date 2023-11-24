<template>
  <div class="board-page">
    <h1 class="board-title">게시판 페이지</h1>
    <div class="board-links">
      <RouterLink to="{ name: 'ProductBoardView' }" class="board-link">
        <button class="board-button">금융 상품 리뷰 게시판</button>
      </RouterLink>
      <span class="separator"> | </span>
      <RouterLink to="{ name: 'QnABoardView' }" class="board-link">
        <button class="board-button">상담 게시판</button>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

.board-page {
  text-align: center;
  padding: 20px;
  font-family: 'Nanum Gothic', sans-serif;
  background-color: #e0f7fa;
  margin: 10px auto; /* 중앙 정렬 */
  width: 90%; /* 페이지의 전체 너비를 조정 */
  max-width: 1200px; /* 최대 너비 설정 */
}

.board-title {
  font-size: 28px; /* 글자 크기 증가 */
  color: #0277bd; /* 상단 바의 글자 색상과 동일하게 설정 */
  font-family: 'Black Han Sans', sans-serif;
  margin-bottom: 30px; /* 여백 증가 */
}

.board-links {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px; /* 링크 하단에 여백 추가 */
}

.board-link {
  text-decoration: none;
}

.board-button {
  background-color: #b3e5fc; /* 하늘색에 어울리는 더 밝은 파란색으로 설정 */
  color: #0277bd; /* 버튼 텍스트 색상도 하늘색과 어울리게 설정 */
  border: 2px solid #81d4fa;
  border-radius: 5px; /* 테두리 둥글게 설정 */
  padding: 15px 30px; /* 버튼 패딩 증가 */
  font-family: 'Nanum Gothic', sans-serif;
  font-size: 18px; /* 폰트 사이즈 증가 */
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 2px 2px 0 #bbb; /* 그림자 색상을 더 가볍게 조정 */
  margin: 0 5px; /* 버튼 사이의 간격 조정 */
}

.board-button:hover {
  background-color: #81d4fa; /* 호버 시 더 밝은 회색으로 변경 */
}

.separator {
  margin: 0 10px;
  font-size: 20px;
  color: #29b6f6;
  font-family: 'Nanum Gothic', sans-serif;
}
</style>
