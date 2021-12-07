<template>
  <div id="review-detail">
    <h1>{{reviewItem.title}}</h1>
    <div id="username">
      <p>작성자: {{reviewItem.user.username}}</p>
    </div>
    <div id="time">
      <p>작성 날짜: {{created_at}}</p>
    </div>
    <div id="time">
      <p>수정한 날짜:{{updated_at}}</p>
    </div>
    <hr>
    <div>
      <h4>관련 영화: {{selectedMovie.title}}</h4>
    </div>
    <br>
    <div>
      <img :src="selectedMovie.poster_path" alt="movie poster" id="movie-poster">
    </div>
    <br>
    <div>
      <p>{{reviewItem.content}}</p>
    </div>
    <br>
    <div v-if="username===reviewItem.user.username">
      <v-btn flat small @click="goUpdate" >Update </v-btn>
      <v-btn flat small @click="goDelete">Delete </v-btn>
    </div>
    <br>
    <hr>
    <div>
      <h4>댓글</h4>
    </div>
    <div>
      <p>총 댓글 개수: {{comments.length}}</p>
    </div>
    <hr>
    <create-comment-form></create-comment-form>
    <hr>
    <comment-list></comment-list>
  </div>
</template>
<script>
import { mapState, mapGetters, mapActions} from 'vuex'
import CommentList from '@/components/movies/CommentList.vue'
import CreateCommentForm from '@/components/movies/CreateCommentForm.vue'

export default {
  name:'ReviewDetail',
  data: function (){
    return {
      created_at: null,
      updated_at: null,
    }
  },
  components:{
    CommentList,
    CreateCommentForm,
  },
  computed:{
    ...mapState([
      'username',
      'reviewItem',
      'selectedMovie',
      'comments'
    ]),
    ...mapGetters([
      'config'
    ]),
  },
  methods:{
    ...mapActions([
      'updateReview',
      'deleteReview',
      'goDetail'
    ]),
    goUpdate:function(){
      this.$router.push({name:'UpdateReview'})
    },
    goDelete:function(){
      console.log(this.reviewItem.id)
      this.deleteReview(this.reviewItem)
      this.goDetail(this.selectedMovie)
    },
    changeDateFormat: function () {
      let subDate = this.reviewItem.created_at.substr(0,16)
      let subDate2 = this.reviewItem.updated_at.substr(0,16)
      // 2021-11-25T00:07:54.534815+09:00
      this.created_at = subDate.replace('T',' ')
      this.updated_at = subDate2.replace('T',' ')
    }
  },
  created: function () {
    this.changeDateFormat()
    console.log(this.created_at)
    console.log(this.updated_at)
  }

}
</script>

<style scoped>
#review-detail {
  outline-style: solid;
  background-color: rgb(34, 33, 33);
  color: white;
  margin-left: 20px;
  margin-right: 20px;
}
#movie-poster {
  width: 300px;
}
#username {
  color: white;
  text-align: left;
}
#time {
  color: white;
  text-align: right;
}
</style>

