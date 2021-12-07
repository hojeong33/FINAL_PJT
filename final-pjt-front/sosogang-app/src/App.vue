<template>
  <div id="app">
    <font-awesome-icon icon="https://kit.fontawesome.com/dafa0f7138.js" />
    <v-card v-if="isLogin" 
      class="mx-auto overflow-hidden"
      height=100%
    >
      <v-app-bar style="position: fixed; " 
      >
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

        <v-toolbar-title>소소무비</v-toolbar-title>
        <v-spacer></v-spacer>
        
        <v-toolbar-title @click="logout">
          LOGOUT
        </v-toolbar-title>
      </v-app-bar>
      <router-view style="padding-top: 75px"/>
      <v-navigation-drawer style="position: fixed;"
        v-model="drawer"
        absolute
        temporary
      >
        <v-list
          nav
          dense
        >
          <v-list-item-group
            v-model="group"
            active-class="text--accent-4"
          >
            <v-list-item @click="$router.push({name:'Main'})">
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item>

            <v-list-item @click="$router.push({name:'RecommendMovieList'})">
              <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
              </v-list-item-icon>
              <v-list-item-title>추천영화보기</v-list-item-title>
            </v-list-item>

            <v-list-item @click="$router.push({name:'MovieVoteIndex'})">
              <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
              </v-list-item-icon>
              <v-list-item-title>평점순영화보기</v-list-item-title>
            </v-list-item>

            <v-list-item @click="$router.push({name:'MoviePopularIndex'})">
              <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
              </v-list-item-icon>
              <v-list-item-title>인기순영화보기</v-list-item-title>
            </v-list-item>

            <v-list-item @click="$router.push({name:'MovieRecentIndex'})">
              <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
              </v-list-item-icon>
              <v-list-item-title>최신순영화보기</v-list-item-title>
            </v-list-item>

            <v-list-item @click="$router.push({name:'Profile'})">
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Account</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-card>
    <div v-else>
      <router-view />
    </div>
  </div>
</template>
<script>
  import {mapActions,mapState} from 'vuex'

  export default {
  
    data: () => ({
      drawer: false,
      group: null,
    }),
    methods:{
      ...mapActions([
        'logout',
        'showVote',
        'showPopular',
        'showRecent'
      ]),
    },
    computed:{
      ...mapState([
        'isLogin',
        'username',
      ])
    },
    created: function() {
    if (this.isLogin) {
      this.$router.push({name: 'Main'})
      this.showVote('vote_average')
      this.showPopular('popularity')
      this.showRecent('release_date')
    } else {
      this.$router.push({name:'Login'})
    }
  }
}
</script>


<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>
