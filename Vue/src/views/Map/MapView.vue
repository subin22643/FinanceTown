<template>
  <div class="map_wrap">
    <!-- 검색 폼의 위치를 조정하기 위해 추가된 wrapper -->
    <div class="search_form_wrapper">
      <form @submit.prevent="searchPlaces" class="search_form">
        <!-- 드롭다운 메뉴를 추가합니다 -->
        <select v-model="selectedCity" class="me-1 custom-select">
          <option disabled value="" style="font-size: 20px;">도시 선택</option>
          <option v-for="city in cities" :value="city" style="font-size: 20px;">{{ city }}</option>
        </select>
        <select v-model="selectedDistrict" class="me-1 custom-select">
          <option disabled value="" style="font-size: 20px;">구/군 선택</option>
          <option v-for="district in filteredDistricts" :value="district" style="font-size: 20px;">{{ district }}</option>
        </select>
        <select v-model="selectedBank" class="me-1 custom-select">
          <option disabled value="" style="font-size: 20px;">은행 선택</option>
          <option v-for="bank in banks" :value="bank" style="font-size: 20px;">{{ bank }}</option>
        </select>
        <button type="submit" class="btn btn-primary">검색</button>
      </form>
    </div>
    <div id="map" class="map" ref="map"></div>
    <div id="menu_wrap" class="bg_white">
      <hr>
      <ul id="placesList">
        <li v-if="placesList.length === 0" class="no-results" style="font-size: 20px;">검색 결과가 여기에 표시됩니다</li>
        <li v-for="(place, index) in placesList" :key="index" class="item" @click="focusOnMarker(place)">
          <div :class="['markerbg', `marker_${index + 1}`]"></div>
          <div class="info">
            <h5>{{ place.place_name }}</h5>
            <span>{{ place.address_name }}</span>
            <span class="tel">{{ place.phone }}</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import city_data from '@/assets/city_data.json'
  
  console.log(city_data)
  const map = ref(null)
  const markers = ref([])
  const placesList = ref([])
  const pagination = ref(null)
  
  let mapInstance = null
  let infowindow = null
  


  //@@@@@@@@@@@@@ 시,구, 은행 검색 구현@@@@@@@@@@
  const cities = Object.keys(city_data)
  const cityDistricts = {};
  const banks = ['한국스탠다드차타드은행', '부산은행', '대구은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '국민은행', '신한은행', '농협은행', '하나은행', '주식회사 케이뱅크', '수협은행', '카카오뱅크', '토스뱅크']
  

  Object.keys(city_data).forEach(city => {
    // 각 도시의 구 명칭들을 추출합니다.
    cityDistricts[city] = Object.keys(city_data[city])
  })


  
  // 선택된 값들
  const selectedCity = ref('');
  const selectedDistrict = ref('');
  const selectedBank = ref('');
  

  const filteredDistricts = computed(() => {
  return cityDistricts[selectedCity.value] || []
  });
  
  
  // 지도를 생성하는 함수
  onMounted(() => {
    const kakao = window.kakao;
    const mapContainer = map.value;
    const options = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3
    };
    mapInstance = new kakao.maps.Map(mapContainer, options)
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
  });
  
  // 검색을 요청하는 함수
  const searchPlaces = () => {
  markers.value.forEach(marker => marker.setMap(null))
  markers.value = []

  const searchKeyword = `${selectedCity.value} ${selectedDistrict.value} ${selectedBank.value}`;
  const ps = new kakao.maps.services.Places()
  ps.keywordSearch(searchKeyword, placesSearchCB)
  }
  
  
  // 장소검색이 완료됐을 때 호출되는 콜백함수
  const placesSearchCB = (data, status, pagi) => {
    if (status === kakao.maps.services.Status.OK) {
        displayPlaces(data);
        pagination.value = pagi;
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.');
        placesList.value = [];
    } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.');
        placesList.value = [];
    } else {
      // 검색 결과가 없거나 오류가 발생한 경우 placesList를 비웁니다.
      placesList.value = [];
    }
  }
  

  // 검색 결과 목록과 마커를 표출하는 함수
  const displayPlaces = (places) => {
    const bounds = new kakao.maps.LatLngBounds()
  
    markers.value.forEach(marker => marker.setMap(null))
    markers.value = [];
  
    placesList.value = places.map((place, index) => {
        const position = new kakao.maps.LatLng(place.y, place.x)
        const marker = addMarker(position, index)
        bounds.extend(position)
        return {
            ...place,
            marker
        };
    });
    mapInstance.setBounds(bounds)
  };
  
  // 마커를 생성하고 지도 위에 마커를 표시하는 함수
  const addMarker = (position, idx) => {
  const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png' // 마커 이미지 URL
  const imageSize = new kakao.maps.Size(36, 37) // 마커 이미지의 크기
  const imgOptions = {
    spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 전체 크기
    spriteOrigin: new kakao.maps.Point(0, (idx * 46)), // 스프라이트 이미지 중 사용할 시작 위치 (y 위치)
    offset: new kakao.maps.Point(13, 37) // 마커의 위치 조정
  };
  const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions)

  const marker = new kakao.maps.Marker({
    position: position,
    image: markerImage
  });

  marker.setMap(mapInstance);
  return marker;
  }
  
  // 인포윈도우를 표시하는 함수
  const displayInfowindow = (marker, title) => {
    const content = '<div style="padding:5px;z-index:1;">' + title + '</div>'
    infowindow.setContent(content)
    infowindow.open(mapInstance, marker)
  };
  
  // 지도의 특정 위치로 클로즈업 하는 함수
  const focusOnMarker = (place) => {
    const position = new kakao.maps.LatLng(place.y, place.x);
    mapInstance.setCenter(position);
    mapInstance.setLevel(3); // 클로즈업 레벨 설정 (작은 숫자일수록 더 클로즈업)
  }

</script>
  
<style scoped>
.map {
  position: absolute;
  left: 650px; /* #menu_wrap 너비 + 좌측 마진 */
  width: 1400px; /* 전체 너비에서 #menu_wrap 너비와 좌측 마진을 뺀 너비 */
  height: 800px; /* 전체 높이에서 상단과 하단의 margin을 뺀 높이 */
  top: 45px; /* 상단으로부터의 거리 조정 */
}

.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:20px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {
  position: relative;
  width: 100%;
  height: 500px; /* 지도와 목록의 높이를 지정 */
  display: flex;
}

#menu_wrap {
  width: 615px;
  height: 810px; /* map_wrap의 높이에 맞춤 */
  margin-top: 35px; /* 상단 위치 조정 */
  padding: 5px;
  overflow-y: auto;
  background: #f8f9fa;;
  z-index: 1;
  font-size: 20px;
  border-radius: 10px;
}
.bg_white {background:#fff;}
.search_form_wrapper {
  position: absolute;
  left: 5px;
  z-index: 2;
}

#placesList .no-results {
  padding: 20px;
  text-align: center;
  color: #777;
  font-size: 20px;
  white-space: nowrap;
}

#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}

.custom-select {
  font-size: 20px;
  padding: 6px 12px;
  border: 1px solid #B3B3B3;
  border-radius: 4px;
  width: auto;
  margin-right: 5px;
}

.search_form button {
  background-color: #375a7f;
  color: white;
  border: none;
  border-radius: 5px;
  margin-top: -9px;
  padding: 6px 12px;
  font-size: 20px;
  height: 46px;
  cursor: pointer;
}

.search_form button:hover {
  background-color: #2c446b;
}
</style>