<template>
  <div id="movieInfo">
    <div class="col">
      <h4><strong>{{ movieTitle }}</strong></h4>
      <button id="like" v-if="isPicked" style="border:none" @click="unpickMovie">
        <i class="fas fa-heart" style="color:red"></i>
      </button>
      <button id="like" v-else style="border:none;" @click="pickMovie">
        <i class="fas fa-heart" style="color:gray"></i>
      </button>
    </div>
    <hr>
    <div class="col ">
      <p>{{movieReleaseDate}}</p>
      <p>평점: {{total_rate}}</p>
    </div>
    <hr>
    <div>
      장르: &nbsp;
      <p v-for="moviegenre in movieGenres" :key="moviegenre.id"> 
        {{ moviegenre }},&nbsp;
      </p>
    </div>
    <hr>
    <div>
      <p>개봉일: {{ movieReleaseDate}}</p>
    </div>
    <hr>
    <div>  
      <p>감독: {{ movieDirectors }}</p>
    </div>
    <hr>
    <div>
      출연배우:
      <span v-for="movieactor in movieActors" :key="movieactor.id">
        {{ movieactor }},&nbsp;
        <br> 
      </span>
    </div>
    <hr>
    <div>
      <h4><strong>영화 이야기 : </strong></h4>
    </div>
    <br>
    <div>
      <p class="justify-content-start" v-html="overview"></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters, mapState} from 'vuex'
export default {
  name: 'MovieInfo',
  data: function () {
    return {
      movieTitle: null,
      movieGenres: [], 
      movieReleaseDate: null,
      movieDirectors:null,
      movieActors: [],
      movieOverview: null,
      total_rate: 0,
      tmdb_rate: 0,
      tmdb_vote_count: 0,
      isPicked:false,
    }
  },
  computed:{
    ...mapGetters([
      'config',
      'rateSum',
    ]),
    ...mapState([
      'selectedMovie',
      'rates',
      'rateItem',
    ]),
    overview () {
      return this.movieOverview.split('\n').join('<br />')
    }
  },
  methods:{
    pickMovie:function(){
      const movieId = this.$route.params.movieId
      const pickMovieData = {
        movie: this.selectedMovie,
        title: this.movieTitle,
        poster_path: this.selectedMovie.poster_path,
        genres: this.selectedMovie.genres
      }
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/pick/${movieId}/`,
        data: pickMovieData,
        headers:this.config,
      })
        .then(() =>{
          //console.log(res.data)
          this.isPicked=true
        })
        .catch(err=>{
          console.log(err)
        })
    },
    unpickMovie:function(){
      const movieId = this.$route.params.movieId
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/api/v1/pick/${movieId}/`,
        headers:this.config,
      })
        .then(()=>{
          this.isPicked=false
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created: function() {
    const movieId = this.$route.params.movieId
    let tmp_rate

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${movieId}/`,
      headers:this.config,
    })
      .then((res) => {
        if (res.data.title) {
          this.movieTitle = res.data.title
        } else {
          this.movieTitle = '정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.'
        }
        if (res.data.release_date) {
          this.movieReleaseDate = res.data.release_date
        } else {
          this.movieReleaseDate = '정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.'
        }
        // this.movieReleaseDate = res.data.release_date
        if (res.data.overview) {
          this.movieOverview = res.data.overview
        } else {
          this.movieOverview = '정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.'
        }
        // this.movieOverview = res.data.overview
        // 동영상 정보
        if (res.data.videos[0].video_keys) {
          const videoUrl = `https://www.youtube.com/embed/${res.data.videos[0].video_keys}?autoplay=1`
          this.movieVideoPath = videoUrl
        } else {
          this.movieVideoPath = '정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.'
        }
        // const videoUrl = `https://www.youtube.com/embed/${res.data.videos[0].video_keys}?autoplay=1`
        // this.movieVideoPath = videoUrl
        // 감독 정보
        if (res.data.directors[0].name) {
          this.movieDirectors = res.data.directors[0].name
        } else {
          this.movieDirectors = '정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.'
        }
        // this.movieDirectors = res.data.directors[0].name
        // 배우 정보
        if (res.data.actors) {
          res.data.actors.forEach(actor => {
            this.movieActors.push(actor.name)
          })
        } else {
          this.movieActors.push('정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.')
        }
        // res.data.actors.forEach(actor => {
        //   this.movieActors.push(actor.name)
        // })
        // 장르 정보
        if (res.data.genres) {
          res.data.genres.forEach(genre => {
            this.movieGenres.push(genre.name)
          })
        } else {
          this.movieGenres.push('정보가 준비 중입니다. 빠른 시일 내에 업데이트 하겠습니다.')
        }
        // res.data.genres.forEach(genre => {
        //   this.movieGenres.push(genre.name)
        // })
        // tmdb 평점
        this.tmdb_rate = res.data.tmdb_vote_sum
        this.tmdb_vote_count = res.data.tmdb_vote_count
        // console.log(this.res.data.tmdb_vote_sum)
        // console.log(this.tmbdb_vote_count)

        tmp_rate = ((this.tmdb_rate + this.rateSum) / (this.tmdb_vote_count+this.rates.length))
        if (!isNaN(this.tmp_rate)) {
          this.total_rate = Math.round(tmp_rate * 100) / 100
        } else {
          this.total_rate = 0
        }
        //this.total_rate = Math.round(tmp_rate * 100) / 100
        
      })
    
    //'popularity', 'tmdb_vote_sum', 'tmdb_vote_count', 'our_vote_sum', 'our_vote_count', 'reviews', 'reviews_count',
    axios ({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/pick/${movieId}/`,
        headers: this.config
      })
      .then(res => {
        if (Object.keys(res.data).length) {
          this.isPicked = true
        } else {
          this.isPicked = false
        }
      })
  }
  
}
</script>

<style>
#MovieTitle {
  font-size: large; 
  font-weight: bold;
}
#movieInfo {
  margin-top: 10px;
}
.vl {
  border-left: 6px solid green;
  height: 500px;
  position: absolute;
  left: 50%;
  margin-left: -3px;
  top: 0;
}
</style>