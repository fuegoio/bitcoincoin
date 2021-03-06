import Vue from 'vue'
import VueRouter from 'vue-router'

import CurrenciesPage from '@/pages/CurrenciesPage.vue'
import CurrencyPage from '@/pages/CurrencyPage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'
import RankingPage from '@/pages/RankingPage.vue'
import BanksPage from '@/pages/BanksPage.vue'
import BankPage from '@/pages/BankPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/profile',
  },
  {
    path: '/currencies',
    name: 'currencies',
    component: CurrenciesPage,
  },
  {
    path: '/currencies/:currencyId',
    name: 'currency',
    component: CurrencyPage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
  },
  {
    path: '/ranking',
    name: 'ranking',
    component: RankingPage,
  },
  {
    path: '/banks',
    name: 'banks',
    component: BanksPage,
  },
  {
    path: '/banks/:bankId',
    name: 'bank',
    component: BankPage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
