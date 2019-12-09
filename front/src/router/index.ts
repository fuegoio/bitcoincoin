import Vue from 'vue'
import VueRouter from 'vue-router'
import MoleculePage from '@/pages/MoleculePage.vue'
import ProfilePage from '@/pages/ProfilePage.vue'

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
