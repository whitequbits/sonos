<template>
  <div class="card">
    <div class="card-body">
      {{symbol}}
    </div>
  </div>
</template>

<script>

export default {
  name: 'StockCard',
  props: {
    symbol: String,
  }
}
</script>

<style scoped>
  .card {
    margin-top: 2%;
    margin-bottom: 2%;
    width: 75%;
  }
</style>
