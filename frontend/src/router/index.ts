// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { useLoggedInUserStore } from '../stores/loggedInUser'; //

// Define routes
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
  },
  {
    path: '/services',
    name: 'services',
    component: () => import('../views/ServicesView.vue'),
  },
  {
    path: '/quote',
    name: 'quote',
    component: () => import('../views/QuoteView.vue'),
  },
  {
    path: '/gallery',
    name: 'gallery',
    component: () => import('../views/GalleryView.vue'),
  },
  {
    path: '/review',
    name: 'review',
    component: () => import('../views/ReviewView.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue'),
  },
  {
    path: '/quoterequest',
    name: 'quoterequest',
    component: () => import('../views/QuoteRequests.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/editreview',
    name: 'editreview',
    component: () => import('../views/EditReview.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/editservices',
    name: 'editservices',
    component: () => import('../views/EditServices.vue'),
    meta: { requiresAuth: true },
  },
];

// Create router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Navigation guard for protected routes
router.beforeEach((to, from, next) => {
  const store = useLoggedInUserStore();

  if (to.meta.requiresAuth && !store.isLoggedIn) {
    // Redirect to login page if not authenticated and trying to access a protected route
    next({
      path: '/login',
      query: { redirect: to.fullPath },
    });
  } else {
    next();
  }
});

export default router;
