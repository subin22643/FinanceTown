import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainView.vue'

// 예적금 조회
import Search from '@/views/Search/SearchView.vue'
import SearchList from '../components/Search/SearchList.vue'
import SearchSavingList from '../components/Search/SearchSavingList.vue'
import SearchOption from '../views/Search/SearchOptionView.vue'
import SearchSavingOption from '../views/Search/SearchSavingOptionView.vue'

// 카카오맵
import MapView from '../views/Map/MapView.vue'

// 환전
import ExchangeRate from '../views/Exchange/ExchangeRateView.vue'

//게시판
import BoardView from '@/views/Board/BoardView.vue'
import BoardDetail from '@/views/Board/BoardDetailView.vue'
import BoardCreate from '@/views/Board/BoardCreateView.vue'
import QnABoard from '@/views/Board/QnABoardView.vue'
import ProductBoard from '@/views/Board/ProductBoardView.vue'


//로그인
import SignUpView from '@/views/User/SignUpView.vue'
import LogInView from '@/views/User/LogInView.vue'
import UserUpdateView from '@/views/User/UserUpdateView.vue'
import ProfileView from '@/views/User/ProfileView.vue'
import DeleteView from '@/views/User/DeleteView.vue'
import PasswordChangeView from '@/views/User/PasswordChangeView.vue'
import CartView from '@/views/User/CartView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPage
    },
    // 예적금
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
      path: '/search/deposit-product/:fin_prdt_cd',
      name: 'searchOptions',
      component: SearchOption
    },
    {
      path: '/search/saving-products-options/:fin_prdt_cd',
      name: 'SearchSavingOption',
      component: SearchSavingOption
    },
    // 카카오맵
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    // 환전
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
      path: '/boards/product',
      name: 'ProductBoardView',
      component: ProductBoard,
    },
    {
      path: '/boards/QnA',
      name: 'QnABoardView',
      component: QnABoard,
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
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView
    },
    {
      path: '/delete',
      name: 'UserDelete',
      component: DeleteView
    },
    {
      path: '/passwordChange',
      name: 'PasswordChange',
      component: PasswordChangeView
    },
    {
      path: '/user/update',
      name: 'UserUpdate',
      component: UserUpdateView,
    },
    {
      path: '/user/cart',
      name: 'Cart',
      component: CartView,
    },
  ]
})

export default router
