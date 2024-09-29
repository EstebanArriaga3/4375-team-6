<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <header>
      <nav>
          <div class="logotemp">
            <img alt="Logo" class="logo" src="@/assets/logotemp.png" width="190" height="50" />
          </div>
          <div class="routerlinks">
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/quote">Free Quote</RouterLink>
            <RouterLink to="/services">Services</RouterLink>
            <RouterLink to="/gallery">Gallery</RouterLink>

          </div>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  text-align: center;
  flex-direction: column;
  position: fixed;
  right: 0;
  top: 0;
  height: 80px;
  width: 100%;     
  z-index: 1000;
  background: #111111; /* temp color */
}

main {
  margin-top: 100px;
  text-align: center; 
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.routerlinks{
  position: fixed;
  right: 0;
  margin-right: 5%;
  font-family: 'Kulim Park';
  font-style: normal;
}
.logotemp{
  position: fixed;
  left: 0;
  margin-top: -15px;
  margin-left: 5%;
}


nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
