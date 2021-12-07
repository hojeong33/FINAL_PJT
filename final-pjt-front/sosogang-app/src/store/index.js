import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router/index.js'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[createPersistedState()],
  state: {
    username:null,
    email:null,
    userId: 0,
    authToken:localStorage.getItem('jwt'),
    isLogin:false,
    movieList: [],
    selectedMovie:null,
    reviewItem:null,
    rates: [],
    rateItem: null,
    comments:[],
    movieRecentList:[],
    moviePopularList:[],
    movieVoteList:[],
    movieTenList:[],
    TenPopularMovies:[],
    TenVoteMovies:[],
  },
  mutations: {
    SET_TOKEN:function(state,token){
      state.authToken=token
      localStorage.setItem('jwt',token)
      state.isLogin=true
    },
    REVOKE_TOKEN:function(state){
      localStorage.removeItem('jwt')
      state.authToken=null
      state.isLogin=false
    },
    GET_USER:function(state,user){
      state.username=user.username
      state.email=user.email
      state.userId=user.userId
    },
    GET_MOVIES: function(state, results) {
      state.movieList = results.slice(0,21)
    },
    SELECT_MOVIE:function(state,movie){
      state.selectedMovie=movie
      console.log(movie.id)
    },
    GET_REVIEW_DETAIL:function(state,review){
      state.reviewItem=review
    },
    CREATED: function(state, rateItem) {
      state.rates = rateItem
    },
    GET_Rate_DETAIL: function(state, rate) {
      state.rateItem = rate
    },
    GET_COMMENTS:function(state,comments){
      state.comments=comments
    },
    SHOW_POPULAR:function(state,results){
      state.moviePopularList=results.slice(0,40)
      state.TenPopularMovies=results.slice(0,10)
    },
    SHOW_VOTE:function(state,results){
      state.movieVoteList=results.slice(0,40)
      state.TenVoteMovies=results.slice(0,10)
    },
    SHOW_RECENT:function(state,results){
      state.movieRecentList=results.slice(0,40)
      state.movieTenList=results.slice(0,10)
    },
  },
  actions: {
    signup: function(context, credentials){
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/v2/signup/',
        data:credentials,
      })
        .then(()=>{
          this.dispatch('login',credentials)
          
        })
        .catch(err=>{
          alert(err.response.data.error)
        })
    },
    login:function({commit},credentials){
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/v2/api-token-auth/',
        data:credentials,
      })
        .then(res=>{
          commit("SET_TOKEN",res.data.token)

          // router.push({name:'Profile', params: {username: this.state.username}})
          router.push({name: 'Main'})
          this.dispatch('getProfiles',credentials)

        })
        .catch(()=>{
          alert('아이디와 비밀번호를 정확히 입력해 주세요.')
        })
    },
    logout:function({commit}){
      commit("REVOKE_TOKEN")
      router.push({name:'Login'})
    },
    getProfiles:function({commit,getters}){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v2/profile/',
        headers:getters.config,
      })
        .then((res)=>{
          console.log(res.data)
          const username=res.data.username
          const email=res.data.email
          const userId=res.data.id
          console.log(userId)
          commit('GET_USER',{username,email,userId})
        })
    },
    getMovies: function ({commit,getters}, mode) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/v1/movies/',
        headers:getters.config,
        params: {
          mode
        },
      })
        .then((res) => {
          commit('GET_MOVIES', res.data)
        })
    },
    goDetail:function({commit},movie){
      router.push({ name: 'Detail', params: { movieId: movie.id}})
      commit('SELECT_MOVIE',movie)
    },
    getReviewDetail:function({commit},review){
      router.push({name:'ReviewDetail'})
      commit('GET_REVIEW_DETAIL',review)
    },
    deleteReview:function({getters},review){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/api/v1/reviews/${review.id}/`,
        headers:getters.config,
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    updateReview:function({getters},review){
      console.log(review)
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/api/v1/reviews/${review.id}/`,
        data:review,
        headers:getters.config,
      })
      .then(res=>{
        console.log(res)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    goReviewDetail:function({getters},reviewId){
      axios({
          method:'get',
          url:`http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
          headers:getters.config,
      })
        .then(res=>{
          console.log(res)
          this.dispatch('getReviewDetail',res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    // 평점을 저장소에 등록
    created: function ({commit}, rateItem) {
      commit('CREATED', rateItem)
    },
    getRateDetail:function({commit},rate){
      router.push({name:'RateDetail'})
      commit('GET_Rate_DETAIL',rate)
    },
    updateRate:function({getters},rate){
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/api/v1/rates/${rate.id}/`,
        data:rate,
        headers:getters.config,
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getComments:function({commit,getters},reviewItem){
      const review=reviewItem
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/reviews/${review.id}/comments/`,
        headers:getters.config,
      })
        .then(res=>{
          // this.comments=res.data
          commit('GET_COMMENTS',res.data)
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    deleteRate:function({getters},rate){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/api/v1/rates/${rate.id}/`,
        headers:getters.config,
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    showPopular: function ({commit,getters}, mode) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/v1/movies/',
        headers:getters.config,
        params: {
          mode
        },
      })
        .then((res) => {
          commit('SHOW_POPULAR', res.data)
        })
    },
    showVote: function ({commit,getters}, mode) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/v1/movies/',
        headers:getters.config,
        params: {
          mode
        },
      })
        .then((res) => {
          commit('SHOW_VOTE', res.data)
        })
    },
    showRecent: function ({commit,getters}, mode) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/v1/movies/',
        headers:getters.config,
        params: {
          mode
        },
      })
        .then((res) => {
          commit('SHOW_RECENT', res.data)
        })
    }
  },
  modules: {
  },
  getters:{
    isLoggedIn:function(state){
      return state.authToken ? true: false
    },
    config:function(state){
      return {
        Authorization: `JWT ${state.authToken}`
      }
    },
    rateSum: function (state){
      let rate_sum = 0
      state.rates.forEach(rate => {
        rate_sum += rate.rate
      })
      return rate_sum
    }
  }
})

