<template>
  <div>
    <input
      type="text"
      v-model.trim="commentContent"
      label="comment"
      outline
      @keyup.enter="createComment">
      &nbsp;
    <v-btn small @click="createComment">댓글 작성</v-btn>
  </div>
</template>

<script>
import axios from 'axios'
import {mapGetters,mapState,mapActions} from 'vuex'

export default {
  name:'CreateCommentForm',
  data:function(){
    return{
      commentContent:null,
    }
  },
  computed:{
    ...mapGetters([
      'config'
    ]),
    ...mapState([
      'reviewItem',
      'comments'
    ])
  },
  methods:{
    ...mapActions([
      'getComments'
    ]),
    createComment:function(){
      const commentItem={
        content:this.commentContent
      }
      const review=this.reviewItem
      if(commentItem.content){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/api/v1/reviews/${review.id}/comments/`,
          data:commentItem,
          headers:this.config,
        })
          .then(res=>{
            console.log(res)
            this.commentContent=null
            this.getComments(review)

          })
          .catch(err=>{
            console.log(err)
        })
      }else{
        alert('내용을 채워주세요')
      }
    }
  }
}
</script>

<style>
input {
  outline-style: auto;
  color: white
}
</style>