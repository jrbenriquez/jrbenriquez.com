import Vue from "vue/dist/vue.js";

import '../assets/css/tailwind.css'

const MainPage = () => import( /* webpackChunkName: "chunk-main" */ "../components/MainPage.vue");

Vue.config.productionTip = false

Vue.component('main-page', MainPage);

// Mount top level components
new Vue({
  el: "#app",
  components: {MainPage},
});
