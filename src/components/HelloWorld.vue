<script setup>
import { ref } from 'vue'

const props = defineProps({
  msg: String
})

const count = ref(1)
const msg = props.msg.split("")

function addCount() {
  count.value += 1
  console.log(msg)
  //copy
  let a = msg.map(a=>a)

  //reverse/duplicate
  msg.forEach((e,i,arr) => {
    a.push(arr[arr.length-1-i])
  });

  //replace
  msg.splice(0,msg.length)
  a.forEach(e=>msg.push(e))
}
</script>

<template>
  <h1>{{ msg.join("") }}</h1>

  <div class="py-4 fw-light">
    <button type="button" @click="addCount" class="btn btn-dark rounded text-light">count is {{ 2**count }}</button>
    <p class="fw-lighter fs-5">
      Edit
      <code class="text-info fs-5">components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
