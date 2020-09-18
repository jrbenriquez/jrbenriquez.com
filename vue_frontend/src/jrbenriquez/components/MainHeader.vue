<template>

  <div id="main" class="text-center">

      <section ref="header" data-index="0" class="fade-top pt-16 h-screen" id="trigger-arrow" data-aos="fade" data-aos-offset="-100" data-aos-mirror="true">
        <div class="flex justify-around py-16 md:py-24">
          <div class="flex-col text-5xl md:text-6xl">
              <div class="mb-2 md:mb-0"><span class="font-secondary font-thin ">I'm a</span></div>


              <div class="flex flex-col items-center">
                <div v-if="labels[0]['iconify']" v-html="labelIconify" class="m-auto px-10 py-10 md:py-4">
                </div>
                <div class="border-b-4 inline border-gray-600">
                  {{labels[0]["label"]}}
                </div>
              </div>
          </div>
        </div>


        <div class="flex justify-around" data-aos="fade" data-aos-anchor="#trigger-arrow" data-aos-anchor-placement="top-center">
            <transition name="fade">
              <img ref="downArrow" v-if="showArrow" class="bounce w-10 h-10" src="../assets/down-arrow.svg" />
            </transition>
        </div>

      </section>
  </div>
</template>

<script>

  export default {
    name: 'MainHeader',
    props: ['currentScrollY'],
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
        showArrow: true,
        arrowLocation: null,
        containerData: null,
        labels: [
          {
              label: 'Backend Developer',
              iconify: 'carbon:machine-learning'
          },
          {
              label: 'Python Enthusiast',
              iconify: 'logos:python'
          },
          {
              label: 'Django Fanboy',
              iconify: 'logos-django'
          },
          {
              label: 'Bassist',
              iconify: 'noto:guitar'
          },
          ],
      }
    },
    mounted(){
      window.setInterval(()=>{
        this.runLabels();
      }, 2000);
      this.arrowLocation = this.$refs.downArrow.offsetTop
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
      runLabels(){
        if (!this.showArrow){
          return
        }
        const first = this.labels.shift();
        this.labels = this.labels.concat(first);
      },
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
