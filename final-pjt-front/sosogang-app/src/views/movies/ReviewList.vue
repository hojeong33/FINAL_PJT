<template>
  <div id="reviewList">
    <div class="row justify-content-center" id="review_head">
      <div class="col align-content-center">
        <h3>Reviews</h3>
      </div>
    </div>
    <div class="row justify-content-end">
      <div class="align-content-center">
        <p>총 리뷰 수: {{reviews.length}}</p>
      </div>
    </div>
    <hr>
    <br>
    <div v-for="review in reviews" :key="review.id">
      <div class="row justify-content-start">
        <div class="col col-2 align-content-center">
          <p>{{username}} &nbsp; </p>
        </div>
        <div id="review_detail" class="font-weight-black align-content-center" style="color: blue;">
          <p @click="goReviewDetail(review.id)"> {{review.title}}</p>
        </div>
      </div>  
      <hr>
    </div>
    <br>
    <v-btn @click="goCreateReview">리뷰 작성</v-btn>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters, mapState,mapActions} from 'vuex'

export default {
  name:'ReivewList',
  data:function(){
    return{
      reviews:[],

    }
  },

  computed:{
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'selectedMovie',
      'username',
    ])
  },
  methods:{
    ...mapActions([
      'goReviewDetail'
    ]),
    addTodo() {
      if (this.doItem) {
        this.$emit("addOne", this.doItem);
        this.clearInput();
      } else {
        this.showModal = !this.showModal;
      }
    },
    clearInput() {
      this.doItem = "";
    },
    getReviews:function(){
      const movie=this.selectedMovie
      axios({
        methods:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/${movie.id}/reviews/`,
        headers:this.config,
      })
        .then(res=>{
          // console.log(res)
          this.reviews=res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    goCreateReview:function(){
      this.$router.push({name:'CreateReview'})
    },
  },
  created:function(){
      this.getReviews()
    },

}
</script>

<style>
#review_haed {
  display: flex;
}
#review_detail:hover {
  text-decoration: underline;
}
#reviewList {
  margin: 10px;
}
</style>
