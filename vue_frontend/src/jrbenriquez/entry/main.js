import Vue from "vue/dist/vue.js";
import AOS from 'aos';
import "aos/dist/aos.css";

import '@/jrbenriquez/assets/css/tailwind.css'

const MainHeader = () => import( /* webpackChunkName: "chunk-main" */ "../components/MainHeader.vue");

Vue.config.productionTip = false

// Mount top level components
new Vue({
  created() {
    AOS.init();
  },
  el: "#app",
  components: {MainHeader}
});

