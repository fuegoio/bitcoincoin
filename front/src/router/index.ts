import Vue from 'vue'
import VueRouter from 'vue-router'
import MoleculePage from '@/pages/MoleculePage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/molecule/34',
  },
  {
    path: '/molecule/:id',
    name: 'molecule',
    component: MoleculePage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
