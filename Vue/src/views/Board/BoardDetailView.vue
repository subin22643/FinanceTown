<template>
  <div>
    <h1 class="detail-title">Detail</h1>
    <div v-if="board" class="form-container">
      <div class="form-group">
        <label for="title">제목</label>
        <input id='title' :readonly="isBoardReadonly" v-model="board.title" />
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea id="content" :readonly="isBoardReadonly" v-model="board.content"></textarea>
      </div>
      <div class="form-group">
        <label for="created">작성일</label>
        <input id="created" v-model="board.created_at" readonly>
      </div>
      <div class="form-group">
        <label for="updated">수정일</label>
        <input id="updated" v-model="board.updated_at" readonly>
      </div>
      
      <div class="like-section">
        <button v-if="!board.liked" @click="toggleLike(board)" class="like-button">👍 좋아요 {{ board.likeCount }}</button>
        <button v-if="board.liked" @click="toggleLike(board)" class="like-button">👎 좋아요 취소 {{ board.likeCount }}</button>
      </div>
      <div v-if="board.author.username === useStore.loginUsername" class="button-group">
        <button v-if="isBoardReadonly" @click="toggleBoardReadonly" class="edit-button">수정</button>
        <button v-if="isBoardReadonly" @click="boardDelete" class="delete-button">삭제</button>
        <button v-if="!isBoardReadonly" @click="boardUpdate" class="save-button">저장</button>
      </div>
    </div>

    <div v-if="comments">
      <h2 class="comment-title">댓글</h2>
      <div v-for="comment in comments" :key="comment.id" class="comment-container">
        <div class="form-group">
          <label for="content">{{ comment.author.nickname }}:</label>
          <textarea id="content" :readonly="comment.isCommentReadonly" v-model="comment.content"></textarea>
        </div>
        <div v-if="comment.author.username === useStore.loginUsername" class="button-group">
          <button v-if="comment.isCommentReadonly" @click="toggleCommentReadonly(comment)" class="edit-button">댓글 수정</button>
          <button v-if="comment.isCommentReadonly" @click="commentDelete(comment)" class="delete-button">댓글 삭제</button>
          <button v-if="!comment.isCommentReadonly" @click="commentUpdate(comment)" class="save-button">댓글 저장</button>
        </div>
      </div>
    </div>
    
    <div v-if="isAuthenticated" class="add-comment">
      <label for="newComment">댓글 추가:</label>
      <textarea id="newComment" v-model="newComment"></textarea>
      <button @click="addComment" class="add-comment-button">댓글 추가</button>
    </div>
  </div>
</template>


<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useBoardStore } from '@/stores/board.js'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
const store = useBoardStore()
const useStore = useUserStore()
const route = useRoute()
const board = ref()
const isBoardReadonly = ref(true)
const comments = ref([])
const newComment = ref('')

const isAuthenticated = computed(() => useStore.token)
const toggleBoardReadonly = () => {
  isBoardReadonly.value = !isBoardReadonly.value;
}
const toggleCommentReadonly = (comment) => {
  comment.isCommentReadonly = !comment.isCommentReadonly;
}

//게시판 업데이트
const boardUpdate = () => {
  const boardData = ref({title:board.value.title, content:board.value.content})
  axios({
      method: 'put',
      url: `${store.API_URL}/boards/${route.query.type}/${route.params.id}/`,
      data: boardData.value,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      board.value = res.data
      isBoardReadonly.value = true
    })
    .catch((err) => {
      console.log(err)
    })
  }


//게시판 삭제
const boardDelete = () => {
  axios({
      method: 'delete',
      url: `${store.API_URL}/boards/${route.query.type}/${route.params.id}`,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      board.value = ''
    })
    .catch((err) => {
      console.log(err)
    })
  }


//댓글 정보 요청
const getComments = () => {
  axios({
      method: 'get',
      url: `${store.API_URL}/boards/${route.query.type}/comments/${route.params.id}/`,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      comments.value = res.data.map(comment => ({ ...comment, isCommentReadonly: true }))
    })
    .catch((err) => {
      console.error(err)
    })
  }


//댓글 추가
const addComment = () => {
  const commentData = { content: newComment.value }
  axios({
      method: 'post',
      url: `${store.API_URL}/boards/${route.query.type}/comments/${route.params.id}/`,
      data: commentData,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      newComment.value = ''
      getComments()
    })
    .catch((err) => {
      console.error(err)
    })
  }
  
//댓글 수정
const commentUpdate = (comment) => {
  const commentData = ref({content:comment.content})
  axios({
      method: 'put',
      url: `${store.API_URL}/boards/${route.query.type}/comments/${route.params.id}/`,
      data: commentData.value,
      params: { commentId: comment.id},
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      board.value = res.data
      comment.isCommentReadonly = true
      alert("댓글이 수정되었습니다.")
      getComments()
    })
    .catch((err) => {
      console.log(err)
    })
  }

//댓글 삭제
const commentDelete = (comment) => {
  console.log(comment)
  axios({
      method: 'delete',
      url: `${store.API_URL}/boards/${route.query.type}/comments/delete/${comment.id}/`,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      alert('댓글이 삭제 되었습니다')
      getComments()
    })
    .catch((err) => {
      console.log(err)
    })
  }

//좋아요 기능
const toggleLike = (board) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/${route.query.type}/${board.id}/like/`,
    headers: {
      Authorization: `Token ${useStore.token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    board.liked = res.data.liked
    board.likeCount = res.data.likeCount
  })
  .catch((err) => {
    console.error(err)
  })
}

onMounted(() => {
  //게시판 1개 디테일 정보 요청
   axios({
      method: 'get',
      url: `${store.API_URL}/boards/${route.query.type}/${route.params.id}/`,
      headers: {
          Authorization: `Token ${useStore.token}`
      }
    })
    .then((res) => {
      console.log(res.data)
      board.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })

  //댓글 정보 요청
  getComments()

  })

</script>

<style>
<style scoped>
.detail-title {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 20px;
}

.form-container {
  background-color: #fff;
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  font-size: 1rem;
  color: #555;
  display: block;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  font-size: 1rem;
  color: #333;
}

.like-section {
  margin-top: 20px;
}

.like-button {
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  font-size: 1rem;
  cursor: pointer;
  margin-right: 10px;
}

.button-group {
  margin-top: 20px;
}

.edit-button,
.save-button,
.delete-button,
.add-comment-button {
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  font-size: 1rem;
  cursor: pointer;
  margin-right: 10px;
}

.comment-title {
  font-size: 1.3rem;
  color: #333;
  margin-top: 20px;
  margin-bottom: 10px;
}

.comment-container {
  background-color: #fff;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.add-comment {
  margin-top: 20px;
}

.add-comment label {
  font-size: 1rem;
  color: #555;
  display: block;
}

.add-comment textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  font-size: 1rem;
  color: #333;
  margin-bottom: 10px;
}

.add-comment-button {
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  font-size: 1rem;
  cursor: pointer;
}

.add-comment-button:hover,
.edit-button:hover,
.save-button:hover,
.delete-button:hover,
.like-button:hover {
  background-color: #2c446b;
}

</style>
