<template>
  <div class="login">
    <h1>Login</h1>
    <br>
    <div class="int-area">
      <input  type="text" id="username" v-model="credentials.username" placeholder="아이디" >
    </div>
    <br>
    <div class="int-area">
      <input type="password" id="password" v-model="credentials.password" @keyup.enter="login(credentials)" placeholder="비밀번호">
    </div>
    <br>
    <div class="btn">
      <b-button 
      @click="login(credentials)">로그인</b-button>
    </div>
    <div>
      <b-link @click="$router.push({name:'Signup'})">아직 회원이 아니신가요?</b-link>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name:'Login',
  data:function(){
    return {
      credentials:{
        username:null,
        password:null,
      }
    }
  },
  methods:{
    ...mapActions([
      'login'
    ])
      
  }
}
</script>

<style scoped>
*{
  margin-left: 20px;
  margin-right: 20px;
  padding:0;
  box-sizing: border-box;
  background-color: rgb(34, 33, 33);
  color: white;
}
.login {
  display: flex;
  flex-direction: column;
  /* align-content: center; */
  justify-content: center;
  align-items: center; 
  height: 80vh;
  text-align: center;
}
.int-area{
  width:400px;
}
.int-area input{
  width:250px;
  padding: 20px 10px 10px;
}
/* .btn{
  width:250px;

} */

</style>