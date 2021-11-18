<template>
  <div>
    
    <my-list-item
      v-for="(movielist, idx) in movielists"
      :movielist="movielist"
      :key="idx"
    >MyList</my-list-item>
    
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MyListItem from '@/components/MyListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MyListItem,
  },
  computed: {
    ...mapState([
      'movielists'
    ])
  }
}
</script>

<style>

</style>