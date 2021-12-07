import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/movies/Main.vue'
import Detail from '@/views/movies/Detail.vue'
import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'
import Profile from '@/views/accounts/Profile.vue'
import ReviewDetail from '@/views/movies/ReviewDetail.vue'
import CreateReview from '@/views/movies/CreateReview.vue'
import UpdateReview from '@/views/movies/UpdateReview.vue'
import CreateRate from '@/views/movies/CreateRate.vue'
import UpdateRate from '@/views/movies/UpdateRate.vue'
import RateDetail from '@/views/movies/RateDetail.vue'
import MoviePopularIndex from '@/views/movies/MoviePopularIndex.vue'
import MovieRecentIndex from '@/views/movies/MovieRecentIndex.vue'
import MovieVoteIndex from '@/views/movies/MovieVoteIndex.vue'
import RecommendMovieList from '@/views/movies/RecommendMovieList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/detail/:movieId',
    name: 'Detail',
    component: Detail,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component:Login,
  },
  {
    path: '/profile/:username',
    name: 'Profile',
    component:Profile,
  },
  {
    path:'/createReview',
    name:'CreateReview',
    component:CreateReview,
  },
  {
    path:'/updateReview',
    name:'UpdateReview',
    component:UpdateReview,
  },
  {
    path:'/reviewDetail',
    name:'ReviewDetail',
    component:ReviewDetail,
  },
  {
    path:'/createRate',
    name:'CreateRate',
    component:CreateRate,
  },
  {
    path:'/updateRate',
    name:'UpdateRate',
    component:UpdateRate,
  },
  {
    path:'/rateDetail',
    name:'RateDetail',
    component:RateDetail,
  },
  {
    path:'/moviePopularIndex',
    name:'MoviePopularIndex',
    component:MoviePopularIndex,
  },
  {
    path:'/movieRecentIndex',
    name:'MovieRecentIndex',
    component:MovieRecentIndex,
  },
  {
    path:'/movieVoteIndex',
    name:'MovieVoteIndex',
    component:MovieVoteIndex,
  },
  {
    path:'/recommendMovieList',
    name:'RecommendMovieList',
    component:RecommendMovieList,
  }
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes 
})

export default router


