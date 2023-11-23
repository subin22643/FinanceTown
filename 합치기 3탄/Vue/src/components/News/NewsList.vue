<script setup>
import { onMounted } from 'vue'
import { useNewsStore } from '@/stores/news'

const store = useNewsStore()

onMounted(() => {
    store.getNews()
})

const newsList = store.news

<<<<<<< HEAD

</script>

<template>
    <div class="card">
        <h3>오늘의 금융 뉴스</h3>
            <p v-for="news in newsList">
                <a :href="news.link" v-html="news.title"></a>
=======
</script>

<template>
    <div>
        <h3>오늘의 금융 뉴스</h3>
            <p v-for="news in newsList">
                <a :href="news.link"><p v-html="news.title"></p></a>
>>>>>>> jonggil
            </p>
    </div>
</template>

<style scoped>

<<<<<<< HEAD
.card {
    width: 700px;
    padding: 20px;
    border: 5px gray solid;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    align-items: flex;
}


=======
>>>>>>> jonggil
</style>