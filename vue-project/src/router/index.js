import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue';
import UserList from '../views/UserList.vue'; 
import CreateUser from '../views/Practice.vue'; 
import EditUser from '../views/EditForm.vue';
import LoginForm from '../views/Login.vue';
import Landing from '../views/blogpost/Landing.vue';
import MyBlog from '../views/blogpost/MyBlog.vue';



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
    },
    { path: '/my-blogs', component: MyBlog }


  ]
})



export default router;

