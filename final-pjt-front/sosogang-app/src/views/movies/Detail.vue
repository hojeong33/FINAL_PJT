<template>
  <div id="detail">
    <div class="container" id="video">
      <div class="row justify-content-md-center">
        <div class="col-md-auto">
          <iframe :src="movieVideoPath"  frameborder="0" gesture="media" allow="autoplay"></iframe>
        </div>
      </div>
    </div>
    <div id="Info">
      <div class="row">
        <v-btn id="tab" class="col" text outlined x-large @click="changeComponent('MovieInfo')"><strong>영화 정보</strong></v-btn>
        <v-btn id="tab" class="col" text outlined x-large @click="changeComponent('ReviewList')"><strong>영화 리뷰</strong></v-btn>
        <v-btn id="tab" class="col" text outlined x-large  @click="changeComponent('RateList')"><strong>영화 평점</strong></v-btn>
      </div>
      <br>
      <div class="tab-item">
        <keep-alive>
          <components :is="comp"></components>
        </keep-alive>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewList from '@/views/movies/ReviewList'
import {mapGetters, mapState} from 'vuex'
import RateList from '@/views/movies/RateList'
import MovieInfo from '@/views/movies/MovieInfo'

export default {
  name: 'Detail',
  data: function () {
    return {
      movieVideoPath: null,
      comp: 'ReviewList',
    }
  },
  components:{
    ReviewList,
    RateList,
    MovieInfo,
  },
  computed:{
    ...mapGetters([
      'config',

    ]),
    ...mapState([
      'selectedMovie',
    ]),
  },
  methods:{
    changeComponent: function (componentName) {
      this.comp = componentName
      console.log(this.comp)
    }
  },
  created: function() {
    const movieId = this.$route.params.movieId

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${movieId}/`,
      headers:this.config,
    })
      .then((res) => {
        const videoUrl = `https://www.youtube.com/embed/${res.data.videos[0].video_keys}?autoplay=1`
        this.movieVideoPath = videoUrl
      })
  }
}

</script>

<style>
#detail {
   background-color: rgb(34, 33, 33);
}
iframe {
  width: 1440px;
  height:700px;
}
#Info {
  color: white;
  margin-left: auto;
  margin-right:auto;
  margin-top: 40px;
  /* text-align:justify */
  width: 1440px;
  outline-style: auto;

}
#video {
  width: 1440px;
  height:700px;
}

#tab {
  color: white;
  background-color: gray;
}
hr {
  background-color: white;
}

</style>
