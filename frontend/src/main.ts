// src/main.ts
import './assets/base.css';
import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import { useLoggedInUserStore } from './stores/loggedInUser';

const app = createApp(App);

const pinia = createPinia();
app.use(pinia);
app.use(router);

// Load user session if it exists
const userStore = useLoggedInUserStore();
userStore.loadUserSession();

app.mount('#app');
