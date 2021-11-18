<template>
  <div class="col">
    <div class="card" style="width: 18rem;">
      <img :src="movieImgSrc" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movieCard.title }}</h5>
        <p class="card-text" style="overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 3;  -webkit-box-orient: vertical; word-wrap:break-word;">{{ movieCard.overview }}</p>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object,
  },
  computed: {
    movieImgSrc: function () {
      console.log(this.movieCard.poster_path)
      return `https://image.tmdb.org/t/p/w500/${this.movieCard.poster_path}`
    }
  },
}
</script>

<style>

</style>