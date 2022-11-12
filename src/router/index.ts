import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  linkActiveClass: "active",
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name:'index',
      component: () => import('../views/Index.vue')
    },
    {
      path: '/urban-farming',
      name:'UrbanFarming',
      component: () => import('../views/UrbanFarming.vue')
    },
    {
      path: '/dashboard',
      name:'dashboard',
      component: () => import('../views/Dashboard.vue')
    },
    {
      path: '/blog',
      name: 'Blog',
      component: () => import('../views/ListBlog.vue')
    },
    {
      path: '/blog/:id',
      name: 'blog',
      component: () => import('../views/Blog.vue')
    },
    {
      path: '/login',
      name:'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: () => import('../views/404.vue')
    }
  ]
})

export default router