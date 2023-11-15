import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainView.vue'
import SearchView from '../views/SearchView.vue'
import MapView from '../views/MapView.vue'

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
      component: SearchView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
  ]
})

export default router
