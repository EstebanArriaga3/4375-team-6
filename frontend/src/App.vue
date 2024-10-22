<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';

const showMenu = ref(false);

function toggleMenu() {
  showMenu.value = !showMenu.value;
}
</script>

<template>
  <div>
    <header>
      <div class="logo">
        <img src="@/assets/logotemp.png" alt="Logo" />
      </div>

      <!-- Hamburger Menu -->
      <div class="hamburger" @click="toggleMenu">
        &#9776;
      </div>

      <!-- Navigation Menu -->
      <nav :class="{ active: showMenu }">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/quote">Free Quote</RouterLink>
        <RouterLink to="/services">Services</RouterLink>
        <RouterLink to="/gallery">Gallery</RouterLink>
        <RouterLink to="/review">Reviews</RouterLink>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="sticky-footer">
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

/* Mobile hamburger active state */
.hamburger {
  display: none;
  font-size: 2rem;
  cursor: pointer;
}

nav.active {
  display: flex !important;
}
.sticky-footer {
  background-color: var(--color-background-mute);
  color: var(--color-text);
  text-align: center;
  padding: 1rem;
  width: 100%;
  margin-top: auto; /* Makes sure footer sticks to the bottom */
}

footer a {
  margin: 0 10px;
  color: var(--color-primary);
  transition: color 0.3s ease;
}

footer a:hover {
  color: var(--color-primary-light);
}

@media (max-width: 768px) {
  .hamburger {
    display: block;
  }

  nav {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 80px;
    right: 10px;
    background-color: var(--color-background-soft);
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    z-index: 99;
  }

  nav a {
    margin-bottom: 10px;
  }
}
</style>
