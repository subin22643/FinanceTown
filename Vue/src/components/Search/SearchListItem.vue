<script setup>
import { ref, computed } from 'vue'
import { useFinanceStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const props = defineProps({
    deposits: Object,
    month: Object,
    bankmonth: Object,
    ox: Boolean
})

const store = useFinanceStore()
store.getDeposit()

const headers = ref([
  { title: '금융상품명', value: 'fin_prdt_nm' },
  { title: '금융회사명', value: 'kor_co_nm' },
  { title: '6개월', value: '6_months', sortable: true },
  { title: '12개월', value: '12_months', sortable: true },
  { title: '24개월', value: '24_months', sortable: true },
  { title: '36개월', value: '36_months', sortable: true },
])


const getInterestRate = (item, months) => {
  if (item.deposit_options && item.deposit_options.length > 0) {
    const option = item.deposit_options.find(option => option.save_trm === months);
    return option ? option.intr_rate2 : '-'
  }
  return '-'
}


const virtualDeposits = computed(() => {
  return props.deposits.map(deposit => {
    // deposit_options에서 각 기간의 데이터를 추출합니다.
    const optionsMap = deposit.deposit_options.reduce((acc, option) => {
      acc[`${option.save_trm}_months`] = option.intr_rate2;
      return acc;
    }, {});
    
    return {
      ...deposit,
      ...optionsMap
    };
  })
});



const virtualBankMonth = computed(() => {
    if (props.bankmonth && props.bankmonth.length > 0) {
        return props.bankmonth.map(item => {
            // bankmonth 데이터를 처리하는 로직
            const optionsMap = item.deposit_options.reduce((acc, option) => {
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
        const optionsMap = item.deposit_options.reduce((acc, option) => {
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
        <div class="card" v-if="month?.length === 0 && deposits?.length != 0 && ox === true">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualDeposits"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                    <td><RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
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
                    <td><RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                    <td>{{ item.kor_co_nm }}</td>
                    <td>{{ getInterestRate(item, 6) }}</td>
                    <td>{{ getInterestRate(item, 12) }}</td>
                    <td>{{ getInterestRate(item, 24) }}</td>
                    <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
        <div class="card" v-if="month?.length != 0 && deposits?.length === 0 && ox === true">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualMonth"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                    <td><RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
                    <td>{{ item.kor_co_nm }}</td>
                    <td>{{ getInterestRate(item, 6) }}</td>
                    <td>{{ getInterestRate(item, 12) }}</td>
                    <td>{{ getInterestRate(item, 24) }}</td>
                    <td>{{ getInterestRate(item, 36) }}</td>
                    </tr>
                </template>
            </v-data-table-virtual>
        </div>
        <div v-if="bankmonth?.length === 0 && month?.length != 0 && deposits?.length != 0 && ox === true">
            <p>조건에 맞는 상품이 없습니다</p>
        </div>

        <div v-if="ox === false">
            <v-data-table-virtual
                :headers="headers"
                :items="virtualDeposits"
                :item-key="'id'"
                :virtual-item-height="32">
                <template #item="{ item }">
                    <tr>
                        <td><RouterLink :to="{ name: 'searchOptions', params: { fin_prdt_cd: item.fin_prdt_cd }}">{{ item.fin_prdt_nm }}</RouterLink></td>
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

/* .card {
    width: 821px;
    height: 159px;
    flex-shrink: 0;
    border-radius: 24px;
    border: 2px solid #E6E6E6;
    background: #FAFAF5;
} */


/* gpt가 해준 이상한 갈색 테마 */
/* .card {
    width: 300px;
    padding: 20px;
    background-color: #f5e0c5;
    border: 1px solid #d8a074;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.card-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.card-description {
    font-size: 16px;
    margin-bottom: 20px;
    }

.card-button {
    background-color: #9d5736;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
    }

.card-button:hover {
background-color: #74422f;
} */



</style>
