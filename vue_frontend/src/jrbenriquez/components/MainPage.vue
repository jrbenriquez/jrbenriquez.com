<template>

  <div id="main" class="text-center">
      <main-header :currentScrollY="currentScrollY"></main-header>
    <br>
      <main-spiel></main-spiel>
    <br>
    
  </div>
</template>

<script>

  const MainHeader = () => import( /* webpackChunkName: "chunk-main-header" */ "./MainHeader.vue");
  const MainSpiel = () => import( /* webpackChunkName: "chunk-main-spiel" */ "./MainSpiel.vue");

  export default {
    name: 'MainPage',
    components: {MainHeader, MainSpiel},
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
        showArrow: true,
        arrowLocation: null,
        containerData: null,
        currentScrollY: 0,
      }
    },
    mounted(){
      window.addEventListener('scroll', this.handleScroll);
    },
    computed: {
      labelIconify: function () {
        var iconName = this.labels[0]["iconify"];
        return `<span class="iconify" data-icon=${iconName} data-inline="false"></span>`
      },
    },
    watch: {
      currentScrollY: function (currentY, oldY) {

        // Fade out arrow on scroll down 
        if (this.showArrow && currentY > this.arrowLocation - (this.$refs.header.clientHeight * 0.9)){
          this.showArrow = false;
        }

        // Fade in arrow on scroll up
        else if (!this.showArrow && currentY < (this.$refs.header.clientHeight *1.25) && currentY < oldY){
          this.showArrow = true;
        }

        // Fade section on scroll up
        var header = this.$refs.header
        var headerCheckpoint = header.offsetTop * 20
        header.style.opacity = 1 - (this.currentScrollY/headerCheckpoint)
      }
        
    

    },
    methods: {
      handleScroll () {
        this.currentScrollY = window.top.scrollY
        
      },
      onScroll(e, position){
        console.log(e, position)
      },
    },
    destroyed () {
      window.removeEventListener('scroll', this.handleScroll);
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  .fade-top {
    transition: opacity 1s;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
  .bounce {
  -webkit-animation: bounce 2s;
  animation: bounce 2s;
	-webkit-animation-iteration-count: infinite;
  animation-iteration-count: infinite;
  }

@-webkit-keyframes bounce {
	0%,
	25%,
	50%,
	75%,
	100% {
   -webkit-transform: translateY(0);
    transform: translateY(0);
	}
	40% {
    -webkit-transform: translateY(-20px);
    transform: translateY(-20px);
	}
	60% {
		-webkit-transform: translateY(-12px);
    transform: translateY(-12px);
	}
}

@keyframes bounce {
	0%,
	25%,
	50%,
	75%,
	100% {
		-webkit-transform: translateY(0);
    transform: translateY(0);
	}
	40% {
		-webkit-transform: translateY(-20px);
    transform: translateY(-20px);
	}
	60% {
		-webkit-transform: translateY(-12px);
    transform: translateY(-12px);
	}
}



</style>
