<template>
  <div>
    <h1>MyMovieList</h1>
    <my-list-form></my-list-form>
    <movie-list>MyList</movie-list>
    
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import MyListForm from '@/components/MyListForm.vue'

export default {
  name: 'MyMovieList',
  components: {
    MovieList,
    MyListForm,
  },
  computed: {

  }
}
</script>

<style>

</style>