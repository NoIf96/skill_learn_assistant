import Vue from 'vue'
import Router from 'vue-router'

import AdminRouter from '../router/admin'
import OrdinaryRouter from '@/router/ordinary'

Vue.use(Router);

let routes = new Set([...AdminRouter, ...OrdinaryRouter]);

let router = new Router({
  routes
});

export default router;
