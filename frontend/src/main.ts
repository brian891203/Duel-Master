import { createApp, defineAsyncComponent } from 'vue'
import App from './App.vue'
import router from './router'
import './all.css'

window.devicePixelRatio = 2.5

const app = createApp(App)

app.component('CanvasCard', defineAsyncComponent(() =>
  import('./components/canvas-card/CanvasCard.vue'),
))

app.use(router)
app.mount('#app')
