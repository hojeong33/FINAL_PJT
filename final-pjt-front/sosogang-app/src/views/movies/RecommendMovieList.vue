<template>
  <div class="container">
    <div v-for="(image, index) in recommendedMovies" :key="index" >
      <div class="item">
        <img :src="image.poster_path" class="card-img-top" alt="movie-img" @click="goDetail(image)">
      </div>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions, mapGetters} from 'vuex'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'RecommendMovieList',
  data: function () {
    return {
      recommendedMovies: [],
      myGenres: [],
    }
  },
  computed:{
    ...mapState([
      'username',
      'movieList',
      'userId',
    ]),
    ...mapGetters([
      'config',
    ])
  },
  methods: {
    ...mapActions([
      'getProfiles',
      'goDetail'
    ]),
    movieRecommend: function () {
      this.recommendedMovies = []
      if (this.myGenres.length !== 0) {
        this.movieList.forEach(movie => {
          if (this.myGenres.some(i => movie.genres.includes(i))) {
            this.recommendedMovies.push(movie)
            this.recommendedMovies = _.sampleSize(this.recommendedMovies, this.recommendedMovies.length)
          }
        })
        this.recommendedMovies=_.sampleSize(this.recommendedMovies,30)
      } else {
        alert('좋아하는 영화를 선택해주세요')
      }
    }
  },
  created: function() {
    console.log(this.userId)
    console.log(this.username)
    axios({
      methods:'get',
      url:`http://127.0.0.1:8000/api/v1/mymovies/${this.userId}/`,
      headers:this.config,
    })
      .then(res=>{
        res.data.forEach(myMovie => {
          this.movieList.forEach(movie => {
            if (myMovie.movie === movie.id) {
              movie.genres.forEach(genre => {
                if (this.myGenres.includes(genre) === false) {
                  this.myGenres.push(genre)
                }
              })
            }
          })
        })
        this.movieRecommend()
      })
      .catch(err=>{
        console.log(err)
      })
  }
}
</script>

<style>
.container {
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  justify-content: space-around;
  flex-wrap: wrap;
  background-color: rgb(34, 33, 33)
}
.item {
  background-color: rgb(34, 33, 33);
  font-size: 30px;
  text-align: center;
  margin: 0px;
  width: 300px;
}
.item > img {
  border-radius: 10px;
  transition: 0.3s;
  cursor: pointer;
}
.item > img:hover {
  width: 95%;
  transform: translateY(1.5px) rotate(-10deg);
}
</style>