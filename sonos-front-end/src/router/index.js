import Vue from 'vue'
import VueRouter from 'vue-router'
import StockList from '../views/StockList.vue'
import Home from "../views/Home.vue";

Vue.use(VueRouter)

  const routes = [
    {
      path: "/",
      name: "Home",
      metaTags: [
        {
          name: "Sonos",
          content: "Dashboard"
        }
      ],
      component: Home
    },
    {
      path: "/stocklist",
      name: "Stocklist",
      metaTags: [
        {
          name: "Sonos",
          content: "Stock List"
        }
      ],
      component: StockList
    },
    {
      path: "/about",
      name: "About",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/About.vue")
    },
    {
      path: "/stock_detail/:symbol",
      name: "StockDetail",
      component: () => import("../views/StockDetail.vue")
    }
  ];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
