<template>
<div class="container">
  <div v-for="(image, index) in TenVoteMovies" :key="index" >
    <div class="item">
      <img :src="image.poster_path" class="card-img-top" alt="movie-img" @click="goDetail(image)">
    </div>
  </div>
</div>
</template>

<script scoped>
  import {mapState,mapActions} from 'vuex'
  export default {
    computed:{
      ...mapState([
        'TenVoteMovies'
      ])
    },
    methods:{
      ...mapActions([
        'goDetail'
      ])
    },
  }
</script>

<style scoped>
.container {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  justify-content: space-around;
  flex-wrap: wrap;
}
.item {
  background-color: teal;
  font-size: 30px;
  text-align: center;
  padding: 5px;
  margin: 10px;
  width: 100px;
}
.movie-images {
  z-index: 7;
  padding-top: 6rem;
  padding-left: 31rem;
  width: 100%;
  height: 100%;
}
.movie-image {
  width: 18%;
  padding: 0.1rem;
  margin: 0.1rem;
}
.card {
  background-color: rgba(0, 0, 0, 0);
  border: none;
}
.card > img {
  border-radius: 10px;
  transition: 0.3s;
  cursor: pointer;
}
.card > img:hover {
  width: 95%;
  transform: translateY(1.5px) rotate(-10deg);
}
</style>