<template>
  <div class="Main">
    <br>
    <temp/>
    <br>
    <h1>인기영화</h1>
    <b-link @click="$router.push({name:'MoviePopularIndex'})">더 보러가기</b-link>
    <ten-popular></ten-popular>
    <h1>평점높은영화</h1>
    <b-link @click="$router.push({name:'MovieVoteIndex'})">더 보러가기</b-link>
    <ten-vote></ten-vote>
  </div>
</template>

<script>
import temp from '@/components/movies/temp'
import TenPopular from '@/components/movies/TenPopular'
import TenVote from '@/components/movies/TenVote'

export default {
  name: 'Main',
  components: {
    temp,
    TenVote,
    TenPopular
  }
}
</script>

<style>
.Main {
   background-color: rgb(34, 33, 33);
   color: white;
}

</style>

