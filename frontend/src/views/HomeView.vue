<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

main {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  flex-direction: column;
  margin-left: 50%;
  width: 100%;
}
</style>