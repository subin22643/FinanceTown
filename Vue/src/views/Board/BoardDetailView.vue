<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board" class="form-container">
      <label for="title">제목 : </label><input id='title' :readonly="isBoardReadonly" v-model="board.title" />
      <label for="content">내용 : </label><input id="content" :readonly="isBoardReadonly" v-model="board.content" />
      <label for="created">작성일 : </label><input id="created" v-model="board.created_at" readonly>
      <label for="updated">수정일 : </label><input id="updated" v-model="board.updated_at" readonly>
      
      <div class="like-section">
        <button v-if="!board.liked" @click="toggleLike(board)">👍 좋아요 {{ board.likeCount }}</button>
        <button v-if="board.liked" @click="toggleLike(board)">👎 좋아요 취소 {{ board.likeCount }}</button>
      </div>
      <div v-if="board.author.username === useStore.loginUsername">
        <button v-if="isBoardReadonly" @click="toggleBoardReadonly">수정</button>
        <button v-if="isBoardReadonly" @click="boardDelete">삭제</button>
        <button v-if="!isBoardReadonly" @click="boardUpdate">저장</button>
      </div>
    </div>

    <div v-if="comments">
      <h2>댓글</h2>
      <div v-for="comment in comments" :key="comment.id">
        <label for="content">{{ comment.author.nickname }}: </label><input id="content" :readonly="comment.isCommentReadonly" v-model="comment.content" />
        <div v-if="comment.author.username === useStore.loginUsername">
          <button v-if="comment.isCommentReadonly" @click="toggleCommentReadonly(comment)">댓글 수정</button>
          <button v-if="comment.isCommentReadonly" @click="commentDelete(comment)">댓글 삭제</button>
          <button v-if="!comment.isCommentReadonly" @click="commentUpdate(comment)">댓글 저장</button>
        </div>
      </div>
    </div>
    <div v-if="isAuthenticated">
      <textarea v-model="newComment"></textarea>
      <button @click="addComment">댓글 추가</button>
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
.form-container input {
  display: block;
  margin-bottom: 10px;
}
</style>
