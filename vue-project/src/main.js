import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import LoginForm from './views/Login.vue';
import UserList from './views/UserList.vue';
import './interceptors/axios'

import store from './store'; 

import Practice from './views/Practice.vue';
import axios from 'axios'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import Landing from './views/blogpost/Landing.vue'


axios.defaults.baseURL = "https://127.0.0.1:8000"



const app = createApp(App)
app.component(LoginForm)
app.component(UserList)
app.component(Practice)
app.component(Landing)
app.use(store)
app.use(createPinia())
app.use(router,axios)
app.use(Toast, { position: "top-right" });




app.mount('#app')























