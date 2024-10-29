<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useLoggedInUserStore } from './stores/loggedInUser.js'

const showMenu = ref(false);
const user = useLoggedInUserStore(); 

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
    <header class="smallheader">
      <div>

      </div>
      <div class="adminnav">
        <RouterLink to="/login" v-if="!user.isLoggedIn">Login</RouterLink>
        <RouterLink to="/admin" v-if="user.role === 'editor'">Dashboard</RouterLink>
        <RouterLink to="/editgallery" v-if="user.role === 'editor'">Edit Gallery</RouterLink>
        <RouterLink to="/editreview" v-if="user.role === 'editor'">Edit Review</RouterLink>
        <RouterLink to="/editservices" v-if="user.role === 'editor'">Edit Services</RouterLink>
        <RouterLink to="/" v-if="user.isLoggedIn" @click.prevent="user.logout" style="cursor: pointer;">Logout</RouterLink>
    </div>
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
  margin-top:25px;
}
.smallheader{
  display: flex;
  justify-content: right;
  align-items: right;
  margin-top: 0px;
  height: 20px;
}
.adminnav{
  display: inline-flex;
  padding: 10px;
}

main {
  padding-top: 125px; /* To avoid overlap with fixed header */
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
