<template>
    <div class="min-h-screen items-center bg-white justify-center py-4 px-6  ">
      <header class="header">
        <h1 class="text-center py-8 text-xl">Blog</h1>
        <nav class="nav-bar">
          <router-link to="/blogs" class="nav-link">All Blog</router-link>
          <router-link to="/my-blogs" class="nav-link">My Blog</router-link>
          <router-link to="/add-blog" class="nav-link">Add Blog</router-link>
          <span class="nav-link">{{ user.email }}</span>
          <button @click="logout" class="nav-link logout-button">Logout</button>
        </nav>
      </header>
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'Landing',
    setup() {

      return {
      };
    }
  };
  </script>
  
  <style scoped>

 
  </style>
  