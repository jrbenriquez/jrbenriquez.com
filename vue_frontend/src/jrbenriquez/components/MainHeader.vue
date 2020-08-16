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
    <br>
    <section class="fade-top h-screen" data-aos="fade-up">
      <div class="flex justify-around">
        <div class="text-3xl text-center mt-10 text-gray-700">
          
          <p class="font-secondary font-thin pt-16" data-aos="fade-down" data-aos-delay="0" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">A</span> curious <span class="text-bold">Web Developer</span> that makes sure the <span class="text-bold">kid inside</span> him 
          </p>
          
          <p class="font-secondary font-thin" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">brings out </span> all his fascination with <span class="text-bold">technology</span> into <span class="text-bold">reality</span>.
          </p> 
          <p class="font-secondary font-thin my-8" data-aos="fade-right" data-aos-delay="2000" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">I entrust</span> my ideas to the power of <span class="text-bold">Python</span> and <span class="text-bold">Django</span>.
          </p>
          <p class="font-secondary font-thin my-8" data-aos="fade-down" data-aos-delay="3000" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">I carry</span> sparkles of <span class="text-bold">VueJS</span>, <span class="text-bold">Flutter</span> and <span class="text-bold">React</span> in case I need to bust it out in the <span class="text-bold">frontend</span>
          </p>

          <!-- Add Social links
          <br>
          Add Site Stack -->
          
          
        </div>
      </div>
   
    
    </section>
    <br>
    
  </div>
</template>

<script>
  export default {
    name: 'MainHeader',
    props: {
      msg: String
    },
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
        showArrow: true,
        arrowLocation: null,
        containerData: null,
        currentScrollY: 0,
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
      window.addEventListener('scroll', this.handleScroll);
      window.setInterval(()=>{
        this.runLabels();
      }, 2000);
      console.log()
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
      handleScroll () {
        this.currentScrollY = window.top.scrollY
        
      },
      runLabels(){
        if (!this.showArrow){
          return
        }
        const first = this.labels.shift();
        this.labels = this.labels.concat(first);
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
