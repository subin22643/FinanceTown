<script setup>

const props = defineProps({
    exchange: Object,
})

</script>

<template>
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

</template>

<style scoped>

</style>
