import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authState: false,
    adminAuthState: false
  },
  mutations: {
    login: state => (state.authState = true),
    adminLogin: state => (state.adminAuthState = true),
    logout: state => (state.authState = false),
    adminLogout: state => (state.adminAuthState = false)
  },
  actions: {
    login: context => context.commit('login'),
    adminLogin: context => context.commit('adminLogin'),
    logout: context => context.commit('logout'),
    adminLogout: context => context.commit('adminLogout')
  }
})
