<template>
  <div class="stock-detail">
    {{ $route.params.symbol }}
  </div>
</template>

<script>

export default {
  name: 'StockDetail',
  props: {
    symbol: String
  }
}
</script>

<style scoped>

</style>
