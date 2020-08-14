<template>

  <div class="">
      <div class="flex justify-around">
        <div class="text-3xl text-center mt-10 text-gray-700">
          
          <p class="font-secondary font-thin">
            <span class="text-bold">I am</span> a <span class="text-bold">Web Developer</span> that makes sure the <span class="text-bold">kid inside</span> him 
          </p>
          
          <p class="font-secondary font-thin">
            <span class="text-bold">brings out </span> all his fascination with <span class="text-bold">technology</span> into <span class="text-bold">reality</span>.
          </p> 
          <p class="font-secondary font-thin my-8">
            <span class="text-bold">I entrust</span> my ideas to the power of <span class="text-bold">Python</span> and <span class="text-bold">Django</span>.
          </p>
          <p class="font-secondary font-thin my-8">
            <span class="text-bold">I have</span> a sparkle of <span class="text-bold">VueJS</span>, <span class="text-bold">Flutter</span>, <span class="text-bold">React</span> in case I need to bust it out in the <span class="text-bold">frontend</span>
          </p>

          Add Social links
          <br>
          Add Site Stack
          
          
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
      }
    },
    mounted() {
    },
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  
</style>
