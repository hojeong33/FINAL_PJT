<template>
  <div id="rate-detail">
    <h1>{{selectedMovie.title}}</h1>
    <p>{{username}}</p>
    <p>평점: {{ rateItem.rate }}</p> 
    <p>한줄평: {{ rateItem.short_comment }}</p>
    <div v-if="rateItem.user.username === username">
      <v-btn small @click="goUpdate">Update</v-btn>
      <v-btn small @click="goDelete">Delete</v-btn>
    </div>
  </div>
</template>

<script>
import {mapState, mapGetters, mapActions} from 'vuex'

export default {
  name: 'RateDetail',
  computed: {
    ...mapState([
      // username은 로그인 한 유저의 이름
      'username',
      'selectedMovie',
      'rateItem',
    ]),
    ...mapGetters([
      'config'
    ])
  },
  methods: {
    ...mapActions([
      'updateRate',
      'deleteRate',
      'goDetail',
    ]),
    goUpdate: function () {
      this.$router.push({name: 'UpdateRate'})
    },
    goDelete:function () {
      this.deleteRate(this.rateItem)
      this.goDetail(this.selectedMovie)
    },
  },
}
</script>

<style scoped>
*{
  margin-left: 50px;
  margin-bottom: 100px;
  margin-right: 50px;
  padding: 0;
  box-sizing: border-box;
  background-color: rgb(34, 33, 33);
  margin-top: 100px;
  color:white;
}
</style>