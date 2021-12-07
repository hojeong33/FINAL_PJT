<template>
  <div>
    <div v-for="comment in comments" :key="comment.id" >
      <div class="row justify-content-around" id="commments">
        <p>{{comment.user.username}}</p>
        <div id="content">
          <p>{{comment.content}}</p>
        </div>
        <div>
          <v-btn v-if="comment.user.username==username" 
          @click="deleteComment(comment)"
          flat small
          >
            Delete
          </v-btn>
        </div>
      </div>
      <br>
      <hr>
    </div>
  </div>
</template>

<script>
import {mapState, mapGetters,mapActions} from 'vuex'
import axios from 'axios'
export default {
  name:'CommentList',
  computed:{
    ...mapState([
      'reviewItem',
      'username',
      'comments'
    ]),
    ...mapGetters([
      'config'
    ])
  },
  methods:{
    ...mapActions([
      'getComments'
    ]),
    deleteComment:function(comment){
      axios({
          method:'delete',
          url:`http://127.0.0.1:8000/api/v1/comments/${comment.id}/`,
          headers:this.config,
      })
        .then(res=>{
          console.log(res)
          this.getComments(this.reviewItem)
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created:function(){
    this.getComments(this.reviewItem)
  }

}
</script>

<style>
#content {
  text-align: left;
}
#comments {
 width: 90%;
 align-content: center;
}
</style>