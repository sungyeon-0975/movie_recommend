<template>
  <div>
    <input type="text" v-model.trim="myListTitle" @keypress.enter="createMyList">
    <button @click="createMyList">Add</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      myListTitle: '',
    }
  },

  methods: {
    createMyList: function () {
      const myListItem = {
        title: this.myListTitle,
        isCompleted: false,
      }

      if (this.myListTitle) {
        this.$store.commit('CREATE_MYLIST', myListItem)
      }
      this.myListTitle = ''
    }
  }
}
</script>

<style>

</style>