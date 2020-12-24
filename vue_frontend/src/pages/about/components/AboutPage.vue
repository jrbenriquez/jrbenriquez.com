<template>

  <div ref="main" class="text-center">
      <div class="flex-none xs:flex-col md:flex justify-around items-center py-16 md:py-24" style="height: 120vh">
        <div class="flex-1 self-center pb-24">
            <div ref="textdiv" class="" :style="textDivStyle">
                <div class="text-4xl">
                    Contact Me
                </div>
                <div>
                    johnrei.enriquez@gmail.com
                </div>
            </div>
        </div>
        <div class="flex-1 self-start">
          <div ref="picdiv" :style="picDivStyle">
              <img ref="mypic" class="" src="../../../jrbenriquez/assets/me.jpg" />
          </div>
        </div>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'AboutPage',
    data: function () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
        picDivStyle: {},
        textDivStyle: {},
        currentScrollY: 0,
      }
    },
    mounted(){
      window.addEventListener('scroll', this.handleScroll);
    },
    watch: {
      currentScrollY: function () {
        var mypic = this.$refs.mypic;
        var mytext = this.$refs.textdiv;
        var mypicReference = mypic.offsetTop;
        var mainElement = this.$refs.main
        mypic.style.opacity = 1 - (this.currentScrollY*3/mypicReference);
        mytext.style.opacity = 1 - (this.currentScrollY*3/mypicReference);

        let padding = this.currentScrollY;
        if (padding <= mainElement.clientHeight/3) {
            this.picDivStyle = {paddingTop:`${(padding*3)}px` };
            this.textDivStyle = {paddingBottom:`${(padding/3)}px` };
            }
        //header.style.opacity = 1 - (this.currentScrollY/headerCheckpoint)
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

</style>
