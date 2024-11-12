<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useLoggedInUserStore } from './stores/loggedInUser.js';

const showMenu = ref(false);
const user = useLoggedInUserStore();

// Load user session on app startup
onMounted(() => {
  user.loadUserSession();
  console.log("User session loaded:", user); // Debugging log
});

function toggleMenu() {
  showMenu.value = !showMenu.value;
}
</script>

<template>
  <div class="container">
    <header>
      <div class="logo">
        <img src="@/assets/logotemp.png" alt="Logo" />
      </div>

      <!-- Hamburger Menu for Mobile -->
      <div class="hamburger" @click="toggleMenu">
        &#9776;
      </div>

      <!-- Main Navigation Menu -->
      <nav :class="{ active: showMenu }">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/quote">Free Quote</RouterLink>
        <RouterLink to="/services">Services</RouterLink>
        <RouterLink to="/gallery">Gallery</RouterLink>
        <RouterLink to="/review">Reviews</RouterLink>
      </nav>
    </header>

    <!-- Secondary Navigation for Admin/Editor Links -->
    <header class="smallheader">
      <div class="adminnav">
        <RouterLink to="/login" v-if="!user.isLoggedIn">Login</RouterLink>
        <RouterLink to="/quoterequest" v-if="user.isLoggedIn && user.role === 'admin'">Quote Requests</RouterLink>
        <RouterLink to="/editreview" v-if="user.isLoggedIn && user.role === 'admin'">Edit Review</RouterLink>
        <RouterLink to="/editservices" v-if="user.isLoggedIn && user.role === 'admin'">Edit Services</RouterLink>
        <RouterLink to="/" v-if="user.isLoggedIn" @click.prevent="user.logout" style="cursor: pointer;">Logout</RouterLink>
      </div>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="sticky-footer">
      <p>&copy; 2024 Texas Lawns & Liberty Gardens. All Rights Reserved.</p>
      <div>
        <a href="https://www.facebook.com/profile.php?id=61556578467091&mibextid=LQQJ4d">Facebook</a>
        <a href="https://www.instagram.com/texas_lawns_liberty_gardens?igsh=d3B2Zmk1cmwyODJ6&utm_source=qr">Instagram</a>
        <a href="#">LinkedIn</a>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Main header styles */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  margin-top: 25px;
}
.smallheader {
  display: flex;
  justify-content: right;
  align-items: right;
  margin-top: 0px;
  height: 15px;
  background-color: #272727;
  box-shadow: none;
}

/* Admin nav styling */
.adminnav {
  display: inline-flex;
  padding: 10px;
}
.adminnav a {
  margin: 0 10px;
  text-decoration: none;
  color: var(--color-primary);
}
.logo {
  display: flex;
  align-items: center;
}
main {
  flex-grow: 1;
  padding-top: 125px; /* To avoid overlap with fixed header */
}
.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
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

/* Footer link styling */
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
