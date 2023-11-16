<template>
  <div>
    <h1>Detail</h1>
    <div v-if="board">
      <p>제목 : {{ board.title }}</p>
      <p>내용 : {{ board.content }}</p>
      <p>작성일 : {{ board.created_at }}</p>
      <p>수정일 : {{ board.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useBoardStore } from '@/stores/board.js'
import { useRoute } from 'vue-router'

const store = useBoardStore()
const route = useRoute()
const board = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      board.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
