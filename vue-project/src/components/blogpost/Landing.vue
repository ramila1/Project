<template>
    <div class="max-h-screen items-center bg-white justify-center py-4 px-6  ">
      <header>
        <h1 >Blog</h1>
        <nav >
          <router-link to="/blogs" >All Blog</router-link>
          <router-link to="/my-blogs" >My Blog</router-link>
          <router-link to="/add-blog">Add Blog</router-link>
   
          <button>Logout</button>
        </nav>
      </header>
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  import '../../assets/main.css';
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
  