<template>
  <div class="total">
    <br>
    <div id="userInfo">
      <h1 style="font-weight: bold;"> 아이디 : {{username}}</h1>
      <h1 style="font-weight: bold;"> 이메일 : {{email}}</h1>
    </div>
    <br>
    <div class="main-container">
      <div class="temp-box box-two">
        <div>
          <p>작성 리뷰</p>
          <hr>
            <div v-for="review in reviews" :key="review.id">
              <b-link @click="goReviewDetail(review.id)">제목:{{review.title}}</b-link>
            </div>
        </div>
      </div>
      <div class="temp-box box-three">
        <div> 
          <p>작성 댓글</p>
          <hr>
            <div v-for="comment in comments" :key="comment.id">
              <b-link @click="goReviewDetail(comment.review)">{{comment.content}}
              </b-link>
            </div>
        </div>
      </div>
      <div class="temp-box box-one">
        <br>
        <p>좋아요 영화</p>
        <div class="container">
          <div v-for="movie in movies" :key="movie.id">
            <span @click="getMovieData(movie.movie)">
              <div class="item" id="posters">
                <img :src="movie.poster_path" class="card-img-top">
              </div>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState,mapGetters,mapActions} from 'vuex'
import axios from 'axios'

export default {
  name:'UserInfo',
  data:function(){
    return{
      reviews:[],
      comments:[],
      movies:[],
    }
  },
  computed:{
    ...mapState([
      'username',
      'email',
      'userId',
      'movieList',
    ]),
    ...mapGetters([
      'config'
    ])
  },
  methods:{
    ...mapActions([
      'goReviewDetail',
      'goDetail',
      'getProfiles',
    ]),
    getMyReviews:function(){
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/myreviews/${this.userId}/`,
        headers:this.config,
      })
        .then(res=>{
          // console.log(res)
          this.reviews=res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getMyComments:function(){
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/mycomments/${this.userId}/`,
        headers:this.config,
      })
        .then(res=>{
          this.comments=res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getMyMovies:function(){
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/mymovies/${this.userId}/`,
        headers:this.config,
      })
        .then(res=>{
          console.log(res)
          this.movies=res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getMovieData:function(movieId){
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${movieId}/`,
        headers:this.config,
      })
        .then(res=>{
          // console.log(res)
          this.goDetail(res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created: function () {
    this.getProfiles()
    this.getMyReviews()
    this.getMyComments()
    this.getMyMovies()
  },
}
</script>

<style>
.main-container {
  width: 1080px;
  margin: auto;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  background-color: rgb(34, 33, 33);
  color: white;
}
.temp-box {
  text-align: center;
  font-size: 30px;
  border: 1px solid #dee3eb;
}
.box-one {
  grid-column: 1 / 3;
}
.box-two{
  grid-column: 1/2;
}
.box-three{
  grid-column:2/3;
}
#posters {
  padding:5px;
}
.total {
  background-color: rgb(34, 33, 33);
  color: white;
}

</style>
