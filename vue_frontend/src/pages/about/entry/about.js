import Vue from "vue/dist/vue.js";

import '@/jrbenriquez/assets/css/tailwind.css'

const AboutPage = () => import( /* webpackChunkName: "chunk-about" */ "../components/AboutPage.vue");

Vue.config.productionTip = false

// Mount top level components
new Vue({
  el: "#app",
  components: {AboutPage},
});
