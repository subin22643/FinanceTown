import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainView.vue'
import Search from '../views/SearchView.vue'
import SearchList from '../components/SearchList.vue'
import SearchSavingList from '../components/SearchSavingList.vue'
import SearchOption from '../views/SearchOptionView.vue'
import SearchSavingOption from '../views/SearchSavingOptionView.vue'
import MapView from '../views/MapView.vue'
import ExchangeRate from '../views/ExchangeRateView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPage
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      children: [
        {
          path: '/searchlist',
          name: 'searchlist',
          component: SearchList
        },
        {
          path: '/searchsavinglist',
          name: 'searchsavinglist',
          component: SearchSavingList
        },
      ]
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeRate
    },
    {
      path: '/search/deposit-product/:fin_prdt_cd',
      name: 'searchOptions',
      component: SearchOption
    },
    {
      path: '/search/saving-products-options/:fin_prdt_cd',
      name: 'SearchSavingOption',
      component: SearchSavingOption
    },
  ]
})

export default router
