<template>
  <div class="rate">

    <h1>평점 등록하기</h1>

    <h2>{{selectedMovie.title}}</h2>
    <div class="int-area">
      평점 : 
      <input type="text"
        v-model.trim="rate" 
      >
    </div>
    <div class="int-area">
      한줄평 : 
      <input type="text"
        v-model.trim="shortComment" placeholder="한줄평을 꼭 입력해주세요"
      >
    </div>
    <br>
    <v-btn @click="registerRate">확인</v-btn>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters,mapState, mapActions} from 'vuex'
// mapActions

export default {
  name: 'CreateRate',
  data: function () {
    return {
      rate: 0,
      shortComment: null,
      movie: null,
      valid: true,
    }
  },
  computed: {
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'selectedMovie',
    ])
  },
  methods: {
    ...mapActions([
      'goDetail'
    ]),
    registerRate: function () {
      const rateInfo = {
        short_comment: this.shortComment,
        rate: this.rate,
        movie: this.selectedMovie,
      }
      if (rateInfo.short_comment && rateInfo.rate <= 10 && rateInfo.rate >= 1) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/v1/movies/${rateInfo.movie.id}/rates/`,
          data: rateInfo,
          headers: this.config,
        })
          .then((res) => {
            console.log(res) 
            this.goDetail(rateInfo.movie)
          })
          .catch(err=>{
            console.log(err)
          }) 
      } else if (rateInfo.short_comment){
        alert('평점은 1-10점만 입력해주세요.') 
      } else {
        alert ('한줄평을 입력해주세요.')
      }
    }
  },
  created: function() {
    console.log(this.rateInfo)
  }
}
</script>

<style scoped>
*{
  margin-top: 30px;
  margin-bottom: 30px;
  padding:0;
  box-sizing: border-box;
  background-color: rgb(34, 33, 33);
  color: white;
}
.rate {
  outline-style: auto;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  align-items: center;
  height:100vh;
  width: 100vh;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.int-area{
  width:400px;
}
.int-area input{
  /* outline-style: auto; */
  width:250px;
  padding: 20px 10px 10px;
}
</style>

