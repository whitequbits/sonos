<template>
  <div class="card" style="width: 18rem;">
    <router-link :to="{name: 'StockDetail', params: { symbol: symbol }}">
      <img class="card-img-top" src="">
      <div class="card-body">
        <p class="card-text">{{symbol}}</p>
      </div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'Card',
  props: {
    src: String,
    symbol: String
  }
}
</script>

<style scoped>
  .card {
    margin-left: 1%;
    margin-top: 2%;
  }

  a {
    color: black;
    margin-left: 6px;
    margin-right: 6px;
  }

  a:hover {
    color: black;
  }
</style>
