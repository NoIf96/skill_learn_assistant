import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store'
import echarts from 'echarts'
import 'echarts-gl'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import animated from 'animate.css'

Vue.config.productionTip = false;
Vue.prototype.$echarts = echarts;

Vue.use(Vuex);
Vue.use(ElementUI);
Vue.use(animated);

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if ((store.state.adminAuthState && to.meta.type === 'admin') || (store.state.authState && to.meta.type === 'ordinary')) {
      next();
    } else {
      let path;
      (to.meta.type === 'admin') ? path = '/skill_learn_assistant/admin/login' : path = '/skill_learn_assistant/login';
      next({
        path: path,
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next();
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
