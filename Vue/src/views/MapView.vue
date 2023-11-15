<script>
import { ref, onMounted } from 'vue'

export default {
    setup() {
        const map = ref('')
        onMounted(() => {
            const kakao = window.kakao
            const container = map.value
            const options = { //지도를 생성할 때 필요한 기본 옵션
                center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
                level: 3 //지도의 레벨(확대, 축소 정도)
            };
            new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
        })
        return { map }
    }   
}

</script>

<template>
  <div>
    <h3>지도 페이지</h3>
    <div class="map" ref="map"></div>
  </div>
</template>

<style scoped>

.map {
    width: 500px;
    height: 400px;
}

</style>
