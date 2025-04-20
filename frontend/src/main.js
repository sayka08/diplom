// frontend/src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index.js';
import api from './api';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import './assets/base.css';

const app = createApp(App);
app.use(router);
app.config.globalProperties.$axios = api;
app.mount('#app');