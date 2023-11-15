<template>
    <div>
      <form @submit.prevent="searchPlaces">
        <!-- 드롭다운 메뉴를 추가합니다 -->
        <select v-model="selectedCity" class="me-1">
            <option disabled value="">도시 선택</option>
            <option v-for="city in cities" :value="city">{{ city }}</option>
        </select>
        <select v-model="selectedDistrict" class="me-1">
            <option disabled value="">구 선택</option>
            <option v-for="district in filteredDistricts" :value="district">{{ district }}</option>
         </select>
         <select v-model="selectedBank" class="me-1">
            <option disabled value="">은행 선택</option>
            <option v-for="bank in banks" :value="bank">{{ bank }}</option>
        </select>
        <button type="submit">검색</button>
      </form>
        <h3>지도 페이지</h3>
        <div class="map" ref="map"></div>
    </div>
</template>


<script setup>
import { ref, onMounted,computed } from 'vue'

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


//@@@@@@@@@@@@@ 시,구, 은행 검색 구현@@@@@@@@@@
//추후 최신 행정구역 api나 DB로 다운받아서 리스트 만들기 + 은행목록도
const banks = ['KB국민은행', '신한은행', '우리은행', '하나은행', 'NH농협은행'];
const cities = ['서울', '부산', '대구', '인천']
const cityDistricts = {
  서울: ['강남구', '서초구', '종로구', '중구'],
  부산: ['해운대구', '남구', '동래구', '부산진구'],
  대구: ['달서구', '수성구', '북구', '중구'],
  인천: ['중구', '동구', '미추홀구', '연수구']
}


// 선택된 값들
const selectedCity = ref('');
const selectedDistrict = ref('');
const selectedBank = ref('');

const filteredDistricts = computed(() => {
  return cityDistricts[selectedCity.value] || [];
});


const searchPlaces = () => {
  const searchKeyword = `${selectedCity.value} ${selectedDistrict.value} ${selectedBank.value}`;
  const ps = new kakao.maps.services.Places()
  ps.keywordSearch(searchKeyword, placesSearchCB)
}


//@@@@@@@@@@@@@@검색된 장소 위치를 기준으로 지도 범위를 재설정 및 마커 형성@@@@@@@@@@@@@@@
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