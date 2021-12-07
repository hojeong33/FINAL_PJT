<template>
  <div class="rate">
    <h1>UpdateRate</h1>
    <br>
    <h2>{{selectedMovie.title}}</h2>
    <br>
    <div class="int-area">
      평점: 
      <input type="text"
      v-model.trim="rateItem.rate">
    </div>
    <br>
    <div class="int-area">
      한줄평: 
      <input type="text"
      v-model.trim="rateItem.short_comment" placeholder="한줄평을 꼭 입력해주세요">
    </div>
    <br>
    <v-btn @click="updateRateData">수정</v-btn>
    <br>
  </div>
</template>


<script>
import {mapGetters,mapState,mapActions} from 'vuex'
export default {
  name:'UpdateRate',
  computed:{
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'selectedMovie',
      'rateItem',
    ])
  },
  methods:{
    ...mapActions([
      'updateRate',
      'goDetail'
    ]),
    updateRateData:function(){
      const rate={
        id:this.rateItem.id,
        movie:this.selectedMovie,
        rate:this.rateItem.rate,
        short_comment:this.rateItem.short_comment,
      }
      if(rate.short_comment && rate.rate <= 10 && rate.rate >= 1){
        this.updateRate(rate)
        this.goDetail(this.selectedMovie)
      }else if (rate.short_comment){
        alert('평점은 1-10점만 입력해주세요.') 
      } else {
        alert ('한줄평을 입력해주세요.')
      }
    }
  }
}
</script>
<style scoped>
*{
  margin:0;
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
input {
  outline-style: auto;
}
</style>