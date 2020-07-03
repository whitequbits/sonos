<template>
  <div class="card" style="width: 18rem;">
    <img class="card-img-top" src="">
    <div class="card-body">
      <p class="card-text">{{text}}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Card',
  props: {
    src: String,
    text: String
  }
}
</script>

<style scoped>
  .card {
    margin-left: 1%;
    margin-top: 2%;
  }
</style>
