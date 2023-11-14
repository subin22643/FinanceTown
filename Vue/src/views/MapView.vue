<template>
    <div>
      <form @submit="searchPlaces">
        <input type="text" v-model="searchQuery" placeholder="장소 검색">
        <button type="submit">검색</button>
      </form>
        <h3>지도 페이지</h3>
        <div class="map" ref="map"></div>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'

const map = ref(null)
let mapInstance; // 지도 인스턴스 전역 변수 선언
let infowindow = new kakao.maps.InfoWindow({zIndex:1}); // 인포윈도우 생성


onMounted(() => {
    const kakao = window.kakao
    const container = map.value
    const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
    };
    mapInstance = new kakao.maps.Map(container, options); // 지도 생성 및 인스턴스 저장
})


const searchQuery=ref('')
const searchPlaces = () => {
  const ps = new kakao.maps.services.Places()
  ps.keywordSearch(searchQuery.value, placesSearchCB)
}

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        const bounds = new kakao.maps.LatLngBounds();

        for (let i=0; i<data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }       

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        mapInstance.setBounds(bounds);
    } 
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
    // 마커를 생성하고 지도에 표시합니다
    const marker = new kakao.maps.Marker({
        map: mapInstance,
        position: new kakao.maps.LatLng(place.y, place.x) 
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(mapInstance, marker);
    });
}
</script>


<style scoped>
.map {
    width: 500px;
    height: 400px;
}
</style>