<template>
  <div class="card">
    <router-link :to="{name: 'StockDetail', params: { symbol: symbol }}">
    <div class="card-header">
      {{symbol}}
    </div>
    <div class="card-body">
      <blockquote class="blockquote mb-0">
        <p>{{name}}</p>
      </blockquote>
    </div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'Card',
  props: {
    src: String,
    symbol: String,
    name: String,
  }
}
</script>

<style scoped>
  .card {
    margin-left: 1%;
    margin-top: 2%;
    margin-bottom: 2%;
    width: 100%; 
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
