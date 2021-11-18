<template>
  <div>
    <span :class="{ completed: mylist.isCompleted }">{{ mylist.title }}</span>
  </div>
</template>

<script>
export default {
  name: 'MyListItem',
  props: {
    mylist: Object,
  },

}
</script>

<style>

</style>