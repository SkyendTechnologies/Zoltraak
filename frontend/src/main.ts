import '@/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

import App from '@/App.vue'
import router from '@/router'

gsap.registerPlugin(ScrollTrigger);
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
