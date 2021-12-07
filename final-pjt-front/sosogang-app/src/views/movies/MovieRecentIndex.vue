<template>
<div class="container">
  <div v-for="(image, index) in movieRecentList" :key="index" >
    <div class="item">
      <img :src="image.poster_path" class="card-img-top" alt="movie-img" @click="goDetail(image)">
    </div>
  </div>
</div>
</template>

<script>
  import {mapState,mapActions} from 'vuex'
  export default {
    name:'MovieRecentIndex',
    computed:{
      ...mapState([
        'movieRecentList'
      ])
    },
    methods:{
      ...mapActions([
        'goDetail',
      ])
    }, 
  }
</script>

<style scoped>

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