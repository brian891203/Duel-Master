import { createPinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './all.css'

window.devicePixelRatio = 2.5
const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
