<template>
  <div class="container">
    <div class="row row-cols-2 row-cols-md-4 g-4">
      <movie-card
        v-for="movieCard in movieCards"
        :key="movieCard.id"
        :movieCard="movieCard"
      >
      </movie-card>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },

  computed: {
    ...mapState([
      'movieCards',
    ])
  }

}
</script>
