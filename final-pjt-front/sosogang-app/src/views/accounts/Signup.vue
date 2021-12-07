<template>
  <div class="signup">
    <h1>Signup</h1>
    <br>
    <div class="int-area">
      <input type="text" id="username" v-model="credentials.username" placeholder="아이디">
    </div>
    <br>
    <div class="int-area">
      <input type="email" id="email" v-model="credentials.email" placeholder="이메일">
    </div>
    <br>
    <div class="int-area">
      <input type="password" id="password" v-model="credentials.password" placeholder="비밀번호">
    </div>
    <br>
    <div class="int-area">
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation"
      @keyup.enter="signup(credentials)" placeholder="비밀번호 확인">
    </div>
    <br>
    <div class="btn">
      <b-button @click="signup(credentials)">회원가입</b-button>
    </div>
    <br>
    <div>
      <b-link @click="$router.push({name:'Login'})">이미 회원이신가요?</b-link>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name:'Signup',
  data:function(){
    return{
      credentials:{
        username:null,
        password:null,
        passwordConfirmation:null,
        email:null,
      }
    }
  },
  methods:{
    ...mapActions([
      'signup'
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

.signup {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; 
  height: 100vh;
  text-align: center;
}
.int-area{
  width:400px;
}
.int-area input{
  width: 100;
  padding: 20px 10px 10px;

}
</style>

