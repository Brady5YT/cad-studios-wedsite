<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
// import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue'
const navbar_height = ref("4rem")
</script>

<template>
  <div class="navbar row g-0 justify-content-around">
    <a class="col-1" href="https://vitejs.dev">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <div class="fs-1 col-10 text-capitalize text-center">C.A.D Games Studios</div>
    <div class="col-1"></div>
  </div>
  <div class="content container-fluid d-flex flex-row justify-content-center text-center align-items-center">
    <a href="https://vitejs.dev" target="_blank">
      
    </a>
    <!-- <HelloWorld msg=" Vite+Vue . " /> -->
  </div>
</template>

<style scoped>
.logo {
  width: 3rem !important;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 1rem #646cffee);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 1rem #42b883ee);
}
.content {
  background-color:rgb(20, 19, 24);
  color: aliceblue;
  height: calc(100vh - v-bind(navbar_height));
}
.navbar {
  background-color:rgb(32, 36, 46);
  color: aliceblue;
  height: v-bind(navbar_height);
}
</style>
