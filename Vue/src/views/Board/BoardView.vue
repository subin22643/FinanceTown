<template>
  <div class="board-page">
    <h1 class="board-title">게시판 페이지</h1>
    <div class="board-links">
      <RouterLink :to="{ name: 'ProductBoardView' }" class="board-link">
        <button class="board-button">금융 상품 리뷰 게시판</button>
      </RouterLink>

      <RouterLink :to="{ name: 'QnABoardView' }" class="board-link">
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
  font-family: 'Black Han Sans', sans-serif; /* 전체 페이지에 Black Han Sans 폰트 적용 */
  background-color: #FAFAFA; /* 배경색 일치 */
  margin: 50px auto; /* 상단 여백 조정 및 중앙 정렬 */
  width: 100%; /* 전체 너비 적용 */
  max-width: 700px; /* 최대 너비 일치 */
  border: 1px solid #B3B3B3; /* 테두리 스타일 일치 */
  border-radius: 8px; /* 테두리 둥글기 일치 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 일치 */
}

.board-title {
  font-size: 3em; /* 제목 폰트 크기 조정 */
  color: #375a7f; /* 제목 색상 일치 */
  margin-bottom: 1rem; /* 하단 여백 조정 */
  font-weight: normal; /* Black Han Sans는 볼드 스타일을 지원하지 않을 수 있음 */
}

.board-links {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem; /* 하단 여백 조정 */
}

.board-link {
  margin: 0 10px; /* 링크 사이의 간격 조정 */
}

.board-button {
  background-color: #375a7f; /* 버튼 배경색 일치 */
  color: white; /* 버튼 텍스트 색상 흰색으로 설정 */
  border: none; /* 테두리 제거 */
  border-radius: 5px; /* 테두리 둥글기 일치 */
  padding: 0.8rem 1.6rem; /* 버튼 패딩 조정 */
  font-size: 1.5rem; /* 버튼 폰트 크기 조정 */
  cursor: pointer; /* 커서 포인터 스타일 */
  transition: background-color 0.3s; /* 배경 색상 전환 효과 */
  margin: 0 5px; /* 버튼 사이의 간격 조정 */
}

.board-button:hover {
  background-color: #2c446b; /* 호버 색상 조정 */
}

.separator {
  color: #B3B3B3; /* 구분선 색상 일치 */
  font-size: 1rem; /* 구분선 폰트 크기 조정 */
}

</style>
