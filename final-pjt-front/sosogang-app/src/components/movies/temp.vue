<template>
  <div class="page">
    <div class="carusel">
      <h1>최신영화</h1>
      <v-carousel
      height=100%
      :show-arrows="false" >
        <v-carousel-item 
          v-for="(item,i) in movieTenList"
          :key="i"
          :src="item.poster_path"
          reverse-transition="fade-transition"
          transition="fade-transition"
          aria-hidden="true"
          @click="goDetail(item)"
        ></v-carousel-item>
      </v-carousel>
    </div>
  </div>
</template>
<script>
  import {mapState,mapActions} from 'vuex'
  export default {
    computed:{
      ...mapState([
        'movieTenList'
      ])
    },
    methods:{
      ...mapActions([
        'goDetail'
      ])
    }
  }
</script>
<style scoped>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
}
.carusel{
  display: flex;
  flex-direction: column;
  /* align-content: center; */
  justify-content: center;
  align-items: center; 
  height: 80vh;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  height: 20%;
  width: 20%;
}

</style>