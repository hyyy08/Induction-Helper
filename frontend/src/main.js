//Main
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { getServerIp } from './services/fetch_ip';

createApp(App)
  .use(router)
  .mount('#app');