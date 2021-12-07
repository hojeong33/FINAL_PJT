<template>
  <div class="review">
    <h1>UpdateReview</h1>
    <br>
    <h2>{{selectedMovie.title}}</h2>
    <br>
    <div class="int-area">
      <input type="text"
      v-model.trim="reviewItem.title">
    </div>
    <br>
    <div class="int-area">
      <b-form-textarea v-model.trim="reviewItem.content" rows="4"  ></b-form-textarea>
    </div>
    <br>
    <v-btn @click="updateReviewData">Upload</v-btn>
    <br>
    <br>
  </div>
</template>

<script>
import {mapGetters,mapState,mapActions} from 'vuex'
export default {
  name:'UpdateReview',
  computed:{
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'reviewItem',
      'selectedMovie'
    ])
  },
  methods:{
    ...mapActions([
      'goDetail',
      'updateReview'
    ]),
    updateReviewData:function(){
      const review={
        id:this.reviewItem.id,
        movie:this.selectedMovie,
        title:this.reviewItem.title,
        content:this.reviewItem.content,
      }
      if(review.title && review.content){
        this.updateReview(review)
        this.goDetail(this.selectedMovie)
      }else if (review.title){
        alert('내용을 채워주세요')
      }else{
        alert('제목을 채워주세요')
      }
    }
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
.review {
  outline-style: auto;
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vh;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.int-area{
  width:400px;
}
.int-area input{
  outline-style: auto;
  width:250px;
  padding: 20px 10px 10px;
}
</style>

