<template>

  <div id="main" class="text-center">
    <section class="">
      <div class="flex justify-around my-20 md:my-28">
        <div class="flex-col text-4xl md:text-6xl">
            <div class="mb-2 md:mb-0"><span class="font-secondary font-thin ">I'm a</span></div>
            

            <div class="flex border-solid">
              <div v-if="labels[0]['iconify']" v-html="labelIconify" class="m-auto px-10">
              </div> 
              <div class="border-b-4 inline border-gray-600">
                {{labels[0]["label"]}}
              </div>
            </div>
        </div>
      </div>
    </section>
    Add Bouncing Arrow
    <br>
    Add More Content
  </div>
</template>

<script>
  export default {
    name: 'MainPage',
    props: {
      msg: String
    },
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
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
    },
    computed: {
      labelIconify: function () {
        var iconName = this.labels[0]["iconify"];
        return `<span class="iconify" data-icon=${iconName} data-inline="false"></span>`
      }
    },
    methods: {
      runLabels(){
        const first = this.labels.shift();
        this.labels = this.labels.concat(first);

      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  
</style>
