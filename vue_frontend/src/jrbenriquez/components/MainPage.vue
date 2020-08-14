<template>

  <div id="app" class="text-center">
    <section class="">
      <div class="flex justify-around my-10 md:my-32">
        <div class="flex-col text-6xl">
            <div><span class="font-secondary font-thin ">I am a</span></div>
            
            

            <div class="flex border-solid border-b-4 inline border-gray-600">
              <div v-if="labels[0]['iconify']" v-html="labelIconify" class="my-auto px-10">
              </div> 
              <div>
                {{labels[0]["label"]}}
              </div>
            </div>
        </div>
      </div>
    </section>
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
              label: '🎸 Bassist',
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
