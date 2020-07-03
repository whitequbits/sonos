import Vue from 'vue'
import router from "./router";
import App from './App.vue'
import BootstrapVue from "bootstrap-vue";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.config.productionTip = false
Vue.prototype.$axios = axios;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
