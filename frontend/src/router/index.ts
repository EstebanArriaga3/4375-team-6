import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { useLoggedInUserStore } from '../stores/loggedInUser'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicesView.vue')
    },
    {
      path: '/quote',
      name: 'quote',
      component: () => import('../views/QuoteView.vue')
    },
    {
      path: '/gallery',
      name: 'gallery',
      component: () => import('../views/GalleryView.vue')
    },
    {
      path: '/review',
      name: 'review',
      component: () => import('../views/ReviewView.vue')
    },
    
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue')
    },
    {
      path: '/quoterequest',
      name: 'quoterequest',
      meta: { requiresAuth: true },
      component: () => import('../views/QuoteRequests.vue')
    },
    {
      path: '/editreview',
      name: 'editreview',
      meta: { requiresAuth: true },
      component: () => import('../views/EditReview.vue')
    },
    {
      path: '/editservices',
      name: 'editservices',
      meta: { requiresAuth: true },
      component: () => import('../views/EditServices.vue')
    }
  ]
})

router.beforeEach((to) => {
  const store = useLoggedInUserStore()
  if (to.meta.requiresAuth && !store.isLoggedIn) {
    return {
      path: '/login',
      // save the location we were at to come back later
      query: { redirect: to.fullPath },
    }
  }
})

export default router
