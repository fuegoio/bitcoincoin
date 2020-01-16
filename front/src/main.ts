import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app')

Vue.filter('toCurrency', function(value: number) {
  return '$' + value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
})
