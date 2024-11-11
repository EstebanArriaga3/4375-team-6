// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { useLoggedInUserStore } from '../stores/loggedInUser'; // Import the store to access logged-in user details

// Define routes with role-based access control
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
    meta: { requiresAuth: true, role: 'admin' }, // Restricted to users with 'admin' role
  },
  {
    path: '/editreview',
    name: 'editreview',
    component: () => import('../views/EditReview.vue'),
    meta: { requiresAuth: true, role: 'admin' }, // Restricted to 'admin' role
  },
  {
    path: '/editservices',
    name: 'editservices',
    component: () => import('../views/EditServices.vue'),
    meta: { requiresAuth: true, role: 'admin' }, // Restricted to 'admin' role
  },
];

// Create router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Navigation guard for protected routes
router.beforeEach((to, from, next) => {
  const store = useLoggedInUserStore(); // Access the user store

  // Check if the route requires authentication
  if (to.meta.requiresAuth && !store.isLoggedIn) {
    // Redirect to login page if not authenticated and trying to access a protected route
    next({
      path: '/login',
      query: { redirect: to.fullPath },
    });
  } else if (to.meta.role && store.role !== to.meta.role) {
    // Check if the user has the required role for the route
    // Redirect to the home page if the user does not have the appropriate role
    alert("You don't have access to this page.");
    next('/');
  } else {
    // Allow access to the route
    next();
  }
});

export default router;
