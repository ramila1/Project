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
      const router = useRouter();
      const user = ref({ user_id: null, email: '' });
      const fetchUser = () => {
        const userData = JSON.parse(localStorage.getItem('user'));
        if (userData) {
          user.value = userData;
        } else {
          router.push('/login');
        }
      };
  
      const logout = () => {
        localStorage.removeItem('user');
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        user.value = { user_id: null, email: '' };
        router.push('/login');
      };
  
      onMounted(() => {
        fetchUser();
      });
  
      return {
        user,
        logout,
      };
    }
  };
  </script>
  
  <style scoped>

  
  .header-title {
    color: #333;
    font-size: 28px;
    margin-bottom: 20px;
  }
  
  .nav-bar {
    display: flex;
    justify-content: space-around;
    width: 100%;
    background-color: #f2f2f2;
    padding: 10px;
    border-radius: 4px;
  }
  
  .email-link {
    color: #007bff;
    text-decoration: none;
    font-size: 16px;
    padding: 10px 20px;
  }
  
  .email-link:hover {
    background-color: #e9ecef;
    border-radius: 4px;
  }
  
  .logout-button {
    background-color: #dc3545;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    padding: 10px 20px;
  }
  
  .logout-button:hover {
    background-color: #c82333;
  }
  </style>
  