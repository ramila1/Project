import { createPinia } from 'pinia';
import axios from 'axios';
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'; 

import LoginForm from './components/user/Login.vue'; 
import UserList from './components/user/UserList.vue';
import CreateForm from './components/user/CreateForm.vue';
import Landing from './components/blogpost/Landing.vue'; 

import './interceptors/axios';
import './assets/main.css';

axios.defaults.baseURL = "https://127.0.0.1:8000";

const app = createApp(App);

app.component('LoginForm', LoginForm);
app.component('UserList', UserList);
app.component('CreateForm', CreateForm);
app.component('Landing', Landing);

app.use(store);
app.use(createPinia());
app.use(router);
app.use(axios);
app.use(Toast, { position: "top-right" });

app.mount('#app');




















