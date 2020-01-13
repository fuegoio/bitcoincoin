import Vue from 'vue'
import VueRouter from 'vue-router'

import DashboardPage from '@/pages/DashboardPage.vue'
import CurrenciesPage from '@/pages/CurrenciesPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import LoginPage from '@/pages/LoginPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/dashboard',
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardPage,
  },
  {
    path: '/currencies',
    name: 'currencies',
    component: CurrenciesPage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
