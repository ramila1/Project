<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">Sign in to your account</h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="submit()">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input id="email-address" name="email" type="email" autocomplete="email" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Email address" v-model="user_data.email">
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" autocomplete="current-password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password" v-model="user_data.password">
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded">
            <label for="remember-me" class="ml-2 block text-sm text-gray-900"> Remember me </label>
          </div>

          <div class="text-sm">
            <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500"> Forgot your password? </a>
          </div>
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">

            </span>
            Sign in
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; 
import { useRouter } from 'vue-router'; 
import axios from 'axios';
import { useToast } from "vue-toastification";

const toast = useToast({ position: 'bottom-left' });
const router = useRouter();
const user_data = ref({
  email: '',
  password: '',
});

const submit = () => {
  axios.post('http://127.0.0.1:8000/api/users/login/', {
      email: user_data.value.email, 
      password: user_data.value.password
  })
  .then(response => {
    const { access_token, refresh_token, user_id, email } = response.data;
    localStorage.setItem('user', JSON.stringify({ user_id, email }));
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);

    router.push({ name: 'Landing' });
    toast.success("Login Successful!!", { position: 'bottom-right' });
  })
  .catch(error => {
    console.error('Login failed:', error.message);
    toast.error("Login Unsuccessful!!", { position: 'bottom-right' });
  });
};
</script>

<style scoped>
.login-form {
  margin-top: 15px;
}
</style>
