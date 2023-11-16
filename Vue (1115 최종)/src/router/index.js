import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '@/views/MainView.vue'


//예금적금
import Search from '@/views/Search/SearchView.vue'

//카카오맵
import MapView from '@/views/Map/MapView.vue'

//환전
import ExchangeRate from '@/views/Exchange/ExchangeRateView.vue'

//게시판
import BoardView from '@/views/Board/BoardView.vue'
import BoardDetail from '@/views/Board/BoardDetailView.vue'
import BoardCreate from '@/views/Board/BoardCreateView.vue'
import FinanceBoard from '@/views/Board/FinanceBoardView.vue'
import ProductBoard from '@/views/Board/ProductBoardView.vue'

//로그인
import SignUpView from '@/views/User/SignUpView.vue'
import LogInView from '@/views/User/LogInView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPage
    },
    
    //예적금
    {
      path: '/search',
      name: 'search',
      component: Search
    },

    //카카오 맵
    {
      path: '/map',
      name: 'map',
      component: MapView
    },

    //환전
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeRate
    },

    // 게시판
    {
      path: '/boards',
      name: 'BoardView',
      component: BoardView,
    },
    {
      path: '/boards/finance',
      name: 'FinanceBoardView',
      component: FinanceBoard,
    },
    {
      path: '/boards/product',
      name: 'ProductBoardView',
      component: ProductBoard,
    },
    {
      path: '/boards/:id',
      name: 'BoardDetail',
      component: BoardDetail
    },
    {
      path: '/create',
      name: 'BoardCreate',
      component: BoardCreate
    },

    //로그인
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogInView
    }
    // {
    //   path: '/user/update',
    //   name: 'UserUpdate',
    //   component: LogInView
    // }
  ]
})

export default router