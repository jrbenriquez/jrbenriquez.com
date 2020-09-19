<template>
    <div>
    <section class="fade-top h-screen" data-aos="fade-up">
      <div class="flex justify-around">
        <div class="text-3xl text-center mt-10 text-gray-700">

          <p class="font-secondary font-thin pt-16" data-aos="fade-down" data-aos-delay="0" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">A</span> curious <span class="text-bold">Web Developer</span> that makes sure the <span class="text-bold">kid inside</span> him
          </p>

          <p class="font-secondary font-thin" data-aos="fade-up" data-aos-delay="1000" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">brings out </span> his fascination with <span class="text-bold">technology</span> into <span class="text-bold">actuality</span>.
          </p>
          <p class="font-secondary font-thin my-8" data-aos="fade-right" data-aos-delay="1500" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">I entrust</span> my ideas to the power of <span class="text-bold">Python</span> and <span class="text-bold">Django</span>.
          </p>
          <p class="font-secondary font-thin mt-8" data-aos="fade-down" data-aos-delay="1800" data-aos-duration="1000" data-aos-easing="ease-in-out">
            <span class="text-bold">I also carry</span> sparkles of <span class="text-bold">VueJS</span>, <span class="text-bold">Flutter</span> and <span class="text-bold">React</span>
          </p>
          <p class="font-secondary font-thin" data-aos="fade-down" data-aos-delay="1800" data-aos-duration="1000" data-aos-easing="ease-in-out">
            if ever I need to bust it out in the <span class="text-bold">frontend</span>
          </p>

        </div>
      </div>


    </section>
  </div>
</template>

<script>
  export default {
    name: 'MainSpiel',
    data () {
      return {
        staticRoot: process.env.VUE_APP_STATIC_ROOT,
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">



</style>
