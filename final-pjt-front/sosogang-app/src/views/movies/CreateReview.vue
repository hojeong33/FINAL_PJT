<template>
  <div class="review">
    <h1>CreateReview</h1>
    <h2>{{selectedMovie.title}}</h2>
    <br>
    <div class="int-area">
      <input type="text" placeholder="title"
      v-model.trim="title">
    </div>
    <br>
    <div class="int-area">
       <b-form-textarea v-model.trim="content" placeholder="content" rows="4" no-resize ></b-form-textarea>
    </div>
    <br>
    <v-btn @click="createReview">Upload</v-btn>
    <br>
    <br>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters,mapState,mapActions} from 'vuex'
export default {
  name:'CreateReview',
  data:function(){
    return{
      movie:null,
      title:null,
      content:null,
      valid: true,
      titleRules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 1) || 'Min 1 characters',
      ],
      reviewRules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 50) || 'Min 50 characters',
      ],
      loading4:false
    }
  },
  computed:{
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'selectedMovie'
    ])
  },
  methods:{
    ...mapActions([
      'goDetail'
    ]),
    handleWrapperClick(){
      this.$emit('update:visible', false)
    },
    createReview:function(){
      const review={
        movie:this.selectedMovie,
        title:this.title,
        content:this.content,
      }
      if(review.title && review.content){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/api/v1/movies/${review.movie.id}/reviews/`,
          data:review,
          headers:this.config,
        })
          .then(res=>{
            console.log(res)
            this.goDetail(review.movie)
          })
          .catch(err=>{
            console.log(err)
          })     
      }else if (review.title){
        alert('내용을 채워주세요')
      }else{
        alert('제목을 채워주세요')
      }
    }
  },
  watch: {
    loader () {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 3000)

      this.loader = null
    }
  }
}
</script>

<style scoped>
*{
  margin:20px;
  padding:0;
  box-sizing: border-box;
  background-color: rgb(34, 33, 33);
  color:white;
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
