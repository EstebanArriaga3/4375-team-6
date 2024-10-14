<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div>
    <header>
      <div class="logo">
        <img src="@/assets/logotemp.png" alt="Logo" />
      </div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/quote">Free Quote</RouterLink>
        <RouterLink to="/services">Services</RouterLink>
        <RouterLink to="/gallery">Gallery</RouterLink>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
    <footer>
      <p>&copy; 2024 Texas Lawns & Liberty Gardens. All Rights Reserved.</p>
      <div>
        <a href="#">Facebook</a>
        <a href="#">Instagram</a>
        <a href="#">LinkedIn</a>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Align header logo and navigation */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

main {
  padding-top: 100px; /* To avoid overlap with fixed header */
}
</style>
