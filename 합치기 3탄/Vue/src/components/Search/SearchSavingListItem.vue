<script setup>
<<<<<<< HEAD
import { ref, computed } from 'vue'
=======
>>>>>>> jonggil
import { useSavingStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'


const props = defineProps({
    savings: Object,
    month: Object,
    bankmonth: Object,
    ox: Boolean
})

const store = useSavingStore()
store.getSaving()

<<<<<<< HEAD
const headers = ref([
  { title: '금융상품명', value: 'fin_prdt_nm' },
  { title: '금융회사명', value: 'kor_co_nm' },
  { title: '6개월', value: '6_months', sortable: true },
  { title: '12개월', value: '12_months', sortable: true },
  { title: '24개월', value: '24_months', sortable: true },
  { title: '36개월', value: '36_months', sortable: true },
])


const getInterestRate = (item, months) => {
  if (item.saving_options && item.saving_options.length > 0) {
    const sameTermOptions = item.saving_options.filter(option => option.save_trm === months);
    if (sameTermOptions.length > 0) {
      let highestInterest = -Infinity; // 최고 이자율을 저장할 변수를 가장 낮은 값으로 초기화
      for (const option of sameTermOptions) {
        if (option.intr_rate2 > highestInterest) {
          highestInterest = option.intr_rate2; // 더 높은 이자율을 찾으면 해당 값을 저장
        }
      }
      return highestInterest !== -Infinity ? highestInterest : '-';
    }
  }
  return '-';
};


const virtualSavings = computed(() => {
  return props.savings.map(saving => {
    const optionsMap = saving.saving_options.reduce((acc, option) => {
      acc[`${option.save_trm}_months`] = option.intr_rate2;
      return acc;
    }, {});
    
    return {
      ...saving,
      ...optionsMap
    };
  })
});



const virtualBankMonth = computed(() => {
    if (props.bankmonth && props.bankmonth.length > 0) {
        return props.bankmonth.map(item => {
            // bankmonth 데이터를 처리하는 로직
            const optionsMap = item.saving_options.reduce((acc, option) => {
            acc[`${option.save_trm}_months`] = option.intr_rate2;
            return acc;
            }, {});

            return {
            ...item,
            ...optionsMap
            };
        });
    } else {
        return []; // 또는 데이터가 없을 경우 적절히 처리합니다.
    }
    });


const virtualMonth = computed(() => {
if (props.month && props.month.length > 0) {
    return props.month.map(item => {
        // bankmonth 데이터를 처리하는 로직
        const optionsMap = item.saving_options.reduce((acc, option) => {
        acc[`${option.save_trm}_months`] = option.intr_rate2;
        return acc;
        }, {});

        return {
        ...item,
        ...optionsMap
        };
    });
} else {
    return []; // 또는 데이터가 없을 경우 적절히 처리합니다.
}
});



=======
>>>>>>> jonggil

</script>

<template>
<<<<<<< HEAD
    <div>
        <div class="card" v-if="month?.length === 0 && savings?.length != 0 && ox === true">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualSavings"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                    <td><RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                    <td>{{ item.kor_co_nm }}</td>
                    <td>{{ getInterestRate(item, 6) }}</td>
                    <td>{{ getInterestRate(item, 12) }}</td>
                    <td>{{ getInterestRate(item, 24) }}</td>
                    <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
        <div class="card" v-if="bankmonth?.length != 0 && ox === true">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualBankMonth"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                    <td><RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                    <td>{{ item.kor_co_nm }}</td>
                    <td>{{ getInterestRate(item, 6) }}</td>
                    <td>{{ getInterestRate(item, 12) }}</td>
                    <td>{{ getInterestRate(item, 24) }}</td>
                    <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
        <div class="card" v-if="month?.length != 0 && savings?.length === 0 && ox === true">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualMonth"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                    <td><RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                    <td>{{ item.kor_co_nm }}</td>
                    <td>{{ getInterestRate(item, 6) }}</td>
                    <td>{{ getInterestRate(item, 12) }}</td>
                    <td>{{ getInterestRate(item, 24) }}</td>
                    <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
        <div v-if="bankmonth?.length === 0 && month?.length != 0 && savings?.length != 0 && ox === true">
            <p>조건에 맞는 상품이 없습니다</p>
        </div>

        <div v-if="ox === false">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualSavings"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                        <td><RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                        <td>{{ item.kor_co_nm }}</td>
                        <td>{{ getInterestRate(item, 6) }}</td>
                        <td>{{ getInterestRate(item, 12) }}</td>
                        <td>{{ getInterestRate(item, 24) }}</td>
                        <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
=======
    <div v-if="month?.length === 0 && savings?.length != 0 && ox === true">
        <p v-for="saving in savings" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ saving.dcls_month }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ saving.etc_note }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ saving.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ saving.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ saving.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ saving.join_member }}</p>
                <p>가입 방법 : {{ saving.join_way }}</p> -->
                <p>금융회사 명 : {{ saving.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ saving.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ saving.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ saving.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in saving.saving_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: saving.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="bankmonth?.length != 0 && ox === true">
        <p v-for="saving in bankmonth">
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ saving.dcls_month }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ saving.etc_note }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ saving.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ saving.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ saving.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ saving.join_member }}</p>
                <p>가입 방법 : {{ saving.join_way }}</p> -->
                <p>금융회사 명 : {{ saving.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ saving.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ saving.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ saving.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in saving.saving_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: saving.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="month?.length != 0 && savings?.length === 0 && ox === true">
        <p v-for="saving in month" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ saving.dcls_month }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ saving.etc_note }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ saving.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ saving.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ saving.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ saving.join_member }}</p>
                <p>가입 방법 : {{ saving.join_way }}</p> -->
                <p>금융회사 명 : {{ saving.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ saving.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ saving.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ saving.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in saving.saving_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: saving.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
    </div>
    <div v-if="bankmonth?.length === 0 && month?.length != 0 && deposits?.length != 0 && ox === true">
        <p>조건에 맞는 상품이 없습니다</p>
    </div>

    <div v-if="ox === false">
        <p v-for="saving in savings" >
            <h2>상품명</h2>
                <!-- <p>공시 제출월 [YYYYMM] : {{ saving.dcls_month }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>기타 유의사항 : {{ saving.etc_note }}</p>
                <p>금융회사 코드 : {{ saving.fin_co_no }}</p>
                <p>금융회사 제출일 [YYYYMMDDHH24MI] : {{ saving.fin_co_subm_day }}</p> -->
                <p>금융상품 코드 : {{ saving.fin_prdt_cd }}</p>
                <p>금융 상품명 : {{ saving.fin_prdt_nm }}</p>
                <!-- <p>가입 제한 : {{ saving.join_deny }} (1:제한없음, 2:서민전용, 3:일부제한)</p>
                <p>가입 대상 : {{ saving.join_member }}</p>
                <p>가입 방법 : {{ saving.join_way }}</p> -->
                <p>금융회사 명 : {{ saving.kor_co_nm }}</p>
                <!-- <p>최고 한도 : {{ saving.max_limit }}</p> -->
                <p>만기 후 이자율 : {{ saving.mtrt_int }}</p>
                <!-- <p>우대 조건 : {{ saving.spcl_cnd }}</p> -->
                <!-- <p>최고 우대 금리: {{ option.intr_rate2 }}</p> -->
            <!-- </p> -->
        <br>
            <h3>해당 상품 옵션 금리</h3>
                <p v-for="option in saving.saving_options" >
                    <p>저축 금리: {{ option.intr_rate }}</p>
                    <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                    <p>저축기간 (단위: 개월): {{ option.save_trm }}</p>
                    <br>
                </p>
            <RouterLink :to="{ name: 'SearchSavingOption', params: { fin_prdt_cd: saving.fin_prdt_cd }}">옵션 자세히 보기</RouterLink>
            <hr>
            <hr>
        </p>
>>>>>>> jonggil
    </div>
</template>

<style scoped>

</style>