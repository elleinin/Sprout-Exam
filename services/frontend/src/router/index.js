import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginVue.vue';
import DashboardView from '../views/DashboardView.vue';

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: DashboardView,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router