<template>
  <div class="card my-2" style="width: 18rem;">
    <img class="card-img-top" :src="src" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title">{{symbol}}</h5>
      <p class="card-text">{{desc}}</p>
      <router-link :to="{name: 'StockDetail', params: { symbol: symbol }}">
        <button class="btn btn-primary">Detail</button>
      </router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomeCard',
  props: {
    src: String,
    symbol: String,
    desc: String,
  }
}
</script>

<style scoped>
  img {
    float: center;
    width:  100%;
    height: 150px;
    object-fit: scale-down;
  }
</style>
