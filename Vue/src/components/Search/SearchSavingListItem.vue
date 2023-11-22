<script setup>
import { ref, computed } from 'vue'
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




</script>

<template>
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
    </div>
</template>

<style scoped>

</style>