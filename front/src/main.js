import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from './router'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import NavBar from './components/NavBar'

Vue.config.productionTip = false

Vue.component('NavBar', NavBar);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
