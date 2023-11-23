<script setup>

<<<<<<< HEAD
const props = defineProps({
=======
defineProps({
>>>>>>> jonggil
    exchange: Object,
})

</script>

<template>
<<<<<<< HEAD
  <v-table
    fixed-header>
    <thead>
      <tr>
        <th>
          국가/통화명
        </th>
        <th>
          통화코드
        </th>
        <th>
          송금 보내실 때
        </th>
        <th>
          송금 받으실 때
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="exchange in props.exchange">
        <td>{{ exchange.cur_unit }}</td>
        <td>{{ exchange.cur_nm }}</td>
        <td>{{ exchange.tts }}</td>
        <td>{{ exchange.ttb }}</td>
      </tr>
    </tbody>
  </v-table>

=======
    <div>
        <!-- <p>조회결과: {{ exchange.result }}</p> -->
        <p>통화코드: {{ exchange.cur_unit }}</p>
        <p>국가/통화명: {{ exchange.cur_nm }}</p>
        <p>전신환(송금) 보내실 때: {{ exchange.tts }}</p> 
        <p>전신환(송금) 받으실 때: {{ exchange.ttb }}</p>
        <!-- <p>매매 기준율: {{ exchange.deal_bas_r }}</p>  -->
        <hr>
    </div>
>>>>>>> jonggil
</template>

<style scoped>

</style>
