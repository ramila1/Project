<template>
  <div>
    <button>Home</button>
    <button @click="goLogin" >Login</button>
    <button @click="goUser" >View User</button>
    <button @click="goRegister">SignUp</button>
        
  </div>
</template>
<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useToast } from "vue-toastification";
import { useStore } from 'vuex';
import LoginForm from '../views/Login.vue';
import '../assets/main.css';
import UserList from '../views/UserList.vue';
import CreateUser from '../views/Practice.vue';


export default {
  name: 'UserList',
  components: {
    LoginForm,
    UserList,
    CreateUser

  },
  setup() {
    const toast = useToast();
    const router = useRouter();
    const store = useStore();
    const users = ref([]);
    const showEditModal = ref(false);
    const currentUserId = ref(null);

    const goLogin = () => {
      router.push('/login');
    };
    const goUser = () => {
      router.push('/user')
    };
    const goRegister = () =>{
      router.push('/create-user')
    }
    return{
      goLogin,
      goUser,
      goRegister
    }
  }
}
</script>
<style>

</style>