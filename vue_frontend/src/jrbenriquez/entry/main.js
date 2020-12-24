import Vue from "vue/dist/vue.js";
import AOS from 'aos';
import "aos/dist/aos.css";

import '@/jrbenriquez/assets/css/tailwind.css'

const MainPage = () => import( /* webpackChunkName: "chunk-main" */ "../components/MainPage.vue");
const AboutPage = () => import( /* webpackChunkName: "chunk-main" */ "../../pages/about/components/AboutPage.vue");

Vue.config.productionTip = false

// Mount top level components
new Vue({
  created() {
    AOS.init();
  },
  el: "#app",
  components: {MainPage, AboutPage}
});

