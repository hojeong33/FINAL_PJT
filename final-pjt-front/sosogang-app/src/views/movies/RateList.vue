<template>
  <div id="rateList">
    <div class="row justify-content-center" id="rate_head">
      <div class="col align-content-center">
        <h3>Rates</h3>
      </div>
    </div>
    <div class="row justify-content-end">
      <div class="align-content-center">
        <p>총 평가 개수: {{rates.length}}</p>
      </div>
    </div>
    <hr>
    <div v-for="rate in rates" :key="rate.id" :rate="rate">
      <div class="row justify-content-start" id="rates">
        <div class="col col-2 align-content-center">
          <p>{{rate.rate}} &nbsp;</p>
        </div>
        <div class="col col-9 align-content-center">
          <p id="rate_detail" class="font-weight-black" style="color: blue;" @click="goRateDetail(rate)">{{rate.short_comment}}</p>
        </div>
        <div class="col col-1 align-content-center">
          <p>{{username}} &nbsp;</p>
        </div>
      </div>
      <hr>
    </div>
    <br>
    <v-btn @click="goCreateRate">평점 등록</v-btn>
  </div>
</template>

<script>
import {mapGetters, mapState, mapActions} from 'vuex'
import axios from 'axios'

export default {
  name: 'RateList',
  computed:{
    ...mapGetters([
      'config',
      'rateSum',
    ]),
    ...mapState([
      'selectedMovie',
      'rates',
      'username',
    ]),
  },
  methods: {
    ...mapActions([
      'getRateDetail'
    ]),
    goCreateRate:function(){
      this.$router.push({name:'CreateRate'})
    },
    goRateDetail: function(rate) {
      axios({
          method:'get',
          url: `http://127.0.0.1:8000/api/v1/rates/${rate.id}/`,
          headers: this.config,
      })
        .then(res=>{
          this.getRateDetail(res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created: function () {
    const movie = this.selectedMovie
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${movie.id}/rates/`,
      headers: this.config,
    })
      .then((res) => {
        let rateItem = res.data
        this.$store.dispatch('created', rateItem)
      })
      .catch(err=>{
        console.log(err)
      })
  }
}
</script>

<style>
#rateList {
  margin: 10px;
}
#rate_detail:hover {
  text-decoration: underline;
}
#rate_detail {
  text-align: left;
}
#rate_haed {
  display: flex;
}
#rates {
  height: 35px;
  margin-top: auto;
  margin-bottom: auto;
}
</style>
