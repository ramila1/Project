import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../components/user/HomeView.vue';
import UserList from '../components/user/UserList.vue';
import CreateUser from '../components/user/CreateForm.vue';
import EditUser from '../components/user/EditForm.vue';
import LoginForm from '../components/user/Login.vue';
import Landing from '../components/blogpost/Landing.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'HomeView',
      component:HomeView
    },
    {
      path: '/create-user',
      name: 'CreateUser',
      component: CreateUser
    },
    {
      path: '/user',
      name: 'UserList',
      component: UserList
    },
    {
      path:'/login',
      name: 'LoginForm',
      component: LoginForm
    },
    

    { path: '/edit-user/:userId', name: 'EditUser', component: EditUser, props: true },
    {
      path:'/blog_landing',
      name:'Landing',
      component:Landing
    }


  ]
})



export default router;

