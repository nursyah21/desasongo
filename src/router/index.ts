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
      path: '/tanaman',
      name:'Tanaman',
      component: () => import('../views/Tanaman.vue')
    },
    {
      path: '/tanaman/:category',
      name:'TanamanPerCategory',
      component: () => import('../views/TanamanPerCategory.vue')
    },
    {
      path: '/blog',
      name: 'Blog',
      component: () => import('../views/ListBlog.vue')
    },
    {
      path: '/blog/:id',
      name: 'blog_by_id',
      component: () => import('../views/Blog.vue')
    },
    {
      path: '/about',
      name:'About',
      component: () => import('../views/About.vue')
    },
    {
      path: '/login',
      name:'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/dashboard',
      name:'dashboard',
      component: () => import('../views/Dashboard.vue')
    },
    {
      path: '/plant',
      name: 'Plant',
      component: () => import('../views/AdminPlant.vue')
    },
    {
      path: '/solar-panel',
      name: 'SolarPanel',
      component: () => import('../views/SolarPanel.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: () => import('../views/404.vue')
    }
  ]
})

export default router